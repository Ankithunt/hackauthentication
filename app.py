from flask import Flask, render_template, request
import mysql.connector
app = Flask(__name__)
mydb =mysql.connector.connect(
    host="localhost",
    user="root",
    password="3702",
    database="hacksig"
)
cur = mydb.cursor()

@app.route('/')
def home():
    return render_template('index.html')
@app.route('/hm')
def home1():
    return render_template('home1.html')
@app.route('/hm2')
def home2():
    return render_template('home2.html')


@app.route('/', methods=['GET', 'POST'])
def signup():
    if request.method =='POST':
        name = request.form.get('Name')
        email = request.form.get('Email')
        password = request.form.get('Password')
        

        query = "insert into login values (%s,%s,%s)"
        data=(name,email,password)
        
        
        cur.execute(query,data)
        mydb.commit()
        return render_template('index.html')
    return render_template('home1.html')


@app.route('/hm',methods=['post'])
def login():
    
    uname = request.form['Email']
    pwd = request.form['Password']
   
    
    # Execute a query to retrieve user data
    cur.execute("SELECT password FROM login WHERE email = %s", (uname,))
    user = cur.fetchone()

    if user:
        # Verify the hashed password
        if user[0] == pwd:
            return render_template('home2.html', msg=f"Welcome {uname}")
        else:
            return render_template('index.html', msg="Invalid Password")
    else:
        return render_template('index.html', msg="Invalid Username")


if __name__=='__main__':
    app.run(debug=True)