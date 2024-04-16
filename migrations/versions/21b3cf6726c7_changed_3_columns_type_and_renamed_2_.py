"""changed 3 columns type and renamed 2 columns

Revision ID: 21b3cf6726c7
Revises: 84cedb1b7a5e
Create Date: 2024-04-08 11:10:18.036544

"""

# revision identifiers, used by Alembic.
revision = '21b3cf6726c7'
down_revision = '84cedb1b7a5e'

from alembic import op
import sqlalchemy as sa


def delete_existing_rows():
    """
    Delete all existing rows from the PowerPlant table
    """
    from sqlalchemy.sql import text

    connection = op.get_bind()
    stmt = text('DELETE FROM power_plant')
    connection.execute(stmt)


def upgrade():
    delete_existing_rows()
    op.drop_column('power_plant', 'renewable_status')
    op.drop_column('power_plant', 'power_status')
    op.drop_column('power_plant', 'carbon_source_rating')

    op.add_column('power_plant', sa.Column('production_status', sa.Boolean(), nullable=True))
    op.add_column('power_plant', sa.Column('high_carbon_source_status', sa.Boolean(), nullable=True))
    op.add_column('power_plant', sa.Column('renewable_status', sa.Boolean(), nullable=True))


def downgrade():
    op.drop_column('power_plant', 'production_status')
    op.drop_column('power_plant', 'high_carbon_source_status')
    op.drop_column('power_plant', 'renewable_status')

    op.add_column('power_plant', sa.Column('renewable_status', sa.Boolean(), nullable=True))
    op.add_column('power_plant', sa.Column('power_status', sa.Boolean(), nullable=True))
    op.add_column('power_plant', sa.Column('carbon_source_rating', sa.Boolean(), nullable=True))
