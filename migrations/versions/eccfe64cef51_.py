"""empty message

Revision ID: eccfe64cef51
Revises: 
Create Date: 2022-11-15 01:25:46.214377

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'eccfe64cef51'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('producto',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=150), nullable=True),
    sa.Column('stock', sa.Integer(), nullable=False),
    sa.Column('precio', sa.Numeric(precision=10, scale=2), nullable=True),
    sa.Column('estado', sa.String(length=60), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('user',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('email', sa.String(length=120), nullable=False),
    sa.Column('password', sa.String(length=250), nullable=False),
    sa.Column('name', sa.String(length=60), nullable=False),
    sa.Column('phone', sa.String(length=120), nullable=False),
    sa.Column('address', sa.String(length=250), nullable=True),
    sa.Column('is_active', sa.Boolean(), nullable=False),
    sa.Column('estado', sa.String(length=60), nullable=False),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('email')
    )
    op.create_table('carritoCompras',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('userId', sa.Integer(), nullable=True),
    sa.Column('productId', sa.Integer(), nullable=True),
    sa.Column('cantidad', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['productId'], ['producto.id'], ),
    sa.ForeignKeyConstraint(['userId'], ['user.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('favoritoProductos',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('userId', sa.Integer(), nullable=True),
    sa.Column('productId', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['productId'], ['producto.id'], ),
    sa.ForeignKeyConstraint(['userId'], ['user.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('favoritoProductos')
    op.drop_table('carritoCompras')
    op.drop_table('user')
    op.drop_table('producto')
    # ### end Alembic commands ###
