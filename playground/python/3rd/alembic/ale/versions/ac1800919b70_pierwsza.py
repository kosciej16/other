"""nowa

Revision ID: ac1800919b70
Revises: 
Create Date: 2022-01-10 21:59:41.525671

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = "ac1800919b70"
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    op.create_table("tabelka", sa.Column("kolumna", sa.String(), nullable=True))


def downgrade():
    op.drop_table("tabelka")
