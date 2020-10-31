# WebApp
Information for the WebApp folder and all its aspects.

## Table of contents
* [General info](#general-info)
* [Routes](#routes)
* [Services](#services)
* [Static](#static)
* [Templates](#Templates)

## General info
This folder contains all relevant code for the WebApp aside from the
WebApp tests. This folder contains all the HTML, css and python code 
that is neede for the website to run and function like talking to the
REST api.
#### Dependencies:
* [Flask](https://flask.palletsprojects.com/en/1.1.x/)
* [Werkzeug](https://pypi.org/project/Werkzeug/)

## Routes
This folder contains all the logic of the front end such as sending
requests to the REST api, handeling correct forms input, getting 
user input and rendering relevant pages for the website.

## Services
This folder contains all the services the routes need. Currently this
only contains one file with all the REST api calls. It acts as a
mediary between the routes and the REST api and gives back error 
codes in human readable ways.

## Static
This folder contains all static objects that the website needs such
as all the css and image files.

## Templates
This folder contains all the HTML templates of our website. It is
split into 3 subfolders account, auth and habits. Account contains
all account related sites, auth contains the login and register and
habits contains all other sites.