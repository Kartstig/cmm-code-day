"""base schema

Revision ID: 87d4a4944d1a
Revises: 
Create Date: 2016-03-03 08:52:27.095164

"""

# revision identifiers, used by Alembic.
revision = '87d4a4944d1a'
down_revision = None
branch_labels = None
depends_on = None

from alembic import op
import sqlalchemy as sa


def upgrade():
    op.create_table(
        'users',
        sa.Column('id', sa.Integer, primary_key=True),
        sa.Column('username', sa.String(50), nullable=False),
        sa.Column('password', sa.String(60)),
        sa.Column('first_name', sa.String(50)),
        sa.Column('last_name', sa.String(50)),
        sa.Column('created_at', sa.DateTime, nullable=False),
        sa.Column('updated_at', sa.DateTime, nullable=False),
        sa.Column('last_login', sa.DateTime),
        sa.UniqueConstraint('username', name='ux_username')
        )
    op.create_table(
        'customers',
        sa.Column('id', sa.Integer, primary_key=True),
        sa.Column('company', sa.String(255), nullable=False),
        sa.Column('address1', sa.String(50)),
        sa.Column('address2', sa.String(50)),
        sa.Column('address3', sa.String(50)),
        sa.Column('city', sa.String(50)),
        sa.Column('state', sa.String(50)),
        sa.Column('zipcode', sa.String(50)),
        sa.Column('phone1', sa.String(50)),
        sa.Column('phone2', sa.String(50)),
        sa.Column('fax1', sa.String(50)),
        sa.Column('fax2', sa.String(50)),
        sa.Column('email', sa.String(255)),
        sa.Column('website1', sa.String(255)),
        sa.Column('website2', sa.String(255)),
        sa.Column('website3', sa.String(255)),
        sa.Column('created_at', sa.DateTime, nullable=False),
        sa.Column('updated_at', sa.DateTime, nullable=False)
        )
    op.create_table(
        'tasks',
        sa.Column('id', sa.Integer, primary_key=True),
        sa.Column('name', sa.String(50), nullable=False),
        sa.Column('created_at', sa.DateTime, nullable=False),
        sa.Column('updated_at', sa.DateTime, nullable=False)
        )
    op.create_table(
        'projects',
        sa.Column('id', sa.Integer, primary_key=True),
        sa.Column('name', sa.String(50), nullable=False),
        sa.Column('customer_id', sa.Integer, nullable=False),
        sa.Column('created_at', sa.DateTime, nullable=False),
        sa.Column('updated_at', sa.DateTime, nullable=False),
        sa.ForeignKeyConstraint(['customer_id'], ['customers.id'], name='fk_projects_customer_id_customers_id')
        )
    op.create_table(
        'task_entries',
        sa.Column('id', sa.Integer, primary_key=True),
        sa.Column('start', sa.DateTime, nullable=False),
        sa.Column('duration', sa.Float(precision=1, asdecimal=True)),
        sa.Column('task_id', sa.Integer, nullable=False),
        sa.Column('project_id', sa.Integer, nullable=False),
        sa.Column('created_at', sa.DateTime, nullable=False),
        sa.Column('updated_at', sa.DateTime, nullable=False),
        sa.ForeignKeyConstraint(['task_id'], ['tasks.id'], name='fk_task_entries_task_id_tasks_id'),
        sa.ForeignKeyConstraint(['project_id'], ['projects.id'], name='fk_task_entries_project_id_projects_id')
        )

def downgrade():
    op.drop_table('task_entries')
    op.drop_table('projects')
    op.drop_table('tasks')
    op.drop_table('customers')
    op.drop_table('users')
