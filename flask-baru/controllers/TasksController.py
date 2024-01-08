from flask_sqlalchemy import SQLAlchemy
from flask import jsonify, request
from models.modelTables import Task, db, TaskSchema
from marshmallow import validate
 
 
task_schema = TaskSchema()
tasks_schema = TaskSchema(many=True)
 
def index():
    tasks = Task.query.all()
    response = []
    for task in tasks: response.append(task.to_dict())
    return jsonify(response), 200

def store():
    
 
    try:
        request_form = request.form.to_dict()
        errors = task_schema.validate(request_form, session=db.session)
        if(errors):
            return jsonify({"Error: ": errors}), 400
        new_task = Task(
            title = request_form['title'],
            description = request_form['description'],
            done = bool(request_form['done'])
        )
  
        db.session.add(new_task)
        db.session.commit()
  
        return jsonify({"message": "Data berhasil ditambahkan"}), 201
 
    except Exception as e:
     
        return jsonify({'error': str(e)}), 500

def show(task_id):
    response = Task.query.get(task_id)
    if(response):
        response = Task.query.get(task_id).to_dict()
        return jsonify(response)
    else:
        return jsonify({"mesasge": "Data not found"}), 404

def update(task_id):
    data = Task.query.get(task_id)
    if(data):
        request_form = request.form.to_dict()
        data.title = request_form['title']
        data.description = request_form['description']
        return jsonify({"data": "Data berhasil diupdate"}), 200
    else:
        return jsonify({"message": "Data tidak ditemukan"}), 404

def delete(task_id):
    check = Task.query.get(task_id)
    if(check):
        Task.query.filter_by(task_id=task_id).delete()
        db.session.commit()
        return jsonify({"message": "Data berhasil dihapus"}), 200
    else:
        return jsonify({"message": "Data not found", "status": 400})

# from flask_sqlalchemy import SQLAlchemy
# from flask import jsonify, request
# from models.modelTables import Task, db

# # db = SQLAlchemy()

# def index():
#     tasks = Task.query.all()
#     response = []
#     for task in tasks: response.append(task.to_dict())
#     return jsonify(response), 200
# def store():
#     request_form = request.form.to_dict()
#     new_task = Task(
#         title = request_form['title'],
#         description = request_form['description'],
#         done = bool(request_form['done'])
#         )
#     db.session.add(new_task)
#     db.session.commit()

#     response = Task.query.get(new_task.task_id).to_dict()
#     return jsonify({"message": "Data berhasil ditambahkan"}), 201

# def show(task_id):
#     response = Task.query.get(task_id)
#     if(response):
#         response = Task.query.get(task_id).to_dict()
#         return jsonify(response)
#     else:
#         return jsonify({"mesasge": "Data not found"}), 404

# def update(task_id):
#     data = Task.query.get(task_id)
#     if(data):
#         request_form = request.form.to_dict()
#         data.title = request_form['title']
#         data.description = request_form['description']
#         return jsonify({"data": "Data berhasil diupdate"}), 200
#     else:
#         return jsonify({"message": "Data tidak ditemukan"}), 404

# def delete(task_id):
#     check = Task.query.get(task_id)
#     if(check):
#         Task.query.filter_by(task_id=task_id).delete()
#         db.session.commit()
#         return jsonify({"message": "Data berhasil dihapus"}), 200
#     else:
#         return jsonify({"message": "Data not found", "status": 400})
