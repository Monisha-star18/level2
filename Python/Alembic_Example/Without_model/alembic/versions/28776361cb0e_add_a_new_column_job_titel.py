"""add a new column job_titel

Revision ID: 28776361cb0e
Revises: 91baadbcc8da
Create Date: 2026-10-16 12:40:22.551674

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '28776361cb0e'
down_revision: Union[str, Sequence[str], None] = '91baadbcc8da'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    """Upgrade schema."""
    op.add_column(
        "employee",
        sa.Column("job_title",sa.String(10),nullable=False)
    )


def downgrade() -> None:
    """Downgrade schema."""
    op.drop_column("employee","job_title")
