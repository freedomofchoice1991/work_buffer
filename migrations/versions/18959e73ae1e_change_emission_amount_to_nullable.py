"""change_emission_amount_to_nullable

Revision ID: 18959e73ae1e
Revises: 52bb1e68f61b
Create Date: 2024-04-22 11:01:01.300008

"""

# revision identifiers, used by Alembic.
revision = '18959e73ae1e'
down_revision = '52bb1e68f61b'

from alembic import op
import sqlalchemy as sa


def upgrade():
    op.alter_column('emission_data', 'emission_amount',
                    existing_type=sa.DOUBLE_PRECISION(precision=53),
                    nullable=True)


def downgrade():
    op.alter_column('emission_data', 'emission_amount',
                    existing_type=sa.DOUBLE_PRECISION(precision=53),
                    nullable=False)
