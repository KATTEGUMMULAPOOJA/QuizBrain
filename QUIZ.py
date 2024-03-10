class User:
    def __init__(self,id,username,followers):
        self.id=id
        self.username=username
        self.followers=0
        self.following=0
    def follow(self,user):
        user.followers+=1
        self.following+=1

User_1=User(1,"pooja",50)
print(User_1.id)
User_2=User(2,"teja",50)
print(User_2.id)
User_1.follow(User_2)
print(User_1.followers)
print(User_1.following)


