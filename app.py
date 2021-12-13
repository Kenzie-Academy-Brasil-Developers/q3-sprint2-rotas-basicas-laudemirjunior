from flask import Flask
from datetime import datetime

app = Flask(__name__)

@app.route('/')
def home():
    return {'data': 'Hello Flask!'}

@app.route('/current_datetime')
def current_datetime():
    data = datetime.now().strftime('%d/%m/%Y %H:%M:%S PM')
    base = datetime.now().strftime('%H')
    message = ""
    if base < "12":
        message = "Bom dia!"
    elif base < "18":
        message = "Boa tarde!"
    else:
        message = "Boa noite!"
    return dict(current_datetime=data, message=message)
