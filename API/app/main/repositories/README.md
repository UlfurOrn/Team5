# Repositories
Information for the repositories used by the DBapi. 

## Table of contents
* [General info](#general-info)
* [Abctable](#abctable)
* [IO classes](#io_classes)

## General info
This folder contains all the database input and output classes. These classes are used by the DBapi in the services folder.
#### Dependencies:
* [psycopg2](https://www.psycopg.org/) 
#### Main contributors:
* [Erla19](https://github.com/erla19)
* [GudjonIV](https://github.com/GudjonIV)

## Abctable
The Abctable class is an abstract class that provides the template for all the CRUD operations (GET, POST, PUT, DELETE) as well as providing a class variable that creates the connection to the database and a cursor to execute commands in the database. When creating a new table IO class it should inherit this class to get access to the database and to make sure it implements the correct methods.

## IO classes
These classes represent each table in the Habit tracker database. The classes inherit from the Abctable to get the connection and cursor to the database. Each class then has their own implementation of the 4 CRUD operations. The DBapi then talks to these classes to access the database. These classes are named ...io because we think it describes their purpose better since they handle input and output from the database. 