# class User:
#     def __init__(self, id, username) -> None:
#         self.id = id
#         self.username = username
#         self.followers = 0
#         self.following = 0
#     def follow(self, user):
#         user.followers += 1
#         self.following += 1
#     pass
# user1 = User("001", "Ian")
# user2 = User("002", "Kamau")

# user1.follow(user2)
# user2.follow(user1)

# print(user1.id, user1.username, user1.followers, user1.following)