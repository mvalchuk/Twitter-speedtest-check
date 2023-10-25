class User:
   def __init__(self, user_id, username):
       self.id = user_id
       self.username = username
       self.followers = 0
       self.following = 0

   def follow(self, user):
       user.followers += 1
       self.following += 1

user1 = User('001', "Max")
user2 = User('002', 'Vika')
user1.follow(user2)
print(user1.followers)
print(user1.following)
print(user2.followers)
print(user2.following)

class Question:
    def __init__(self, q_text, q_answer):
        self.text= q_text
        self.answer = q_answer

