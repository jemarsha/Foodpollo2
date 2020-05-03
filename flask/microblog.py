from app import app

#Run this on the terminal to let flask know how to import the application: export FLASK_APP=microblog.py
#from the app package (i.e.folder) import the app variable in init_.py

#Flask uses the freely available port 5000

#Then run in a web browser this server "http://localhost:5000/"  which maps to the routes.py url @app.route('/')

#Alternatively can run "http://localhost:5000/index"  which maps to the routes.py line @app.route('/index')


#Since environment variables
#aren't remembered across terminal sessions, you may find tedious to always
#have to set the FLASK_APP environment variable when you open a new terminal window """