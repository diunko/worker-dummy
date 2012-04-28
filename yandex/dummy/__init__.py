# coding: utf-8

from cocaine.context import Log
from cocaine.decorators import native

from hashlib import sha512

log = Log()

@native
def hash(meta, request):
    return sha512(str(request)).hexdigest()
