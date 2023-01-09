import json

from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from .models import TestModel
from xss_protector.decorator import xss_protector


@xss_protector(response_on_error=JsonResponse({"ERROR": "custome error"}, status=400))
def test_view(request, param=None):
    if request.body:
        body = json.loads(request.body)
    test_model = TestModel.objects.create(test_field="1")
    return HttpResponse(str(param) + str(test_model.pk))


@xss_protector(response_on_error=JsonResponse({"ERROR": "custome error"}, status=400), lst_excluding_keys=['excluding_key'])
def test_view_with_exluding_keys(request, param=None):
    if request.body:
        body = json.loads(request.body)
    return HttpResponse("done", 200)


@xss_protector(response_on_error=JsonResponse({"ERROR": "custome error"}, status=400), lst_excluding_keys=['excluding_key'])
def test_view_with_exluding_keys(request, param=None):
    if request.body:
        body = json.loads(request.body)
    return HttpResponse("done", 200)


@xss_protector("key1", "key2", response_on_error=JsonResponse({"ERROR": "custome error"}, status=400))
def test_view_with_keys(request, param=None):
    if request.body:
        body = json.loads(request.body)
    return HttpResponse("done", 200)
