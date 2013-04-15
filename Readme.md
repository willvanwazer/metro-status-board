# MetroStatusBoard #

Panic's Status Board is a really awesome iOS app for Status Board making. I wanted a simple way to add arrival data for my nearest Metro stop to my Status Board. This is that way.

## Requirements ##

Spelled out in requirements.txt, but summarized here for your enjoyment:

    Flask
    Flask-Bootstrap
    Requests

`Gunicorn` is an optional dependency, if you want to run the app on Heroku.

## Getting Started  ##

Other than the standard setup for Python webapps (virtualenv, installing from the requirements file), you must export the `WMATA_API_KEY` enviroment variable for use inside the app. The API key can be obtained [here](http://developer.wmata.com/page).

## Things to Implement  ##

Right now, there is no caching of calls to the WMATA API. Depending on the amount of traffic this recieves, some caching may be in order.