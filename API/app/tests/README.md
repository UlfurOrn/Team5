# Tests
This folder contains all the unit tests of the project.

## Table of contents
* [General Info](#general-info)
* [Usage](#usage)

## General Info
The tests are split into two different directories. The database directory contains all tests from the DBapi down to the database and the endpoints directory contains all the tests for the api endpoints. The tests related to the database run on a different test database that contains a few simple rows of data. The "BEGIN;" and "ROLLBACK;" in the tests are to make sure that database stays consistent.

## Usage
To run the tests use pytest from within the root, API or app directory
``` sh
$ pytest
```
To get code coverage run pytest in coverage
```sh
$ coverage -m pytest
```
Then to see the coverage report
```sh
$ coverage report -m
```