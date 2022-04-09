"""Add dummy student

Revision ID: 4c79b7dd9de8
Revises: fcee8ead338f
Create Date: 2022-04-09 15:08:28.310290

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
from db.models import Student
from db.session import Session

revision = '4c79b7dd9de8'
down_revision = 'fcee8ead338f'
branch_labels = None
depends_on = None

session = Session()


def upgrade():
    student = Student.create_fake_student()
    session.add(student)
    session.commit()


def downgrade():
    engine = session.get_bind()
    engine.execute("TRUNCATE students")
