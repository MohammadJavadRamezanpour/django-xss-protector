import json

from django.http import JsonResponse
from ..utils.silent_delete_from_dictioary import silent_delete_from_dictioary

def xss_protector(*keys, lst_invalid_chars=None, lst_exclude_keys=None, response_on_error=None):
    """
    this decorator will search for all invalid chars in a value for xss protection

    Parameters:
        *keys: each key you want to check for potential xss attack, it will check all keys if you dont send it
        lst_invalid_chars(list): list of invalid chars, default: ["<", ">"]
        lst_exclude_keys: set exception for some keys, default: []
        response_on_error: what to return on error, can be anything, default JsonResponse({"ERROR": "malformed data"}, status=400)
    Returns:
        returns the view function if everything is ok, response_on_error on the other hand
    """

    if lst_invalid_chars is None:
        lst_invalid_chars = ["<", ">"]

    if lst_exclude_keys is None:
        lst_exclude_keys = []

    if response_on_error is None:
        response_on_error = JsonResponse(
            {"ERROR": "malformed data"}, status=400)

    def decorator(function):
        def wrap(request, *args, **kwargs):
            if request.method == "GET":
                return function(request, *args, **kwargs)

            body = silent_delete_from_dictioary(
                json.loads(request.body), lst_exclude_keys)
            query_string = silent_delete_from_dictioary(
                request.GET.dict(), lst_exclude_keys)
            url_params = silent_delete_from_dictioary(kwargs, lst_exclude_keys)
            form_data = silent_delete_from_dictioary(request.POST.dict(), lst_exclude_keys)

            if not keys:
                # check all possible values
                for dictionary in [body, query_string, url_params, form_data]:
                    for value in dictionary.values():
                        for invalid_value in lst_invalid_chars:
                            if invalid_value in value:
                                return response_on_error

            else:
                # check the given keys only
                for dictionary in [body, query_string, url_params, form_data]:
                    for key in keys:
                        for invalid_value in lst_invalid_chars:
                            if invalid_value in str(dictionary.get(key)):
                                return response_on_error

            return function(request, *args, **kwargs)

        return wrap

    return decorator
