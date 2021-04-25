import json

from django.core.exceptions import ValidationError
from django.contrib.auth.password_validation import validate_password
from django.http import HttpResponse, HttpResponseForbidden, HttpResponseBadRequest

from qa.models.user import User
from qa.utils.request_processor import fetch_parameter_dict
from qa.utils.response_generator import generate_response
from qa.services.system.token import update_token, TOKEN_HEADER_KEY, fetch_user_by_token, expire_token


def test(request):
    return HttpResponse("hello world")


def user_register(request):
    try:
        parameter_dict = fetch_parameter_dict(request, 'POST')
        username = parameter_dict['username']
        password = parameter_dict['password']
    except KeyError:
        return HttpResponseBadRequest(generate_response("parameter missing or invalid parameter"))

    try:
        validate_password(password=password)
    except ValidationError:
        return HttpResponseBadRequest(generate_response("password too simple"))

    try:
        User.objects.get(username=username)
        return HttpResponseBadRequest(generate_response("username already exist"))
    except User.DoesNotExist:
        User(username=username, password=password).save()
        return generate_response("OK")


def user_login(request):
    try:
        parameter_dict = fetch_parameter_dict(request, 'POST')
        user = User.objects.get(username=parameter_dict['username'])
        password = parameter_dict['password']
    except KeyError:
        return HttpResponseBadRequest(generate_response("parameter missing or invalid parameter"))
    except User.DoesNotExist:
        return HttpResponseBadRequest(generate_response("username doesn't exist"))

    if password != user.password:
        return HttpResponseForbidden(generate_response("wrong password"))

    new_token, new_expire_time = update_token(user)
    response_data = {'token': new_token, 'expire_time:': new_expire_time}
    return generate_response("OK", response_data)


def user_logout(request):
    token = request.META.get(TOKEN_HEADER_KEY)
    user = fetch_user_by_token(token)
    if user:
        expire_token(token)
        return generate_response("OK")
    else:
        return HttpResponseForbidden(generate_response("invalid token"))
