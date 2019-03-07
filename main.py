from kivy.app import App
import pickle
import webbrowser
import random
from kivy.uix.boxlayout import BoxLayout
import re

wordsDict = pickle.load( open( "wordsdatabase.qad", "rb" ) )
def alphasort(word):
    #global word
    letters = 0
    sorted_x = ''.join(sorted(word))
    return(sorted_x)
def unscramble(word):
    getkey = alphasort(word)
    answerlist = wordsDict[getkey]
    return(answerlist)
def define(word):
    webbrowser.open('http://www.dictionary.com/browse/' + word + '?s=t')
def scramble(word):
    word2 = ''.join(random.sample(word,len(word)))
    return(word2)
def isword(word):
    getkey = alphasort(word)
    answerlist = wordsDict[getkey]
    if word in answerlist:
        bollen = True
    else:
        bollen = False
    return(bollen)

class Unscrambler(BoxLayout):
    def get_words(self):
        search = '{}'.format(self.search_input.text)
        if not isword(search):
            search = re.sub(r" ", "", search)
        outputs = unscramble(search)
        if len(outputs) == 0:
            self.output.text = '''
       No matches found!!!
Check your spelling and try again
'''
        else:
            answer = "\n".join(outputs)
            self.output.text = answer
    def encode(self):
        search = '{}'.format(self.search_input.text)
        if not isword(search):
            search = re.sub(r" ", "", search)
        if isword(search):
            self.output.text = scramble(search)
        else:
            self.output.text = 'This is not a real word!!!'
    def definition(self):
        search = '{}'.format(self.search_input.text)
        if not isword(search):
            search = re.sub(r"  ", "", search)
        if isword(search):
            define(search)
            self.output.text = 'Defined: ' + search
        else:
            self.output.text = 'This is not a real word!!!'
            
            
class UnscrambleApp(App):

    pass

if __name__ == '__main__':
    UnscrambleApp().run()
