from flask import Flask, render_template, redirect, url_for, flash
from forms import registerform, loginform, addform
from flask_login import current_user, login_user, logout_user
from os import path
from ext import app, db
from models import News, usser
from werkzeug.security import generate_password_hash, check_password_hash
app.config["SECRET_KEY"] = "QWWEQDqkekwk12@123"
UPLOAD_FOLDER = path.join(app.root_path, "static/images")



@app.route('/addnews', methods=["GET", "POST"])
def addnew():
    addnews = addform()
    if addnews.validate_on_submit():


        file = addnews.img.data

        add = News(title=addnews.title.data,
                   text=addnews.text.data,
                   img=file.filename
                   )
        db.session.add(add)
        db.session.commit()
        file = addnews.img.data
        file.save(path.join(UPLOAD_FOLDER, file.filename))
        return redirect(url_for('home'))
    return render_template('addnews.html', addnews=addnews)

@app.route('/') 
def home():
    all_news = News.query.all()
    return render_template('home.html', news=all_news)

@app.route("/logout")
def logout():
    logout_user()
    return redirect("/")

@app.route('/profile')
def profile():
    return render_template('profile.html')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/contact')
def contact():
    return render_template('contact.html')

@app.route('/home')
def main():
    all_news = News.query.all()
    return render_template('home.html', news=all_news)

@app.route('/delete/<int:id>')
def delete_news(id):
    newss = News.query.get_or_404(id)

    db.session.delete(newss)
    db.session.commit()
    return redirect(url_for('home'))



@app.route('/cardinfo/<int:news_id>')
def mains(news_id):
    newss = News.query.get(news_id)
    if not newss:
        return "ახალი ამბავი ვერ მოიძებნა"
    return render_template('cardinfo.html', newss=newss)

@app.route('/login', methods=["GET", "POST"])
def login():
    form = loginform()
    if form.validate_on_submit():
        user = usser.query.filter_by(email=form.email.data).first()
        if user and check_password_hash(user.password, form.password.data):
            login_user(user)
            return redirect("/")

        
    return render_template('login.html', form=form)

@app.route('/signup', methods=["GET", "POST"])
def signup():
    form = registerform()
    if form.validate_on_submit():

        is_admin = form.email.data == "tirkiamisha@gmail.com"
        hashed_password = generate_password_hash(form.password.data)
        user = usser(username=form.username.data,
                    password=hashed_password,
                    email=form.email.data,
                    is_admin=is_admin)
        
        db.session.add(user)
        db.session.commit()
        return redirect(url_for('login'))
    return render_template('signup.html', form=form)
