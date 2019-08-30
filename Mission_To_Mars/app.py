from flask import Flask
from flask import render_template, redirect
import scrape_mars
from datetime import datetime

app = Flask(__name__)
app.config['SEND_FILE_MAX_AGE_DEFAULT'] = 0

@app.route('/')
def scrape(name=None):
    return render_template('index.html', name=name)

@app.after_request
def add_header(response):
    # response.cache_control.no_store = True
    response.headers['Cache-Control'] = 'no-store, no-cache, must-revalidate, post-check=0, pre-check=0, max-age=0'
    response.headers['Pragma'] = 'no-cache'
    response.headers['Expires'] = '-1'
    return response


@app.route('/scrapeMars')
def scrapeMars():
	marsData = scrape_mars.scrapeMars()
	scrape_mars.storeInDb(marsData)
	data = scrape_mars.getData()
	return render_template('scrapeMars.html', data=data)