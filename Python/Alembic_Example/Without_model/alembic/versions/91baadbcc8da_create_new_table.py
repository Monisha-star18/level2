"""create new table

Revision ID: 91baadbcc8da
Revises: 
Create Date: 2026-10-16 12:24:55.978631

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '91baadbcc8da'
down_revision: Union[str, Sequence[str], None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    """Upgrade schema."""
    op.create_table(
        "employee",
        sa.Column("id",sa.Integer,primary_key=True),
        sa.Column("name",sa.String(50),nullable=False),
        sa.Column("current",sa.Boolean,default=True)
    )


def downgrade() -> None:
    """Downgrade schema."""
    op.drop_table("employee")
