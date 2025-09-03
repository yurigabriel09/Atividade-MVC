from flask import render_template, request, jsonify, redirect, url_for
from models.task import Task
from models.user import db
from models.user import User

class TaskController():


    @staticmethod
    def list_tasks():
        tasks = db.session.query(Task).all()
        return render_template('tasks.html', tasks=tasks)

    @staticmethod
    def create_task():
        if request.method == 'POST':
            title = request.form.get('title')
            description = request.form.get('description')
            user_id = request.form.get('user_id')
            
            if not title or not user_id:
                return redirect(url_for('task_new'))
            
            task = Task(title=title, description=description, user_id=int(user_id))
            db.session.add(task)
            db.session.commit()
            return redirect(url_for('tasks'))
        else:
            users = db.session.query(User).all()
            return render_template('create_task.html', users=users)

    @staticmethod
    def update_task_status(task_id):
        task = db.session.query(Task).filter_by(id=task_id).first()
        if task:
            if task.status == 'Pendente':
                task.status = 'Concluído'
            else:
                task.status = 'Pendente'
            db.session.commit()
        return redirect(url_for('tasks'))

    @staticmethod
    def delete_task(task_id):
        task = db.session.query(Task).filter_by(id=task_id).first()
        if task:
            db.session.delete(task)
            db.session.commit()
        return redirect(url_for('tasks'))