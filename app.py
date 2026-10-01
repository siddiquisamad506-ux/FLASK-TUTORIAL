from flask import Flask,request

app=Flask(__name__)

#QUERY PARAMETERS/MULTIPLE PARAMETERS
@app.route('/search')
def search():
    name=request.args.get('name','Guest')
    course=request.args.get('course','unknown')
    return f"{name} is learning {course} course"




if __name__ == "__main__":
    app.run(debug=True)
    
