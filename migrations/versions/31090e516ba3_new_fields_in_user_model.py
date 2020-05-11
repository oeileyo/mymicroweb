"""new fields in user model

Revision ID: 31090e516ba3
Revises: 4b06d26f4a33
Create Date: 2020-05-11 15:20:29.564460

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '31090e516ba3'
down_revision = '4b06d26f4a33'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('user', sa.Column('about_me', sa.String(length=140), nullable=True))
    op.add_column('user', sa.Column('last_seen', sa.DateTime(), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('user', 'last_seen')
    op.drop_column('user', 'about_me')
    # ### end Alembic commands ###
