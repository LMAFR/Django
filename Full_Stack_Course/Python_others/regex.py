import re

def multi_re_find(patterns, phrase):

    for pat in patterns:
        print("Searching for pattern {}".format(pat))
        print(re.findall(pat,phrase))
        print("\n")

test_phrase = "This is a string! But it has punctuation. How can we remove it? 1234 ssddd sssd sdsdd sssddd ddsd sd"

test_patterns = ["[^.!?]+", "[A-Z]+", r"\d+", "sd{3}", "sd*", "sd+"]

multi_re_find(test_patterns, test_phrase)