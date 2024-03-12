from httputil import MyHttpServer
from httputil.my_socket_server import MySocketServer


if __name__ == '__main__':
    ''''
    httputil/test/index.htmlに getとpostのテストを準備している。
    port:8080に対して送る
    '''

    #原始的なソケットサーバーでリクエストの平文を得る。
    #リクエストをhttpで書くのめんどいのであくまでどんなリクエストが飛んでくるのが確認する。
    MySocketServer().run()    

    #http.severでサーバー作る。
    # MyHttpServer().run()



