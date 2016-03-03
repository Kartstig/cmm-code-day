#!/usr/bin/ python
# -*- coding: utf-8 -*-

from Config import *
from tracker import db
from tracker.models.Customer import Customer
from tracker.models.User import User
from tracker.models.Project import Project
from tracker.models.Task import Task
from tracker.models.TaskEntry import TaskEntry

def add_tasks():
    tasks = [
        {'name': 'Looking at cat pictures'},
        {'name': 'Surfing Reddit'},
        {'name': 'Fixing your failed builds'}
    ]

    add_objects(tasks, Task)

def add_objects(input_array, obj):
    try:
        print "Building {}...".format(obj.__tablename__)
        for l in input_array:
            db.session.add(obj(**l))
        print "Done"
    except:
        print "Failed"

if __name__ == '__main__':
    pass
