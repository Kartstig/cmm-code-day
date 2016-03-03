#!/usr/bin/ python
# -*- coding: utf-8 -*-

from Base import Base
from sqlalchemy import Column, Integer, String, DateTime, ForeignKey
from datetime import datetime

class Project(Base):

    __tablename__ = 'projects'

    id                  = Column(Integer, primary_key=True)
    customer_id         = Column(Integer, ForeignKey('customers.id'), nullable=False)
    name                = Column(String(50), nullable=False)
    created_at          = Column(DateTime, nullable=False)
    updated_at          = Column(DateTime, nullable=False)

    def __init__(self, name, customer_id):
        timestamp = datetime.now()
        self.name           = name
        self.customer_id    = customer_id
        self.created_at     = timestamp
        self.updated_at     = timestamp

    def __repr__(self):
        return '<{}, {}>'.format(self.__class__.__name__, self.name)
