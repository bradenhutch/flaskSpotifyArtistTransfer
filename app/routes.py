from flask import render_template, request
from app import app
import subprocess
import requests
import json

@app.route('/')
@app.route('/index')
def index():
    return render_template('index.html', title='Home', cid=app.config['CLIENT_ID'])

@app.route('/callbackFrom')
def fromUser():
	# Add error handling in case the request is denied
	auth = request.args.get('code')
	return render_template('stepOne.html', title='Step One', auth=auth)

@app.route('/getCodes', methods=['POST'])
def user1codes():
	grant_type = request.form['grant_type']
	code = request.form['code']
	redirect_uri = request.form['redirect_uri']
	client_id = app.config['CLIENT_ID']
	client_secret = app.config['CLIENT_SECRET']
	request_data = {'grant_type':grant_type,'code':code,'redirect_uri':redirect_uri,'client_id':client_id,'client_secret':client_secret}
	spotify_url = "https://accounts.spotify.com/api/token"
	response = requests.post(spotify_url, data=request_data)
	responseJson = json.loads(response.text)
	return render_template('stepTwo.html', title='Step Two', auth=responseJson['access_token'])
	
@app.route('/getArtists', methods=['POST'])
def artists():
	code = request.form['code']
	artists = []
	contToken = 'x'
	headers = {
    	'Accept': 'application/json',
    	'Content-Type': 'application/json',
    	'Authorization': 'Bearer {}'.format(code)
	}
	while contToken != 'None':	
		if contToken == 'x':
			params = (
	    		('type', 'artist'),
	    		('limit', '50')
			)
		else:
			params = (
				('type', 'artist'),
	    		('limit', '50'),
	    		('after', contToken)
			)
		response = requests.get('https://api.spotify.com/v1/me/following', headers=headers, params=params)
		responseJson = json.loads(response.text)
		for i in responseJson['artists']['items']:
			artists.append(i['id'])
		contToken = str(responseJson['artists']['cursors']['after'])
		print(contToken)
	return render_template('stepThree.html', title='Step Three', artists=artists, cid=app.config['CLIENT_ID'])

@app.route('/callbackTo')
def toUser():
	auth = request.args.get('code')
	return render_template('stepFour.html', title='Step Four', auth=auth)

@app.route('/getCodesAgain', methods=['POST'])
def user2codes():
	grant_type = request.form['grant_type']
	code = request.form['code']
	redirect_uri = request.form['redirect_uri']
	client_id = app.config['CLIENT_ID']
	client_secret = app.config['CLIENT_SECRET']
	request_data = {'grant_type':grant_type,'code':code,'redirect_uri':redirect_uri,'client_id':client_id,'client_secret':client_secret}
	spotify_url = "https://accounts.spotify.com/api/token"
	response = requests.post(spotify_url, data=request_data)
	responseJson = json.loads(response.text)
	return render_template('stepFive.html', title='Step Five', auth=responseJson['access_token'])
	
@app.route('/followArtists', methods=['POST'])
def follow():
	code = request.form['code']
	artists = request.form['artists']
	artList = artists.split(',')
	headers = {
		'Accept': 'application/json',
		'Content-Type': 'application/json',
		'Authorization': 'Bearer {}'.format(code)
	}
	
	spotify_url = "https://api.spotify.com/v1/me/following"
	while len(artList) != 0:
		shortList = artList[:50]
		del artList[:50]
		params = (
			('type', 'artist'),
			('ids', ",".join(shortList))
		)
		response = requests.put(
			spotify_url, 
			headers=headers, 
			params=params)
		print(str(response.text))
	return "Done!"
