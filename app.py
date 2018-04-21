"""
This script runs the application using a development server.
It contains the definition of routes and views for the application.
"""

from flask import Flask, render_template,request
app = Flask(__name__)

# Make the WSGI interface available at the top level so wfastcgi can get it.
wsgi_app = app.wsgi_app


@app.route('/hello')
def hello():
    return "Hello World!"




@app.route('/login',methods=["GET","POST"])
def signup():
    if request.method=="POST":
        return "Hello"
    return render_template("hi.html")
'''
    #Initialize the Error variable
    error=None
    #This method will allow the user to sign up and sign in to a web page
    #if the method of request is post, we will display the user page, else we will display the login page
    if request.method=='POST':
        # we want to run the check method
        if(loginCheck(request.form['username'],request.form['password'])):
            #if the user has passed in the correct credentials
            return "Hello"
        else:
            error="Sorry the password or username entered was incorrect"
    else:
        return render_template("hi.html",error)
'''
def loginCheck(username,password):
    #We are simply going to check to see if the password and the username are the same
    return username==password



































if __name__ == '__main__':
    import os
    HOST = os.environ.get('SERVER_HOST', 'localhost')
    try:
        PORT = int(os.environ.get('SERVER_PORT', '5555'))
    except ValueError:
        PORT = 5555
    app.run(HOST, PORT)
