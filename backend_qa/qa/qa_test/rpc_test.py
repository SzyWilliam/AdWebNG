import os, django

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "backend_qa.settings")
django.setup()

from qa.qa_test.rpc_utils import do_get_request, do_post_request


def sys_register(email: str, full_name: str, password: str):
    return do_post_request('/auth/register', data={'email': email, 'fullName': full_name, 'password': password})


def kg_query(question: str):
    return do_get_request('/kg/query', params={'query': question})


def kg_delete(question: str):
    return do_post_request('/kg/delete', data={'query': question})


def kg_update(question: str, answers: list):
    return do_post_request('/kg/update', data={'query': question, 'answer': answers})


def kg_insert(question_type: str, param1: str, param2: list):
    return do_post_request('/kg/insert', data={'type': question_type, 'param1': param1, "param2": param2})


def show_info(status_code: int, response_dict: dict):
    print('status_code[%d] and response: [%s]' % (status_code, response_dict))


if __name__ == '__main__':
    status_code, response_dict = kg_query("ccc的多久治好")
    show_info(status_code, response_dict)
    status_code, response_dict = kg_insert("disease_last_time", "ccc", ["1个月", "2个月"])
    show_info(status_code, response_dict)
    status_code, response_dict = kg_query("ccc的多久治好")
    show_info(status_code, response_dict)
