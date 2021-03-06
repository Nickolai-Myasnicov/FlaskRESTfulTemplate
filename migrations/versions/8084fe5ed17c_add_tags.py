"""add tags

Revision ID: 8084fe5ed17c
Revises: 11e7d21ca57d
Create Date: 2021-03-12 08:23:14.060603

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '8084fe5ed17c'
down_revision = '11e7d21ca57d'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('tag',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=255), nullable=False),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('name')
    )
    op.create_table('tags',
    sa.Column('tag_id', sa.Integer(), nullable=False),
    sa.Column('note_model_id', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['note_model_id'], ['note_model.id'], ),
    sa.ForeignKeyConstraint(['tag_id'], ['tag.id'], ),
    sa.PrimaryKeyConstraint('tag_id', 'note_model_id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('tags')
    op.drop_table('tag')
    # ### end Alembic commands ###
