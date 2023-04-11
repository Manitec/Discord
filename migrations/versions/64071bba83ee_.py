"""empty message

Revision ID: 64071bba83ee
Revises: 
Create Date: 2023-04-10 13:29:39.067494

"""
from alembic import op
import sqlalchemy as sa

import os
environment = os.getenv("FLASK_ENV")
SCHEMA = os.environ.get("SCHEMA")

# revision identifiers, used by Alembic.
revision = '64071bba83ee'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('users',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('username', sa.String(length=40), nullable=False),
    sa.Column('firstname', sa.String(length=40), nullable=False),
    sa.Column('lastname', sa.String(length=40), nullable=False),
    sa.Column('photo_url', sa.String(length=255), nullable=False),
    sa.Column('email', sa.String(length=255), nullable=False),
    sa.Column('active_status', sa.Boolean(), nullable=True),
    sa.Column('hashed_password', sa.String(length=255), nullable=False),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('email'),
    sa.UniqueConstraint('username')
    )
    
 if environment == "production":
        op.execute(f"ALTER TABLE users SET SCHEMA {SCHEMA};")

    op.create_table('direct_messages',
    sa.Column('content', sa.Text(), nullable=False),
    sa.Column('_time_stamp', sa.DateTime(), nullable=False),
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('recipient_id', sa.Integer(), nullable=False),
    sa.Column('user_id', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['recipient_id'], ['users.id'], ),
    sa.ForeignKeyConstraint(['user_id'], ['users.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    
 if environment == "production":
        op.execute(f"ALTER TABLE direct_messages SET SCHEMA {SCHEMA};")

    op.create_table('friends',
    sa.Column('user1_id', sa.Integer(), nullable=False),
    sa.Column('user2_id', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['user1_id'], ['users.id'], ),
    sa.ForeignKeyConstraint(['user2_id'], ['users.id'], ),
    sa.PrimaryKeyConstraint('user1_id', 'user2_id')
    )
    
 if environment == "production":
        op.execute(f"ALTER TABLE friends SET SCHEMA {SCHEMA};")

    op.create_table('servers',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('_icon_url', sa.String(), nullable=True),
    sa.Column('_public', sa.Boolean(), nullable=False),
    sa.Column('_name', sa.String(length=100), nullable=False),
    sa.Column('_max_users', sa.Integer(), nullable=False),
    sa.Column('_description', sa.Text(), nullable=False),
    sa.Column('_owner_id', sa.Integer(), nullable=False),
    sa.Column('_created_at', sa.DateTime(), nullable=False),
    sa.ForeignKeyConstraint(['_owner_id'], ['users.id'], ),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('_name')
    )
    
 if environment == "production":
        op.execute(f"ALTER TABLE servers SET SCHEMA {SCHEMA};")

    op.create_table('channels',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('_server_id', sa.Integer(), nullable=False),
    sa.Column('_name', sa.String(length=40), nullable=False),
    sa.Column('_type', sa.String(length=40), nullable=False),
    sa.Column('_max_users', sa.Integer(), nullable=True),
    sa.Column('_topic', sa.String(length=100), nullable=False),
    sa.ForeignKeyConstraint(['_server_id'], ['servers.id'], ),
    sa.PrimaryKeyConstraint('id')
    )

 if environment == "production":
        op.execute(f"ALTER TABLE channels SET SCHEMA {SCHEMA};")

    op.create_table('server_memberships',
    sa.Column('user_id', sa.Integer(), nullable=False),
    sa.Column('server_id', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['server_id'], ['servers.id'], ),
    sa.ForeignKeyConstraint(['user_id'], ['users.id'], ),
    sa.PrimaryKeyConstraint('user_id', 'server_id')
    )
    
 if environment == "production":
        op.execute(f"ALTER TABLE server_memberships SET SCHEMA {SCHEMA};")

    op.create_table('channel_messages',
    sa.Column('content', sa.Text(), nullable=False),
    sa.Column('_time_stamp', sa.DateTime(), nullable=False),
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('user_id', sa.Integer(), nullable=False),
    sa.Column('channel_id', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['channel_id'], ['channels.id'], ),
    sa.ForeignKeyConstraint(['user_id'], ['users.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    
 if environment == "production":
        op.execute(f"ALTER TABLE channel_messages SET SCHEMA {SCHEMA};")

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('channel_messages')
    op.drop_table('server_memberships')
    op.drop_table('channels')
    op.drop_table('servers')
    op.drop_table('friends')
    op.drop_table('direct_messages')
    op.drop_table('users')
    # ### end Alembic commands ###
