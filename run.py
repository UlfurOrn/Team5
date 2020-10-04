""" A program that serves up the REST api and the WebApp by simply running python run.py
    from the root directory. """

import subprocess

p = subprocess.Popen('cd ./API/app/ & python app.py', shell=True)
q = subprocess.Popen('flask run', shell=True)