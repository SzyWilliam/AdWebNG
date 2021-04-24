import json

from django.http import HttpResponse


def generate_response(msg: str, data: object = None):
    response_dict = {'msg': msg}
    if object is not None:
        response_dict['data'] = data
    response = HttpResponse(json.dumps(response_dict))
    return response
