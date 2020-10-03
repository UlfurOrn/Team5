# Services
Information for the services used by the REST-API. 

## Table of contents
* [General info](#general-info)
* [Usage](#usage)
* [DBapi](#dbapi)

## General info
This folder contains the service classes that are used by the REST-API. Currently that only contains the database connection class that handles all 4 CRUD operations for each table in the Habit tracker database. 
#### Dependencies:
* [psycopg2](https://www.psycopg.org/) 
#### Main contributors:
* [Erla19](https://github.com/erla19)
* [GudjonIV](https://github.com/GudjonIV)

## Usage
The main gateway that should be used to talk to the database is the DBapi which provides access to the IO classes.
If another table is added to the database and you want to add the methods to the DBapi you first need to create a class like the IO classes that inherits from the abstract class Abctable in the repositories folder. You then fill in the 4 CRUD methods and add the new possible IO class to the DBapiCreator and the DBapi.

## DBapi
The DBapi is made from the DBapiCreator which is a class that stores the IO classes in use. The DBapi variable creates such an instance with what ever IO classes you need/prefer.
Then to use this DBapi you can simply call f.x. DBapi.users.get() to get all users from the database.