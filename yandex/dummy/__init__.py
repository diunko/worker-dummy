# coding: utf-8

from cocaine.context import Log, Dispatch
from cocaine.http import http

from hashlib import sha512

log = Log()
dispatch = Dispatch()

@http
def hash(request, response):
    def process():
        result = "<html><head>Hash</head>%s</html>" % sha512(str(request.headers)).hexdigest()
        
        response.writeHead(200, {
            'Content-Type': 'text/plain'
        })
        
        response.write(result)
        response.close()

    request.on("request", process)
    request.on("body", lambda chunk: pass)

def loop(request, response):
    response.close()

dispatch.on("hash", hash)
dispatch.on("loop", loop)
