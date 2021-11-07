
import random


'''
IDEA:
    initalize
        pass the file name as a constructor

    object creates a list and pop vriables from as we go
'''

class MorningMsg:

    biglist = []

    def __init__(self,filename) -> None:
        self.filename = filename
        self.listgen()
        
    def msg(self):
        
        listofmsgs = self.biglist

        if len(listofmsgs) == 0:
            self.listgen()

        listofmsgs = self.biglist

        numb = random.randint(0,len(listofmsgs)-1)
        msg = listofmsgs[numb].strip('\n')
        listofmsgs.pop(numb)

        return msg

    def listgen(self):
        with open(self.filename) as msgs:
            listofmsgs = msgs.readlines()

        self.biglist = listofmsgs

        return listofmsgs