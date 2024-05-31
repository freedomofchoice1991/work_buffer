"""Add destination_power_plant_id column to power table

Revision ID: b2b124dbcd2e
Revises: 484a048707d5
Create Date: 2024-04-22 14:00:18.608251

"""

# revision identifiers, used by Alembic.
revision = 'b2b124dbcd2e'
down_revision = '484a048707d5'

from alembic import op
import sqlalchemy as sa


def upgrade() -> None:
    op.add_column('power', sa.Column('destination_power_plant_id', sa.Integer(), nullable=True))
    op.create_foreign_key(constraint_name='fk_destination_power_plant_id',
                          source_table='power',
                          referent_table='power_plant',
                          local_cols=['destination_power_plant_id'],
                          remote_cols=['id'])


def downgrade():
    # Drop the foreign key constraint
    op.drop_constraint('fk_destination_power_plant_id', 'power', type_='foreignkey')
    # Remove the destination_power_plant_id column from the power table
    op.drop_column('power', 'destination_power_plant_id')
