from flask import Flask,render_template,flash,redirect, url_for
from flask_wtf import FlaskForm
from wtforms import TextAreaField,SubmitField,StringField,BooleanField
from wtforms.validators import DataRequired,Length
import sqlite3

app = Flask('project')
app.secret_key = 'nata'

conn = sqlite3.connect("Nata.db",check_same_thread=False)
db = conn.cursor()

@app.route('/about_me')
def about_me():
    return render_template('about_me.html')

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/natabuli', methods=['GET','POST'])
def natabuli():
    form = NataForm()
    if form.validate_on_submit():
        body = form.body.data
        name = form.name.data

        try:
            db.execute('CREATE TABLE message(content text)')

        except:
            print("CREATE TABLE message...  Failed!")

        print('INSERT INTO message VALUES ("%s")' % (body))
        try:
            db.execute('INSERT INTO message VALUES ("%s")' % (body))
        except:
            print("Failed!")


        conn.commit()
        flash('Your message have been sent to the world!')

    else:print("表单验证不通过")


    return render_template('natabuli/home.html',form=form)


class NataForm(FlaskForm):
    body = TextAreaField(label='messages',validators=[DataRequired()])
    name = StringField('yourname',validators=[DataRequired()])
    ano = BooleanField('匿名提交')
    submit = SubmitField('submit')


if __name__ == '__main__':
    app.run()