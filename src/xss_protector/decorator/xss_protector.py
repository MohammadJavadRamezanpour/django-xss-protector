from django.http import JsonResponse
from xss_protector.utils import silent_delete_from_dictionary, exclude_fields, filter_fields


def xss_protector(*keys, lst_invalid_chars=None, lst_excluding_keys=None, response_on_error=None):
    """
    this decorator will search for all invalid chars in a value for xss protection

    Parameters:
        *keys: each key you want to check for potential xss attack, it will check all keys if you dont send it
        lst_invalid_chars(list): list of invalid chars, default: ["<", ">"]
        lst_excluding_keys: set exception for some keys, default: []
        response_on_error: what to return on error, can be anything, default JsonResponse({"ERROR": "malformed data"}, status=400)
    Returns:
        returns the view function if everything is ok, response_on_error on the other hand
    """

    if lst_invalid_chars is None:
        lst_invalid_chars = ["<", ">"]

    if lst_excluding_keys is None:
        lst_excluding_keys = []

    if response_on_error is None:
        response_on_error = JsonResponse(
            {"ERROR": "malformed data"}, status=400)

    def decorator(function):
        def wrap(request, *args, **kwargs):
            fields = exclude_fields(request, **kwargs)
            cleared_fields = silent_delete_from_dictionary(
                fields, lst_excluding_keys)
            filtered_fields = filter_fields(cleared_fields, keys)

            for dictionary in filtered_fields:
                for value in dictionary.values():
                    for invalid_value in lst_invalid_chars:
                        if invalid_value in value:
                            return response_on_error

            return function(request, *args, **kwargs)

        return wrap

    return decorator
