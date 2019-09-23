"""remove update table

Revision ID: 22139978c4be
Revises: 6e5c6efcc4a4
Create Date: 2019-09-23 21:59:53.184497

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '22139978c4be'
down_revision = '6e5c6efcc4a4'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('upvotes')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('upvotes',
    sa.Column('id', sa.INTEGER(), autoincrement=True, nullable=False),
    sa.Column('upvote', sa.INTEGER(), autoincrement=False, nullable=True),
    sa.Column('blog_id', sa.INTEGER(), autoincrement=False, nullable=True),
    sa.Column('user_id', sa.INTEGER(), autoincrement=False, nullable=True),
    sa.ForeignKeyConstraint(['blog_id'], ['bloggs.id'], name='upvotes_blog_id_fkey'),
    sa.ForeignKeyConstraint(['user_id'], ['users.id'], name='upvotes_user_id_fkey'),
    sa.PrimaryKeyConstraint('id', name='upvotes_pkey')
    )
    # ### end Alembic commands ###