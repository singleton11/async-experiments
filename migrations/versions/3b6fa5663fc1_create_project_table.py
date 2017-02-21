"""create project table

Revision ID: 3b6fa5663fc1
Revises: 
Create Date: 2017-02-21 23:21:00.930560

"""
import sqlalchemy as sa
from alembic import op

# revision identifiers, used by Alembic.
revision = '3b6fa5663fc1'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    """Create projects table"""
    op.create_table(
        'projects',
        sa.Column('id', sa.Integer, primary_key=True),
        sa.Column('title', sa.String, nullable=False)
    )


def downgrade():
    """Drop projects table"""
    op.drop_table('projects')
