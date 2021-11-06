
import random

class MorningMsg:
        
    def msg():
        with open('text_example.txt') as msgs:
            line = msgs.readlines()

        numb = random.randint(0,len(line)-1)
        
        #print(line[numb].strip('\n'))
        return line[numb].strip('\n')

#MorningMsg.msg()

