"""create projects table

Revision ID: 8e26f4a4094e
Revises: 
Create Date: 2017-02-21 22:24:07.316461

"""
import sqlalchemy as sa
from alembic import op

# revision identifiers, used by Alembic.
revision = '8e26f4a4094e'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    op.create_table(
        'projects',
        sa.Column('id', sa.Integer, primary_key=True),
        sa.Column('title', sa.String, nullable=False)
    )


def downgrade():
    op.drop_table('projects')
