# pizzaAppServer
1. About
2. Setup
3. Design

# About
This project handles requests from pizzaApp and stores user data
including user credentials and their order history.

# Setup
The installation and execution instructions create an environment
that doesn't require App Engine. Feel free to adapt them for App Engine.
## Installation
If you don't have `virtualenv` installed, install it now
(`$ sudo pip install virtualenv`).

CD into the project root directory and activate a virtual environment.
To create a virtual environment: `$ virtualenv env`. Then activate it with `$ ./env/bin/activate`. `$ ./env/bin/deactivate` deactivates it.

Install WebOb, Paste, and webapp2 using pip while in a
virtual environment:
```
$ pip install WebOb
$ pip install Paste
$ pip install webapp2
```

## Execution
`$ python main.py`

The server accessible by sending requests to `127.0.0.1`. Navigating a browser
to this address should verify the server is running.

# Design
The server uses webapp2, a general purpose web framework.

## \*.py
### main.py
Run this file with python to start the server. This instantiates a database
and the webapp2 framework. Request handler methods are defined here in the
`MainPage` class. Requests are generally done with JSON.

## pizza.py
This defines the `Pizza` class representing a pizza a user has created. This
class provides a `toJSON` method that returns a JSON string representing the
pizza's attributes. Support for setting the pizza's attributes with `fromJSON`
is coming.
