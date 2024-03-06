"""Create first API model

Revision ID: ebbfac8aea5a
Revises: 
Create Date: 2024-02-29 11:13:32.654296

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa

# revision identifiers, used by Alembic.
revision: str = 'ebbfac8aea5a'
down_revision: Union[str, None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('carbon_intensity_response',
                    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
                    sa.Column('zone', sa.String(), nullable=False),
                    sa.Column('carbon_intensity', sa.Integer(), nullable=True),
                    sa.Column('date_time', sa.DateTime(), nullable=False),
                    sa.Column('updated_at', sa.DateTime(), nullable=False),
                    sa.Column('created_at', sa.DateTime(), nullable=False),
                    sa.Column('emission_factor_type', sa.String(), nullable=True),
                    sa.Column('is_estimated', sa.Boolean(), nullable=False),
                    sa.Column('estimation_method', sa.String(), nullable=True),
                    sa.PrimaryKeyConstraint('id')
                    )
    op.create_table('power_breakdown_response',
                    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
                    sa.Column('zone', sa.String(), nullable=False),
                    sa.Column('date_time', sa.DateTime(), nullable=False),
                    sa.Column('updated_at', sa.DateTime(), nullable=False),
                    sa.Column('created_at', sa.DateTime(), nullable=False),
                    sa.Column('fossil_free_percentage', sa.Integer(), nullable=False),
                    sa.Column('renewable_percentage', sa.Integer(), nullable=False),
                    sa.Column('power_consumption_total', sa.Integer(), nullable=False),
                    sa.Column('power_production_total', sa.Integer(), nullable=False),
                    sa.Column('power_import_total', sa.Integer(), nullable=False),
                    sa.Column('power_export_total', sa.Integer(), nullable=False),
                    sa.Column('is_estimated', sa.Boolean(), nullable=False),
                    sa.Column('estimation_method', sa.String(), nullable=True),
                    sa.PrimaryKeyConstraint('id')
                    )
    op.create_table('power_consumption_breakdown',
                    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
                    sa.Column('power_breakdown_response_id', sa.Integer(), nullable=False),
                    sa.Column('source', sa.String(), nullable=False),
                    sa.Column('value', sa.Integer(), nullable=True),
                    sa.ForeignKeyConstraint(['power_breakdown_response_id'], ['power_breakdown_response.id'], ),
                    sa.PrimaryKeyConstraint('id')
                    )
    op.create_table('power_export_breakdown',
                    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
                    sa.Column('power_breakdown_response_id', sa.Integer(), nullable=False),
                    sa.Column('source', sa.String(), nullable=False),
                    sa.Column('value', sa.Integer(), nullable=True),
                    sa.ForeignKeyConstraint(['power_breakdown_response_id'], ['power_breakdown_response.id'], ),
                    sa.PrimaryKeyConstraint('id')
                    )
    op.create_table('power_import_breakdown',
                    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
                    sa.Column('power_breakdown_response_id', sa.Integer(), nullable=False),
                    sa.Column('source', sa.String(), nullable=False),
                    sa.Column('value', sa.Integer(), nullable=True),
                    sa.ForeignKeyConstraint(['power_breakdown_response_id'], ['power_breakdown_response.id'], ),
                    sa.PrimaryKeyConstraint('id')
                    )
    op.create_table('power_production_breakdown',
                    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
                    sa.Column('power_breakdown_response_id', sa.Integer(), nullable=False),
                    sa.Column('source', sa.String(), nullable=False),
                    sa.Column('value', sa.Integer(), nullable=True),
                    sa.ForeignKeyConstraint(['power_breakdown_response_id'], ['power_breakdown_response.id'], ),
                    sa.PrimaryKeyConstraint('id')
                    )
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('power_production_breakdown')
    op.drop_table('power_import_breakdown')
    op.drop_table('power_export_breakdown')
    op.drop_table('power_consumption_breakdown')
    op.drop_table('power_breakdown_response')
    op.drop_table('carbon_intensity_response')
    # ### end Alembic commands ###