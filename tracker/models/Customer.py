#!/usr/bin/ python
# -*- coding: utf-8 -*-

from Base import Base
from sqlalchemy import Column, Integer, String, DateTime, ForeignKey
from datetime import datetime

class Customer(Base):

    __tablename__ = 'customers'

    id                  = Column(Integer, primary_key=True)
    company             = Column(String(50), nullable=False)
    address1            = Column(String(50))
    address2            = Column(String(50))
    address3            = Column(String(50))
    city                = Column(String(50))
    state               = Column(String(50))
    zipcode             = Column(String(50))
    phone1              = Column(String(50))
    phone2              = Column(String(50))
    fax1                = Column(String(50))
    fax2                = Column(String(50))
    email               = Column(String(50))
    website1            = Column(String(255))
    website2            = Column(String(255))
    website3            = Column(String(255))
    created_at          = Column(DateTime, nullable=False)
    updated_at          = Column(DateTime, nullable=False)

    def __init__(self, company, address1=None, address2=None, address3=None,
            city=None, state=None, zipcode=None, phone1=None, phone2=None,
            fax1=None, fax2=None, email=None, website1=None, website2=None,
            website3=None):
        timestamp = datetime.now()
        self.company        = company
        self.address1       = address1
        self.address2       = address2
        self.address3       = address3
        self.city           = city
        self.state          = state
        self.zipcode        = zipcode
        self.phone1         = phone1
        self.phone2         = phone2
        self.fax1           = fax1
        self.fax2           = fax2
        self.email          = email
        self.website1       = website1
        self.website2       = website2
        self.website3       = website3
        self.created_at     = timestamp
        self.updated_at     = timestamp

    def __repr__(self):
        return '<{}, {}>'.format(self.__class__.__name__, self.company)
