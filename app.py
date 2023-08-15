# importing modules from flask library
from flask import Flask , render_template

# creating instance of class Flask, by providing __name__ keyword as argument
app = Flask(__name__)

# write the routes using decorator functions
# default route or 'URL'
@app.route("/")
def home():

    name = "Sakshi" 
    age = "15" 

    return render_template('index.html' , name = name , age = age)

# define the route to father webpage
@app.route("/father")
def father():

    name = "Father" 
    age = "41" 

    return render_template('father.html' , name = name , age = age)


# define the route to mother webpage
@app.route("/")
def mother():

    name = "Mother" 
    age = "38" 

    return render_template('mother.html' , name = name , age = age)

# define the route to friends webpage
@app.route("/")
def friend():

    name = "Friend" 
    age = "15" 

    return render_template('friend.html' , name = name , age = age)

# add other routes, if you want




# run the file
if __name__  ==  '__main__':
    app.run(debug=True)
