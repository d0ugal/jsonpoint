try:
    from unittest2 import TestCase
except:
    from unittest import TestCase


class JSONPointTestCase(TestCase):

    def test_get_pointer(self):

        import jsonpoint

        data = '{"foo": ["bar", "baz"], "": 0, "a/b": 1, "c%d": 2, "e^f": 3, "g|h": 4, "i\\\\j": 5, "k\\"l": 6, " ": 7, "m~n": 8}'

        cases = (
            ("", {"foo": ["bar", "baz"], "": 0, "a/b": 1, "c%d": 2, "e^f": 3,
                "g|h": 4, "i\\j": 5, "k\"l": 6, " ": 7, "m~n": 8}),
            ("/foo", ["bar", "baz"]),
            ("/foo/0", "bar"),
            ("/", 0),
            ("/a~1b", 1),
            ("/c%d", 2),
            ("/e^f", 3),
            ("/g|h", 4),
            ("/i\\j", 5),
            ("/k\"l", 6),
            ("/ ", 7),
            ("/m~0n", 8)
        )

        for pointer, expected in cases:

            self.assertEquals(jsonpoint.get(data, pointer), expected)

    def test_get_numeric_strings(self):

        import jsonpoint

        data = '{"0": "1"}'

        self.assertEquals(jsonpoint.get(data, "/0"), "1")

    def test_get_non_numeric_list(self):

        import jsonpoint
        from jsonpoint.parser import InvalidPointer

        data = '{"foo": [1,2,3]}'

        with self.assertRaises(InvalidPointer):
            jsonpoint.get(data, "/foo/a")
