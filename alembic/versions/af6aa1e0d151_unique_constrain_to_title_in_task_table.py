"""unique constrain to title in task table

Revision ID: af6aa1e0d151
Revises: 39f6287acf2a
Create Date: 2026-03-21 00:53:16.420886

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'af6aa1e0d151'
down_revision: Union[str, Sequence[str], None] = '39f6287acf2a'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade():
    with op.batch_alter_table('tasks') as batch_op:
        batch_op.create_unique_constraint('uq_tasks_title', ['title'])

def downgrade():
    with op.batch_alter_table('tasks') as batch_op:
        batch_op.drop_constraint('uq_tasks_title', type_='unique')