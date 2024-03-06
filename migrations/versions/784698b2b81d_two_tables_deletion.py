"""two tables deletion

Revision ID: 784698b2b81d
Revises: 04085d3168cf
Create Date: 2024-03-01 14:28:25.916701

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '784698b2b81d'
down_revision: Union[str, None] = '04085d3168cf'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # Drop the table
    op.drop_table('power_import_breakdown')
    op.drop_table('power_export_breakdown')


def downgrade() -> None:
    pass
