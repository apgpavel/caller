import os, json, sys, time, tempfile
import http.client
from configparser import ConfigParser

# import config file to global obj
config = ConfigParser()
config_file = 'config/config.ini'
config.read(config_file)

VN_SERVER_ADDRESS = config['default']['VnServerAddress']
APP_KEY = config['default']['AppKey']
APP_SECRET = config['default']['AppSecret']
EXTENSION_NUMBER = config['default']['ExtensionNumber']
REDIRECT_URI = 'https://' + VN_SERVER_ADDRESS + '/ouath/token.php'
TYPE = 'unifiedapi'
URI = 'https://' + VN_SERVER_ADDRESS + '/oauth/token.php'
MAX_AGE = 3600

TOKEN_PATH = os.path.join(
    tempfile.gettempdir(),
    '',
    'ifon.token',
)

class RingCaller:
    def __init__(self):
        self._token = None

    def _tokencheck(self):
        if os.path.isfile(TOKEN_PATH):
            token_age = time.time() - os.path.getmtime(TOKEN_PATH)
            if token_age < MAX_AGE:
                with open(TOKEN_PATH, 'r') as infile:
                    self._token = infile.read()

        if self._token is None:
            headerstoken = {"Content-type": "application/x-www-form-urlencoded"}
            contenttoken = "&client_id=" + APP_KEY + "&client_secret=" + APP_SECRET + "&grant_type=client_credentials&type=" + TYPE + "&redirect_uri=" + REDIRECT_URI
            conntoken = http.client.HTTPSConnection(VN_SERVER_ADDRESS)
            conntoken.request("POST", URI, contenttoken, headerstoken)
            response = conntoken.getresponse()
            raw_data = response.read()
            encoding = response.info().get_content_charset('utf8')
            token_json = json.loads(raw_data.decode(encoding))
            self._token = token_json['access_token']

            with open(TOKEN_PATH, 'w') as outfile:
                outfile.write(self._token)

        return self._token

    def call(self, _source, _destination):

        data = {
            "extension": EXTENSION_NUMBER,
            "phoneCallView" : [{
                "source" : _source,
                "destination": _destination
            }]
        }

        headerscall = {"Content-type": "application/json", "Authorization": "Bearer " + self._tokencheck()}

        # Makes a HTTP POST request using SSL
        conncall = http.client.HTTPSConnection(VN_SERVER_ADDRESS)
        conncall.request("POST", "/uapi/phoneCalls/@me/simple", json.dumps(data), headerscall)

        # Parses the JSON response
        response = conncall.getresponse()
        raw_data = response.read()
        encoding = response.info().get_content_charset('utf8')
        data = json.loads(raw_data.decode(encoding))

        if data is not None:
            return True
        else:
            return False
