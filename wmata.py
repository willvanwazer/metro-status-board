from flask import Flask, render_template
from flask.ext.bootstrap import Bootstrap
import requests
import json
import urllib
import os

app = Flask(__name__)
Bootstrap(app)


WMATA_API_KEY = os.environ.get("WMATA_API_KEY", None)
if WMATA_API_KEY is None:
    raise NotImplementedError("You must define a WMATA_API_KEY enviroment var")


@app.template_filter('status_board_url')
def status_board_url(s):
    return "panicboard://?url=" + urllib.quote(s) +\
            "&panel=table&sourceDisplayName=Will%20Van%20Wazer"


@app.template_filter('wmata_full_name')
def wmata_full_name(s):
    line_names = {
        'RD': 'red',
        'BL': 'blue',
        'OR': 'orange',
        'GR': 'green',
        'YL': 'yellow',
    }
    return line_names.get(s, "")


@app.route('/')
def list_of_stations_for_arrivals():
    raw_station_json = open('stations.json')
    stations = json.loads(raw_station_json.read())
    context = {
        'stations': stations,
    }
    return render_template('station-list.html', **context)


@app.route('/about/')
def about():
    return render_template('about.html')


@app.route('/rail-arrivals/<station_code>/')
def station_arrivals(station_code):
    r = requests.get("http://api.wmata.com/StationPrediction.svc/json/GetPrediction/"\
                      + station_code + "?api_key=" + WMATA_API_KEY)
    context = {
        'arrivals': r.json()['Trains'],
    }
    return render_template('station-arrivals.html', **context)

if __name__ == '__main__':
    app.debug = True
    app.run()
