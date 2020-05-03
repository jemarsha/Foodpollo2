#View Functions - Mapped one or more route urls so that flask knows what logic to execute when a client requests a given url
from flask import render_template
from app import app

@app.route('/')  #@app.route decorater creates an association between the url.  IN this cause the URL is '/'
#this means that when a web browser requests either of these flask is going to invoke this function and pass return value back to browser as response.
@app.route('/index')  #in this case the url is '/index'
def index():
    user = {'username': 'Ashy'}

    # return "Hello, World!"

    #The render_template() function invokes the Jinja2 template engine that comes bundled with the Flask framework
    return render_template('index.html',title= 'Home', user=user) #if you remove title variable, else statement executes in index.html
    # #The operation that converts a template into a complete HTML page is called rendering
    #This function takes a template filename and a variable list of template arguments and returns the same template,
    # but with all the placeholders in it replaced with actual values





