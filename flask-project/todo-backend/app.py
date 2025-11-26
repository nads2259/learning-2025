from flask import Flask,request,jsonify
from flask_cors import CORS
import sqlite3
import os

app = Flask(__name__)
CORS(app)

DB_NAME = "tasks.db"

# Create the table if not exists
def init_db():
    
    if not os.path.exists(DB_NAME):
        
        conn = sqlite3.connect(DB_NAME)
        cur = conn.cursor()
        cur.execute('''
                    CREATE TABLE tasks (id integer primary key autoincrement, text TEXT not null);
                    ''')
        
        conn.commit()
        conn.close()


# Fetch all tasks
@app.route('/api/tasks',methods = ['GET'])
def get_tasks():
    
    conn = sqlite3.connect(DB_NAME)
    cur = conn.cursor()
    cur.execute('select id,text from tasks order by id desc;')
    rows = cur.fetchall()
    conn.close()
    
    tasks = [{'id' : row[0],'text' : row[1]} for row in rows]
    return jsonify(tasks)


# Add a task
@app.route('/api/tasks',methods = ['POST'])
def add_task():
    
    data = request.get_json() or {}
    text = (data.get('text') or "").strip()
    
    if not text:
        return jsonify({'error' : 'Task is empty'}),400
    
    conn = sqlite3.connect(DB_NAME)
    cur = conn.cursor()
    cur.execute('insert into tasks (text) values (?);',(text,))
    conn.commit()
    
    task_id = cur.lastrowid
    conn.close()
    
    return jsonify({'id' : task_id,'text' : text}),201
    
# Delete a task
@app.route('/api/tasks/<int:task_id>',methods = ['DELETE'])
def delete_task(task_id):
    
    conn = sqlite3.connect(DB_NAME)
    cur = conn.cursor()
    cur.execute('delete from tasks where id = ?;',(task_id,))
    conn.commit()
    
    deleted_rows = cur.rowcount
    conn.close()
    
    if deleted_rows:
        return jsonify({'deleted' : True})
    else:
        return jsonify({'deleted' : False,'error' : 'Task not found'}),404


if __name__ == "__main__":
    init_db()
    app.run(debug=True)