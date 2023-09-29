from function import *

app = Flask(__name__)

jwt = JWTManager(app)
app.config["JWT_SECRET_KEY"] = "jeeva143"
app.config["JWT_ACCESS_TOKEN_EXPIRES"] = datetime.timedelta(days=1)

@app.route("/register",methods=["POST"])
def register():
    user_data = request.json
    return pass_data(user_data,"register")

@app.route("/login",methods=["GET"])
def login():
    user_data = request.json
    if pass_data(user_data,"login") == "yes":
        token = create_access_token(request.json["email"])
        return token
    elif pass_data(user_data,"login") == "wrong":
        return "You have no account"
    elif pass_data(user_data,"login") == "no":
        return "incorrect credentials"

@app.route("/movie",methods=["POST"])
def likes():
    user_data = request.json
    return pass_data(user_data,"movie")

@app.route("/likes",methods=["POST"])
def movie():
    user_data = request.json
    return pass_data(user_data,"likes")

def pass_data(get_userdata,type):
    obj = movie_management("movies_management", get_userdata)
    obj.mongodb()
    obj.collections()
    if type == "register":
        return obj.register()
    elif type == "login":
        return obj.login()
    elif type == "likes":
        return obj.likes()
    elif type == "movie":
        return obj.movies()

app.run(debug=True)