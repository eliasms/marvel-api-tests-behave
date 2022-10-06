from behave import given, when, then, step
from dotenv import load_dotenv
load_dotenv()
import os
import hashlib
import requests
from datetime import datetime
import json

api_url = None
api_endpoints = {}
public_key = {}
ts = {}
hash = {}
request_params = {}
response_codes = {}
response_texts = {}

@given(u'I set Marvel API url')
def step_impl(context):
    global api_url
    api_url = os.environ["API_URL"]

@given(u'I have authorization keys to authenticate myself')
def step_impl(context):
    global ts  
    ts = datetime.now().strftime("%d-%m-%Y-%H:%M:%S")

    global public_key
    public_key = os.environ["PUBLIC_KEY"]
    private_key = os.environ["PRIVATE_KEY"]

    pre_hash = ts+private_key+public_key

    global hash
    hash = hashlib.md5(pre_hash.encode('utf-8')).hexdigest()

@given(u'I Set GET posts api endpoint "{endpoint}"')
def step_impl(context, endpoint):
    api_endpoints['GET_URL'] = api_url+endpoint

@given(u'I Set HEADER param request with limit {limit}')
def step_impl(context, limit):
    request_params['GET'] = {
        "apikey": public_key,
        "ts": ts,
        "hash": hash,
        "limit": limit
    }

@when(u'Send GET HTTP request')
def step_impl(context):
    response = requests.get(url=api_endpoints['GET_URL'], params=request_params['GET'])
    response_texts['GET'] = response.text

    statuscode = response.status_code
    response_codes['GET'] = statuscode

@then(u'I receive valid HTTP response code 200')
def step_impl(context):
    assert response_codes['GET'] == 200

@then(u'I get {title_expected:d} titles returned from the request')
def step_impl(context, title_expected):
    data = json.loads(response_texts['GET'])
    results = data["data"]["results"]
    assert len(results) == title_expected

    for i in results:
        title = i["title"]
        print ('Title: ', title, '\n')