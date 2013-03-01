Requests EventSource
=====================

requests-eventsource is an EventSource_ implementation on top of
Requests_ and eventsource-parser_.

.. _EventSource: http://www.w3.org/TR/eventsource/
.. _Requests: http://docs.python-requests.org/
.. _eventsource-parser: https://github.com/tOkeshu/eventsource-parser

Example
-------

::

    r = requests.get('http://example.com/ev', stream=True)
    for event in eventsource(r):
        if event.type == 'rpc':
            do_something(event)
        if event.type == 'json':
            print(json.loads(event.data))


License
-------

Licensed under the Apache License, Version 2.0.

