from flask import Flask, render_template, request, redirect, url_for, session
from Story import Story
from UserList import UserList
import os

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        # Grab POST data from submitted form
        input_username = request.form.get("username")
        input_password = request.form.get("password")
        # Grab the intended user as indicated by the form POST
        user = UserList.getUserByUsername(input_username)
        # Default success to false, only set to true after verification below
        success = False
        if user:
            # User is found, now check the password
            import hashlib
            # Password is stored as sha256 hash, no salt unfortunately :(
            input_password = hashlib.sha256(input_password.encode("utf-8"))
            # Convert binary data to hex readable stuff
            input_password = input_password.hexdigest()
            database_password = user.getPassword().hexdigest()
            if input_password == database_password:
                success = True
                # Save UID to a session variable
                session["uid"] = user.getUID()
            # Else password does not match
            message = "Password does not match"
        # Else, user is not found
        message = "User not found"
        if success:
            return redirect(url_for("feed"))
        else:
            # message = "Login failed. Please try again"
            return render_template("login.html", message=message)
    else:
        # Else method is GET - display login form
        return render_template("login.html")

@app.route("/feed")
def feed():
    message = request.args.get("message")
    users = UserList.users
    # Pass users to the render template which will iteratively render all of them
    return render_template("feed_components.html", users=users, message=message)

def isValidFileType(filename):
    ALLOWED_EXTENSIONS = ("py")
    return "." in filename and filename.split(".", 1)[1] in ALLOWED_EXTENSIONS

@app.route("/upload", methods=["GET", "POST"])
def upload():
    if request.method == "POST":
        # Grab POST data from submitted form
        input_title = request.form.get("title")
        input_file = request.files["file"]
        # Get specific user based on uid stored in session
        user = UserList.getUserByID(session["uid"])

        # Handle file upload
        isValidFile = True
        message = "Upload successful"
        filename = input_file.filename
        # Checks for valid file name / format
        if not isValidFileType(filename):
            isValidFile = False
            message = "Invalid file type"
        if isValidFile:
            # Get the directory of this current User.py script
            currPath = os.path.dirname(__file__)
            relativePath = "/userdata" + user.getDirectory()
            projectPath = currPath + relativePath + filename
            input_file.save(projectPath)
        else:
            # If invalid, return now, providing an error message
            return redirect(url_for("feed", message=message))

        # Otherwise, continue to make a new story
        newStory = Story(projectPath, input_title)
        user.addStory(newStory)
        return redirect(url_for("feed", message=message))
    else:
        # Else method is GET - display login form
        return render_template("login.html", message="Must be logged in to upload.")

@app.route("/stories", methods=["GET", "POST"])
def stories():
    # Post UID of the feed we want to view
    if request.method == "POST":
        userID = int(request.form.get("uid"))
        # Get the appropriate UserByID and then get that storyList
        targetUser = UserList.getUserByID(userID)
        if not targetUser:
            # User is not found in the list, despite being the UID being
            # the post data, which actually should not happen
            error = "User Authentication error. Please login again."
            return render_template("login.html", message=error)
        else:
            # Set storyList to the specified user's list and push
            # this data to the render_template
            storyList = targetUser.getStoryList()

        return render_template(
            "stories_components.html",
            storyList=storyList,
            username=targetUser.getName(),
            uid=userID
        )
    else:
        # Else this is a GET request. Under normal circumstances, coming to
        # feed should be from posting the UID in order to fetch and appropriate
        # stories feed; however directly navigating to this link without POST
        # data would yield nothing, so redirect to login page
        error = "This is a restricted page. Please login to continue."
        return render_template("login.html", message=error)

@app.route("/runcode", methods=["GET", "POST"])
def runCode():
    if request.method == "POST":
        POST_userID = int(request.form.get("user"))
        POST_index = int(request.form.get("ind"))

        user = UserList.getUserByID(POST_userID)
        # Gets absolute path of user data directory
        currPath = os.path.dirname(__file__)
        relativePath = "userdata" + user.getDirectory()
        fullPath = os.path.join(currPath, relativePath)

        # Uses this absolute path to list all files in this directory
        filesList = os.listdir(fullPath)

        # POST_index was passed from ajax call
        # Grab that specific file
        fileDirectory = filesList[POST_index]
        filePath = os.path.join(relativePath, fileDirectory)

        # Run it as a subprocess terminal command
        import subprocess
        command = ["python", filePath]
        subprocess.Popen(command)

        return "Success"

    # Should only be a POST
    else:
        error = "This is a restricted page. Please login to continue."
        return redirect(url_for("login", message=error))

# Page not found error handling
@app.errorhandler(404)
def pageNotFound(e):
    return render_template("404.html"), 404

# Key is necessary to store session variables
app.secret_key = "ITP115"

# Runs the application
if __name__ == "__main__":
    app.run()