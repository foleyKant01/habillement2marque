"""empty message

Revision ID: 3bba050e6526
Revises: 
Create Date: 2024-05-17 20:03:08.968027

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import mysql

# revision identifiers, used by Alembic.
revision = '3bba050e6526'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column('products', 'color',
               existing_type=mysql.VARCHAR(length=128),
               nullable=True)
    op.alter_column('products', 'taille1',
               existing_type=mysql.VARCHAR(length=128),
               nullable=True)
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column('products', 'taille1',
               existing_type=mysql.VARCHAR(length=128),
               nullable=False)
    op.alter_column('products', 'color',
               existing_type=mysql.VARCHAR(length=128),
               nullable=False)
    # ### end Alembic commands ###
