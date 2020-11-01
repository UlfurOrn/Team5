# Authentication
Information for the authentication folder used by the REST-API. 

### Table of contents
* [General info](#general-info)
* [Interface](#interface)
* [Plugins](#plugins)
* [Test](#test)

## General info
This folder contains classes related to password validity, including an interface,
plugins and a password security test.

## Interface
The authentication interface file contains the AuthInterface class. This class should
be inherited by all plugins used for the auth test system.


## Plugins
The authentication plugins file contains the Plugin classes. These classes implement
the authentication interface and test a specific thing about an inputted password.

## Test
The authentication test file contains the AuthTest class. This class has a list of
plugins that test the password. It also contains a MIN_SECURITY_LEVEL for the number
of plugins needed to be valid. The method returns a True/False value depending
on if the password is valid or not.