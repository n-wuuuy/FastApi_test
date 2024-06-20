from sqlalchemy import Column, Integer, String, ForeignKey, Boolean, LargeBinary, DateTime
from sqlalchemy.orm import relationship

from src.database import Base


class Task(Base):
    __tablename__ = "task"

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String)
    description = Column(String)
    completed = Column(Boolean)
    photo = Column(LargeBinary)
    deadlines = Column(DateTime)
    group_id = Column(Integer, ForeignKey("group_tasks.id"))

    group_tasks = relationship("GroupTasks", backref="group", foreign_keys=[group_id])


class GroupTasks(Base):
    __tablename__ = "group_tasks"

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String)
    description = Column(String)

    tasks = relationship("Task", backref="tasks")
