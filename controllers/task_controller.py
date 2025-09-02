from flask import render_template
from models.task import Task
from config.database import db

class TaskController:

    @staticmethod
    def list_tasks():
        
        tasks = db.session.query(Task).all()


        return render_template('tasks.html', tasks=tasks)
