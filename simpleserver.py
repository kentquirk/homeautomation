# simple flask server test
#! /usr/bin/env python

import os
from flask import Flask, abort
app = Flask(__name__)

secret = os.environ['AUTOMATION_SECRET']
if not secret:
    exit(1)

@app.route('/')
def goaway():
    abort(403)

@app.route('/' + secret + '/environ')
def dump_environment():
    s = '\n'.join(['<p>%s=%s</p>' % (e, os.environ[e]) for e in os.environ])
    return 'Hello World!: \n%s' % s

@app.route('/' + secret + '/test/<int:return_code>')
def test_response(return_code):
    #return 'this is a test of %s' % return_code
    return ('This is a test of %s' % return_code, return_code, [])

if __name__ == '__main__':
    # for now, let's turn debug on
    app.debug = True
    app.run(host='0.0.0.0', port=5151)
