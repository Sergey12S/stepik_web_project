def application(environ, start_response):
    start_response('200 OK', [('Content-Type', 'text/plain')])
    return "\n".join(environ.get('QUERY_STRING').split("&"))
