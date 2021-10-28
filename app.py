import json
import sys
import logging.handlers
import logging
import covertT0json
import starter
import requests
import configparser
from flask import Flask, render_template, url_for


##config##
config = configparser.ConfigParser()
config.read('config_file.ini')


admin_mail = config['default']['admin_mail']
admin_pass = config['default']['admin_pass']
client_mail = config['client']['client_mail']
mail_msg = config['log_credentials']['message']

##endconfig##

logging.basicConfig(filename='errorlog.log', level=logging.CRITICAL, format='%(asctime)s , %(filename)s , %(name)s , %(levelname)s , %(message)s')

logger = logging.getLogger(__name__)


formatter = logging.Formatter('%(asctime)s , %(filename)s , %(name)s ,  %(levelname)s , %(message)s')

file_handler = logging.FileHandler('errorlog.log')
smtp_handler = logging.handlers.SMTPHandler(mailhost=('smtp.gmail.com', 587),
                                            fromaddr=admin_mail,
                                            toaddrs=[client_mail],
                                            subject=mail_msg,
                                            credentials=(admin_mail, admin_pass),
                                            secure=()
                                            )

stream_handler = logging.StreamHandler(sys.stdout)

file_handler.setFormatter(formatter)
smtp_handler.setFormatter(formatter)
stream_handler.setFormatter(formatter)


file_handler.setLevel(logging.DEBUG)
smtp_handler.setLevel(logging.INFO)
stream_handler.setLevel(logging.DEBUG)

logger.addHandler(file_handler)
logger.addHandler(smtp_handler)
logger.addHandler(stream_handler)



werkzeug_logger = logging.getLogger('werkzeug')

werkzeug_logger.setLevel(logging.INFO)

werkzeug_logger.addHandler(smtp_handler)
werkzeug_logger.addHandler(file_handler)

logger.setLevel(logging.INFO)


# logger.info(f'{"#"*15} INITIALIZING THE LOGGER {"#"*15}')


app = Flask(__name__)



@app.after_request
def after_request(response):
    # logger.info('{}'.format(response))
    return response


@app.route('/')
def _hello_world():
 filename = 'trending.json'
 with open(filename) as f:
  file_data = json.load(f)
 return render_template('index.html', data=file_data)

@app.route('/log')
def show_log():
    filename = 'errorlog.json'
    with open(filename) as f:
        file_data = json.load(f)
    return render_template('logData.html', data=file_data)


if(__name__ == "__main__"):
    app.run(debug=False)

