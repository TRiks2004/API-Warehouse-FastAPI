"""Creat Rack and Cell

Revision ID: 9c24f97ed062
Revises: 0fe2a856aee2
Create Date: 2024-04-14 19:08:50.444104

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '9c24f97ed062'
down_revision: Union[str, None] = '0fe2a856aee2'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('rack',
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('number', sa.Integer(), nullable=False),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('number')
    )
    op.create_index(op.f('ix_rack_id'), 'rack', ['id'], unique=False)
    op.create_table('cell',
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('number', sa.Integer(), nullable=False),
    sa.Column('rack', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['rack'], ['rack.id'], ),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('number')
    )
    op.create_index(op.f('ix_cell_id'), 'cell', ['id'], unique=False)
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index(op.f('ix_cell_id'), table_name='cell')
    op.drop_table('cell')
    op.drop_index(op.f('ix_rack_id'), table_name='rack')
    op.drop_table('rack')
    # ### end Alembic commands ###