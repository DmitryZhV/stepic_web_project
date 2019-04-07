#import multiprocessing

bind = "0.0.0.0:8080"
#workers = multiprocessing.cpu_count() * 2 + 1

def app(environ, start_response):
        data = [bytes(i+'\n') for i in environ['QUERY_STRING'].split('&')]
        print(len(data))
        print(len([data]))
        s=''
        for i in data:
            s+=i
        print(s)

        
        
        start_response("200 OK", [
            ("Content-Type", "text/plain"),
            ("Content-Length", str(len(s)))
        ])
        
        return s
