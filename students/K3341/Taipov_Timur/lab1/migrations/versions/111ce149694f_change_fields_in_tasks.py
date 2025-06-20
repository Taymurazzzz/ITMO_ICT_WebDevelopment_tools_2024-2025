"""change fields in tasks

Revision ID: 111ce149694f
Revises: 307e396d4bce
Create Date: 2025-04-23 23:46:09.221960

"""
from typing import Sequence, Union
import sqlmodel
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '111ce149694f'
down_revision: Union[str, None] = '307e396d4bce'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    """Upgrade schema."""
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column('task', 'time_spent',
               existing_type=sa.INTEGER(),
               nullable=True)
    # ### end Alembic commands ###


def downgrade() -> None:
    """Downgrade schema."""
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column('task', 'time_spent',
               existing_type=sa.INTEGER(),
               nullable=False)
    # ### end Alembic commands ###
