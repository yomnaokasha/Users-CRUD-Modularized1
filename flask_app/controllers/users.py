from flask import render_template, redirect, request
from flask_app.models.user import User
from flask_app import app


@app.route('/users')
def users():
    users = User.get_all()
    return render_template("index.html", all_users=users)


@app.route('/users/new')
def add_user():
    return render_template("form.html")


@app.route('/users/create', methods=['post'])
def create_user():
    # first_name = request.form['first_name']
    # last_name = request.form['last_name']
    # email = request.form['email']
    User.add(request.form)
    return redirect('/users')


@app.route('/users/<int:user_id>')
def show(user_id):
    data = {
        "id": user_id,
    }
    user = User.get_one(data)
    return render_template("show.html", user=user)


@app.route('/users/<int:user_id>/edit')
def edit_user(user_id):
    data = {
        "id": user_id,
    }
    user = User.get_one(data)
    return render_template('edit.html', user=user)


@app.route('/users/<int:user_id>/update', methods=['post'])
def update(user_id):
    data = {
        "id": user_id,
        "first_name": request.form['first_name'],
        "last_name": request.form['last_name'],
        "email": request.form['email'],
    }

    User.update_info(data)
    return redirect(f'/users/{user_id}')


@app.route('/users/<int:user_id>/destroy')
def delete_user(user_id):
    data = {
        "id": user_id,
    }
    User.delete(data)
    return redirect('/users')
