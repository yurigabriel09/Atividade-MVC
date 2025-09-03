import os
from flask import Flask
from config import Config # importa as 
from controllers.user_controller import UserController
from models.user import db
from controllers.task_controller import TaskController 

app = Flask(__name__, template_folder=os.path.join('view', 'templates'))
app.config.from_object(Config)

db.init_app(app)

with app.app_context():
    db.create_all()

app.add_url_rule('/', 'index',  UserController.index)
app.add_url_rule('/contact', 'contact', UserController.contact, methods=['GET', 'POST'])
app.add_url_rule('/tasks', view_func=TaskController.list_tasks, methods=['GET'], endpoint='tasks')
app.add_url_rule('/tasks/new', view_func=TaskController.create_task, methods=['GET', 'POST'], endpoint='task_new')
app.add_url_rule('/tasks/update/<int:task_id>', view_func=TaskController.update_task_status, methods=['POST'], endpoint='task_update_status')
app.add_url_rule('/tasks/delete/<int:task_id>', view_func=TaskController.delete_task, methods=['POST'], endpoint='task_delete')


if __name__ == '__main__':
    app.run(debug=True, port=5002)