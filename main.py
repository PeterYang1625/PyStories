from flask import Flask, render_template, request, redirect, url_for

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
        # Call from UserList "database"
        from UserList import UserList
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
            # Else password does not match
        # Else, user is not found
        if success:
            return redirect(url_for("feed"))
        else:
            message = "Login failed. Please try again"
            return render_template("login.html", message=message)
    else:
        # Else method is GET - display login form
        return render_template("login.html")

@app.route("/feed")
def feed():
    # Due to lack of a database this will suffice as our "database call"
    from UserList import UserList
    users = UserList.users
    # Pass users to the render template which will iteratively render all of them
    return render_template("feed_components.html", users=users)

@app.route("/stories", methods=["GET", "POST"])
def stories():
    # Post UID of the feed we want to view
    if request.method == "POST":
        userID = int(request.form.get("uid"))
        # Yes this is our stand in for not having SQL
        from UserList import UserList
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
            username=targetUser.getName()
        )
    else:
        # Else this is a GET request. Under normal circumstances, coming to
        # feed should be from posting the UID in order to fetch and appropriate
        # stories feed; however directly navigating to this link without POST
        # data would yield nothing, so redirect to login page
        error = "This is a restricted page. Please login to continue."
        return render_template("login.html", message=error)

# Page not found error handling
@app.errorhandler(404)
def pageNotFound(e):
    return render_template("404.html"), 404

"""
@app.route("/peter")
def userPage():
    linesOfCode = []
    with open("userdata/peter/A3.py", "r") as file:
        for line in file:
            line = line.rstrip()
            linesOfCode.append(line)

    import subprocess, os
    # Checks if Windows Platform
    if os.name == "nt":
        subprocess.Popen("python userdata/peter/A3.py")
    # Otherwise on macOS / OSX
    else:
        subprocess.Popen("python3 userdata/peter/A3.py")
    return render_template("stories_components.html", code=linesOfCode)
"""

if __name__ == "__main__":
    app.run()