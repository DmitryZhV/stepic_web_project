
def app(environ, start_response):
        data =[(i+'\n') for i in environ['QUERY_STRING'].split('&')]
        s=''
        for i in data:
            s+=i
        start_response("200 OK", [
            ("Content-Type", "text/plain"),
            ("Content-Length", str(len(s)))
        ])
        return s
