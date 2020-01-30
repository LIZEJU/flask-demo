"""empty message

Revision ID: 0448c4dcf14f
Revises: 8b36a38fa06a
Create Date: 2020-01-29 15:19:23.598593

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import mysql

# revision identifiers, used by Alembic.
revision = '0448c4dcf14f'
down_revision = '8b36a38fa06a'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint('live_ibfk_1', 'live', type_='foreignkey')
    op.drop_column('live', 'chapter_id')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('live', sa.Column('chapter_id', mysql.INTEGER(display_width=11), autoincrement=False, nullable=True))
    op.create_foreign_key('live_ibfk_1', 'live', 'chapter', ['chapter_id'], ['id'], ondelete='CASCADE')
    # ### end Alembic commands ###