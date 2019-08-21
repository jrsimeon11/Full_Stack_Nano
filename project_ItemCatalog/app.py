
from flask import (Flask, render_template, request, redirect, url_for, make_response, jsonify, session as login_session, flash)
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, scoped_session
from database_setup import Base, GameCompany, GameConsole, User
from flask_oauth import OAuth
from urllib2 import Request, urlopen, URLError
from oauth2client.client import flow_from_clientsecrets
from oauth2client.client import FlowExchangeError
import random, string, json, httplib2, requests

app = Flask(__name__)
engine = create_engine('sqlite:///dbconsolecatalog.db')
Base.metadata.bind = engine
DBSession = sessionmaker(bind=engine)
session = scoped_session(DBSession)

GOOGLE_CLIENT_ID = '404273179613-k0k7998ijupfdulrpmr8pps6h9jb63q1.apps.googleusercontent.com'
GOOGLE_CLIENT_SECRET = 'ctwFjfNCUCUlARs_XiNN_zMB'
REDIRECT_URL = '/google-oauth-callback'
SECRET_KEY = 'AIzaSyCA1cwe0SxSfPiF4NdHOinilox-9-J-554'
DEBUG = True

app.debug = DEBUG
app.secret_key = SECRET_KEY
oauth = OAuth()
google = oauth.remote_app(
    'google',
    base_url='https://www.google.com/accounts/',
    authorize_url='https://accounts.google.com/o/oauth2/auth',
    request_token_url=None,
    request_token_params={'scope': 'https://www.googleapis.com/auth/userinfo.email', 'response_type': 'code'},
    access_token_url='https://accounts.google.com/o/oauth2/token',
    access_token_method='POST',
    access_token_params={'grant_type': 'authorization_code'},
    consumer_key=GOOGLE_CLIENT_ID,
    consumer_secret=GOOGLE_CLIENT_SECRET)

# Create JSON object for Categories
@app.route('/gamecompany/JSON')
def gamecompanyJSON():
	gamecompany = session.query(GameCompany).all()
	return jsonify(gamecompany = [g.serialize for g in gamecompany])

# Create JSON object for Item
@app.route('/gameconsoles/JSON')
def gameconsoleJSON():
	gameconsole = session.query(GameConsole).all()
	return jsonify(gameconsole = [i.serialize for i in gameconsole])

# Load main home page
@app.route('/')
def load_main_page():
	complete_companys = session.query(GameCompany).all()
	if ('name' in login_session):
		logged_in_name = login_session['name']
	else:
		logged_in_name = "Viewer"
	return render_template('index.html', companies = complete_companys, user_name = logged_in_name)

# View the consoles in the selected company
@app.route('/gamecompany/<gamecompany_id>')
def view_company_consoles(gamecompany_id):
	complete_companys = session.query(GameCompany).all()
	current_company = session.query(GameCompany).filter_by(id = gamecompany_id).first()
	gameconsoles = session.query(GameConsole).filter_by(gamecompany_id = gamecompany_id).all()
	if ('name' in login_session):
		logged_in_name = login_session['name']
	else:
		logged_in_name = "Viewer"
	return render_template('R-gameconsole.html',companies = complete_companys, gameconsoles = gameconsoles , gamecompany = current_company, user_name = logged_in_name)

# Add a new game company
@app.route('/gamecompany/add', methods=['GET', 'POST'])
def add_gamecompany():
    if (request.method == 'POST'):
        new_name = request.form['gamecompany-name']
        new_gameCompany = GameCompany(name = new_name, user_id = login_session['id'])
        session.add(new_gameCompany)
        session.commit()
        
        return redirect(url_for('load_main_page', user_name = login_session['name']))
    else:
        if ('name' in login_session):
            complete_companys = session.query(GameCompany).all()
            logged_in_name = login_session['name']
            
            return render_template('C-gamecompany.html', companies = complete_companys, user_name = logged_in_name)
        else:
            return redirect(url_for('login'))

# Companies to delete
@app.route('/gamecompany/delete')
def companys_delete():
	if ('name' in login_session):
		logged_in_name = login_session['name']
		deleted_companys = session.query(GameCompany).filter_by(user_id = login_session['id']).all()
		complete_companys = session.query(GameCompany).all()
		return render_template('D-gamecopany.html', companies=complete_companys, deleted = deleted_companys, user_name=logged_in_name)
	else:
		return redirect(url_for('login'))

# Delete a company
@app.route('/gamecopny/<cgamecompany_id>/delete')
def delete_present_company(gamecompany_id):
    if ('name' in login_session):
        delete_company = session.query(GameCompany).filter_by(id = gamecompany_id).first()
        if (delete_company.user_id != login_session['id']):
            flash("You can only delete companies you have created")
        else:
            session.delete(delete_company)
            session.commit()
        return redirect(url_for('companys_delete', user_name = login_session['name']))
    else:
        return redirect(url_for('login'))

# Add a new console to the table
@app.route('/gamecompany/<gamecompany_id>/add', methods=['GET', 'POST'])
def add_gameconsole(gamecompany_id):
    if (request.method == 'POST'):
        new_console_name = request.form['gameconsole-name']
        new_console_description = request.form['gameconsole-description']
        new_console_price = request.form['gameconsole-price']
        new_console = GameConsole(name = new_console_name, description = new_console_description, price = new_console_price, gamecompany_id = gamecompany_id, user_id = login_session['id'])
        session.add(new_console)
        session.commit()
        return redirect(url_for('view_company_consoles', gamecompany_id = gamecompany_id, gamecompany_name = gamecompany.name, user_name=login_session['name']))
    else:
        if ('name' in login_session):
            complete_companys = session.query(GameCompany).all()
            gamecompany = session.query(GameCompany).filter_by(id=gamecompany_id).first()
            logged_in_name = login_session['name']
            return render_template('C-gameconsole.html', companies = complete_companys, gamecompany = gamecompany, user_name=logged_in_name)
        else:
            return redirect(url_for('login'))

# Edit Game Console
@app.route('/gamecompany/<gamecompany_id>/<gameconsole_id>/edit', methods=['GET', 'POST'])
def edit_gameconsole(gamecompany_id, gameconsole_id):
    if (request.method == 'POST'):
        gameconsole_edit = session.query(GameConsole).filter_by(id=gameconsole_id).first()
        if (gameconsole_edit.user_id != login_session['id']):
            flash("You can only edit your own consoles")
        else:
            new_name = request.form['gameconsole-name']
            new_description = request.form['gameconsole-description']
            new_price = request.form['gameconsole-price']
            gameconsole_edit.name = new_name
            gameconsole_edit.description = new_description
            gameconsole_edit.price = new_price
            session.add(gameconsole_edit)
            session.commit()
        return redirect(url_for('view_company_consoles', gamecompany_id = gamecompany_id, user_name = login_session['name']))
    else:
        if ('name' in login_session):
            complete_companys = session.query(GameCompany).all()
            gamecompany = session.query(GameCompany).filter_by(id = gamecompany_id).first()
            logged_in_name = login_session['name']
            return render_template('U-gameconsole.html', companies = complete_companys, gameconsole = gameconsole_edit, gamecompany = gamecompany, gameconsole_id = gameconsole_id, user_name = logged_in_name)
        else:
            return redirect(url_for('login'))

# Delete GameConsole
@app.route('/gamecompany/<gamecompany_id>/<gameconsole_id>/delete')
def delete_gameconsole(gamecompany_id, gameconsole_id):
    if ('name' in login_session):
        gameconsole_delete = session.query(GameConsole).filter_by(id=gameconsole_id).first()
        if (gameconsole_delete.id != login_session['id']):
            flash("You can only delete the consoles you have created.")
        else:
            session.delete(gameconsole_delete)
            session.commit()
    	return redirect(url_for('view_company_consoles', gamecompany_id = gamecompany_id, user_name = login_session['name']))
    else:
        return redirect(url_for('login'))

# Viewer Login
@app.route('/login')
def login():
	callback = url_for('authorized', _external = True)
	return google.authorize(callback = callback)

# Viewer Logout
@app.route('/logout')
def logout():
	login_session.pop('id', None)
	login_session.pop('name', None)
	return redirect(url_for('load_main_page'))

# Google authorization handler
@app.route(REDIRECT_URL)
@google.authorized_handler
def authorized(resp):
	access_token = resp['access_token']
	login_session['access_token'] = access_token, ''
	access_token = login_session.get('access_token')
	access_token = access_token[0]
	headers = {'Authorization': 'OAuth '+ access_token}
	requesting = Request('https://www.googleapis.com/oauth2/v1/userinfo', None, headers)
	res = urlopen(requesting)
	arr = res.read().split(",")
	email_1 = arr[1].split(":")
	name_1 = arr[3].split(":")
	email = email_1[1].replace("\"", "")
	name = name_1[1].replace("\"", "")
	user = session.query(User).filter_by(email = email).first()
	if (user is None):
		userlogin = User(name = name, email = email)
		session.add(userlogin)
		session.commit()
		user = session.query(User).filter_by(email = email).first()
	login_session['name'] = user.name
	login_session['id'] = user.id

	return redirect(url_for('load_main_page'))


# required for the Google OAuth API
@google.tokengetter
def get_access_token():
    return login_session.get('access_token')

# Main
if __name__ == '__main__':
	app.debug = True
	app.run(host='0.0.0.0', port=5000)