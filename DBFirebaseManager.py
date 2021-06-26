#pip install requests

#pip install python-firebase
from firebase import firebase

class DBFirebaseManager:
    def __init__(self):
        self.isConected = False
        self.urlDb = 'https://vipcell-bot-default-rtdb.europe-west1.firebasedatabase.app/'
        self.firebase = firebase.FirebaseApplication(self.urlDb, None)
        self.dBName = 'credbot'
    

    def getCredByModel(self, model):
        result = self.firebase.get(self.dBName, model)
        return result
    
    def update(self, id, val):
        self.firebase.put(self.dBName,id,val)
        
        



        

