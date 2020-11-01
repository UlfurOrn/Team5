# Authentication
Information for the authentication folder used by the REST-API. 

### Table of contents
* [General info](#general-info)
* [Interface](#interface)
* [Plugins](#mappers)
* [Test](#Test)

## General info
This folder contains classes related to password validity, including an interface,
plugins and a password security test.

## Interface
The authentication interface file contains the AuthInterface class. This class


## Mappers
This folder contains all the main mapper classes that we use between the REST-API and the Database. Each table in the database has its own mapper class. Each mapper class inherits from the super mapper class that defines functions that transform them into query variables for the database queries and into dictionaries for the REST-API. These mappers simplify our code a lot and removed redundant code from the code base.

## Test
Blas