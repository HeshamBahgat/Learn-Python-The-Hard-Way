
from nose.tools import *
from ex48_icon import Lexicon

def test_directions():
    assert_equal(Lexicon.scan("north"), [("direction", "north")])
    result = Lexicon.scan("north south east")
    assert_equal(result, [("direction", "north"), ("direction", "south"), ("direction", "east")])

    
    
   
def test_verbs():
    assert_equal(Lexicon.scan("go"), [("verb", "go")])
    result = Lexicon.scan("go kill eat")
    assert_equal(result, [('verb', "go"), ("verb", "kill"), ("verb", "eat")])



def test_stops():
    assert_equal(Lexicon.scan("the"), [("stop", "the")])
    result = Lexicon.scan("the in of")
    assert_equal(result, [('stop', "the"), ("stop", "in"), ("stop", "of")])
    



def test_errors():
    assert_equal(Lexicon.scan("ASDFASDF"), [("error", "ASDFASDF")])
    result = Lexicon.scan("bear IAS princess")
    assert_equal(result, [('noun', "bear"), ("error", "IAS"), ("noun", "princess")])


def test_numbers():
    assert_equal(Lexicon.scan("1234"), [("number", 1234)])
    result = Lexicon.scan("3 9123400")
    assert_equal(result, [('number', 3), ("number", 9123400)])


