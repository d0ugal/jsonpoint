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

    from jsonpoint import jsonpoint

Examples::

    >>> jsonpoint('/foo/inner%20object', json_s)
    {'baz': 'qux'}

    >>> jsonpoint('/foo/inner%20object/baz', json_s)
    'qux'

    >>> jsonpoint('/foo/bar/0', json_s)
    'element0'


See Also
--------

http://www.ietf.org/id/draft-pbryan-zyp-json-pointer-01.txt