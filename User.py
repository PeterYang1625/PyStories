import hashlib
from Story import Story
import os

class User():
    userID = 0
    def __init__(self, name, password, directory="/", imageURL="/static/img/default_profile.jpg"):
        # Username
        self.__name = name
        # Directory of data stored
        self.__directory = directory
        # Profile picture URL
        self.__imageURL = imageURL

        storiesList = []
        # Get the directory of this current User.py script
        currPath = os.path.dirname(__file__)
        relativePath = "userdata" + directory
        fullPath = os.path.join(currPath, relativePath)
        filesList = os.listdir(fullPath)
        for file in filesList:
            projectPath = os.path.join(fullPath, file)
            storiesList.append(Story(projectPath, file.split(".")[0]))
        # Stories List
        self.__storiesList = storiesList

        # userID
        self.__userID = User.userID
        # Increment static UID by 1
        User.userID += 1
        password = password.encode("utf-8")
        hashed_password = hashlib.sha256(password)
        self.__password = hashed_password

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

    def setPassword(self, password):
        hashed_password = hashlib.sha256(password)
        self.__password = hashed_password
    def getPassword(self):
        return self.__password

    def __str__(self):
        return \
            "\nName: " + self.__name \
            + "\nDirectory: " + self.__directory \
            + "\nImage URL: " + self.__imageURL