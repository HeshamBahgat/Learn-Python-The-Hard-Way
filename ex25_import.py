import os
os.chdir(r"/root/PycharmProjects/Python_Study/Learn Python The Hard Way")
import ex25


sentence = "All good things come to those who wait"


words = ex25.break_words(sentence)
print(words)

sorted_words = ex25.sort_words(words)
print(sorted_words)

ex25.print_first_word(words)
ex25.print_last_word(words)
