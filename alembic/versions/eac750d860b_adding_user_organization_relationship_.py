"""adding user/organization relationship table

Revision ID: eac750d860b
Revises: 1ef4a5337a
Create Date: 2015-06-01 15:44:50.323810

"""

# revision identifiers, used by Alembic.
revision = 'eac750d860b'
down_revision = '1ef4a5337a'
branch_labels = None
depends_on = None

from alembic import op
import sqlalchemy as sa


def upgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.organization_relationships = sa.Table(
        'organization_relationships',
        sa.Column('user_id', sa.Integer,
                  sa.ForeignKey('user.id'), nullable=False),
        sa.Column('organization_id', sa.Integer,
                  sa.ForeignKey('organization.id'), nullable=False),
        sa.PrimaryKeyConstraint('user_id', 'organization_id'))
    ### end Alembic commands ###


def downgrade():
    ### commands auto generated by Alembic - please adjust! ###
    pass
    ### end Alembic commands ###