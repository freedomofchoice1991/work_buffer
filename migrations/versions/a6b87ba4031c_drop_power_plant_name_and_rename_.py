"""drop power_plant_name and rename country column and add a new column to Location table

Revision ID: a6b87ba4031c
Revises: b2b124dbcd2e
Create Date: 2024-04-26 13:53:21.766378

"""

# revision identifiers, used by Alembic.
revision = 'a6b87ba4031c'
down_revision = 'b2b124dbcd2e'

from alembic import op
import sqlalchemy as sa


def upgrade():
    op.drop_column('power_plant', 'power_plant_name')
    op.alter_column('location', 'country', new_column_name='country_code')
    op.add_column('location', sa.Column('country_name', sa.String(), nullable=True))


def downgrade():
    op.add_column('power_plant', sa.Column('power_plant_name', sa.String(), nullable=True))
    op.alter_column('location', 'country_code', new_column_name='country')
    op.drop_column('location', 'country_name')
