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
@jwt_required()
def movie():
    user_data = request.json
    user_data["user_id"] = get_jwt_identity()
    return pass_data(user_data,"movie")

@app.route("/likes",methods=["POST"])
@jwt_required()
def likes():
    user_data = request.json
    user_data["user_id"] = get_jwt_identity()
    return pass_data(user_data,"likes")

@app.route("/getmovies",methods=["GET"])
def allmovies():
    return pass_data(type="getallmovies")
@app.route("/getsinglemovie",methods=["GET"])
def getsinglemovie():
    return pass_data(type="getmovies", target_id = request.args.get('id'))

@app.route("/getlikessingle",methods=["GET"])
def getsinglelike():
    return pass_data(type="getlikes", target_id = request.args.get('id'))

@app.route("/getlikes",methods=["GET"])
def getlikes():
    return pass_data(type="getalllikes")

def pass_data(get_userdata = None,type = None, target_id = None):
    obj = movie_management("movies_management", get_userdata)
    obj.mongodb()
    obj.collections()
    if type == "register":
        return obj.register()
    elif type == "login":
        return obj.login()
    elif type == "likes":
        return obj.likes(target_id)
    elif type == "movie":
        return obj.movies(target_id)
    elif type == "getmovies":
        return obj.show_movies(target_id)

app.run(debug=True)