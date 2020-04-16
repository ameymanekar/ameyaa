from urllib.request import urlopen

from flask import *
import requests
import urllib, json

app = Flask(__name__, template_folder='templates')


@app.route('/')
def index():
    url = "https://api.covid19india.org/state_district_wise.json"
    json_url = urlopen(url)

    data = json.loads(json_url.read())

    data2 = data['Maharashtra']

    data3 = data2['districtData']

    url = "https://covid19india.p.rapidapi.com/getStateData/MH"

    headers = {
        'x-rapidapi-host': "covid19india.p.rapidapi.com",
        'x-rapidapi-key': "8e88d02bc4mshcd151b981c7bc87p1b9079jsn54cabcb1ac7c"
    }

    response = requests.request("GET", url, headers=headers)
    dataa = json.loads(response.text)

    return render_template('index.html', result=data3, result2=dataa)







if __name__ == '__main__':
    app.run(debug=True)

