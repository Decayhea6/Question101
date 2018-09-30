#Question 101 by Denis K.
import pickle
import sys
print('welcome to question 101 raw text converter')
print()
while True:
    path = input('path to question pack raw text file:  (type quit to quit) ')
    print()
    if path == 'quit':
        sys.exit()
    try:
        qp = open(path).read()
        print('Seems ligit...')
        print()
        break
    except:
        print('Cannot open file. Seems to have been corrupted or not text.')
        print()
lineslist = qp.splitlines()
finallist = []
#the final output file will be a list of lists where the first item is the question and the proceding items are the answers.
for line in lineslist:
    if line != '':
        
        if line[0] == '@':
            print()
            print('#######')
            print(line)
            print('#######')
            print()
        elif line[0] != '#':
            question = line.split('|')
            print('Converted Item: '+str(question))
            finallist.append(question)
            print()
print('exporting data values: '+str(finallist))
print()

while True: 
    filename = input('Save File As?: ')
    filename = [w.replace(' ', '_') for w in filename]
    #FIle is saved under the extension IOI, or ioi 
    filename +=  '.ioi'
    filename = ''.join(filename)
    print()
    print('Your file wil be saved as:', str(filename))
    reasure = input('Continue? (y/n/quit)')
    if reasure == 'y':
        break
    elif reasure == 'quit':
        sys.exit()
    else:
        print('Restart')
print()
pickle.dump(finallist , open( filename, "wb" ) )
print("FINISHED")
