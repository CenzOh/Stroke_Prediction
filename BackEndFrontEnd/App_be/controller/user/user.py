from distutils.command.upload import upload
import os
from flask import Blueprint, redirect, render_template, url_for, session, request
from App_be.config import User, db, application

user_actions = Blueprint('user_actions', __name__, template_folder='templates')

@user_actions.route('/login', methods=['GET', 'POST'])
def login():
    if "user_id" in session:
        return redirect(url_for('home_actions.index'))
    if request.method=='POST':
        user = User.query.filter_by(username=request.form['username'], password=request.form['password']).first()
        if user:
            session['user_id'] = user.id
            return redirect(url_for('home_actions.index'))
        return render_template('login.html', error='Invalid username or password')
    return render_template('login.html')

@user_actions.route('/register', methods=['GET', 'POST'])
def register():
    if "user_id" in session:
        return redirect(url_for('home_actions.index'))
    if request.method=='POST':
        user = User.query.filter_by(username=request.form['username']).first()
        if user:
            return render_template('register.html', error='username already exists')
        user = User(username=request.form['username'], password=request.form['password'], name=request.form['name'])
        db.session.add(user)
        db.session.commit()
        session['user_id'] = user.id
        return redirect(url_for('home_actions.index'))
    return render_template('register.html')

@user_actions.route('/settings', methods=['GET', 'POST'])
def settings():
    if "user_id" not in session:
        return redirect(url_for('user_actions.login'))
    user = User.query.filter_by(id=session['user_id']).first()
    if request.method=='POST':
        if user:
            user.name = request.form['name']
            user.password = request.form['password']
            user.image = upload(request.files.get('image'), user)
            db.session.commit()
        return redirect(url_for('user_actions.settings'))
    return render_template('settings.html', user=user)

@user_actions.route('/logout')
def logout():
    session.clear()
    return redirect(url_for('user_actions.login'))

@user_actions.route('/delete-account')
def delete_account():
    if "user_id" in session:
        User.query.filter_by(id=session['user_id']).delete()
        db.session.commit()
    session.clear()
    return redirect(url_for('user_actions.login'))

def upload(file, user):
    if file.filename:
        new_filename = f'{user.id}_{user.username}.{file.filename.split(".")[-1]}'
        if user.image!='profile.png':
            try:
                os.remove( os.path.join(application.static_folder, 'profiles', user.image))
            except:
                pass
        file.save( os.path.join(application.static_folder, 'profiles', new_filename) )
        return new_filename
    else:
        return user.image
