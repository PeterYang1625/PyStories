from User import User

class UserList():
    users = [
        User("Peter Yang", "password", "/peter/"),
        User("Kevin Tran", "password", "/peter/"),
        User("Brandon Nguyen", "password", "/peter/"),
        User("Jesus Christ", "password", "/peter/"),
        User("Jason Bourne", "password", "/peter/"),
        User("John Doe", "password", "/peter/")
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