from dataclasses import dataclass
import requests

@dataclass
class Response:
    status_code: int
    text: str
    as_dict: object
    headers: dict

class APIRequest:
    def get(self, url, params):
        response = requests.get(url, params)
        return self.__get_responses(response)

    def __get_responses(self, response):
        status_code = response.status_code
        text = response.text

        try:
            as_dict = response.json()
        except Exception:
            as_dict = {}

        headers = response.headers

        return Response(
            status_code, text, as_dict, headers
        )