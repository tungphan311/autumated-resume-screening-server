"""updateResume

Revision ID: 15d9edaece0d
Revises: d1c7db9071de
Create Date: 2020-12-20 00:48:14.602833

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '15d9edaece0d'
down_revision = 'd1c7db9071de'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('job_posts', sa.Column('total_saves', sa.Integer(), nullable=True))
    op.add_column('job_posts', sa.Column('total_views', sa.Integer(), nullable=True))
    op.add_column('resumes', sa.Column('total_saves', sa.Integer(), nullable=True))
    op.add_column('resumes', sa.Column('total_views', sa.Integer(), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('resumes', 'total_views')
    op.drop_column('resumes', 'total_saves')
    op.drop_column('job_posts', 'total_views')
    op.drop_column('job_posts', 'total_saves')
    # ### end Alembic commands ###
