from flask import Flask, render_template, request, url_for, redirect
import mysql.connector
import time
app = Flask(__name__)

# MySQL connection configuration
db = mysql.connector.connect(
    host="localhost",
    user="root",
    password="thegreat1",
    database="street_guardian_db"
)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/casestudy')
def casestudy():
    return render_template('case-study.html')

@app.route('/contact')
def contact():
    return render_template('contact.html')

@app.route('/admin_login')
def admin_login():
    # Your admin login logic goes here
    return render_template('admin_login.html')

@app.route('/share_sighting')
def share_sighting():
    # Your share sighting logic goes here
    return render_template('share_sighting.html')

@app.route('/submit_form', methods=['POST'])
def submit_form():
    cursor = db.cursor()
    if request.method == 'POST':
        full_name = request.form['full_name']
        email = request.form['email']
        phone_number = request.form['phone_number']
        birth_date = request.form['birth_date']
        gender = request.form['gender']
        unsheltered_full_name = request.form['unsheltered_full_name']
        unsheltered_location = request.form['unsheltered_location']
        state = request.form['state']
        city = request.form['city']
        region = request.form['region']
        postal_code = request.form['postal_code']
        
        # Insert data into the database
        insert_query = "INSERT INTO registrations (full_name, email, phone_number, birth_date, gender, unsheltered_full_name, unsheltered_location, state, city, region, postal_code) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"
        values = (full_name, email, phone_number, birth_date, gender, unsheltered_full_name, unsheltered_location, state, city, region, postal_code)
        cursor.execute(insert_query, values)
        db.commit()

        cursor.close()
        time.sleep(7)
        return redirect(url_for('index', message='Form submitted successfully'))


        # sign up and login
@app.route('/signup', methods=['POST'])
def signup():
    if request.method == 'POST':
        username = request.form['username']
        email = request.form['email']
        password = request.form['password']

        # Check if username or email already exists in the database
        cursor = db.cursor()
        cursor.execute("SELECT * FROM users WHERE username = %s OR email = %s", (username, email))
        existing_user = cursor.fetchone()

        if existing_user:
            return "Username or email already exists."
        elif len(password) < 8:
            return "Password must be at least 8 characters long."
        else:
            cursor.execute("INSERT INTO users (username, email, password) VALUES (%s, %s, %s)", (username, email, password))
            db.commit()
            return redirect(url_for('admin_login'))
    else:
        return "Method Not Allowed: Only POST requests are allowed for this URL."


@app.route('/login', methods=['POST'])
def login():
    username = request.form['username']
    password = request.form['password']

    cursor = db.cursor()
    cursor.execute("SELECT * FROM users WHERE username = %s AND password = %s", (username, password))
    user = cursor.fetchone()

    if user:
        return redirect(url_for('dashboard'))
    else:
        return "Invalid username or password."

@app.route('/dashboard')
def dashboard():
    cursor = db.cursor(dictionary=True)  # This will return data as dictionaries instead of tuples
    cursor.execute("SELECT * FROM registrations")
    registrations = cursor.fetchall()
    cursor.close()
    return render_template('dashboard.html', registrations=registrations)

    
if __name__ == '__main__':
    app.run(debug=True)
