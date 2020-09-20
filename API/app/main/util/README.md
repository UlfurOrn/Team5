# Util
Information for the util folder used by the REST-API. 

## Table of contents
* [General info](#general-info)
* [DTO](#dto)
* [Mappers](#mappers)

## General info
This folder contains objects that are used as mappers between the REST-API and the Database. The DTO classes are redundant and were only used for the Flask restplus test site. 
#### Dependencies:
* [flask restplus](https://github.com/noirbizarre/flask-restplus) 

## DTO
As previously mentioned these classes are redundant since they are no longer used. They were used by Flask restplus in version 0.1 alpha for a test website to test the REST-API.

## Mappers
This folder contains all the main mapper classes that we use between the REST-API and the Database. Each table in the database has its own mapper class. Each mapper class inherits from the super mapper class that defines functions that transform them into query variables for the database queries and into dictionaries for the REST-API. These mappers simplify our code a lot and removed redundant code from the code base.