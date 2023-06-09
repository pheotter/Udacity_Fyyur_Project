"""empty message

Revision ID: da49b9ec780b
Revises: 74e9fdf7185e
Create Date: 2023-04-04 09:03:38.343262

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'da49b9ec780b'
down_revision = '74e9fdf7185e'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('genre',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('artist_genre',
    sa.Column('artist_id', sa.Integer(), nullable=False),
    sa.Column('genre_id', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['artist_id'], ['artist.id'], ),
    sa.ForeignKeyConstraint(['genre_id'], ['genre.id'], ),
    sa.PrimaryKeyConstraint('artist_id', 'genre_id')
    )
    op.create_table('venue_genre',
    sa.Column('venue_id', sa.Integer(), nullable=False),
    sa.Column('genre_id', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['genre_id'], ['genre.id'], ),
    sa.ForeignKeyConstraint(['venue_id'], ['venue.id'], ),
    sa.PrimaryKeyConstraint('venue_id', 'genre_id')
    )
    with op.batch_alter_table('artist', schema=None) as batch_op:
        batch_op.add_column(sa.Column('website_link', sa.String(length=120), nullable=False))
        batch_op.add_column(sa.Column('looking_for_venues', sa.Boolean(), nullable=True))
        batch_op.add_column(sa.Column('venue_description', sa.String(length=500), nullable=True))
        batch_op.alter_column('name',
               existing_type=sa.VARCHAR(),
               nullable=False)
        batch_op.alter_column('city',
               existing_type=sa.VARCHAR(length=120),
               nullable=False)
        batch_op.alter_column('state',
               existing_type=sa.VARCHAR(length=120),
               nullable=False)
        batch_op.alter_column('phone',
               existing_type=sa.VARCHAR(length=120),
               nullable=False)
        batch_op.alter_column('image_link',
               existing_type=sa.VARCHAR(length=500),
               nullable=False)
        batch_op.alter_column('facebook_link',
               existing_type=sa.VARCHAR(length=120),
               nullable=False)
        batch_op.drop_column('genres')

    with op.batch_alter_table('venue', schema=None) as batch_op:
        batch_op.add_column(sa.Column('website_link', sa.String(length=120), nullable=False))
        batch_op.add_column(sa.Column('seeking_for_talent', sa.Boolean(), nullable=True))
        batch_op.add_column(sa.Column('talent_description', sa.String(length=500), nullable=True))
        batch_op.alter_column('city',
               existing_type=sa.VARCHAR(length=120),
               nullable=False)
        batch_op.alter_column('state',
               existing_type=sa.VARCHAR(length=120),
               nullable=False)
        batch_op.alter_column('address',
               existing_type=sa.VARCHAR(length=120),
               nullable=False)
        batch_op.alter_column('phone',
               existing_type=sa.VARCHAR(length=120),
               nullable=False)
        batch_op.alter_column('image_link',
               existing_type=sa.VARCHAR(length=500),
               nullable=False)
        batch_op.alter_column('facebook_link',
               existing_type=sa.VARCHAR(length=120),
               nullable=False)

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('venue', schema=None) as batch_op:
        batch_op.alter_column('facebook_link',
               existing_type=sa.VARCHAR(length=120),
               nullable=True)
        batch_op.alter_column('image_link',
               existing_type=sa.VARCHAR(length=500),
               nullable=True)
        batch_op.alter_column('phone',
               existing_type=sa.VARCHAR(length=120),
               nullable=True)
        batch_op.alter_column('address',
               existing_type=sa.VARCHAR(length=120),
               nullable=True)
        batch_op.alter_column('state',
               existing_type=sa.VARCHAR(length=120),
               nullable=True)
        batch_op.alter_column('city',
               existing_type=sa.VARCHAR(length=120),
               nullable=True)
        batch_op.drop_column('talent_description')
        batch_op.drop_column('seeking_for_talent')
        batch_op.drop_column('website_link')

    with op.batch_alter_table('artist', schema=None) as batch_op:
        batch_op.add_column(sa.Column('genres', sa.VARCHAR(length=120), autoincrement=False, nullable=True))
        batch_op.alter_column('facebook_link',
               existing_type=sa.VARCHAR(length=120),
               nullable=True)
        batch_op.alter_column('image_link',
               existing_type=sa.VARCHAR(length=500),
               nullable=True)
        batch_op.alter_column('phone',
               existing_type=sa.VARCHAR(length=120),
               nullable=True)
        batch_op.alter_column('state',
               existing_type=sa.VARCHAR(length=120),
               nullable=True)
        batch_op.alter_column('city',
               existing_type=sa.VARCHAR(length=120),
               nullable=True)
        batch_op.alter_column('name',
               existing_type=sa.VARCHAR(),
               nullable=True)
        batch_op.drop_column('venue_description')
        batch_op.drop_column('looking_for_venues')
        batch_op.drop_column('website_link')

    op.drop_table('venue_genre')
    op.drop_table('artist_genre')
    op.drop_table('genre')
    # ### end Alembic commands ###
