#!/usr/bin/ python
# -*- coding: utf-8 -*-

from flask import Flask, render_template
from flask.ext.sqlalchemy import SQLAlchemy
from config import app_config

# Main Application and Config
app = Flask('cmm')
app.config.from_object(app_config)

# Database initialization
db = SQLAlchemy(app=app)

@app.route('/', methods=['GET'])
def index():
    return "Hello"
