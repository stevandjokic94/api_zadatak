from flask import Flask, jsonify, request
import json
import urlparse

app = Flask(__name__)


@app.route("/employees", methods=['GET', 'POST'])
def employees():
	url = request.url
	par = urlparse.parse_qs(urlparse.urlparse(url).query)
	if par['token'][0] != '123':
		return jsonify({'error':'Validation failed'}), 403

	if request.method == 'POST':
		with open('data.json', 'r') as f:
			data = json.load(f)
			f.close()
		some_json = request.get_json()
		data['employees'].append(some_json)
		with open('data.json', 'w') as f:
			f.write(json.dumps(data))
			f.close()
		return jsonify({'you_sent': some_json})
	else:
		with open('data.json', 'r+') as f:
			data = json.load(f)
		return jsonify(data['employees'])


@app.route("/departments", methods=['GET', 'POST'])
def departments():
	url = request.url
	par = urlparse.parse_qs(urlparse.urlparse(url).query)
	if par['token'][0] != '123':
		return jsonify({'error':'Validation failed'}), 403

	if request.method == 'POST':
		with open('data.json', 'r') as f:
			data = json.load(f)
			f.close()
		some_json = request.get_json()
		data['departments'].append(some_json)
		with open('data.json', 'w') as f:
			f.write(json.dumps(data))
			f.close()
		return jsonify({'you_sent': some_json})
	else:
		with open('data.json', 'r+') as f:
			data = json.load(f)
		return jsonify(data['departments'])


@app.errorhandler(404) 
def non_existant_route(error):
	return jsonify({'error':'Route does not exist'}), 403


@app.errorhandler(405)
def method_not_allowed(e):
	return jsonify({'error': 'Method not allowed'}), 405

if __name__ == '__main__':
	app.run(debug=True)