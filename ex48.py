
class lexicon(object):
    def __init__(self):
        self.result = []
        self.direction_words = ("north", "south", "west", "down", "up", "left", "right", "back")
        self.verbs = ("go", "stop", "kill", "eat")
        self.stop_words = ("the", "in", "of", "from", "at", "it")
        self.nouns = ("door", "bear", "princess", "cabinet")
        self.numbers = (1, 2, 3, 4, 5, 6, 7, 8, 9)

    def scan(self, user_input):
        for i in user_input.split():
            if i in self.direction_words:
                self.result.append(("directiom", i))
            elif i in self.verbs:
                self.result.append(("verb", i))
            elif i in self.stop_words:
                self.result.append(("stop", i))
            elif i in self.nouns:
                self.result.append(("noun", i))
            elif i in self.numbers:
                self.result.append(("number", i))
            else:
                self.result.append(("error", i))
        return self.result


###############################################################################
from nose.tools import *
from ex48 import lexicon

def test_directions():
    assert_equal(lexicon.scan("north"), [("direction", "north")])
    result = lexicon.scan("north south east")
    assert_equal(result, [("direction", "north"),
                          ("direction", "south"),
                          ("direction", "east")])


def test_verbs():
    assert_equal(lexicon.scan("go"), [("verb", "go")])
    result = lexicon.scan("go kill eat")
    assert_equal(result, [('verb', "go"),
                          ("verb", "kill"),
                          ("verb", "eat")])




def test_stops():
    assert_equal(lexicon.scan("the"), [("stop", "the")])
    result = lexicon.scan("the in of")
    assert_equal(result, [('stop', "the"),
                          ("stop", "in"),
                          ("stop", "of")])



def test_numbers():
    assert_equal(lexicon.scan("1234"), [("number", "1234")])
    result = lexicon.scan("3 91234")
    assert_equal(result, [('number', 3),
                          ("number", 91234)])


def test_errors():
    assert_equal(lexicon.scan("ASDFASDF"), [("error", "ASDFASDF")])
    result = lexicon.scan("bear IAS princess")
    assert_equal(result, [('noun', "bear"),
                          ("error", "IAS")
                          ("noun", "princess")])










































