import chap10_hangman
import chap10_randomname

count = 3
anser = chap10_randomname.random_string(count)
chap10_hangman.hangman(anser)
