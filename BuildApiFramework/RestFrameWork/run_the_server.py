import http.server
from create_request_handeler import MyRequestHandler


def run_server():
    port_number = 8000
    server_address = ('',port_number)
    httpd = http.server.HTTPServer(server_address,MyRequestHandler)
    print('Server running on port 8000')
    httpd.serve_forever()

if __name__ =='__main__':
    run_server()
