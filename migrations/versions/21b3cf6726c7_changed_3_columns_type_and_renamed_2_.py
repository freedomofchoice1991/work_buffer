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


def upgrade():
    # add three new columns
    op.add_column('power_plant', sa.Column('production_status', sa.Boolean(), nullable=True))
    op.add_column('power_plant', sa.Column('high_carbon_source_status', sa.Boolean(), nullable=True))
    op.add_column('power_plant', sa.Column('renewable_energy_status', sa.Boolean(), nullable=True))
    # fill them with data
    op.execute("""
        UPDATE power_plant
        SET production_status = CASE
            WHEN power_status = 'Produced' THEN True
            WHEN power_status = 'Consumed' THEN False
        END
    """)

    op.execute("""
            UPDATE power_plant
            SET high_carbon_source_status = CASE
                WHEN carbon_source_rating = 'low' THEN False
                WHEN carbon_source_rating = 'high' THEN True
                Else null
            END
        """)

    op.execute("""
                UPDATE power_plant
                SET renewable_energy_status = CASE
                    WHEN renewable_status = 'renewable' THEN True
                    WHEN renewable_status = 'conventional' THEN False
                    Else null
                END
            """)

    # drop old columns
    op.drop_column('power_plant', 'renewable_status')
    op.drop_column('power_plant', 'power_status')
    op.drop_column('power_plant', 'carbon_source_rating')


def downgrade():
    # add back old columns
    op.add_column('power_plant', sa.Column('renewable_status', sa.String(length=255), nullable=True))
    op.add_column('power_plant', sa.Column('power_status', sa.String(length=255), nullable=True))
    op.add_column('power_plant', sa.Column('carbon_source_rating', sa.String(length=255), nullable=True))

    # fill them with data
    op.execute("""
        UPDATE power_plant
        SET renewable_status = CASE
            WHEN renewable_energy_status = True THEN 'renewable'
            WHEN renewable_energy_status = False THEN 'conventional'
            Else null
        END
    """)

    op.execute("""
            UPDATE power_plant
            SET power_status = CASE
                WHEN production_status = True THEN 'Produced'
                WHEN production_status = False THEN 'Consumed'
            END
        """)

    op.execute("""
                UPDATE power_plant
                SET carbon_source_rating = CASE
                    WHEN high_carbon_source_status = True THEN 'high'
                    WHEN high_carbon_source_status = False THEN 'low'
                    Else null
                END
            """)

    # drop new columns
    op.drop_column('power_plant', 'production_status')
    op.drop_column('power_plant', 'high_carbon_source_status')
    op.drop_column('power_plant', 'renewable_energy_status')
