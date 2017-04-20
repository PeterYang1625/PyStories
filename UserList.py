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

    @staticmethod
    def add(User):
        UserList.users.append(User)

    @staticmethod
    def get(index):
        return UserList.users[index]

    @staticmethod
    def getUserByID(index):
        for User in UserList.users:
            if User.getUID() == index:
                return User
        # Return false on user not found
        else:
            return False

    @staticmethod
    def getUserByUsername(username):
        for User in UserList.users:
            # Must be case sensitive
            if User.getName() == username:
                return User
            # Return false on user not found
            else:
                return False