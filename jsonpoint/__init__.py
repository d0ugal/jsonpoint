__version__ = (0, 1, 0, "dev", 0)

# Import json modules in order of speed.
try:
    import ujson as json
except:
    try:
        import simplejson as json
    except:
        import json

from .parser import walk


def get(json_string, pointer):
    j = json.loads(json_string)
    return walk(j, pointer)
