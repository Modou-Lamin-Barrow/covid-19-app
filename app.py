import requests
import pprint

from flask import Flask, render_template, request



app = Flask(__name__)


@app.route('/')
def home():

    try:
        req = requests.get("https://corona.lmao.ninja/v2/countries")

        data = req.json()

        # World Stats
        req = requests.get("https://corona.lmao.ninja/v2/all")
        world_stats = req.json()
        
        return render_template('index.html', covid_data=data, world_stats=world_stats,  page_title="Global Stats")

    except Exception as error:
        print('There is an error', error)
        return "There is an error " + error


@app.route('/countries/<country>')
def country(country):
    try:
        req = requests.get(f"https://corona.lmao.ninja/v2/countries/{country}")

        data = req.json()

        return render_template('country.html', country=data)

    except Exception as error:
        print('There is an error', error)
        return "There is an error " + error
    return f"data for a {country}"


@app.route('/search')
def search():
    country = request.args.get('country')

    try:
        req = requests.get(f"https://corona.lmao.ninja/v2/countries/{country}")

        data = req.json()

        return render_template('country.html', country=data)

    except Exception as error:
        print('There is an error', error)
        return "There is an error " + error
    return f"data for a {country}"


@app.route('/continents/<continent>')
def continent(continent):
    req = requests.get("https://corona.lmao.ninja/v2/countries")

    data = req.json()

    continent_data = []

    for country in data:
        if continent in country['continent'].lower():
            continent_data.append(country)

    return render_template('index.html', covid_data=continent_data, page_title=continent)

if __name__ == '__main__':
    app.run(debug=True)