import sys
import json
from typing import Any
from socket import  socket
from http.server import BaseHTTPRequestHandler, HTTPServer
from http import HTTPStatus
from socketserver import BaseServer
from httputil.HttpConfiguration import HttpConfiguration
from typing import BinaryIO
from http.client import HTTPMessage

from httputil.GetRequestReader import GetRequestReader


class MyHttpSeverHandler(BaseHTTPRequestHandler):
    path : str
    headers : HTTPMessage
    rfile : BinaryIO

    def __init__(self, request: socket | tuple[bytes, socket], client_address: Any, server: BaseServer) -> None:
        super().__init__(request, client_address, server)
        # リクエストされたパスはpath、HTTPヘッダーはheaders、HTTPボディはrfileに格納される。
        # path
        # headers
        # rfile

        # レスポンスを返す時は、send_responseでHTTPステータスコードを指定し、必要に応じてHTTPヘッダーをsend_headerで指定する。
        # HTTPヘッダーの終了をend_headersで指定。HTTPボディを送るにはwfileを使用します。
        # send_response
        # send_header
        # end_headers
        # wfile

    # @override
    def do_GET(self):
        enc = sys.getfilesystemencoding()
        # // self.headersに格納されている。headersオブジェクトはイテレータ
        # [print(f'key = {k}, value = {self.headers[k]}') for k in self.headers]

        reader = GetRequestReader(self.path)
        print(reader)

        # //　ステータス行
        self.send_response(HTTPStatus.OK)
        #// リターンするデータ Jsonで返すAPIを想定
        responce_data = {
            'status' : 200,
            'path' : self.path,
            'message' : 'GetMethoのテストです',
            'get_value': str(reader),
        }
        encoded_data = json.dumps(responce_data).encode(enc)

        self.send_header('Access-Control-Allow-Origin', '*') # オープンなAPI等どっからでもアクセスOKの意
        self.send_header("Content-type", "text/plain; charset=%s" % enc)
        self.send_header("Content-Length", str(len(encoded_data)))
        self.end_headers()

        self.wfile.write(encoded_data)

        print('*'*100)

    # @override
    def do_POST(self):
        enc = sys.getfilesystemencoding()
        # print('path = ',self.path)
        # [print(f'key = {k}, value = {self.headers[k]}') for k in self.headers]
        length = self.headers.get('content-length')

        decodedPostData = ''
        if length is not None:
            nbytes = int(length)
            rawPostData = self.rfile.read(nbytes)
            decodedPostData = rawPostData.decode(enc)
            print(decodedPostData)

        #// リターンするデータ Jsonで返すAPIを想定
        responce_data = {
            'status' : 200,
            'path' : self.path,
            'message' : 'PostMethoのテストです',
            'request': str(decodedPostData)
        }
        encoded_data = json.dumps(responce_data).encode(enc)

        #//ステータス情報
        self.send_response(HTTPStatus.OK)

        #//ヘッダー情報
        self.send_header('Access-Control-Allow-Origin', '*') # オープンなAPI等どっからでもアクセスOKの意
        self.send_header("Content-type", "text/plain; charset=%s" % enc)
        self.send_header("Content-Length", str(len(encoded_data)))
        self.end_headers()
        #//body 書きこむ
        self.wfile.write(encoded_data)

        print('+'*100)


class MyHttpServer:
    PORT : int = HttpConfiguration.PORT.value
    def __init__(self) -> None:
        pass

    def run(self, server_class=HTTPServer, handler_class=MyHttpSeverHandler):
        server_address = ('', self.PORT)
        httpd = server_class(server_address, handler_class)
        print(f'Starting httpd on port {server_address[1]}...')
        httpd.serve_forever()

