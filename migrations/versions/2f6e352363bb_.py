"""empty message

Revision ID: 2f6e352363bb
Revises: 756c02dd8a3e
Create Date: 2022-04-22 14:54:17.159078

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import postgresql

# revision identifiers, used by Alembic.
revision = '2f6e352363bb'
down_revision = '756c02dd8a3e'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('user', sa.Column('cart', postgresql.ARRAY(sa.String(length=255)), nullable=True))
    op.drop_column('user', 'cart1')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('user', sa.Column('cart1', postgresql.ARRAY(sa.VARCHAR(length=255)), autoincrement=False, nullable=True))
    op.drop_column('user', 'cart')
    # ### end Alembic commands ###