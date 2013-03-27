import os.path
import sys
sys.path.append( "PickleMonger" )
from PickleMonger.PickleMonger import PickleMonger
from Model import Model

def dbSetup():
   	PM = PickleMonger('bayesDict.dat')
   	PM.create('ham')
   	PM.create('spam')
   	ham = Model('ham',{"the":1})
   	spam = Model('spam',{"the":1})
   	PM.updateObject(ham)
   	PM.updateObject(spam)

if __name__ == "__main__":
	dbSetup()