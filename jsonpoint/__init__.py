__version__ = (0, 1, 0, "dev", 0)

# Import json modules in order of speed.
try:
    import ujson as json
except:
    try:
        import simplejson as json
    except:
        import json


class InvalidPointer(Exception):
    pass


def parse(pointer):
    """
    Parse the JSON pointer and split into tokens.
    Converts ~0 to ~ and ~1 to /
    """

    if pointer == "":
        # optimisation for empty pointers.
        raise StopIteration

    if not pointer.startswith("/"):
        raise InvalidPointer("JSON pointer %r does not start with /" % (pointer))

    pointer = pointer[1:]
    parts = pointer.split("/")

    for part in parts:

        part = part.replace("~0", "~")
        part = part.replace("~1", "/")

        yield part


def walk(document, pointer):

    tokens = list(parse(pointer))

    for i, token in enumerate(tokens, 1):

        if isinstance(document, list):
            if token.isdigit():
                token = int(token)
            else:
                error = "Token %r (position: %s) from pointer %r is invald for the current evaluated value (%r) which is a list"
                raise InvalidPointer(error % (token, i, pointer, document))
            document = document[token]
        else:
            document = document[token]

    return document


def get(json_string, pointer):
    j = json.loads(json_string)
    return walk(j, pointer)
