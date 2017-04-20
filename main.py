from flask import Flask, render_template, request

app = Flask(__name__)
@app.route("/")
def index():
    # Due to lack of a database this will suffice as our "database call"
    from UserList import UserList
    users = UserList.users
    return render_template("menu_components.html", users=users)

@app.route("/feed", methods=["GET", "POST"])
def userFeed():
    if request.method == "POST":
        linesOfCode = []
        with open("userdata/peter/A3.py", "r") as file:
            for line in file:
                line = line.rstrip()
                linesOfCode.append(line)
        return render_template("stories_components.html", code=linesOfCode)
    else:
        pass

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