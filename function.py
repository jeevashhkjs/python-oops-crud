from flask import Flask,request,jsonify
from pymongo import MongoClient
from flask_jwt_extended import create_access_token
from flask_jwt_extended import JWTManager, jwt_required, get_jwt_identity
import hashlib,json,datetime

class db_config:
    def __init__(self,dbname):
        self.dbname = dbname

    def mongodb(self):
        mongo_client = MongoClient("mongodb://127.0.0.1:27017")
        self.database = mongo_client[self.dbname]

    def collections(self):
        self.users_collection = self.database.users
        self.movies_collection = self.database.movies
        self.likes_collection = self.database.likes

class login_signup(db_config):
    def __init__(self,db_name,user_data):
        super().__init__(db_name)
        self.user_data = user_data

    def register(self):
        checking_user = self.users_collection.find_one({"email":self.user_data["email"]})
        if not checking_user:
            self.user_data["password"] = hashlib.sha256(user_data["password"].encode("utf-8")).hexdigest()
            self.users_collection.insert_one(self.user_data)
            return "users registered successfully"
        return "you have already registered"

    def login(self):
        checking_user = self.users_collection.find_one({"email":self.user_data["email"]})
        if checking_user:
            if hashlib.sha256(self.user_data["password"].encode("utf-8")).hexdigest() == checking_user["password"]:
                return "yes"
            return "wrong"
        else:
            return "no"

class movie_management(login_signup):
    def __init__(self,db_name, datum):
        super().__init__(db_name, datum)
        self.datum = datum

    def movies(self):
        self.movies_collection.insert_one(self.user_data)
        return "jasm"

    def likes(self):
        self.likes_collection.insert_one(self.datum)
        return "successfully like"

    def show_movies(self):
        return json.dumps(self.movies_collection.find({},{"_id":0}))
    def show_movies_single(self,id):
        return json.dumps(self.movies_collection.find_many({"user_id":id},{"_id":0}))

    def show_likes_single(self,id):
        return json.dumps(self.likes_collection.find_many({"user_id":id},{"_id":0}))

    def show_likes(self):
        return json.dumps(self.likes_collection.find({},{"_id":0}))





# obj = login_signup("movies_management","jeeva")
# obj.mongodb()
# obj.collections()
# print(obj.register())
