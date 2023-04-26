import os
import ssl
from flask import Flask, render_template, request
import mindsdb_sdk 
from config import Config
from settings import MINDSDB_EMAIL, MINDSDB_PASSWORD
from forms import CoinForm
# context = ssl.SSLContext(ssl.PROTOCOL_TLS_SERVER)
# context.load_cert_chain('server.crt', 'server.key')

app = Flask(__name__)

app.config.from_object(Config)

server = mindsdb_sdk.connect('https://cloud.mindsdb.com', email=MINDSDB_EMAIL, password=MINDSDB_PASSWORD)

@app.route('/')
def index():
    return render_template('index.html', title='Home')


@app.route('/coins')
def coins():
    return render_template('coins.html', title='Coins')


@app.route('/bitcoin', methods=['GET', 'POST'])
def bitcoin():
    """
    Method to return bitcoin prediction data when a user clicks the bitcoin card on coins.html
    """
    # if request.method == 'POST':
    # print(server)
    # databases = server.list_databases()
    # print(databases)
    # print(project)
    # model = project.get_model('btcusd_prediction_mod')
    # print(model)
    # query = project.query('SELECT close_price FROM mindsdb.btcusd_prediction_mod WHERE date="2019-04-25"')
    # print(str(query.fetch()))
    # result = model.query.with_entities('close_price'.column_name).fetch()
    return render_template('bitcoin.html')

@app.route('/ethereum', methods=['GET', 'POST'])
def ethereum():
    """
    Method to return ethereum prediction data when a user clicks the ethereum card on coins.html
    """
    # project = server.get_project('mindsdb')
    # databases = server.get_database('files')
    # model = project.get_model('ethereum_predictions')
    # query = project.query('SELECT * FROM ethereum_predictions as EP JOIN files.Ethereum as E WHERE E.Date > "2023-04-25" LIMIT 1;')
    # print(query.fetch())
    return render_template('ethereum.html')


if __name__ == '__main__':
    app.run(ssl_context='adhoc')
