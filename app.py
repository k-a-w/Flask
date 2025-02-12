#Assignment: Project 1 - Flask (due February 12)
#Course: MATH 2213 - Fundamentals of Data Science
#Semester: Spring 2025

from flask import Flask, render_template, request #this imports the flask library
app = Flask(__name__) #initiates a private flask object

@app.route('/')
def madlib():
    return render_template("madlib.html")


@app.route('/result',methods = ['POST', 'GET'])
def result():
    if request.method == 'POST':
        result = request.form
        return render_template("result.html", result = result)



if __name__ == "__main__":
    app.run(host="0.0.0.0",port=5000) #in video port set to 5000