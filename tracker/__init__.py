#!/usr/bin/ python
# -*- coding: utf-8 -*-

from datetime import datetime

from flask import Flask, render_template, request, redirect, \
    url_for, flash
from flask.ext.sqlalchemy import SQLAlchemy
from flask.ext.login import LoginManager, login_user, \
    current_user, logout_user
from config import app_config

from tracker.models.User import User
from tracker.models.Customer import Customer
from tracker.models.Project import Project
from tracker.models.Task import Task
from tracker.models.TaskEntry import TaskEntry

# Main Application and Config
app = Flask(__name__)
app.config.from_object(app_config)

# Database initialization
db = SQLAlchemy(app=app)

# Login Manager
login_manager = LoginManager()
login_manager.init_app(app)
@login_manager.user_loader
def load_user(userid):
    return get_user({'id': userid})

@app.route('/', methods=['GET'])
def index():
    bindings = {
        'error': None,
        'user': current_user,
        'projects': db.session.query(Project).all(),
        'tasks': db.session.query(Task).all()
    }
    if current_user and not current_user.is_anonymous:
        u = get_user({'id': current_user.id})
        bindings["task_entries"] = u.task_entries
    return render_template('index.html', **bindings)

@app.route('/task_entry/create/', methods=['POST'])
def te_create():
    errors = {}
    if request.method == 'POST' and current_user and not current_user.is_anonymous:
        start = request.form['start'] if request.form['start'] else datetime.now()
        te = TaskEntry(
            start = start,
            duration = request.form['duration'],
            task_id = request.form['task_id'],
            project_id = request.form['project_id'],
            user_id = current_user.id
            )
        try:
            db.session.add(te)
            db.session.commit()
            flash("Created new time entry")
            return redirect(url_for('index'))
        except:
            db.session.rollback()

@app.route('/task_entry/edit/<int:id>', methods=['GET','POST'])
def te_edit(id=None):
    errors = {}
    if id:
        te = db.session.query(TaskEntry).filter_by(id=id).one()
        if request.method == 'POST' and te:
            te.duration = request.form['duration']
            try:
                db.session.add(te)
                db.session.commit()
                flash("Updated successfully")
            except:
                db.session.rollback
            return redirect(url_for('index'))


@app.route('/login/', methods=['GET','POST'])
def login():
    errors ={}
    if request.method == 'POST':
        user = get_user({'username': request.form['username']})
        if user:
            if user.valid_password(request.form['password']):
                login_user(user, remember=True)
                flash("Logged in successfully")
                return redirect(url_for('index'))
            else:
                errors["password"] = ["Invalid Password"]
        else:
            errors["username"] = ["Invalid Username"]
    return render_template('login.html', errors=errors)

@app.route("/logout/", methods=["GET", "POST"])
def logout():
    logout_user()
    flash("Logged out successfully.")
    return redirect(url_for("login"))

def get_user(filter):
    try:
        return db.session.query(User).filter_by(**filter).one()
    except:
        return None