from flask import Flask, render_template, flash
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired



#Create a flask instance 
app = Flask(__name__)
app.config['SECRET_KEY'] = "my super secret key that no one is supposed to know"

#Create a Form class
class NamerForm(FlaskForm):
    name = StringField("What's your name", validators=[DataRequired()])
    submit = SubmitField("Submit")

    #BooleanField
    #DateField
    #DateTimeField
    #DecimalField
    #FileField
    #HiddenField
    #MultipleField
    #FieldList
    #FloatField
    #FormField
    #IntegerField
    #PasswordField
    #RadioField
    #SelectField
    #SelectMultipleField
    #SubmitField
    #StringField
    #TextAreaField

    ##Validators
    #DataRequired
    #Email
    #EqualTo
    #InputRequired
    #IPAddress
    #Length
    #MacAddress
    #NumberRange
    #Optional
    #Regexp
    #URL
    #UUID
    #AnyOf
    #NoneOf


#Create  a route decorator
@app.route('/')

#def index():
    #return "<h1>Hello World!</h1>"

#safe makes a text bold
#

def index():
    first_name = "Natasha"
    stuff = "This is bold text"

    favorite_pizza = ["Pepperoni", "Cheese", "Mushroom", "Pineapple"]


    return render_template("index.html", 
        first_name=first_name,
        stuff=stuff,
        favorite_pizza = favorite_pizza)

#localhost:5000/user/john
@app.route('/user/<name>')

#def user(name):
   # return  "<h1>Hello {}!</h1>".format(name)

def user(name):
    return render_template("user.html", user_name=name)

#Custom Error Pages

#Invalid URL
@app.errorhandler(404)
def page_not_found(e):
    return render_template("404.html"), 404

#Internal Server Error URL
@app.errorhandler(500)
def page_not_found(e):
    return render_template("500.html"), 500

#Create name page 
@app.route('/name', methods=['GET', 'POST'])
def name():
    name = None
    form = NamerForm()
    #Validate Form
    if form.validate_on_submit():
        name = form.name.data
        form.name.data = ''
        flash("Form Submitted Successfuly")

    return render_template("name.html",
        name = name,
        form = form)
