from eventsource_parser import Event, parse


class ContentTypeError(Exception):
    pass

def eventsource(response):
    if response.headers['Content-Type'] != 'text/event-stream':
        message = 'Bad Content-Type, found "%s" instead of "text/event-stream"'
        raise ContentTypeError(message % response.headers['Content-Type'])

    extra = ''
    for chunk in response.iter_content():
        extra += chunk
        event, extra = parse(extra)
        while event:
            yield event
            event, extra = parse(extra)

