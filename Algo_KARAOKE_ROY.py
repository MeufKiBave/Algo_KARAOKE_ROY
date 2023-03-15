import random

class PlayerKarao:
    def __inti__ (self,name,score1,score2,score3,score4,score5,moyenscore):
        self.__pseudo=name
        self.__pscoresing1=score1
        self.__pscoresing2=score2
        self.__pscoresing3=score3
        self.__pscoresing4=score4
        self.__pscoresing5=score5
        self.__moyenscoresing=moyenscore #1+2+3+4+5 diviser par 5

#score minim 50 to 100

                                    #recup des infos PlayerKarao
    def getpseudo(self):
        return self.__pseudo

    def getscore1(self):
        return self.__pscoresing1

    def getscore2(self):
        return self.__pscoresing2

    def getscore3(self):
        return self.__pscoresing3

    def getscore4(self):
        return self.__pscoresing4

    def getscore5(self):
        return self.__pscoresing5

    def getmoyen(self):
        return self.__moyenscoresing

    def sing(self,titre1,titre2,titre3,titre4,titre5):  #nom des chansons
        self.__1sing=titre1
        self.__2sing=titre2
        self.__3sing=titre3
        self.__4sing=titre4
        self.__5sing=titre5

  #score des chansons possible
    def singscore(self):
        self.__1sing= random.randint(50,100)
        self.__2sing= random.randint(50,100)
        self.__3sing= random.randint(50,100)
        self.__4sing= random.randint(50,100)
        self.__5sing= random.randint(50,100)






#test
"""scoob = ("Scooby",random.randint(50,100),random.randint(50,100),random.randint(50,100),random.randint(50,100),random.randint(50,100))
samy = ("Samy",random.randint(50,100),random.randint(50,100),random.randint(50,100),random.randint(50,100),random.randint(50,100))
fred = ("Fred",random.randint(50,100),random.randint(50,100),random.randint(50,100),random.randint(50,100),random.randint(50,100))
vera=("Véra",random.randint(50,100),random.randint(50,100),random.randint(50,100),random.randint(50,100),random.randint(50,100))"""


scoob = ("Scooby",singscore)
samy = ("Samy",)
fred = ("Fred",)
vera=("Véra",)