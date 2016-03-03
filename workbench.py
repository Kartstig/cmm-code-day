#!/usr/bin/ python
# -*- coding: utf-8 -*-

import csv
from Config import *
from tracker import db
from tracker.models.Customer import Customer
from tracker.models.User import User
from tracker.models.Project import Project
from tracker.models.Task import Task
from tracker.models.TaskEntry import TaskEntry

from sqlalchemy.sql.expression import func

def bootstrap_data():
    add_user()
    add_tasks()
    load_csv()
    add_projects()

def add_tasks():
    tasks = [
        {'name': 'Looking at cat pictures'},
        {'name': 'Surfing Reddit'},
        {'name': 'Fixing your failed builds'}
    ]

    add_objects(tasks, Task)

def load_csv():
    with open('data.csv') as csvfile:
        reader = csv.DictReader(csvfile)
        companies = [r for r in reader]
    add_objects(companies, Customer)

def add_user():
    u = User(
        username =      "kartstig@gmail.com",
        password =      "password",
        first_name =    "Herman",
        last_name =     "Singh"
    )
    db.session.add(u)

def add_projects():
    rand_client = db.session.query(Customer).order_by(func.rand()).first
    projects = [
        {
            "customer_id": 1,
            "name": "Build a time tracker application"
        },
        {
            "customer_id": 2,
            "name": "New landing page"
        },
        {
            "customer_id": 3,
            "name": "Migrate database architectures"
        }
    ]
    add_objects(projects, Project)

def add_objects(input_array, obj):
    try:
        print "Building {}...".format(obj.__tablename__)
        for l in input_array:
            db.session.add(obj(**l))
        print "Done"
    except:
        print "Failed"
    finally:
        db.session.commit()

if __name__ == '__main__':
    pass
