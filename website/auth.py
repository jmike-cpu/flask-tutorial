from flask import Blueprint, render_template, request, flash

auth = Blueprint('auth',__name__)

@auth.route('/login', methods=['GET','POST'])
def login():  
    return render_template("login.html")

@auth.route('/logout')
def logout():
    return "<p>logout</p>"

@auth.route('/signUp', methods=['GET','POST'])
def signUp():
    if request.method =='POST':
        email = request.form.get('email')
        firstname = request.form.get('firstname')
        password1 = request.form.get('password1')
        password2 = request.form.get('password2')

        if len (password1) !=password2:
            flash("passwords do not much .",category='error')
        elif len(password1) < 7:
            flash('password must be at least 7 characters. ',category='error')

    return render_template("signUp.html")


