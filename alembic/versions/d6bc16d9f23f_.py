"""empty message

Revision ID: d6bc16d9f23f
Revises: 
Create Date: 2024-04-19 22:49:34.525255

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa
import sqlmodel

# revision identifiers, used by Alembic.
revision: str = 'd6bc16d9f23f'
down_revision: Union[str, None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('localauthsession',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('user_id', sa.Integer(), nullable=False),
    sa.Column('session_id', sqlmodel.sql.sqltypes.AutoString(), nullable=False),
    sa.Column('expiration', sa.DateTime(timezone=True), server_default=sa.text('(CURRENT_TIMESTAMP)'), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_localauthsession_session_id'), 'localauthsession', ['session_id'], unique=True)
    op.create_index(op.f('ix_localauthsession_user_id'), 'localauthsession', ['user_id'], unique=False)
    op.create_table('localuser',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('username', sqlmodel.sql.sqltypes.AutoString(), nullable=False),
    sa.Column('password_hash', sa.LargeBinary(), nullable=False),
    sa.Column('enabled', sa.Boolean(), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_localuser_username'), 'localuser', ['username'], unique=True)
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index(op.f('ix_localuser_username'), table_name='localuser')
    op.drop_table('localuser')
    op.drop_index(op.f('ix_localauthsession_user_id'), table_name='localauthsession')
    op.drop_index(op.f('ix_localauthsession_session_id'), table_name='localauthsession')
    op.drop_table('localauthsession')
    # ### end Alembic commands ###
