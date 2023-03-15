import random

#exo A

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


"""scoob = PlayerKarao("Scooby",random.randint(50,100),random.randint(50,100),random.randint(50,100),random.randint(50,100),random.randint(50,100))"""

scoob = PlayerKarao("Scooby",0,0,0,0,0)

"""scoob = (PlayerKarao("Scooby",0,0,0,0,0))"""
"""samy = PlayerKarao("Samy",0,0,0,0,0)
fred = PlayerKarao("Fred",0,0,0,0,0)
vera= PlayerKarao("Véra",0,0,0,0,0)"""

"""print(PlayerKarao)"""



#exo B
class PlayerKarao:
    def __inti__ (self,name,score1,score2,score3,score4,score5,moyenscore):
        self.pseudo=name #p pour player
        self.pscoresing1=score1
        self.pscoresing2=score2
        self.pscoresing3=score3
        self.pscoresing4=score4
        self.pscoresing5=score5
        self.moyenscoresing=moyenscore 



                                    #recup des infos PlayerKarao
    def getpseudo(self):
        return self.pseudo

    def getscore1(self):
        return self.pscoresing1

    def getscore2(self):
        return self.pscoresing2

    def getscore3(self):
        return self.pscoresing3

    def getscore4(self):
        return self.pscoresing4

    def getscore5(self):
        return self.pscoresing5

    def getmoyen(self):
        return self.moyenscoresing

class Titresing:
    def scoobydoobydoo(self,letitre1,scoresing1):
        self.bydoo=letitre1
        self.scorebydoo=scoresing1

    def foutacagoule(self,letitre2,scoresing2):
        self.cagoule=letitre2
        self.cagoulescore=scoresing2

    def hakunamatata(self,letitre3,scoresing3):
        self.matata=letitre3
        self.matata=scoresing3


    def vaderetro(self,letitre4,scoresing4):
        self.vade=letitre4
        self.vade=scoresing4

    def satanas(self,letitre5,scoresing5):
        self.matata=letitre5
        self.matata=scoresing5

    def gettitre1(self):
        return self.matata
