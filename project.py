from flask import Flask,render_template,flash
from flask_wtf import FlaskForm
from wtforms import TextAreaField,SubmitField,StringField,BooleanField
from wtforms.validators import DataRequired,Length

app = Flask('project')
app.secret_key = 'nata'

@app.route('/about_me')
def about_me():
    return render_template('about_me.html')

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/natabuli', methods=['GET','POST'])
def natabuli():
    form = NataForm()
    return render_template('natabuli/home.html',form=form)


class NataForm(FlaskForm):
    body = TextAreaField(label='messages',validators=[DataRequired(message=u'说点什么吧，哈哈'), Length(1,300)])
    name = StringField('yourname',validators=[DataRequired(message=u'需要留下你的大名哟，啦啦')])
    ano = BooleanField('匿名提交')
    submit = SubmitField('submit')


if __name__ == '__main__':
    app.run()