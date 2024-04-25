"""Rename one column of power table

Revision ID: 484a048707d5
Revises: 18959e73ae1e
Create Date: 2024-04-22 13:20:20.613500

"""

# revision identifiers, used by Alembic.
revision = '484a048707d5'
down_revision = '18959e73ae1e'

from alembic import op
import sqlalchemy as sa


def upgrade() -> None:
    # Rename the column
    op.alter_column('power', 'power_plant_id', new_column_name='source_power_plant_id', existing_type=sa.Integer)
    op.drop_constraint(constraint_name='power_power_plant_id_fkey', table_name='power', type_='foreignkey')
    op.create_foreign_key(constraint_name='power_power_plant_id_fkey',
                          source_table='power',
                          referent_table='power_plant',
                          local_cols=['source_power_plant_id'],
                          remote_cols=['id'])


def downgrade() -> None:
    # Drop the foreign key constraint
    op.drop_constraint(constraint_name='power_power_plant_id_fkey', table_name='power', type_='foreignkey')

    # Rename the column back to its original name
    op.alter_column('power', 'source_power_plant_id', new_column_name='power_plant_id', existing_type=sa.Integer)

    # Recreate the foreign key constraint with the original name and column
    op.create_foreign_key(constraint_name='power_power_plant_id_fkey',
                          source_table='power',
                          referent_table='power_plant',
                          local_cols=['power_plant_id'],
                          remote_cols=['id'])