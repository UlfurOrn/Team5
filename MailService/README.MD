# Mail Service

## Gateway
The Gateway design pattern was used in this microservice to let
developers use the external api without having to use their 
complicated methods. We create a more basic api microservice
used to send emails.

## Service Stub
The Service Stub design pattern was used to unittest the gateway,
since we don't always have access to the external service we created
a fake external service or service stub to unittest against.


**Note:** Our account for the external service was temporarily
terminated for exposing our api key. They have yet to give us access
again. This means that we are unable to send emails through our
microservice although all other functions work. This will be fixed
for the next sprint :)