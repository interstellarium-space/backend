# -*- coding: utf-8 -*-

from sqlalchemy import Column
from sqlalchemy import Integer
from sqlalchemy import String
from sqlalchemy import Boolean
from sqlalchemy import Date
from sqlalchemy import Double

from sqlalchemy import PrimaryKeyConstraint
from sqlalchemy import ForeignKeyConstraint
from sqlalchemy import UniqueConstraint

from werkzeug.security import check_password_hash
from werkzeug.security import generate_password_hash

from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class User(Base):
    __tablename__ = 'users'

    id = Column(Integer, autoincrement=True)
    email = Column(String(255), nullable=False)
    password_hash = Column(String(512), nullable=False)
    is_superuser = Column(Boolean, nullable=False, default=False)
    is_admin = Column(Boolean, nullable=False, default=False)

    name = Column(String(255), nullable=True)
    birthdate = Column(Date, nullable=True)

    department_id = Column(Integer, nullable=True)

    __table_args__ = (
        PrimaryKeyConstraint('id', name='user_pk'),
        UniqueConstraint('email', name='user_email_unique'),
        ForeignKeyConstraint(
            ['department_id'],
            ['departments.id'],
            ondelete='SET NULL',
            onupdate='CASCADE',
            name='user_department_department_fk'
        )
    )

    def set_password(self, password):
        self.password_hash = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password_hash, password)


class Designer(Base):
    __tablename__ = 'designers'

    id = Column(Integer, autoincrement=True)
    user_id = Column(Integer, nullable=False)

    __table_args__ = (
        ForeignKeyConstraint(
            ['user_id'],
            ['users.id'],
            ondelete='CASCADE',
            onupdate='CASCADE',
            name='designer_user_fk'
        ),
        PrimaryKeyConstraint('id', name='designer_pk'),
        UniqueConstraint('user_id', name='designer_user_unique')
    )


class Engineer(Base):
    __tablename__ = 'engineers'

    id = Column(Integer, autoincrement=True)
    user_id = Column(Integer, nullable=False)

    __table_args__ = (
        ForeignKeyConstraint(
            ['user_id'],
            ['users.id'],
            ondelete='CASCADE',
            onupdate='CASCADE',
            name='engineer_user_fk'
        ),
        PrimaryKeyConstraint('id', name='engineer_pk'),
        UniqueConstraint('user_id', name='engineer_user_unique')
    )


class Technician(Base):
    __tablename__ = 'technicians'

    id = Column(Integer, autoincrement=True)
    user_id = Column(Integer, nullable=False)

    __table_args__ = (
        ForeignKeyConstraint(
            ['user_id'],
            ['users.id'],
            ondelete='CASCADE',
            onupdate='CASCADE',
            name='technician_user_fk'
        ),
        PrimaryKeyConstraint('id', name='technician_pk'),
        UniqueConstraint('user_id', name='technician_user_unique')
    )


class Laboratorian(Base):
    __tablename__ = 'laboratorians'

    id = Column(Integer, autoincrement=True)
    user_id = Column(Integer, nullable=False)

    __table_args__ = (
        ForeignKeyConstraint(
            ['user_id'],
            ['users.id'],
            ondelete='CASCADE',
            onupdate='CASCADE',
            name='laboratorian_user_fk'
        ),
        PrimaryKeyConstraint('id', name='laboratorian_pk'),
        UniqueConstraint('user_id', name='laboratorian_user_unique')
    )


class Department(Base):
    __tablename__ = 'departments'

    id = Column(Integer, autoincrement=True)
    name = Column(String(512), nullable=True)
    chief_id = Column(Integer, nullable=True)

    __table_args__ = (
        ForeignKeyConstraint(
            ['chief_id'],
            ['users.id'],
            ondelete='SET NULL',
            onupdate='CASCADE',
            name='department_chief_user_fk'
        ),
        PrimaryKeyConstraint('id', name='department_pk'),
        UniqueConstraint('chief_id', name='department_chief_unique'),
        UniqueConstraint('name', name='department_name_unique')
    )


class Contract(Base):
    __tablename__ = 'contracts'

    id = Column(Integer, autoincrement=True)
    name = Column(String(512), nullable=True)
    chief_id = Column(Integer, nullable=True)
    group_id = Column(Integer, nullable=True)

    start_date = Column(Date, nullable=True)
    finish_date = Column(Date, nullable=True)

    __table_args__ = (
        PrimaryKeyConstraint('id', name='contract_pk'),
        ForeignKeyConstraint(
            ['chief_id'],
            ['users.id'],
            ondelete='SET NULL',
            onupdate='CASCADE',
            name='contract_chief_fk'
        ),
        ForeignKeyConstraint(
            ['group_id'],
            ['groups.id'],
            ondelete='SET NULL',
            onupdate='CASCADE',
            name='contract_group_fk'
        ),
    )


class Project(Base):
    __tablename__ = 'projects'

    id = Column(Integer, autoincrement=True)
    name = Column(String(512), nullable=True)
    chief_id = Column(Integer, nullable=True)
    group_id = Column(Integer, nullable=True)

    start_date = Column(Date, nullable=True)
    finish_date = Column(Date, nullable=True)

    __table_args__ = (
        PrimaryKeyConstraint('id', name='project_pk'),
        ForeignKeyConstraint(
            ['chief_id'],
            ['users.id'],
            ondelete='SET NULL',
            onupdate='CASCADE',
            name='project_chief_fk'
        ),
        ForeignKeyConstraint(
            ['group_id'],
            ['groups.id'],
            ondelete='SET NULL',
            onupdate='CASCADE',
            name='project_group_fk'
        ),
    )


class Equipment(Base):
    __tablename__ = 'equipment'

    id = Column(Integer, autoincrement=True)
    name = Column(String(512), nullable=True)
    department_id = Column(Integer, nullable=True)
    group_id = Column(Integer, nullable=True)

    __table_args__ = (
        PrimaryKeyConstraint('id', name='equipment_pk'),
        ForeignKeyConstraint(
            ['department_id'],
            ['departments.id'],
            ondelete='SET NULL',
            onupdate='CASCADE',
            name='equipment_department_fk'
        ),
        ForeignKeyConstraint(
            ['group_id'],
            ['groups.id'],
            ondelete='SET NULL',
            onupdate='CASCADE',
            name='equipment_group_fk'
        ),
    )


class Work(Base):
    __tablename__ = 'works'

    id = Column(Integer, autoincrement=True)
    name = Column(String(512), nullable=True)
    cost = Column(Double, nullable=False, default=0.0)

    contract_id = Column(Integer, nullable=True)
    project_id = Column(Integer, nullable=True)

    group_id = Column(Integer, nullable=True)

    __table_args__ = (
        PrimaryKeyConstraint('id', name='work_pk'),
        ForeignKeyConstraint(
            ['contract_id'],
            ['contracts.id'],
            ondelete='SET NULL',
            onupdate='CASCADE',
            name='work_contract_fk'
        ),
        ForeignKeyConstraint(
            ['project_id'],
            ['projects.id'],
            ondelete='SET NULL',
            onupdate='CASCADE',
            name='work_project_fk'
        ),
        ForeignKeyConstraint(
            ['group_id'],
            ['groups.id'],
            ondelete='SET NULL',
            onupdate='CASCADE',
            name='work_group_fk'
        ),
    )


class Group(Base):
    __tablename__ = 'groups'

    id = Column(Integer, autoincrement=True)
    name = Column(String(512), nullable=True)

    __table_args__ = (
        PrimaryKeyConstraint('id', name='group_pk'),
    )


class AssociationContractProject(Base):
    __tablename__ = 'associations_contract_project'

    id = Column(Integer, autoincrement=True)
    contract_id = Column(Integer, nullable=False)
    project_id = Column(Integer, nullable=False)

    __table_args__ = (
        PrimaryKeyConstraint('id', name='association_contract_project_pk'),
        ForeignKeyConstraint(
            ['contract_id'],
            ['contracts.id'],
            ondelete='CASCADE',
            onupdate='CASCADE',
            name='association_contract_project_contract_fk'
        ),
        ForeignKeyConstraint(
            ['project_id'],
            ['projects.id'],
            ondelete='CASCADE',
            onupdate='CASCADE',
            name='association_contract_project_project_fk'
        ),
    )


class AssociationUserGroup(Base):
    __tablename__ = 'associations_user_group'

    id = Column(Integer, autoincrement=True)
    user_id = Column(Integer, nullable=False)
    group_id = Column(Integer, nullable=False)

    __table_args__ = (
        PrimaryKeyConstraint('id', name='association_user_group_pk'),
        ForeignKeyConstraint(
            ['user_id'],
            ['users.id'],
            ondelete='CASCADE',
            onupdate='CASCADE',
            name='association_user_group_user_fk'
        ),
        ForeignKeyConstraint(
            ['group_id'],
            ['groups.id'],
            ondelete='CASCADE',
            onupdate='CASCADE',
            name='association_user_group_group_fk'
        ),
    )


class AssignmentUserProject(Base):
    __tablename__ = 'assignments_user_project'

    id = Column(Integer, autoincrement=True)
    user_id = Column(Integer, nullable=False)
    project_id = Column(Integer, nullable=False)

    assignment_date = Column(Date, nullable=True)
    is_assigned = Column(Boolean, nullable=True)

    __table_args__ = (
        PrimaryKeyConstraint('id', name='assignment_user_project_pk'),
        ForeignKeyConstraint(
            ['user_id'],
            ['users.id'],
            ondelete='CASCADE',
            onupdate='CASCADE',
            name='assignment_user_project_user_fk'
        ),
        ForeignKeyConstraint(
            ['project_id'],
            ['projects.id'],
            ondelete='CASCADE',
            onupdate='CASCADE',
            name='assignment_user_project_project_fk'
        ),
    )


class AssignmentUserContract(Base):
    __tablename__ = 'assignments_user_contract'

    id = Column(Integer, autoincrement=True)
    user_id = Column(Integer, nullable=False)
    contract_id = Column(Integer, nullable=False)

    assignment_date = Column(Date, nullable=True)
    is_assigned = Column(Boolean, nullable=True)

    __table_args__ = (
        PrimaryKeyConstraint('id', name='assignment_user_contract_pk'),
        ForeignKeyConstraint(
            ['user_id'],
            ['users.id'],
            ondelete='CASCADE',
            onupdate='CASCADE',
            name='assignment_user_contract_user_fk'
        ),
        ForeignKeyConstraint(
            ['contract_id'],
            ['contracts.id'],
            ondelete='CASCADE',
            onupdate='CASCADE',
            name='assignment_user_contract_contract_fk'
        ),
    )


class AssignmentEquipmentDepartment(Base):
    __tablename__ = 'assignments_equipment_department'

    id = Column(Integer, autoincrement=True)
    equipment_id = Column(Integer, nullable=False)
    department_id = Column(Integer, nullable=False)

    assignment_date = Column(Date, nullable=True)
    is_assigned = Column(Boolean, nullable=True)

    __table_args__ = (
        PrimaryKeyConstraint('id', name='assignment_equipment_department_pk'),
        ForeignKeyConstraint(
            ['equipment_id'],
            ['equipment.id'],
            ondelete='CASCADE',
            onupdate='CASCADE',
            name='assignment_equipment_department_equipment_fk'
        ),
        ForeignKeyConstraint(
            ['department_id'],
            ['departments.id'],
            ondelete='CASCADE',
            onupdate='CASCADE',
            name='assignment_equipment_department_department_fk'
        ),
    )


class AssignmentEquipmentGroup(Base):
    __tablename__ = 'assignments_equipment_group'

    id = Column(Integer, autoincrement=True)
    equipment_id = Column(Integer, nullable=False)
    group_id = Column(Integer, nullable=False)

    assignment_date = Column(Date, nullable=True)
    is_assigned = Column(Boolean, nullable=True)

    __table_args__ = (
        PrimaryKeyConstraint('id', name='assignment_equipment_group_pk'),
        ForeignKeyConstraint(
            ['equipment_id'],
            ['equipment.id'],
            ondelete='CASCADE',
            onupdate='CASCADE',
            name='assignment_equipment_group_equipment_fk'
        ),
        ForeignKeyConstraint(
            ['group_id'],
            ['groups.id'],
            ondelete='CASCADE',
            onupdate='CASCADE',
            name='assignment_equipment_group_group_fk'
        ),
    )
