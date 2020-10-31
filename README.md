[![Contributors][contributors-shield]][contributors-url]
[![Forks][forks-shield]][forks-url]
[![Stargazers][stars-shield]][stars-url]
[![Issues][issues-shield]][issues-url]



<!-- PROJECT LOGO -->
<br />
<p align="center">
  <a href="https://github.com/UlfurOrn/Team5">
    <img src="https://upload.wikimedia.org/wikipedia/en/thumb/b/b7/Reykjavik_University_Logo.svg/1200px-Reykjavik_University_Logo.svg.png" alt="Logo" width="80" height="80">
  </a>

  <h3 align="center">Team 5</h3>

  <p align="center">
    Habit tracking platform for nutritional information
    <br />
    <a href="https://github.com/UlfurOrn/Team5"><strong>Explore the docs »</strong></a>
    <br />
    <br />
    <a href="https://habittracker.gudjoniv.com">View Site</a>
    ·
    <a href="https://github.com/UlfurOrn/Team5/issues">Report Bug</a>
    ·
    <a href="https://github.com/UlfurOrn/Team5/issues">Request Feature</a>
  </p>
</p>



<!-- TABLE OF CONTENTS -->
## Table of Contents

* [About the Project](#about-the-project)
  * [Screenshots](#screenshots)
  * [Built With](#built-with)
* [Getting Started](#getting-started)
  * [Prerequisites](#prerequisites)
  * [Installation](#installation)
* [Testing](#testing)
* [Lecure Aspects](#lecture-aspects)
  * [Sprint 1](#sprint-1)
  * [Sprint 2](#sprint-2)
  * [Sprint 3](#sprint-3)
  * [Sprint 4](#sprint-4)
  * [Sprint 5](#sprint-5)
* [Website](#website)
* [Docker](#docker)
* [Team Members](#team-members)
* [Teacher](#teacher)
* [TA](#ta)



<!-- ABOUT THE PROJECT -->
## About The Project

[![Swagger UI Screen Shot][product-screenshot]](https://i.imgur.com/WP7MQJj.png)

This is the Github repository for Team 5's project in T-302-HONN.
We created a habit tracking platform for any information a user would
like to track like kilometers run, calories eaten, books read etc.
The project was built in 5 sprints using the scrum framework where
each sprint got us closer and closer to our goal of a finished system.  
Sprint 1 consisted of creating a REST api and a Database with a 
database api using Flask-restplus and a Postgresql database.  
Sprint 2 was the start of the website as well as a database redesign,
refactoring of the REST and DB apis and the creation of a logger and
a mail-service. This sprint also included some lecture aspects that
we needed to implement.  
Sprint 3 was mostly about making all the required diagrams and
documenting the design principles as well as more refactoring to
make the codebase more understandable and easily maintainable. We
also added a lot of functionality to the website.  
Sprint 4 was when the website took its current look. We made the
website look a lot better, added functionality, documented some
lecture aspects like risk management, non-functional requirements
and plan logs. We also started hosting the website on a domain and
made a docker container for future hosting. We also added more
functionality to the REST api and did general debugging.  
Sprint 5 was the final sprint. We went over all README files, tied up
loose ends, fixed bugs, wrote more tests, reviewed previous
conditional passes, added final functionality and made the website a
functional application for people to use.  

### Screenshots
Here are a few screenshots of the current system which can also be
accessed at https://habittracker.gudjoniv.com 


### Built With

* [Python][python]
* [Flask][flask]
* [Flask-restplus][flask-restplus]
* [Psycopg2][psycopg2]



<!-- GETTING STARTED -->
## Getting Started

To get a local copy up and running follow these simple steps.

### Prerequisites

* pip
```sh
curl https://bootstrap.pypa.io/get-pip.py -o get-pip.py
python get-pip.py
```

### Installation

1. Clone the repo
```sh
git clone https://github.com/UlfurOrn/Team5.git
```
2. Create a virtual environment(optional)
```sh
python3 -m venv venv
```


API:


1. Move to API folder
```sh
cd API/
```
2. Install packages with pip
```sh
pip install -r requirements.txt
```
3. Move to main app folder
```sh
cd app/
```
4. Run the API
```sh
python app.py
```
5. Open the link: http://127.0.0.1:8000/ in a web browser and try out the REST API


WebApp:


1. Move to the Project folder
```sh
cd
```
2. Export the environmental variables:
```sh
Terminal: export FLASK_APP=WebApp
Windows: set FLASK_APP=WebApp
```
3. Run the Flask app
```sh
flask run
```
4. Open the link: http://127.0.0.1:5000 in a web browser and try out the WebApp


Serve up the WebApp and the REST api at the same time:
1. run the run.py file in the root directory after previous environment variable setup
```sh
python run.py
```


Mail Service:

1. Move to MailService folder
```sh
cd MailService/
```
2. Install packages with pip
```sh
pip install -r requirements.txt
```
3. Move to main src folder
```sh
cd src/
```
4. Run the MailService Api
```sh
python app.py
```
5. Open the link: http://127.0.0.1:8001/ in a web browser and try out the Mail Service

**Note:** The mail api service we were using closed our account for exposing an api key.
          The service was working but unfortunately not anymore. Hopefully this is alright
          for this sprint, and this will be fixed by the end of the next one.


<!-- TESTING -->
## Testing
### API testing
The current code coverage of the API is **97%**. The tests should be run from with in API/app with the commands below
* Running the unit tests, with coverage
```sh
coverage run -m pytest
```
* Getting the coverage report
```sh
coverage report -m
```

### WebApp testing
Our current code coverage of the WebApp is **59%**. To run the tests you should be positioned in the root directory and run:
Before running these tests you need to first start both the REST API and the WebApp. See instructions above.
* Running the unit tests, with coverage
```sh
coverage run -m pytest WebAppTests
```
* Getting the coverage report
```sh
coverage report -m
```

<!-- LECTURE ASPECTS -->
## Lecture Aspects

### Sprint 1
For this sprint we used a layered design where the database (data) and the Rest API (domain) work as independant entities. The presentation layer will be implemented in a future sprint.
Objer-Oriented Programming was implemented in the DBapi using abstract classes and a main gateway (see more in services README.md). Encapsulation is also used is various places in the API.

### Sprint 2
The six of the eight Base Design Patterns we decided on implementing for our system are the following:

* Registry: 
The registry design pattern is used to implement a global sole instance logger that we use for error logging, 
this introduces logging to our system.

* Plug-in: 
The Plug-in pattern is used to read a config file for the logger, aka output format, output file and more

* Mapper:
The Mapper design pattern is implemented to make changing between the rest api bodies and database structure easier. 
This also makes changes to the models easier.

* Layer Supertype:
For the Layer Supertype we created a Mapper interface with some methods to implement which the other Mapper classes inherit from.

* Gateway:
To implement the Gateway pattern we introduced a small external service into our project, a mail service, 
and we created a more basic api for said service.

* Service Stub:
For the service stub we created a fake mail service to remove the dependency on the mail service during unit tests.

### Sprint 3
The Single Responsibility Principle:
* The first place where we implement this principle is in our Mapper classes. These classes have only one reason to change and that
reason is if the underlying tables in the database change. That is if we where to, f.x. add a new column to a table or rename an existing
column we would change it but that is the only reason these classes have to change.
* The second place where we implement this principle is in the DBapi class. The only reason this class has to change is if we add/remove 
a table that we want to query from the database.
* The third place where we implement this principle is in our controller classes for the REST api. These classes/modules have only one
reason to change which is the addition/removal of a REST api function/route. These classes do not concern themselves with anything else.

The Dependency Injection:
To get the dependency injection we did a little bit of refactoring. We decided to create a new DBapi class that takes in the 5 IO classes.
These IO classes get assigned to instance variables named after the tables. This means that each call to f.x. users changes from DBapi.users("GET")
to DBapi.users.get(). This allows us to change out the DBapi that is used in the REST api by simply changing what IO classes we use allowing for
a swift transfer between f.x. different databases while still maintaining the same code that uses the DBapi (i.e. with dependency injection). We do
realize that this depends on the IO classes to implement the same types of interfaces which is just something that needs to be done when implementing
new IO classes.

### Sprint 4
Conway´s Law: 
* Our team has a unique structure to it. We are a team of eight, we split our tasks in a way where one team member does database work, another works on the REST API, a few members on the Flask web application, another few on design for our website, and the rest on lecture aspects, amongst giving their opinions on improvements on various things in our system. This kind of team structure has resulted in a system where our database, REST API, and web application function as individual systems, while still offering an outside perspective when implementing each service for our system.
* The communication amongst our team can sometimes be quite difficult, with the current status of the world we must communicate solely online.This has proven to have it’s challenges, it would be much easier to meet together in-person to discuss our problems, help each other with our tasks, create diagrams and documents and so on.
* We do however, not believe this has had a large impact on our specific system, perhaps working on our project took slightly more time than it should have, we could have, for example, implemented more functionality to our system, but in reality we probably would have just finished out tasks sooner in the sprint, resulting in not having to crunch the final weekend to get the last few tasks done.

Components:
* The first component is the Database. The current database we are using is a PostgreSQL 12.2 running on a Ubuntu 18.04.4 machine. This component is easily replaceable requiring only 
the change of the database IO classes in the DBapi. The database component is responisble for storing all the data of the system like the users, records and habits as well as storing 
the users passwords and offering a way to verify passwords.
* The second component is the Mail service. This component is an individual and easily replaceable component that simply handles sending out emails for the system. Changing out this 
component is not hard since it is not tigtly coupled with other components.

Non-Functional requirements:

Num | Non Functional Requirement | Priority 
--- | --- | --- 
1 | The system shall handle 10000 users at once | A 
2 | The response time shall be under 0.5 seconds | A 
3 | The front end shall communicate with the backend | A 
4 | The system shall be easy to use and understand | A 
5 | If some parts of out system fails, the users info should be maintained and kept safe | A 
6 | The system shall fulfil general security standards | A 
7 | The user’s password shall be hashed in the database| A 
8 | The system shall store the user’s information securely | A 
9 | The system shall maintain the user’s habits and records | A 
10 | The system shall be functional both on mobile and on a web browser | B 

Constraints:
Flask has some known issues, for example the flask-RESTplus extension is unmaintained and may become a constraint to our system in the future. We address this by using an older version of werkzeug for flask restplus to function properly. In the future we might want to migrate our system to using flask-RESTX which is a maintained project forked from the flask-RESTplus repo by the community.
The system is currently hosted by Guðjón’s at-home server.

Logs:  
We are currently handeling logs of the active systems that is the WebApp requests, the REST api and the Database. These logs are simply auto generated for us when the applications 
run and they are all currently stored on the server that is hosting the Database and the Website. Here below are the 5 components we would like to monitor in more depth.
* The first component we would like to monitor is the Server that hosts the database. This server is a fundimental to the whole service and so it is paramount that is stayes up and 
running. The metrics we would like to monitor are the hardware loads, network usage, power consumption and error rates. These metrics would give us a good idea of how our database 
server is being used, how much it costs us and would give us errors about network issues or the server going offline.
* The second component we would monitor is the database. Here the metrics would be number of queries, query logs, average response time, data usage and number of rows in the tables. 
These metrics would help us get a good look at the time people need to wait, the highs and lows of traffic and it would also give us time to prepare for the event that the data usage 
goes over our available data as well as give us insight into the ammount of data in the database like number of users. The query logs would then also enable us to look at suspicious 
activities.
* The third component is the REST api. Here we would like to get metrics for the number of requests, number of individual users, logs of requests and average respons time. These 
metrics allow us to catch potential missuse of the system for example one individual sending many requsts in a short time frame as well as give us an idea of the load on the system.
* The fourth component would be the servers or the docker containers hosting the Webapp. Here we would monitor the load of each server/container to enable us to increase or decrease 
the number of servers hosting the website/REST api to give the users a good experience with latency and to save money in hosting costs.
* The fifth and final component would be the Website itself. Here we could utilize Google Analytics or other similar applications to monitor how the users interact with our website. 
The main metrics of interest would be average time per page, where users click, locations of users, demographic and user interactions on the website. These metrics would help us make 
the website as user friendly and possible and to get it fit for the users of the website.

Risk management:  
For risk management we went through the 4 steps of risk identification using the diagrams from the previous sprint. From our observations we found X parts of the system with high 
risk. From these observations we identified that the Database, REST api and Hosting had the biggest risk involved. These components all rely on each other and if one fails the whole 
system will not be accessible by anyone.
* The database is at great risk since we only have one database which many REST apis and WebServices can rely on. This means that it is easy to create a new node that hosts the REST 
and the Website but the database is only one and if it fails everything will fail. 
    * The first high risk event is the event of a hard-drive failure. This would cause all the data to be lost and the service would effectively seize to exist if real world users 
    relied on it. To mitigate this risk the server running the database would need to utilize either a Raid 1 or Raid 4/5 for redundancy.
    * The second high risk factor is the possibility of a lost connection or power-outage to the server. In case of a power-outage a good UPS would help to stop the possiblity of the 
    server going down. The connection issue and the power-issue can also be solved by utilizing another backup server somewhere else in the world, preferably not in the same country/
    city, that would always run alongside the main server. This would mean that in the case of an outage on the main the backup could hold the connection up. This would also mean 
    that the backup server could help with query requests to reduce latency and wait times between queries.
* The REST api has a relatively high risk of being misuesed and abused. Since it is a connection to the database, getting access to the REST api could be very usefull to an attacker. 
    * The highest risk of the REST api is the possibility of abuse to get information or alter information in the database a user should not be able to get or do. To mitigate this 
    risk we need to implement an authentication method for the REST api where a logged in person can only send requests to the REST api for their own data. This mitigates the risk of 
    someone easily sending a REST request on another persons data.
    * The second way to reduce the potential of missuse is hosting the REST api on a secure server somewhere. Meaning that if we secure the REST api to its full potential we also 
    need to secure the machine it is running on.
* The third and final highest risk we identified is the Hosting of the service. In this sprint we started hosting the website and so it is good to look at ways to minimize downtime 
if the server hosting the website fails.
    * The risk involved in hosting is always to maintain a steady uptime of the website. If the uptime is low the users will leave and find another service. To mitigate this risk we 
    decided to use Docker. We utilize docker by making preset docker containers of the REST api and the website allowing us to host it easily on multiple machines. The docker 
    containers contain our code as well as all dependencies and allow us to quickly bring up new website hosts if others where to fail. More information can be seen in the Docker 
    chapter below.

### Sprint 5
Previous conditional passes:  
* Dependency injection:  
In sprint 3 we kind of got a conditional pass for our dependency injection not being quite correct. So we decided to rather talk about our other dependency injection which can be 
found in the mail service. The mail_service.py file contains a class that takes in another class which can then be used. This class allows for a quick and easy change of classes by 
simply changing the inserted class allowing us to have different classes with different functionality be interchangeable and creates no dependencies in the classes that use this 
class to rely specifically on a single class. We hope that this class follows the correct dependency injection pattern.

Microservice aspect:  
For our microservice aspect we decided that it would be good to make a microservice out of our authentication in the REST api. This functionality is a big security risk and moving it 
to an independent microservice would allow us to secure it more and make sure it does not get exploited. For the patterns involved in the integration from monolith to microservice we 
would either utilize the Strangler approach or the Branch by abstraction. Both of these aproaches are good for our system, the strangler aporach can be done using a HTTP proxy since 
our REST api utilizes HTTP for communication. We could then simply start to implement the new authentication microservice and when it is ready change the proxy to the new one. The 
Branch by abstraction could also work really well for us since it is closely related to the Strangler approach but instead we would create an abstraction instead of a HTPP proxy. The 
reason both of these approaches would be good for our integration is because the authentication part is a really important one for the website an if the new one fails we can always 
go back to the old one. After the integration of the new one is fully complete and we make sure it works we would then start to remove the old authentication from the monolith system 
for security reasons as well as remove the test password functionality of the DBapi and implement it again in the new microservice.

Screenshots of the system:  
See chapter [About the Project](#about-the-project)


## Website
In the 4th sprint we decided to start hosting the website. We hosted it on the same server that currently runs the database and the link to the website is https://habittracker.gudjoniv.com/. For the hosting part we decided to implement a systemd daemon for the REST api and the WebApp to enable easy monitoring and to allow for easier setup for the docker containers that would enable fast setup of a new host.


## Docker
For the 4th sprint we also decided to make a docker container for the hosting of the website. The docker container currently contains the git repository, an apache2 service with 
configuration to get connections from habittracker.gudjoniv.com and systemd configuration files to run the REST api and the WebApp. To get the docker container simply enter:
1. Get the docker container
```sh
docker run -d -p 8080:80 gudjoniv/habittracker-host tail -f /dev/null
```
2. Enter and setup
```sh
docker exec <container_id>  
systemctl start apache2
systemctl start rest
systemctl start webapp
```
3. View webpage in browser at localhost:8080

We are not sure this is going to work 100% since Guðjón was the only one doing this part and for some reasing WSL2 that provides linux on windows does not have Systemd enabled so 
running the systemctl functions did not work. This container also only contains apache2 config for http and not https since we have yet to test out with Docker if we can just copy 
and paste the keys and ssl configuration. This docker container was more of a proof of concept and a test of how we could utilize docker to our advantage and lower our risk involved 
in hosting on a single server. This docker container also enables us to quickly respond to demand.  
Few things to note are that f.x. tail -f /dev/null in the end of command 1 is to make sure docker does not exit a soon as it starts up. Also if you have problems running with the 
systemctl commands you can also do service apache2 start and then run the run.py from within /home/Team5 with the environment variable FLASK_APP=WebApp set. This variable is already 
set for root but for some reason flask run does not work unless you manually set it before. We will see in the next and final sprint if we will continue to improve this docker 
container or not.


<!-- TEAM MEMBERS -->
## Team Members

The members of Team-5 include RU students from the Computer Science department. We are a mixture of second and third year computer science and software engineering students.

* Annija Apine, Computer Science - annija17@ru.is
* Bent Gunnarsson, Software Engineering - bent19@ru.is
* Bjartur Þórhallsson, Software Engineering - bjartur19@ru.is
* Erla Óskarsdóttir, Computer Science - erla19@ru.is
* Guðjón Ingi Valdimarsson, Software Engineering - gudjonv18@ru.is
* Magnús Konráð Sigurðsson, Software Engineering - magnusks19@ru.is
* Páll Þorsteinsson Sonnentag, Computer Science - pallt18@ru.is
* Úlfur Örn Björnsson, Software Engineering - ulfur19@ru.is



<!-- TEACHER -->
## Teacher

Gerardo Reynaga



<!-- TA -->
## TAs

* Gunnar Jörgen Viggósson
* Svanur Jóhannesson
* Þórður Friðriksson





<!-- MARKDOWN LINKS & IMAGES -->
[contributors-shield]: https://img.shields.io/github/contributors/UlfurOrn/Team5.svg?style=flat-square
[contributors-url]: https://github.com/UlfurOrn/Team5/graphs/contributors
[forks-shield]: https://img.shields.io/github/forks/UlfurOrn/Team5.svg?style=flat-square
[forks-url]: https://github.com/UlfurOrn/Team5/network/members
[stars-shield]: https://img.shields.io/github/stars/UlfurOrn/Team5.svg?style=flat-square
[stars-url]: https://github.com/UlfurOrn/Team5/stargazers
[issues-shield]: https://img.shields.io/github/issues/UlfurOrn/Team5.svg?style=flat-square
[issues-url]: https://github.com/UlfurOrn/Team5/issues
[product-screenshot]: https://i.imgur.com/WP7MQJj.png
[python]: https://www.python.org/
[flask]: https://flask.palletsprojects.com/en/1.1.x/
[flask-restplus]: https://github.com/noirbizarre/flask-restplus
[psycopg2]: https://www.psycopg.org/docs/
