from features.steps.utils import *
import requests
import json
from behave import given, when, then
from dotenv import load_dotenv
load_dotenv()

@given(u'I set Marvel API url')
def set_api_url(context):
    context.api_url = get_var_from_environment("API_URL")

@given(u'I have authorization keys to authenticate myself')
def set_authorization_keys(context):
    context.ts = get_timestamp()
    context.public_key = get_var_from_environment("PUBLIC_KEY")
    private_key = get_var_from_environment("PRIVATE_KEY")
    context.hash = make_a_hash(context.ts,private_key,context.public_key)

@given(u'I Set GET posts api endpoint "{endpoint}"')
def set_api_endpoint(context, endpoint):
    context.request_endpoint = endpoint

@given(u'I set the characterId {value} in Path')
def set_value_in_path(context, value):
    context.path_value = value
    print ( context.api_url + context.request_endpoint + value )

@given(u'I Set param request with "{parameter}" {value}')
def set_parameter_with_query_params(context, parameter, value):
    context.request_params = {
        "apikey": context.public_key,
        "ts": context.ts,
        "hash": context.hash,
        parameter: value
    }
    pre_endpoint = context.api_url + context.request_endpoint
    context.api_endpoints = pre_endpoint

@given(u'I Set param request')
def set_parameter_request(context):
    context.request_params = {
        "apikey": context.public_key,
        "ts": context.ts,
        "hash": context.hash
    }
    pre_endpoint = context.api_url + context.request_endpoint + context.path_value
    context.api_endpoints = pre_endpoint

@when(u'Send GET HTTP request')
def step_impl(context):
    print('    ',context.api_endpoints)
    response = requests.get(url=context.api_endpoints, params=context.request_params)
    context.response_texts = response.text
    statuscode = response.status_code
    context.response_codes = statuscode

@then(u'I receive valid HTTP response code {http_code:d}')
def receive_http_code(context, http_code):
    assert context.response_codes == http_code

@then(u'I get {title_expected:d} titles returned from the request')
def step_impl(context, title_expected):
    data = json.loads(context.response_texts)
    results = data["data"]["results"]
    assert len(results) == title_expected

    for i in results:
        title = i["title"]
        print ('    Title: ', title)

@then(u'I receive character {name} returned from the request')
def step_impl(context, name):
    data = json.loads(context.response_texts)
    results = data["data"]["results"]
    assert name == results[0]["name"]

@then(u'I receive the message error "{message_error}"')
def step_impl(context, message_error):
    data = json.loads(context.response_texts)
    assert message_error == data["status"]