# Questioner
Crowd-source questions for a meetup. Questioner helps the meetup organizer prioritize questions to be answered. Other users can vote on asked questions and they bubble to the top or bottom of the log.


[![forthebadge made-with-python](http://ForTheBadge.com/images/badges/made-with-python.svg)](https://www.python.org/)
[![GitHub license](https://img.shields.io/github/license/Naereen/StrapDown.js.svg)](https://github.com/Naereen/StrapDown.js/blob/master/LICENSE)
[![Build Status](https://travis-ci.com/munniomer/Questioner-Api-V1.svg?branch=ft-user-registration-v1-163083345)](https://travis-ci.com/munniomer/Questioner-Api-V1)
[![Coverage Status](https://coveralls.io/repos/github/munniomer/Questioner-Api-V1/badge.svg?branch=ft-user-registration-v1-163083345)](https://coveralls.io/github/munniomer/Questioner-Api-V1?branch=ft-user-registration-v1-163083345)
<a href="https://codeclimate.com/github/munniomer/Questioner-Api-V1/maintainability"><img src="https://api.codeclimate.com/v1/badges/b50955cabef7296a3b5b/maintainability" /></a>

## The required API Endpoints that enable one:
1. Create a meetup record.
2. Create a question record.
3. Get a specific meetup record..
4. Get all meetup records.
5. Upvote or downvote a question.
6. Rsvp for a meetup.

 
 ## The list of the functioning API Endpoints

Method        | EndPoint      | Functionality |
------------- | ------------- | ---------------
POST  | `/api/v1/user/register`  | Creates a user   |
POST  | `/api/v1/user/login`  | Sign in a user   |
POST  | `/api/v1/meetups`  | Create a meetup record  |
POST  | `/api/v1/questions` | Create a question record   
GET  | `/api/v1/meetups/<meetupId>` | Get a specific meetup record  |
GET  | `/api/v1/meetups/upcomimg`| Get all meetup records   |
POST  | `/api/v1/meetups/<meetupsId>/rsvps`|Respond to meetup RSVP    |
PATCH  | `/api/v1/questions/<questionsId>/upvote` | Upvote a specific question.   |
PATCH  | `/api/v1/questions/<questionsId>downvote`| Downvote a specific questions   |

## Installation
Make sure you have Python3 installed on your machine
- Clone this repo and Switch to it
 ```bash
$ git clone https://github.com/munniomer/Questioner-Api-V1.git 
$ cd Questioner-Api-V1
```
- Install a virtual Environment and activate it
 ```bash
$ python -m venv venv 	
$ source venv/bin/activate
```
- Install the dependencies using the requirements file
 ```bash
$ pip install -r requirements.txt
```
- Run the app
 ```bash
$ export FLASK_ENV=development
$ export FLASK_APP=run.py
$ flask run
```
## Testing the endpoints
- Install postman to test the endpoints 

- Open postman and navigate to the localhost and add the enpoint route you are testing
 ```bash
 http://localhost:5000/api/v1/<endpoint>
 
```
## Running tests
To Run the tests you have to use the terminal, switch to the project folder and activate the venv.

- To check if all tests pass
```bash
$ pytest 
```
- To check the test Coverage 

```bash
$ pytest --cov app  
```

## Technologies used
- Python 3.6
- Flask framework
- Unittest for testing

## Author: Munira Omar

__Copyright © Andela 2019__


