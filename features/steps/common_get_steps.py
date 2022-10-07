import os
import hashlib
import requests
from datetime import datetime
import json
from behave import given, when, then
from dotenv import load_dotenv
load_dotenv()

api_url = None
api_endpoints = {}
public_key = {}
ts = {}
hash = {}
request_params = {}
response_codes = {}
response_texts = {}
path_value = None

@given(u'I set Marvel API url')
def set_api_url(context):
    global api_url
    api_url = os.environ["API_URL"]

@given(u'I have authorization keys to authenticate myself')
def set_authorization_keys(context):
    global ts  
    ts = datetime.now().strftime("%d-%m-%Y-%H:%M:%S")

    global public_key
    public_key = os.environ["PUBLIC_KEY"]
    private_key = os.environ["PRIVATE_KEY"]

    pre_hash = ts+private_key+public_key

    global hash
    hash = hashlib.md5(pre_hash.encode('utf-8')).hexdigest()

@given(u'I Set GET posts api endpoint "{endpoint}"')
def set_api_endpoint(context, endpoint):
    global request_endpoint
    request_endpoint = endpoint

@given(u'I set the characterId {value} in Path')
def set_value_in_path(context, value):
    global path_value
    path_value = value
    print ( api_url + request_endpoint + path_value )

@given(u'I Set param request with "{parameter}" {value}')
def set_parameter_with_query_params(context, parameter, value):
    request_params['GET'] = {
        "apikey": public_key,
        "ts": ts,
        "hash": hash,
        parameter: value
    }
    pre_endpoint = api_url + request_endpoint
    api_endpoints['GET_URL'] = pre_endpoint

@given(u'I Set param request')
def set_parameter_request(context):
    request_params['GET'] = {
        "apikey": public_key,
        "ts": ts,
        "hash": hash
    }
    pre_endpoint = api_url + request_endpoint + path_value
    api_endpoints['GET_URL'] = pre_endpoint

@when(u'Send GET HTTP request')
def step_impl(context):
    print('    ',api_endpoints['GET_URL'])
    response = requests.get(url=api_endpoints['GET_URL'], params=request_params['GET'])
    response_texts['GET'] = response.text

    statuscode = response.status_code
    response_codes['GET'] = statuscode

@then(u'I receive valid HTTP response code {http_code:d}')
def receive_http_code(context, http_code):
    assert response_codes['GET'] == http_code

@then(u'I get {title_expected:d} titles returned from the request')
def step_impl(context, title_expected):
    data = json.loads(response_texts['GET'])
    results = data["data"]["results"]
    assert len(results) == title_expected

    for i in results:
        title = i["title"]
        print ('    Title: ', title)

@then(u'I receive character {name} returned from the request')
def step_impl(context, name):
    data = json.loads(response_texts['GET'])
    results = data["data"]["results"]
    assert name == results[0]["name"]

@then(u'I receive the message error "{message_error}"')
def step_impl(context, message_error):
    data = json.loads(response_texts['GET'])
    assert message_error == data["status"]