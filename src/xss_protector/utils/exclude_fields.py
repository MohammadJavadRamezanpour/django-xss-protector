import json
from django.http import HttpRequest


def exclude_fields(request: HttpRequest, **kwargs) -> list:
    """
    this functions chooses proper field based on request method
    inputs:
        request: django request object
    returns a list
    """
    query_string = request.GET.dict()
    url_params = kwargs
    body = request.body
    form_data = request.POST.dict()
    fields = [query_string, url_params, form_data]

    if body:
        body = json.loads(body)
        fields.append(body)
    return fields
