"""remove columns of power_breakdown

Revision ID: 04085d3168cf
Revises: 2b1f2a07c3cf
Create Date: 2024-03-01 13:06:57.343174

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa

# revision identifiers, used by Alembic.
revision: str = '04085d3168cf'
down_revision: Union[str, None] = '2b1f2a07c3cf'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # Create a temporary table without the column to be removed
    op.create_table('temp_power_breakdown',
                    sa.Column('id', sa.Integer, primary_key=True),
                    sa.Column('zone', sa.String()),
                    sa.Column('date_time', sa.DateTime),
                    )

    # Copy data from the original table to the temporary table, excluding the column to be removed
    op.execute('INSERT INTO temp_power_breakdown '
               'SELECT id, zone, date_time '
               'FROM carbon_intensity_response')

    # Drop the original table
    op.drop_table('power_breakdown_response')

    # Rename the temporary table to the original table name
    op.rename_table('temp_power_breakdown', 'power_breakdown_response')


def downgrade() -> None:
    pass
