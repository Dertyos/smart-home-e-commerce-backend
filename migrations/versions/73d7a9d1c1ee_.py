"""empty message

Revision ID: 73d7a9d1c1ee
Revises: 
Create Date: 2022-12-13 05:50:01.729905

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '73d7a9d1c1ee'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('adminuser',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('email', sa.String(length=120), nullable=False),
    sa.Column('password', sa.String(length=250), nullable=False),
    sa.Column('name', sa.String(length=60), nullable=True),
    sa.Column('phone', sa.String(length=60), nullable=False),
    sa.Column('is_active', sa.Boolean(), nullable=False),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('email')
    )
    op.create_table('blocked_list',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('token', sa.String(length=256), nullable=False),
    sa.Column('created_at', sa.DateTime(), nullable=False),
    sa.Column('email', sa.String(length=250), nullable=True),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('token')
    )
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
    sa.Column('img_profile', sa.Text(), nullable=True),
    sa.Column('is_active', sa.Boolean(), nullable=False),
    sa.Column('estado', sa.String(length=60), nullable=False),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('email')
    )
    op.create_table('carritoCompras',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('idOrder', sa.Integer(), nullable=False),
    sa.Column('userId', sa.Integer(), nullable=True),
    sa.Column('productId', sa.Integer(), nullable=True),
    sa.Column('cantidad', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['productId'], ['producto.id'], ),
    sa.ForeignKeyConstraint(['userId'], ['user.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('compras',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('fecha', sa.Date(), nullable=False),
    sa.Column('userId', sa.Integer(), nullable=True),
    sa.Column('productId', sa.Integer(), nullable=True),
    sa.Column('costo', sa.Numeric(precision=10, scale=2), nullable=False),
    sa.Column('trackId', sa.String(length=250), nullable=True),
    sa.Column('estadoEnvio', sa.String(length=60), nullable=False),
    sa.ForeignKeyConstraint(['productId'], ['producto.id'], ),
    sa.ForeignKeyConstraint(['userId'], ['user.id'], ),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('trackId')
    )
    op.create_table('favoritoProductos',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('userId', sa.Integer(), nullable=True),
    sa.Column('productId', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['productId'], ['producto.id'], ),
    sa.ForeignKeyConstraint(['userId'], ['user.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('preguntasproductos',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('ask_by_userid', sa.Integer(), nullable=True),
    sa.Column('productId', sa.Integer(), nullable=True),
    sa.Column('descripcion', sa.String(length=2000), nullable=True),
    sa.Column('posted_at', sa.DateTime(), nullable=False),
    sa.Column('estado', sa.String(length=60), nullable=False),
    sa.ForeignKeyConstraint(['ask_by_userid'], ['user.id'], ),
    sa.ForeignKeyConstraint(['productId'], ['producto.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('productDescription',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('description', sa.String(length=150), nullable=True),
    sa.Column('product_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['product_id'], ['producto.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('reviews',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('userId', sa.Integer(), nullable=True),
    sa.Column('productId', sa.Integer(), nullable=True),
    sa.Column('descripcion', sa.String(length=2000), nullable=True),
    sa.Column('calificacion', sa.Integer(), nullable=True),
    sa.Column('estado', sa.String(length=60), nullable=False),
    sa.ForeignKeyConstraint(['productId'], ['producto.id'], ),
    sa.ForeignKeyConstraint(['userId'], ['user.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('problemas',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('userId', sa.Integer(), nullable=True),
    sa.Column('compraId', sa.Integer(), nullable=True),
    sa.Column('descripcion', sa.String(length=2000), nullable=True),
    sa.Column('estado', sa.String(length=120), nullable=False),
    sa.ForeignKeyConstraint(['compraId'], ['compras.id'], ),
    sa.ForeignKeyConstraint(['userId'], ['user.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('problemas')
    op.drop_table('reviews')
    op.drop_table('productDescription')
    op.drop_table('preguntasproductos')
    op.drop_table('favoritoProductos')
    op.drop_table('compras')
    op.drop_table('carritoCompras')
    op.drop_table('user')
    op.drop_table('producto')
    op.drop_table('blocked_list')
    op.drop_table('adminuser')
    # ### end Alembic commands ###
