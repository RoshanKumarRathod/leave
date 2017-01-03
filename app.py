#!/usr/bin/env python

import urllib
import json
import os

from flask import Flask
from flask import request
from flask import make_response

# Flask app should start in global layout
app = Flask(__name__)


@app.route('/webhook', methods=['POST'])
def webhook():
    req = request.get_json(silent=True, force=True)

    print("Request:")
    print(json.dumps(req, indent=4))

    res = processRequest(req)
    res = json.dumps(res, indent=4)
    # print(res)
    r = make_response(res)
    r.headers['Content-Type'] = 'application/json'
    return r


def processRequest(req):
    if req.get("result").get("action") != "yea":
        return {}
    r=req.get("result")
      d=json.loads(r)
    id= d.get("contexts").get(0).get("parameters").get("user-id")
     type= d.get("contexts")..get(0).get("parameters").get("leave-typ")
        range= d.get("contexts").get(0).get("parameters").get("date")
    data =id+"hello you reached heroku and your leave type is "+type+" date range is "+range 
    res = makeWebhookResult(data)
    return res

def makeWebhookResult(data):
    

    # print(json.dumps(item, indent=4))

    speech = data

    print("Response:")
    print(speech)

    return {
        "speech": speech,
        "displayText": speech,
        # "data": data,
        # "contextOut": [],
        "source": "apiai-leave-sample"
    }


if __name__ == '__main__':
    port = int(os.getenv('PORT', 5000))

    print "Starting app on port %d" % port

    app.run(debug=False, port=port, host='0.0.0.0')
