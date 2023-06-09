"""empty message

Revision ID: c232712eb2b5
Revises: eec5be4c7194
Create Date: 2023-04-04 15:26:20.537143

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'c232712eb2b5'
down_revision = 'eec5be4c7194'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('venue_genre')
    op.drop_table('artist_genre')
    op.drop_table('genre')
    with op.batch_alter_table('artist', schema=None) as batch_op:
        batch_op.add_column(sa.Column('genres', sa.ARRAY(sa.String()), nullable=False))
        batch_op.drop_column('venue_description')
        batch_op.drop_column('looking_for_venues')

    with op.batch_alter_table('venue', schema=None) as batch_op:
        batch_op.add_column(sa.Column('genres', sa.ARRAY(sa.String()), nullable=False))
        batch_op.add_column(sa.Column('seeking_talent', sa.Boolean(), nullable=True))
        batch_op.add_column(sa.Column('seeking_description', sa.String(length=500), nullable=True))
        batch_op.drop_column('talent_description')
        batch_op.drop_column('seeking_for_talent')

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('venue', schema=None) as batch_op:
        batch_op.add_column(sa.Column('seeking_for_talent', sa.BOOLEAN(), autoincrement=False, nullable=True))
        batch_op.add_column(sa.Column('talent_description', sa.VARCHAR(length=500), autoincrement=False, nullable=True))
        batch_op.drop_column('seeking_description')
        batch_op.drop_column('seeking_talent')
        batch_op.drop_column('genres')

    with op.batch_alter_table('artist', schema=None) as batch_op:
        batch_op.add_column(sa.Column('looking_for_venues', sa.BOOLEAN(), autoincrement=False, nullable=True))
        batch_op.add_column(sa.Column('venue_description', sa.VARCHAR(length=500), autoincrement=False, nullable=True))
        batch_op.drop_column('genres')

    op.create_table('artist_genre',
    sa.Column('artist_id', sa.INTEGER(), autoincrement=False, nullable=False),
    sa.Column('genre_id', sa.INTEGER(), autoincrement=False, nullable=False),
    sa.ForeignKeyConstraint(['artist_id'], ['artist.id'], name='artist_genre_artist_id_fkey'),
    sa.ForeignKeyConstraint(['genre_id'], ['genre.id'], name='artist_genre_genre_id_fkey'),
    sa.PrimaryKeyConstraint('artist_id', 'genre_id', name='artist_genre_pkey')
    )
    op.create_table('genre',
    sa.Column('id', sa.INTEGER(), server_default=sa.text("nextval('genre_id_seq'::regclass)"), autoincrement=True, nullable=False),
    sa.Column('name', sa.VARCHAR(), autoincrement=False, nullable=False),
    sa.PrimaryKeyConstraint('id', name='genre_pkey'),
    postgresql_ignore_search_path=False
    )
    op.create_table('venue_genre',
    sa.Column('venue_id', sa.INTEGER(), autoincrement=False, nullable=False),
    sa.Column('genre_id', sa.INTEGER(), autoincrement=False, nullable=False),
    sa.ForeignKeyConstraint(['genre_id'], ['genre.id'], name='venue_genre_genre_id_fkey'),
    sa.ForeignKeyConstraint(['venue_id'], ['venue.id'], name='venue_genre_venue_id_fkey'),
    sa.PrimaryKeyConstraint('venue_id', 'genre_id', name='venue_genre_pkey')
    )
    # ### end Alembic commands ###
