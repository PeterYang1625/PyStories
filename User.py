class User():
    userID = 0
    def __init__(self, name, directory="/", imageURL="/static/img/default_profile.jpg"):
        # Username
        self.__name = name
        # Directory of data stored
        self.__directory = directory
        # Profile picture URL
        self.__imageURL = imageURL
        # Stories List
        self.__storiesList = []
        # userID
        self.__userID = User.userID
        # Increment static UID by 1
        User.userID += 1

    def setName(self, name):
        self.__name = name
    def getName(self):
        return self.__name

    def setDirectory(self, dir):
        self.__directory = dir
    def getDirectory(self):
        return self.__directory

    def setImage(self, img):
        self.__imageURL = img
    def getImage(self):
        return self.__imageURL

    def addStory(self, Story):
        # Add to front of array so most recent one is presented
        self.__storiesList.insert(0, Story)
    def getStoryList(self):
        return self.__storiesList

    def getUID(self):
        return self.__userID

    def __str__(self):
        return \
            "\nName: " + self.__name \
            + "\nDirectory: " + self.__directory \
            + "\nImage URL: " + self.__imageURL