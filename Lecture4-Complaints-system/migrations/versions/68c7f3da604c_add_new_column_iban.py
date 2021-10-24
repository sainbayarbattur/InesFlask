"""add new column iban

Revision ID: 68c7f3da604c
Revises: 291a49bb420e
Create Date: 2021-10-24 16:25:39.572468

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '68c7f3da604c'
down_revision = '291a49bb420e'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('complainers', sa.Column('iban', sa.String(length=22), nullable=False))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('complainers', 'iban')
    # ### end Alembic commands ###
