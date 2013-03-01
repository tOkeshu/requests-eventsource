import requests
import json
from eventsource_parser import Event, parse


def eventsource(response):
    extra = ''
    for chunk in response.iter_content():
        extra += chunk
        event, extra = parse(extra)
        while event:
            yield event
            event, extra = parse(extra)

