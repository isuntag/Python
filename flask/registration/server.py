# Isaac Suntag 7/10/17 isuntag@gmail.com
from flask import Flask, render_template, request, redirect, sessions, flash
import re
import datetime

app = Flask(__name__)
app.secret_key = 'key'

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/submit', methods=['POST'])
def submit():
    email = request.form['email']
    first_name = request.form['first_name']
    last_name = request.form['last_name']
    birthday = request.form['birthday']
    print birthday
    password = request.form['password']
    confirm_password = request.form['confirm_password']
    validation = True
    password_regex = re.search(r'\d', password)
    password_regex2 = re.search(r'[A-Z]', password)
    birthday_regex = re.compile(r'\d\d\d\d+[-]+\d\d+[-]+\d\d')
    if len(email) < 1 or len(first_name) < 1 or len(last_name) < 1 or len(password) < 1 or len(confirm_password) < 1 or len(birthday) < 1 : #Validate that all forms are filled out
        flash('Everything needs to be filled out, yo.')
        validation = False
    if not first_name.isalpha() or not last_name.isalpha(): #validate that first and last name only contain letters
        flash('Your name can only have letters in it...' )
        validation = False
    if len(password) <= 8: #validate that password is greater than 8 characters
        flash('Password has gotta be more than 8 characters')
        validation = False
    if password != confirm_password: #validate that password and confirm password are the same
        flash('Passwords must match. Try again.')
        validation = False
    if not password_regex or not password_regex2: #confirm that password contains at least one number and one capital letter
        flash('Password must contain one number and one capital letter.')
        validation = False
    if not len(birthday) < 1:
        if not birthday_regex.match(birthday): #validate that birthday is in the correct format
            flash('Select an actual date in MM/DD/YYYY format.')
            validation = False
        if datetime.datetime.strptime(birthday, "%Y-%m-%d") > datetime.datetime.now(): #validate that birthday is not past today's date
            flash('So you\'re from the future? Try that again.')
            validation = False
    if validation == True:
        flash('Thanks for submitting your information.')
    return redirect('/')

app.run(debug=True)
