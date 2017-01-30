
from flask import Flask
from flask import render_template
from pymongo import MongoClient
import json
from bson.json_util import dumps

app = Flask(__name__)

DBS_NAME = 'world_bank'
COLLECTION_NAME = 'project'


@app.route('/')
def index():
	return render_template('index.html')

@app.route('/world_bank')
def world_bank():
	connection = MongoClient()
	collection = connection[DBS_NAME][COLLECTION_NAME]
	projects = collection.find()
	from collections import defaultdict

	country_project, country_sum = defaultdict(list), defaultdict(int)

	for country in projects:
		country_name = country['countryname']
		country_project[country_name].append(country['project_name'])
		country_sum[country_name] += country['lendprojectcost']

	new_list = [ {
		'countryname': country,
		'project_name': country_project[country],
		'lendprojectcost': country_sum[country]} for country in country_project]

	return json.dumps(new_list)


if __name__ == '__main__':
	app.run(debug=True)
