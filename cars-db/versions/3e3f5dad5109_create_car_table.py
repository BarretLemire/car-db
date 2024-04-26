"""Create Car Table

Revision ID: 3e3f5dad5109
Revises: 
Create Date: 2024-04-25 20:18:01.202925

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '3e3f5dad5109'
down_revision: Union[str, None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    """Create tables for cars, dealerships, and inventory."""

from alembic import op
import sqlalchemy as sa

def upgrade():
    op.create_table(
        'cars',
        sa.Column('id', sa.Integer, primary_key=True),
        sa.Column('vin', sa.Text),
        sa.Column('model', sa.Text),
        sa.Column('make', sa.Text),
        sa.Column('engine', sa.Text),
        sa.Column('year', sa.Integer)
    )

    op.create_table(
        'dealerships',
        sa.Column('id', sa.Integer, primary_key=True),
        sa.Column('name', sa.Text),
        sa.Column('address', sa.Text),
        sa.Column('phone_number', sa.Text)
    )

    op.create_table(
        'inventory',
        sa.Column('car_id', sa.Integer, sa.ForeignKey('cars.id'), primary_key=True),
        sa.Column('dealer_id', sa.Integer, sa.ForeignKey('dealerships.id'), primary_key=True),
        sa.Column('cost', sa.Float),
        sa.Column('is_sold', sa.Boolean)
    )

def downgrade():
    op.drop_table('inventory')
    op.drop_table('dealerships')
    op.drop_table('cars')


