import http.server
import json

#Define a custome request handler by subclass

class MyRequestHandler(http.server.BaseHTTPRequestHandler):

    def do_Get(self):
        if self.path =='api/resource':
            self.send_response(200)
            self.send_header('Content-type','application/json')
            self.end_headers()
            response_data = {'Name':'Soumya','wish':'Happy BirthDay'}
            self.wfile.write(json.dumps(response_data).encode())

    # def do_Post(self):
    #     if self.path == 'api/data':
    #         content_length = int(self.headers['Content-Length'])
    #         post_data = self.rfile.read(content_length)
    #         data = json.loads(post_data)
    #         self.send_header(200)
    #         self.send_header('Content-type','application/json')
    #         self.end_headers()
    #         response_data = {'recevied_data':data}
    #         self.wfile.write(json.dumps(response_data).encode())


#Build Framework :- Tester - Framework Build








