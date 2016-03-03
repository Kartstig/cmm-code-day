#!/usr/bin/ python
# -*- coding: utf-8 -*-

from Base import Base
from sqlalchemy import Column, Integer, String, DateTime
from datetime import datetime

class Task(Base):

    __tablename__ = 'tasks'

    id                  = Column(Integer, primary_key=True)
    name                = Column(String(50), nullable=False)
    created_at          = Column(DateTime, nullable=False)
    updated_at          = Column(DateTime, nullable=False)

    def __init__(self, name):
        timestamp = datetime.now()
        self.name       = name
        self.created_at = timestamp
        self.updated_at = timestamp

    def __repr__(self):
        return '<{}, {}>'.format(self.__class__.__name__, self.name)
