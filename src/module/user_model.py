import json
import hashlib
import os
from datetime import datetime, timedelta

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
    
    def create_admin(self, id, pw):
        if self.does_exists(id):
            raise Exception('이미 존재하는 id 입니다. ')
        created = User(id, pw)
        created.is_admin = True
        self.users[id] = created.to_dict()
        self.save_users()
        return True
        
    def get(self, id):
        if self.does_exists(id):
            return {"id": id, "password": self.users[id]["password"], "last login": self.users[id]["last login"], 
                    "attendance": self.users[id]["attendance"], "test score easy": self.users[id]["test score easy"], "test score normal": self.users[id]["test score normal"], "test score hard": self.users[id]["test score hard"], 
                    "time attack score": self.users[id]["time attack score"], "perfect streak score": self.users[id]["perfect streak score"],
                    "is admin": self.users[id]["is admin"]}
        raise Exception('존재하지 않는 id 입니다. ')
    
    def update(self, id, new_password=None):
        if new_password is not None:
            self.set_password(id, new_password)
        self.users[id]["last login"] = TIME_NOW
        self.save_users()
        return True
    
    def set_password(self, id, new_password):
        if self.does_exists(id):
            self.users[id]["password"] = User.hash_password(new_password)
        raise Exception('존재하지 않는 id 입니다. ')
    
    def update_attendance(self, id):
        if datetime.now().date() == (datetime.strptime(self.users[id]["last login"], 
                                                       '%Y-%m-%d %H:%M:%S').date() + timedelta(days=1)):
            self.users[id]["attendance"] += 1
        else:
            self.users[id]["attendance"] = 1
            
    def update_test_score(self, id, level, score):
        if level == 'easy':
            self.users[id]["test score easy"] = score
            self.save_users()
            return True
        elif level == 'normal':
            self.users[id]["test score normal"] = score
            self.save_users()
            return True
        elif level == 'hard':
            self.users[id]["test score hard"] = score
            self.save_users()
            return True
    
    def update_time_attack_score(self, id, score):
        self.users[id]["time attack score"] = score
        self.save_users()
        return True
    
    def update_perfect_streak_score(self, id, score):
        self.users[id]["perfect streak score"] = score
        self.save_users()
        return True

class User:
    def __init__(self, id, password, last_login=None): 
        self.id = id
        self.password = self.hash_password(password)
        self.last_login = "" if last_login is None else last_login
        self.attendance = 0
        self.test_score_easy = 0
        self.test_score_normal = 0
        self.test_score_hard = 0
        self.time_attack_score = 0
        self.perfect_streak_score = 0
        self.is_admin = False
        
    @staticmethod
    def hash_password(password):
        return hashlib.sha256(password.encode()).hexdigest()

    def check_password(self, password):
        hash = hashlib.sha256(password.encode('utf-8')).hexdigest()
        return self.password == hash
    
    def to_dict(self):
        return {"password": self.password, "last login": self.last_login, "attendance": self.attendance, "test score easy": self.test_score_easy, "test score normal": self.test_score_normal, "test score hard": self.test_score_hard, 
                "time attack score": self.time_attack_score, "perfect streak score": self.perfect_streak_score, "is admin": self.is_admin}
    
    def serializing(self):
        return {self.id: {"password": self.password, "last login": self.last_login, "attendance": self.attendance, "test score easy": self.test_score_easy, "test score normal": self.test_score_normal, "test score hard": self.test_score_hard, 
                "time attack score": self.time_attack_score, "perfect streak score": self.perfect_streak_score, "is admin": self.is_admin}}
    
    manager = UserManager()
    
if __name__ == '__main__':
    user_manager = UserManager()
    user_manager.create_admin('admin', '1234')
    user_manager.save_users()