"""remove 4 more unnecessary columns

Revision ID: 2b1f2a07c3cf
Revises: 62d843d84712
Create Date: 2024-02-29 15:12:13.904105

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa

# revision identifiers, used by Alembic.
revision: str = '2b1f2a07c3cf'
down_revision: Union[str, None] = '62d843d84712'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade():
    # Create a temporary table without the column to be removed
    op.create_table('temp_carbon_intensity_response',
                    sa.Column('id', sa.Integer, primary_key=True),
                    sa.Column('zone', sa.String()),
                    sa.Column('carbon_intensity', sa.Integer),
                    sa.Column('date_time', sa.DateTime),
                    )

    # Copy data from the original table to the temporary table, excluding the column to be removed
    op.execute('INSERT INTO temp_carbon_intensity_response '
               'SELECT id, zone, carbon_intensity, date_time '
               'FROM carbon_intensity_response')

    # Drop the original table
    op.drop_table('carbon_intensity_response')

    # Rename the temporary table to the original table name
    op.rename_table('temp_carbon_intensity_response', 'carbon_intensity_response')


def downgrade():
    # This part is for the downgrade operation in case you need to revert the changes
    op.create_table('temp_table',
                    sa.Column('id', sa.Integer, primary_key=True),
                    sa.Column('zone', sa.String()),
                    sa.Column('carbon_intensity', sa.Integer),
                    sa.Column('date_time', sa.DateTime),
                    sa.Column('updated_at', sa.DateTime),
                    sa.Column('created_at', sa.DateTime),
                    sa.Column('emission_factor_type', sa.String()),
                    sa.Column('is_estimated', sa.Boolean),
                    )

    # Copy data from the original table to the temporary table, including the column that was previously removed
    op.execute('INSERT INTO temp_table '
               'SELECT id, zone, carbon_intensity, date_time, NULL, NULL, NULL, NULL '
               'FROM carbon_intensity_response')

    # Drop the original table
    op.drop_table('carbon_intensity_response')

    # Rename the temporary table to the original table name
    op.rename_table('temp_table', 'carbon_intensity_response')
