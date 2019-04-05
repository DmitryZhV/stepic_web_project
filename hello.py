import multiprocessing

bind = "0.0.0.0:8080"
workers = multiprocessing.cpu_count() * 2 + 1

def app(environ, start_response):
        data = b(i+'\n', 'ascii') for i in environ['QUERY_STRING'].split('&')
        start_response("200 OK", [
            ("Content-Type", "text/plain"),
            ("Content-Length", str(len(data)))
        ])
        return iter([data])
