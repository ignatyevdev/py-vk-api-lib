import urllib.request, urllib.parse
import json

from vk_api.error import Error
from vk_api.object import VKObject

def call_method(method_name, **params):

    endpoint = "https://api.vk.com/method/"
    query = urllib.parse.urlencode(params)
    url = endpoint + method_name + "?" + query

    result = json.loads(urllib.request.urlopen(url).read())

    if 'error' in result:
        error = result['error']
        raise Error(error['error_code'], error['error_msg'], error['request_params'])

    if isinstance(result['response'], dict):
        return VKObject(result['response'])

    elif isinstance(result['response'], (list, tuple)):
        objects = []
        for object in result['response']:
            objects.append(VKObject(object))
        return objects

    return result['response']
