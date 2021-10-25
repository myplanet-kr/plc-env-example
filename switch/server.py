# -*- coding: utf-8 -*-

class server:
    def __init__(self, domain, path, token):
        self.domain = domain
        self.path = path
        self.token = token
        path = '/device/auto'

def set_dotori_server_config_script():
    addr = input('0. 도메인 주소를 입력해주세요. (기본:https://api.dotoritory.com) ')
    if (addr == ''): addr = 'https://api.dotoritory.com'
    token = input('1. device 토큰을 입력해주세요.')
    if (token == ''): raise ValueError('token값은 필수적으로 입력돼야 합니다.')
    return server(addr, '/device/auto', token)
