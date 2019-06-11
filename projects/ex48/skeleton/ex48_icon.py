
direction_words = ("north", "south", "west", "east", "down", "up", "left", "right", "back")
verbs = ("go", "stop", "kill", "eat")
stop_words = ("the", "in", "of", "from", "at", "it")
nouns = ("door", "bear", "princess", "cabinet")
#numbers = (1, 2, 3, 4, 5, 6, 7, 8, 9, 1234)



class Lexicon(object):


    @staticmethod
    def scan(user_input):
        convert = True
        result = []
        global direction_words
        global verbs
        global stop_words
        global nouns
        #global numbers

        for i in user_input.split():
            if i in direction_words:
                result.append(("direction", i))
            elif i in verbs:
                result.append(("verb", i))
            elif i in stop_words:
                result.append(("stop", i))
            elif i in nouns:
                result.append(("noun", i))
            else:
                try:
                    int(i)
                    result.append(("number", int(i)))
                except ValueError:
                    result.append(("error", i))
        return result
