import os
from flask import Flask, render_template
import mindsdb_sdk 
from config import Config
from settings import MINDSDB_EMAIL, MINDSDB_PASSWORD
from forms import CoinForm

app = Flask(__name__)

app.config.from_object(Config)

server = mindsdb_sdk.connect('https://cloud.mindsdb.com', email=MINDSDB_EMAIL, password=MINDSDB_PASSWORD)

@app.route('/')
@app.route('/index')
def index():
    server = mindsdb_sdk.connect('https://cloud.mindsdb.com', email=MINDSDB_EMAIL, password=MINDSDB_PASSWORD)
    # Use MindsDB server object here
    project = server.get_project('mindsdb')
    model = project.get_model('btcusd_predictor')
    return render_template('index.html', model=model)
    # run `flask run` command in terminal, then visit 127.0.0.1:5000 to test this function
    

@app.route('/bitcoin', methods=['GET', 'POST'])
def bitcoin():
    form = CoinForm()
    if form.validate_on_submit():
        # Use MindsDB server object he`re
        project = server.get_project('mindsdb')
        model = project.get_model('btcusd_prediction_mod')
        print(model)
        query = project.query('SELECT close_price FROM mindsdb.btcusd_prediction_mod WHERE date="2019-01-05"');
        return 'Your prediction data for Bitcoin is: ' + str(query.fetch())
    return render_template('bitcoin.html', form=form, query=None)
# run `flask run``, then visit 127.0.0.1:5000/bitcoin/ to test this function

if __name__ == '__main__':
    # set debug to true
    app.run(debug=True)