"""empty message

Revision ID: b8036674d649
Revises: 0448c4dcf14f
Create Date: 2020-01-29 22:01:52.480656

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'b8036674d649'
down_revision = '0448c4dcf14f'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('live', sa.Column('author_id', sa.Integer(), nullable=True))
    op.create_foreign_key(None, 'live', 'user', ['author_id'], ['id'], ondelete='CASCADE')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint(None, 'live', type_='foreignkey')
    op.drop_column('live', 'author_id')
    # ### end Alembic commands ###