from flask import g
from flask import render_template
from flask import redirect
from flask import url_for
from flask import request
from flask import flash
from flask.ext.login import current_user
from flask.ext.login import login_user
from flask.ext.login import logout_user
from flask.ext.login import login_required

from app import app
from app import db
from .forms import GuessForm
from .forms import LoginForm
from .forms import RegisterForm
from .models import User
from .models import Guess
from .utils import hash_password


@app.route('/', methods=['GET', 'POST'])
def index():
    if not g.user.is_authenticated():
        return render_template('index.html', form=None, user=g.user)
    form = GuessForm()
    if form.validate_on_submit():
        gender = form.gender.data
        hair = form.hair.data
        weight = form.weight.data
        length = form.length.data
        eyes = form.eyes.data
        name = form.name.data
        guess = Guess.query.filter_by(user=g.user.email).first()
        if guess:
            guess.gender = gender
            guess.hair = hair
            guess.weight = weight
            guess.length = length
            guess.eyes = eyes
            guess.name = name
        else:
            guess = Guess(gender=gender, hair=hair, weight=weight, length=length, eyes=eyes, name=name, user=g.user.email)
        db.session.add(guess)
        db.session.commit()
        flash('Your guess has been submitted! Resubmitting this form will overwrite your previous guess', 'good')
        return redirect(url_for('index'))
    return render_template('index.html', form=form, user=g.user)


@app.route('/login', methods=['GET', 'POST'])
def login():
    if g.user is not None and g.user.is_authenticated():
        return redirect(url_for('index'))
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.get(form.email.data.lower())
        if user:
            if user.password == hash_password(form.password.data):
                user.authenticated = True
                db.session.add(user)
                db.session.commit()
                login_user(user, remember=True)
                flash('Successfully logged in', 'good')
                return redirect(url_for('index'))
            else:
                flash('Not a valid username or password', 'error')
                return redirect(url_for('login'))
        else:
            flash('Not a valid username or password', 'error')
            return redirect(url_for('login'))
    return render_template('login.html', form=form, user=g.user)


@app.route('/logout')
@login_required
def logout():
    user = current_user
    user.authenticated = False
    db.session.add(user)
    db.session.commit()
    logout_user()
    return redirect(url_for('index'))


@app.route('/register', methods=['GET', 'POST'])
def register():
    form = RegisterForm()
    if form.validate_on_submit():
        user = User.query.get(form.email.data.lower())
        if user:
            flash('That user already exists', 'error')
            return redirect(url_for('register'))
        user = User(email=form.email.data.lower(), password=hash_password(form.password.data))
        db.session.add(user)
        db.session.commit()
        flash('User successfully registered', 'good')
        return redirect(url_for('login'))
    return render_template('register.html', form=form, user=g.user)


@app.before_request
def before_request():
    g.user = current_user
