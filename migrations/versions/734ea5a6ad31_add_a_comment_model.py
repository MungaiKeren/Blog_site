"""add a comment model

Revision ID: 734ea5a6ad31
Revises: 0c4798ecbb9c
Create Date: 2019-09-23 12:52:08.951613

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '734ea5a6ad31'
down_revision = '0c4798ecbb9c'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('comments',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('blog_id', sa.Integer(), nullable=False),
    sa.Column('user_id', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['blog_id'], ['bloggs.id'], ),
    sa.ForeignKeyConstraint(['user_id'], ['users.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('comments')
    # ### end Alembic commands ###