"""remove nullable=False from every field except input_parameters

Revision ID: 578066b9772d
Revises: 77f5af4d2a02
Create Date: 2022-08-22 22:11:20.438514

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import postgresql

# revision identifiers, used by Alembic.
revision = '578066b9772d'
down_revision = '77f5af4d2a02'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column('workflows_metadata', 'started_on',
               existing_type=postgresql.TIMESTAMP(),
               nullable=True)
    op.alter_column('workflows_metadata', 'ended_on',
               existing_type=postgresql.TIMESTAMP(),
               nullable=True)
    op.alter_column('workflows_metadata', 'status',
               existing_type=sa.VARCHAR(length=10),
               nullable=True)
    op.alter_column('workflows_metadata', 'logs',
               existing_type=sa.VARCHAR(length=250),
               nullable=True)
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column('workflows_metadata', 'logs',
               existing_type=sa.VARCHAR(length=250),
               nullable=False)
    op.alter_column('workflows_metadata', 'status',
               existing_type=sa.VARCHAR(length=10),
               nullable=False)
    op.alter_column('workflows_metadata', 'ended_on',
               existing_type=postgresql.TIMESTAMP(),
               nullable=False)
    op.alter_column('workflows_metadata', 'started_on',
               existing_type=postgresql.TIMESTAMP(),
               nullable=False)
    # ### end Alembic commands ###
