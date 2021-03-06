"""added product picture

Revision ID: d9ad41639821
Revises: 3456be479281
Create Date: 2022-04-22 02:01:12.160699

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'd9ad41639821'
down_revision = '3456be479281'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('product', sa.Column('photo', sa.String(length=255), nullable=True))
    op.drop_column('product', 'picture')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('product', sa.Column('picture', sa.VARCHAR(length=255), autoincrement=False, nullable=True))
    op.drop_column('product', 'photo')
    # ### end Alembic commands ###
