#The Main Program For Using .ioi files a.k.a. the Question101 client
import pickle
import sys
import time
print('Question 101, Developed by Denis K.')
while True:

    while True:
        try:
            directory = input('Trivia File Directory: (or quit to quit)')
            if directory == 'quit':
                print('quitting')
                quit()
                break
            QuestionList = pickle.load( open( directory, "rb" ) )
            break
        except:
            print()
            print('Are you sure this is the correct file? Unable to open.')
            print()
    questionnum = 0
    print()
    print('Ready...')
    time.sleep(1)
    print('Set...')
    time.sleep(1)
    print('Go...')
    time.sleep(1)
    score = 0
    for QandA in QuestionList:
        questionnum += 1
        print()
        print('Question', str(questionnum))
        print()
        time.sleep(2)
        answer = input(QandA[0] + ' ')
        answer = answer.lower()
        if answer != QandA[0]:
            if answer in QandA:
                print('correct')
                score += 1
            else:
                print('wrong')
        else:
            print('nice try, but you got it wrong')
    print()
    print('Finished')
    print()
    print('You scored', str(score) + '/' + str(questionnum))
    print()
