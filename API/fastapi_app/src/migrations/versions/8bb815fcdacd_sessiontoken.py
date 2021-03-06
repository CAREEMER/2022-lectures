"""sessiontoken

Revision ID: 8bb815fcdacd
Revises: 9c6c92e3bbc0
Create Date: 2022-07-06 13:34:00.664984

"""
import sqlalchemy as sa
from alembic import op

# revision identifiers, used by Alembic.
revision = "8bb815fcdacd"
down_revision = "9c6c92e3bbc0"
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index("ix_tokens_id", table_name="tokens")
    op.create_index(op.f("ix_tokens_id"), "tokens", ["id"], unique=False)
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index(op.f("ix_tokens_id"), table_name="tokens")
    op.create_index("ix_tokens_id", "tokens", ["id"], unique=False)
    # ### end Alembic commands ###
