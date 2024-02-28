from socketutil.test._test_simple_server import TestSinpleServer
from socketutil.test.test_my_sever import TestMyServer


if __name__=="__main__":
    # TestSinpleServer().run()
    TestMyServer().run()

"""
コンソールでPOST
curl "localhost:8080/api/post" -d "test" -s -v


コンソールでGET
curl "localhost:8080/api/get?page=3&num=10"  -s -v

"""

"""
コンソールでPOST
curl "localhost:54321/api/post" -d "test" -s -v


コンソールでGET
curl "localhost:54321/api/get?page=3&num=10"  -s -v

"""