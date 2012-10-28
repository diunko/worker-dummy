# coding: utf-8

from cocaine.context import Log
from cocaine.decorators import simple

from hashlib import sha512

log = Log()

@simple
def hash(meta, request):
    for i in xrange(int(request['n'])):
        request = sha512(str(request)).hexdigest()

    return request

def hash_body(io):
    io.read()
    io.write(io.read())

def loop(io):
    pass
