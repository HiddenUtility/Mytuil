# -*- coding: utf-8 -*-
"""
Created on Fri Aug 11 14:02:04 2023

@author: nanik
"""

import asyncio
import json
from datetime import datetime
import random

class Server:
    MESSAGE_KEY = "message"
    TIMESTAMP_KEY = "timestamp"
    HOST = ""
    PORT = 48888
    BUFFER = 128
    ENCODEING = "utf-8"
    
    @classmethod
    async def process(cls) -> bytes:
        
        #//なんかの非同期処理が走る
        await asyncio.sleep(random.randint(10, 100))
        
        now = datetime.now().strftime("%H:%M:%S")
        data = dict(message="Success!!",
                     timestamp = now)
        json_data = json.dumps(data).encode(cls.ENCODEING)
        return json_data
    

    @classmethod
    async def handle_echo(cls, reader, writer):
        byte_data = await reader.read(cls.BUFFER)
        json_data: bytes = byte_data.decode(cls.ENCODEING)
        data: dict = json.loads(json_data)
        
        message = data[cls.MESSAGE_KEY]
        time_stamp = data[cls.TIMESTAMP_KEY]
        addr = writer.get_extra_info('peername')
    
        print(f"server Received {time_stamp!r} {message!r} from {addr!r}")
        print(f"server Send: {message!r}")
        
        #/*なんか処理*/
        return_data = await cls.process()
        writer.write(return_data)
        #//drain() is wating to write byte data
        await writer.drain()
        
        print(f"server Close the connection from {addr!r}")
        writer.close()
        await writer.wait_closed()
        
    @classmethod
    async def main(cls):
        server = await asyncio.start_server(
            cls.handle_echo, cls.HOST, cls.PORT)
    
        addrs = ', '.join(str(sock.getsockname()) for sock in server.sockets)
        print(f'Serving on {addrs}')
    
        async with server:
            await server.serve_forever()
            
if __name__ == "__main__":
    asyncio.run(Server.main())