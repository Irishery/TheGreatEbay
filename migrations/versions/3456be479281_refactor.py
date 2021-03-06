"""Refactor

Revision ID: 3456be479281
Revises: d2bf97c63b24
Create Date: 2022-04-15 15:56:18.298541

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import postgresql

# revision identifiers, used by Alembic.
revision = '3456be479281'
down_revision = 'd2bf97c63b24'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('product', sa.Column('sold_datetime', sa.DateTime(), nullable=True))
    op.add_column('product', sa.Column('is_sold', sa.Boolean(), nullable=True))
    op.drop_constraint('product_seller_id_fkey', 'product', type_='foreignkey')
    op.create_foreign_key(None, 'product', 'user', ['seller_id'], ['id'])
    op.drop_column('product', 'is_selled')
    op.drop_column('product', 'selled_datetime')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('product', sa.Column('selled_datetime', postgresql.TIMESTAMP(), autoincrement=False, nullable=True))
    op.add_column('product', sa.Column('is_selled', sa.BOOLEAN(), autoincrement=False, nullable=True))
    op.drop_constraint(None, 'product', type_='foreignkey')
    op.create_foreign_key('product_seller_id_fkey', 'product', 'seller', ['seller_id'], ['id'])
    op.drop_column('product', 'is_sold')
    op.drop_column('product', 'sold_datetime')
    # ### end Alembic commands ###
