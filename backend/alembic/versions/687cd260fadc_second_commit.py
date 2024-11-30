"""second commit

Revision ID: 687cd260fadc
Revises: 00d55f4e4b92
Create Date: 2024-11-30 07:42:24.355630

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '687cd260fadc'
down_revision: Union[str, None] = '00d55f4e4b92'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    pass


def downgrade() -> None:
    pass
