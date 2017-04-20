from User import User

class UserList():
    users = [
        User("Peter Yang", "/peter"),
        User("Kevin Tran"),
        User("Brandon Nguyen"),
        User("Jesus Christ"),
        User("Jason Bourne"),
        User("John Doe")
    ]

    def add(self, User):
        self.users.append(User)

    def get(self, index):
        return self.users[index]

    # If users are added or deleted, their UIDs
    # may not align with the users arr index
    def getUserByID(self, index):
        for User in self.users:
            if User.getUID() == index:
                return User
        # Return false on user not found
        else:
            return False