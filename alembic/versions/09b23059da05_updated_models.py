"""Updated models

Revision ID: 09b23059da05
Revises: 4ebb82769206
Create Date: 2023-09-16 12:37:32.047977

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '09b23059da05'
down_revision: Union[str, None] = '4ebb82769206'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('doctors', sa.Column('special_interest', sa.String(), nullable=True))
    op.add_column('doctors', sa.Column('email', sa.String(), nullable=True))
    op.drop_index('ix_doctors_specialty', table_name='doctors')
    op.create_index(op.f('ix_doctors_email'), 'doctors', ['email'], unique=True)
    op.create_index(op.f('ix_doctors_special_interest'), 'doctors', ['special_interest'], unique=False)
    op.drop_column('doctors', 'specialty')
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('doctors', sa.Column('specialty', sa.VARCHAR(), autoincrement=False, nullable=True))
    op.drop_index(op.f('ix_doctors_special_interest'), table_name='doctors')
    op.drop_index(op.f('ix_doctors_email'), table_name='doctors')
    op.create_index('ix_doctors_specialty', 'doctors', ['specialty'], unique=False)
    op.drop_column('doctors', 'email')
    op.drop_column('doctors', 'special_interest')
    # ### end Alembic commands ###