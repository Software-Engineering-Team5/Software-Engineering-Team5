import json
import bcrypt
import hashlib
import os
from datetime import datetime, timezone

DB_PATH = 'data/users/users.json'
TIME_NOW = datetime.now().strftime('%Y-%m-%d %H:%M:%S') # User.last_login의 포맷

class UserManager:
    def __init__(self, db=DB_PATH):
        self.db = DB_PATH
        self.users = self.load_users()
        
    def load_users(self): # User DB 로드
        if os.path.exists(self.db):
            with open(DB_PATH, "r") as f:
                return json.load(f)
        return {}
        
    def save_users(self):
        with open(DB_PATH, 'w') as f:
            json.dump(self.users, f, indent=4)
    
    def does_exists(self, id):
        if id in self.users:
            return True
        return False
    
    def create(self, id, pw):
        if self.does_exists(id):
            raise Exception('이미 존재하는 id 입니다. ')
        created = User(id, pw)
        self.users[id] = created.to_dict()
        self.save_users()
        return True
        
    def get(self, id):
        if self.does_exists(id):
            return {"id": id, "password": self.users[id]["password"], "last login": self.users[id]["last login"]}
        raise Exception('존재하지 않는 id 입니다. ')
    
    def update(self, id, new_password=None):
        if new_password is not None:
            self.set_password(id, new_password)
        self.save_users()
        return True
    
    def set_password(self, id, new_password):
        if self.does_exists(id):
            self.users[id]["password"] = User.hash_password(new_password)
        raise Exception('존재하지 않는 id 입니다. ')
    
    def update_last_login(self, id):
        if self.does_exists(id):
            self.users[id]["last_login"] = TIME_NOW
        raise Exception('존재하지 않는 id 입니다. ')
    
class User:
    def __init__(self, id, password, last_login=None): 
        self.id = id
        self.password = self.hash_password(password)
        self.last_login = "" if last_login is None else last_login
        
    @staticmethod
    def hash_password(password):
        return hashlib.sha256(password.encode()).hexdigest()

    def check_password(self, password):
        hash = hashlib.sha256(password.encode('utf-8')).hexdigest()
        return self.password == hash
    
    def to_dict(self):
        return {"password": self.password, "last login": self.last_login}
    
    def serializing(self):
        return {self.id: {"password": self.password, "last login": self.last_login}}
    
    def __repr__(self):
        return f"<User(id='{self.id}', password='{self.password}', last_login='{self.last_login}')>"
    
    manager = UserManager()
    
if __name__ == '__main__':
    print('123' in {})