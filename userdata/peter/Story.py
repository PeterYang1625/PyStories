class Story():
    def __init__(self, codeLink, caption=""):
        linesOfCode = []
        with open(codeLink, "r") as file:
            for line in file:
                line = line.rstrip()
                linesOfCode.append(line)
        self.__directory = codeLink
        self.__codeList = linesOfCode
        self.__caption = caption

    def getDirectory(self):
        return self.__directory

    def getCodeList(self):
        return self.__codeList

    def getCaption(self):
        return self.__caption