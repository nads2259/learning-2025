class UserStatus:
    
    def __init__(self):
        self.status = "OFFLINE"
        self.friends = []
        
    def addFriends(self,friend):
        self.friends.append(friend)
        
    def changeStatus(self,status):
        self.status = status
        self.notify()
        
    def notify(self):
        
        for friend in self.friends:
            friend.update(self.status)
        
        
class Friend:
    
    def __init__(self,name):
        self.name = name
        
    def update(self,status):
        print(f"{self.name} saw that you are {status}")
        
        
usr_status = UserStatus()

usr_status.addFriends(Friend("Rick"))
usr_status.addFriends(Friend("Tom"))

usr_status.changeStatus("ONLINE")
usr_status.changeStatus("OFFLINE")