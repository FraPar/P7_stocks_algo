class General(object):
     def __init__(self,whatever):
         self.field1 = 0
         self.field2 = whatever

     #Imported methods
     #from .controller import *
     #from .model  import *
     #from .views import *

     #Some more small functions
     def printHi(self):
         print("Hello world")

     #static methods need to be set
     #somthing = staticmethod(something)

     # to access :
     # General().load()
     # General().plot