JSON Pointer for Python
=======================

This module provides JSON Pointer support for Python datastructures, as
well as JSON strings.


Usage
-----

Given::

    json_s = """
    {
        "foo": {
            "bar": [ "element0", "element1" ],
            "inner object": {
            "baz": "qux"
        }
    }
    """

Import it::

    import jsonpoint

Examples::

    >>> jsonpoint.get('/foo/inner%20object', json_s)
    {'baz': 'qux'}

    >>> jsonpoint.get('/foo/inner%20object/baz', json_s)
    'qux'

    >>> jsonpoint.get('/foo/bar/0', json_s)
    'element0'


See Also
--------

http://tools.ietf.org/html/rfc6901
