from flask import Flask, render_template

#Create a flask instance 
app = Flask(__name__)

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