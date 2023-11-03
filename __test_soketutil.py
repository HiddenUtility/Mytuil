# -*- coding: utf-8 -*-
"""
Created on Wed Nov  1 21:47:16 2023

@author: nanik
"""
# from socketutil.request import Request
# from socketutil.response import Response
# from socketutil.request_must_key import RequestMustKeys
# from socketutil.response_must_key import ResponseMustKeys

from threading import Thread
from time import sleep
from _init import main

from socketutil.request_data import RequestData
from socketutil.response_data import ResponseData
from socketutil.errors import NotHasMustKeyError

from socketutil.tcp_client import Client
from socketutil.tcp_server import Server

def test_requ_resp():
    
    data = dict(head="", body="")
    request = RequestData().load_dict(data)
    
    data = dict(test="", body="")
    try:
        request = RequestData().load_dict(data)
    except NotHasMustKeyError:
        pass
    
    data = dict(status="200", body="")
    response = ResponseData().load_dict(data)           


def run_server():
    Server().run()
    sleep(1)


if __name__ == '__main__':
    
    test_requ_resp()
    
    t = Thread(target=run_server)
    t.start()
    
    data = dict(head="", body="")
    request = RequestData().load_dict(data)
    client = Client()
    resp = client.send(request)
    print(resp)
    

    main()
