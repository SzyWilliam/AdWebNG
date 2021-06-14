from django.http import HttpResponse, HttpResponseForbidden, HttpResponseBadRequest

from qa.utils.kg_util import KGUtil
from qa.utils.request_processor import fetch_parameter_dict
from qa.utils.response_generator import generate_response


def query(request):
    try:
        question = request.GET["query"]
    except KeyError:
        return HttpResponseBadRequest(generate_response("parameter missing or invalid parameter"))

    kg_util = KGUtil()
    answers = kg_util.kg_query(question)

    if not answers:
        return generate_response("OK", {"result": "error", "answer": []})
    else:
        return generate_response("OK", answers)


def delete(request):
    try:
        question = fetch_parameter_dict(request, "POST")["query"]
    except KeyError:
        return HttpResponseBadRequest(generate_response("parameter missing or invalid parameter"))

    kg_util = KGUtil()
    t = kg_util.kg_delete(question)

    if not t:
        return generate_response("OK", {"result": "error"})
    else:
        return generate_response("OK", {"result": "ok"})


def update(request):
    try:
        param_dict = fetch_parameter_dict(request, "POST")
        question = param_dict["query"]
        answers = param_dict["answer"]
    except KeyError:
        return HttpResponseBadRequest(generate_response("parameter missing or invalid parameter"))

    kg_util = KGUtil()
    t = kg_util.kg_update(question, answers)

    if not t:
        return generate_response("OK", {"result": "error"})
    else:
        return generate_response("OK", {"result": "ok"})


def insert(request):
    try:
        param_dict = fetch_parameter_dict(request, "POST")
        question_type = param_dict["type"]
        param1 = param_dict["param1"]
        param2 = param_dict["param2"]
    except KeyError:
        return HttpResponseBadRequest(generate_response("parameter missing or invalid parameter"))

    kg_util = KGUtil()
    t = kg_util.kg_insert(question_type, param1, param2)
    if not t:
        return generate_response("OK", {"result": "error"})
    else:
        return generate_response("OK", {"result": "ok"})
