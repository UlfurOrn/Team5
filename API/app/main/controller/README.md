# Controller
Information for the controllers used by the REST api. 

## Table of contents
* [General info](#general-info)
* [Controllers](#controllers)

## General info
This folder contains all the controllers we use for the REST api.
#### Dependencies:
* [flask-restplus](https://flask-restplus.readthedocs.io/en/stable/)
* [Werkzeug](https://pypi.org/project/Werkzeug/)

## Controllers
These controllers represent our routes in the REST api. The routes 
take in a postfix after the ip/url and call database opperations with
the 4 CRUD opperations available. The routes act as a mediery between
the database and the whatever frontend or ui is needed. The routes
are all made using the correct error codes when something goes wrong
as well as providing responses for all opperations.