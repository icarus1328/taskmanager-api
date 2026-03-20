"""remove unique constraint from title

Revision ID: c46544167417
Revises: af6aa1e0d151
Create Date: 2026-03-21 01:47:54.329361

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'c46544167417'
down_revision: Union[str, Sequence[str], None] = 'af6aa1e0d151'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade():
    with op.batch_alter_table('tasks') as batch_op:
        batch_op.drop_constraint('uq_tasks_title', type_='unique')

def downgrade():
    with op.batch_alter_table('tasks') as batch_op:
        batch_op.create_unique_constraint('uq_tasks_title', ['title'])