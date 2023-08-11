# -*- coding: utf-8 -*-
"""
Created on Fri Aug 11 14:00:56 2023

@author: nanik
"""

import asyncio
from datetime import datetime
import json
import time

from random_name import get_random_string

class Client:
    MESSAGE_KEY = "message"
    TIMESTAMP_KEY = "timestamp"
    HOST = "127.0.0.1"
    PORT = 48888
    ENCODEING = "utf-8"
    BUFFER = 128

    @classmethod
    async def tcp_echo(cls, data: dict):
        reader, writer = await asyncio.open_connection(
            cls.HOST, cls.PORT)
    
        print(f'client Send: {data[cls.MESSAGE_KEY]!r}')
        json_data = json.dumps(data).encode(cls.ENCODEING)
        writer.write(json_data)
        await writer.drain()
    
        #//recive
        data: bytes = await reader.read(cls.BUFFER)
        json_data = data.decode(cls.ENCODEING)
        dict_ = json.loads(json_data)
        print(f'client Received: {dict_[cls.TIMESTAMP_KEY]} {dict_[cls.MESSAGE_KEY]!r}')
    
        print('client Close the connection')
        writer.close()
        await writer.wait_closed()


if __name__ == "__main__":
    
    name = get_random_string()
    
    for i in range(10):
        now = datetime.now().strftime("%H:%M:%S")
        data = dict(message=f"{name}君の{i}回目の Hello World!!",
                     timestamp = now)
        asyncio.run(Client.tcp_echo(data))
        
        time.sleep(1)
    

    

