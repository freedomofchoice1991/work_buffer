"""remove estimation_method column from carbon intensity table

Revision ID: 62d843d84712
Revises: ebbfac8aea5a
Create Date: 2024-02-29 14:05:47.734290

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa

# revision identifiers, used by Alembic.
revision: str = '62d843d84712'
down_revision: Union[str, None] = 'ebbfac8aea5a'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade():
    # Create a temporary table without the column to be removed
    op.create_table('temp_carbon_intensity_response',
                    sa.Column('id', sa.Integer, primary_key=True),
                    sa.Column('zone', sa.String()),
                    sa.Column('carbon_intensity', sa.Integer),
                    sa.Column('date_time', sa.DateTime),
                    sa.Column('updated_at', sa.DateTime),
                    sa.Column('created_at', sa.DateTime),
                    sa.Column('emission_factor_type', sa.String()),
                    sa.Column('is_estimated', sa.Boolean),
                    )

    # Copy data from the original table to the temporary table, excluding the column to be removed
    op.execute('INSERT INTO temp_carbon_intensity_response '
               'SELECT '
               'id, '
               'zone, '
               'carbon_intensity, '
               'date_time, '
               'updated_at, '
               'created_at, '
               'emission_factor_type, '
               'is_estimated '
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
                    sa.Column('estimation_method', sa.String())
                    )

    # Copy data from the original table to the temporary table, including the column that was previously removed
    op.execute('INSERT INTO temp_table '
               'SELECT id, '
               'zone, '
               'carbon_intensity, '
               'date_time, '
               'updated_at, '
               'created_at, '
               'emission_factor_type, '
               'is_estimated, '
               'NULL '
               'FROM carbon_intensity_response')

    # Drop the original table
    op.drop_table('carbon_intensity_response')

    # Rename the temporary table to the original table name
    op.rename_table('temp_table', 'carbon_intensity_response')
