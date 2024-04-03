"""druga

Revision ID: 4931a5ad94c5
Revises: ac1800919b70
Create Date: 2022-01-11 12:57:22.780534

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = "4931a5ad94c5"
down_revision = "ac1800919b70"
branch_labels = None
depends_on = None


def upgrade():
    op.create_table("tabelka2", sa.Column("kolumna", sa.String(), nullable=True))


def downgrade():
    op.drop_table("tabelka2")
