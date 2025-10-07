"""Add user role column

Revision ID: 1b156901147b
Revises: 4421c761bd3c
Create Date: 2025-10-07 00:15:28.938996

"""

from typing import Sequence, Union

import sqlalchemy as sa
from alembic import op

# revision identifiers, used by Alembic.
revision: str = "1b156901147b"
down_revision: Union[str, Sequence[str], None] = "4421c761bd3c"
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    """Upgrade schema."""
    # Create the UserRole enum type
    userrole_enum = sa.Enum("user", "admin", name="userrole")
    userrole_enum.create(op.get_bind())

    # Add the role column to the users table
    op.add_column(
        "users", sa.Column("role", userrole_enum, nullable=True, default="user")
    )


def downgrade() -> None:
    """Downgrade schema."""
    # Remove the role column from the users table
    op.drop_column("users", "role")

    # Drop the UserRole enum type
    userrole_enum = sa.Enum("user", "admin", name="userrole")
    userrole_enum.drop(op.get_bind())
