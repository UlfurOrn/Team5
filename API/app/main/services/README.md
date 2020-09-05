# Services
Information for the services used by the REST-API. 

## Table of contents
* [General info](#general-info)
* [Usage](#usage)
* [DBapi](#dbapi)
* [Abctable](#abctable)
* [IO classes](#io-classes)

## General info
This folder contains the service classes that are used by the REST-API. Currently that only contains the database connection classes that handle all 4 CRUD operations for each table in the Habit tracker database. 
#### Dependencies:
* [psycopg2](https://www.psycopg.org/) 
#### Main contributors:
* [Erla19](https://github.com/erla19)
* [GudjonIV](https://github.com/GudjonIV)

## Usage
The main gateway that should be used to talk to the database is the DBapi which provides a method for each table in database that take in arguments related to what operations to perform.   
If another table is added to the database and you want to add the methods to the DBapi you first need to create a class like the IO classes that inherits from the abstract class Abctable. You then fill in the 4 CRUD methods. Then you can make a new method in the DBapi that talks to that class.

## DBapi
As previously mentioned the DBapi is the main gateway that should be used if you want to talk to the database. Each method in the class represents and individual table that takes in arguments (method, id, data) which calls the corresponding IO classes. Each method can easily be removed or added if a table is removed or added to the database.  

## Abctable
The Abctable class is an abstract class that provides the template for all the CRUD operations (GET, POST, PUT, DELETE) as well as providing a class variable that creates the connection to the database and a cursor to execute commands in the database. When creating a new table IO class it should inherit this class to get access to the database and to make sure it implements the correct methods.

## IO classes
These classes represent each table in the Habit tracker database. The classes inherit from the Abctable to get the connection and cursor to the database. Each class then has their own implementation of the 4 CRUD operations. The DBapi then talks to these classes to access the database.