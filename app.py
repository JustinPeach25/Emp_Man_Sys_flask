from flask import Flask, url_for, render_template, redirect, request
from database import get_db
from werkzeug.security import generate_password_hash, check_password_hash

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('home.html')

@app.route('/login')
def login():
    return render_template('login.html')

@app.route('/register', methods = ['GET','POST'])
def register():
    if request.method == 'POST':
        name = request.form['name']
        password = request.form['password']

        hashed_password = generate_password_hash(password)

        db = get_db()
        db.execute('insert in admin ( name, password ) values (?,?)', [name, hashed_password])
        db.commit()
        return redirect(url_for('index'))

    return render_template('register.html')

@app.route('/dashboard')
def dashboard():
    return render_template('dashboard.html')

@app.route('/addnewemployee')
def addnewemployee():
    return render_template('addnewemployee.html')

@app.route('/singleemployeeprofile')
def singleemployeeprofile():
    return render_template('singleemployeeprofile.html')

@app.route('/updateemployee')
def updateemployee():
    return render_template('updateemployee.html')

def logout():
    render_template('home.html')

if __name__ == '__main__':
    app.run(debug=True)