import hashlib
import re

login_possible = False

def validate_username(username):
    # 아이디는 영어와 숫자로만 구성되고, 띄어쓰기는 불가능, 길이는 4~20
        pattern = "^[a-zA-Z0-9]{4,20}$"
        if re.match(pattern, username):
            return True
        else:
            return False
        
def validate_password(password):
    # 비밀번호는 최소 8자 이상이어야 하며, 영어와 숫자로만 구성되어야 합니다.
    return len(password) >= 8 and password.isalnum()

def hash_password(password):
    # 비밀번호를 해싱하여 반환
    return hashlib.sha256(password.encode()).hexdigest()

def verify_password(password, hashed_password):
    # 입력된 비밀번호와 해시화된 비밀번호를 비교
    return hashlib.sha256(password.encode()).hexdigest() == hashed_password