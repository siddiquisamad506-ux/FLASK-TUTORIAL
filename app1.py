from flask import Flask
from uuid import UUID

app=Flask(__name__)

#STATIC ROUTING
@app.route('/')
def home():
    return "Hello ,Flask!"

@app.route('/about')
def about():
    return"WELCOME TO THE ABOUT PAGE"

# DYNAMIC ROUTING
@app.route('/user/<name>')
def user(name):
    return f"Hello  {name}, WELCOME TO THE USER PAGE !"


@app.route('/student/<name>/<course>')
def student(name,course):
    return f"Hello {name}, you are learning {course} course"

#URL CONVERTERS

@app.route('/add/<int:id>')
def add(id):
    return f"USER ID : {id}"


@app.route('/price/<float:id>')
def price(id):
    return f"price is :{id}"

@app.route('/username/<string:name>')
def username(name):
    return f"username is:{name}"


@app.route('/file/<path:file_path>')
def file(file_path):
    return file_path

@app.route('/classmates/<uuid:user_id>')
def classmates(user_id):
    return str(user_id)

if __name__ == "__main__":
    app.run(debug=True)
    
    