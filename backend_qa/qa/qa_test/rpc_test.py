import os, django

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "backend_qa.settings")
django.setup()

from qa.qa_test.rpc_utils import do_get_request, do_post_request

from qa.services.system.token import TOKEN_HEADER_KEY


def sys_register(email: str, full_name: str, password: str):
    return do_post_request('/auth/register', data={'email': email, 'fullName': full_name, 'password': password})


def sys_login(email: str, password: str):
    return do_post_request('/auth/login', data={'email': email, 'password': password})


def sys_logout(token: str):
    return do_post_request('/auth/logout', headers={TOKEN_HEADER_KEY: token})


def show_info(status_code: int, response_dict: dict):
    print('status_code[%d] and response: [%s]' % (status_code, response_dict))


# 数据库初始化脚本
if __name__ == '__main__':
    status_code, response_dict = sys_login('user@qq.com', 'abcdef123456')
    show_info(status_code, response_dict)
