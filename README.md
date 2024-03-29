# AT-Rate-Limitting

## Overview
AT Rate Limitting is an application which aims to set a certain number of limit to HTTP requests given an interval time.

## Pre-requisite
List of language and library needed to be installed on your system.

|Language | Version|
|--- | --- |
|Python | 3.6.4 |
|Flask | 1.1.1 |

## Installation
Installing the application:
1. Ensure you have Python 3.6.4 installed
2. Install flask python library by using the command:
  - Run `pip install flask==1.1.1`
  - Run `pip check`

## Running the application
To run the application, we need to set the environment variable of FLASK_APP.

Windows
1. Change Directory to `app`
2. Run `set FLASK_APP=ratelimiter.py`
3. Run `python -m flask run`

Linux
1. Change Directory to `app`
2. Run `export FLASK_APP=ratelimiter.py`
3. Run `python -m flask run`

## Open in Browser
Once Application is running, we can open up in browser to see the end result. Type `http://127.0.0.1:5000` in the address bar of your browser.
