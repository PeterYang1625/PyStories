from flask import Flask, render_template, request

app = Flask(__name__)
@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        input_username = request.form.get("username")
        input_password = request.form.get("password")
        from UserList import UserList
        user = UserList.getUserByUsername(input_username)
        if user:
            # User is found, now check the password
            import hashlib
            # Password is stored as sha256 hash, no salt unfortunately :(
            input_password = hashlib.sha256(input_password)
            if input_password == user.getPassword():
                print("Successful login")
            else:
                # Password does not match
                print("Login failed. Please try again")
        else:
            # User is not found, login is failed
            print("Username not found")
    else:
        pass

@app.route("/")
def index():
    # Due to lack of a database this will suffice as our "database call"
    from UserList import UserList
    users = UserList.users
    return render_template("menu_components.html", users=users)

@app.route("/feed", methods=["GET", "POST"])
def userFeed():
    # Post UID of the feed we want to view
    if request.method == "POST":
        userID = int(request.form.get("uid"))
        # Yes this is our stand in for not having SQL
        from UserList import UserList
        # Get the appropriate UserByID and then get that storyList
        targetUser = UserList.getUserByID(userID)
        storyList = []
        if not targetUser:
            print(userID)
            print("Debug: POSTed user id does not exist")
        else:
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
        # data would yield nothing, so print a 404 page
        return render_template("404.html")

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

if __name__ == "__main__":
    app.run()

index()