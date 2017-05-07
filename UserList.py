from User import User

class UserList():
    users = [
        User("Peter Yang", "password", "/peter/", "/static/img/peter.jpg"),
        User("Trina Gregory", "password", "/trina/", "/static/img/trina.jpg"),
        User("Rob Parke", "password", "/rob/", "/static/img/rob.jpg"),
        User("John Doe", "password", "/john/")
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