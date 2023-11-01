# -*- coding: utf-8 -*-
"""
Created on Wed Nov  1 21:47:16 2023

@author: nanik
"""
# from socketutil.request import Request
# from socketutil.response import Response
# from socketutil.request_must_key import RequestMustKeys
# from socketutil.response_must_key import ResponseMustKeys

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



if __name__ == '__main__':
    

    
    
    from _init import main
    main()