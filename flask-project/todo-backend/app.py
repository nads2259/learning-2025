from flask import Flask,request,jsonify,g
from flask_cors import CORS
import sqlite3
import os
import datetime
import jwt
from werkzeug.security import generate_password_hash,check_password_hash
from functools import wraps

app = Flask(__name__)
CORS(app)

DB_NAME = "tasks.db"
SECRET_KEY = "ilovecoding"

# Create the table if not exists
def init_db():
    
    if not os.path.exists(DB_NAME):
        
        conn = sqlite3.connect(DB_NAME)
        cur = conn.cursor()
        
        # Create users table
        cur.execute('''
                    CREATE TABLE IF NOT EXISTS users (id integer primary key autoincrement, email TEXT UNIQUE NOT NULL, password_hash TEXT NOT NULL);
                    ''')
        
        cur.execute('''
                    CREATE TABLE IF NOT EXISTS tasks (id integer primary key autoincrement, user_id INTEGER NOT NULL, text TEXT not null, FOREIGN KEY (user_id) REFERENCES users(id));
                    ''')
        
        conn.commit()
        conn.close()

# Create token for user id
def create_token(user_id):
    
    now = datetime.datetime.utcnow()
    expires = now + datetime.timedelta(hours = 12)
    
    payload = {
        'user_id' : user_id,
        'created_at' : now.isoformat() + 'Z',
        'expires_at' : expires,
    }
    
    token = jwt.encode(payload,SECRET_KEY,algorithm = 'HS256')
    return token

# Decode token
def decode_token(token):
    
    try:
        payload = jwt.decode(token,SECRET_KEY,algorithms=['HS256'])
        return payload
    except jwt.ExpiredSignatureError:
        return None
    except jwt.InvalidTokenError:
        return None

def require_auth(f):
    
    @wraps(f)
    def wrapper(*args,**kwargs):
        auth_header =  request.headers.get('Authorization','')
        
        if not auth_header.startswith('Bearer '):
            return jsonify({'error' : 'Missing or invalid Authorization header'}),401
        
        token = auth_header.split(' ',1)[1].strip()
        payload = jwt.decode(token)
        
        if not payload:
            return jsonify({'error' : 'Invalid or expired token'}),401
        
        g.user_id = payload['user_id']
        return f(*args,**kwargs)
    
    return wrapper





# ----- AUTH ROUTES ------

@app.route('/api/register',methods = ['POST','OPTIONS'])
def register():
    
    if request.method == 'OPTIONS':
        return ('',204);
    
    data = request.get_json() or {}
    email = (data.get('email') or '').strip().lower()
    password = data.get('password') or ''
    
    if not email or not password:
        return jsonify({'error' : 'Email and password are required!'}),400
    
    password_hash = generate_password_hash(password)
    
    conn = sqlite3.connect(DB_NAME)
    cur = conn.cursor()
    
    try:
        cur.execute('INSERT INTO users (email,password_hash) values (?,?);', (email,password_hash),)
        conn.commmit()
        user_id = cur.lastrowid
    except sqlite3.IntegrityError:
        conn.close()
        return jsonify({'error' : 'Email already registered'}),400
    
    conn.close()
    
    token = create_token(user_id)
    return jsonify({'token' : token})


@app.route('/api/login',methods = ['POST','OPTIONS'])
def login():
    
    if (request.method == 'OPTIONS'):
        return ('',204);
    
    data = request.get_json() or {}
    email = (data.get('email') or '').strip().lower()
    password = data.get('password') or ''
    
    if not email or not password:
        return jsonify({'error' : 'Email and password are required!'}),400
    
    conn = sqlite3.connect(DB_NAME)
    cur = conn.cursor()
    
    cur.execute('select id,password_hash from users where email = ?;',(email,)) 
    row = cur.fetchone()
    conn.close()
    
    if not row:
        return jsonify({'error' : 'Invalid credentials'}),401
    
    user_id,password_hash = row
    if not check_password_hash(password_hash,password):
        return jsonify({'error' : 'Invalid credentials'}),401
    
    token = create_token(user_id)
    return jsonify({'token' : token})





# ----- TASK ROUTES -----


# Fetch all tasks
@app.route('/api/tasks',methods = ['GET'])
@require_auth
def get_tasks():
   
    user_id = g.user_id
    
    conn = sqlite3.connect(DB_NAME)
    cur = conn.cursor()
    cur.execute('select id,text from tasks where user_id = ? order by id desc;',(user_id,))
    rows = cur.fetchall()
    conn.close()
    
    tasks = [{'id' : row[0],'text' : row[1]} for row in rows]
    return jsonify(tasks)




# Add a task
@app.route('/api/tasks',methods = ['POST'])
@require_auth
def add_task():
    
    user_id = g.user_id
    data = request.get_json() or {}
    text = (data.get('text') or "").strip()
    
    if not text:
        return jsonify({'error' : 'Task is empty'}),400
    
    conn = sqlite3.connect(DB_NAME)
    cur = conn.cursor()
    cur.execute('insert into tasks (user_id,text) values (?,?);',(user_id,text),)
    conn.commit()
    
    task_id = cur.lastrowid
    conn.close()
    
    return jsonify({'id' : task_id,'text' : text}),201
    
# Delete a task
@app.route('/api/tasks/<int:task_id>',methods = ['DELETE'])
@require_auth
def delete_task(task_id):
    
    user_id = g.user_id
    
    conn = sqlite3.connect(DB_NAME)
    cur = conn.cursor()
    cur.execute('delete from tasks where id = ? and user_id = ?;',(task_id,user_id),)
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