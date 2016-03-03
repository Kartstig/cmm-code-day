#!/usr/bin/ python
# -*- coding: utf-8 -*-

import re, os
from Base import Base
from bcrypt import hashpw, gensalt
from sqlalchemy import Column, Integer, String, DateTime
from datetime import datetime
from flask.ext.login import UserMixin

class User(Base, UserMixin):

    __tablename__ = 'users'

    id                  = Column(Integer, primary_key=True)
    username            = Column(String(50), unique=True, nullable=False)
    password            = Column(String(60))
    first_name          = Column(String(50))
    last_name           = Column(String(50))
    created_at          = Column(DateTime, nullable=False)
    updated_at          = Column(DateTime, nullable=False)
    validation_token    = Column(String(64))
    last_login          = Column(DateTime)

    def __init__(self, username, password=None, first_name=None, last_name=None, 
                 last_login=None):
        timestamp = datetime.now()
        self.username           = username
        self.password           = (self.pass_hash(password)) if password else None
        self.first_name         = first_name
        self.last_name          = last_name
        self.created_at         = timestamp
        self.updated_at         = timestamp
        self.last_login         = last_login

    @staticmethod
    def pass_hash(password):
        return hashpw(password.encode('utf-8'), gensalt())

    def valid_password(self, attempt):
        return (self.password 
            and hashpw(attempt.encode('utf-8'), self.password.encode('utf-8')) == self.password)

    def __repr__(self):
        return '<{}, {}>'.format(self.__class__.__name__, self.username)