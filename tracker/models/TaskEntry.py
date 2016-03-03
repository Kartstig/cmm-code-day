#!/usr/bin/ python
# -*- coding: utf-8 -*-

from Base import Base
from sqlalchemy import Column, Integer, String, DateTime, ForeignKey, Float
from sqlalchemy.orm import relationship
from datetime import datetime

class TaskEntry(Base):

    __tablename__ = 'task_entries'

    id                  = Column(Integer, primary_key=True)
    start               = Column(DateTime, nullable=False)
    duration            = Column(Float(precision=1, asdecimal=True))
    task_id             = Column(Integer, ForeignKey('tasks.id'), nullable=False)
    project_id          = Column(Integer, ForeignKey('projects.id'), nullable=False)
    user_id             = Column(Integer, ForeignKey('users.id'), nullable=False)
    created_at          = Column(DateTime, nullable=False)
    updated_at          = Column(DateTime, nullable=False)

    user = relationship("User",
        foreign_keys="TaskEntry.user_id",
        backref="task_entries")

    project = relationship("Project",
        foreign_keys="TaskEntry.project_id",
        backref="task_entries")

    task = relationship("Task",
        foreign_keys="TaskEntry.task_id",
        backref="task_entries")

    def __init__(self, task_id, project_id, user_id, start=None, duration=None):
        timestamp       = datetime.now()
        self.start      = start if start else timestamp
        self.duration   = duration
        self.task_id    = task_id
        self.project_id = project_id
        self.user_id    = user_id
        self.created_at = timestamp
        self.updated_at = timestamp

    def __repr__(self):
        return '<{}, {}>'.format(self.__class__.__name__, self.id)
