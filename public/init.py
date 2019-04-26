# system modules
import os, sys
sys.path.append(os.path.abspath('../app/'))

# application modules
from caller import RingCaller
from flask import Flask, render_template, request, redirect, url_for, send_from_directory, session, abort

# init Flask config
template_dir = os.path.abspath('../templates')
app = Flask(__name__, template_folder=template_dir)
app.config['SESSION_PERMANENT'] = False
app.config['SECRET_KEY'] = os.urandom(24)
app.config['SESSION_COOKIE_SECURE'] = True
app.config['SESSION_COOKIE_NAME']='Caller-WebSession'
app.config['WTF_CSRF_TIME_LIMIT'] = None

@app.route('/')
def index_site():
    return render_template('index.html')

@app.route('/callc2c', methods=['POST'])
def callc2c():
    _source = request.form["sourcephone"]
    _destination = request.form["destinationphone"]

    if (_source and _destination):
        if (len(_source) and len(_destination)) == 9:
            if (_source.isdigit() and _destination.isdigit()):
                try:
                    _caller = RingCaller()
                    _caller.call(_source, _destination)
                    return render_template('ok.html')
                except:
                    return render_template('error.html')

    return render_template('error.html')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8081, debug=False)
