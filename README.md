# CheckPoint
# Installation
1) First of all you need to have python and git installed: https://www.python.org/ https://git-scm.com/
1) Navigate to the folder you want the project to be installed in and open up the console
2) Clone the project from github: git clone https://github.com/Loevik737/CheckPoint.git
3) Set up an viritual envirement: pip install virtualenv
4) Create the envirement: virtualenv venv
5) Activate the envirement: . venv/bin/activate Or on windows: cd venv/Scripts and run(write) activate
6) Navigate into the project you cloned earlier: cd CheckPoint/
7) Install the projects requirements: pip install -r requirements.txt
8) Create the database tables: python manage.py migrate
9) Run the server: python manage.py runserver
- The site is now running on a local server and you can access it from: http://127.0.0.1:8000/
  To run tests to see the sites test coverage run: python manage.py test --with-coverage

