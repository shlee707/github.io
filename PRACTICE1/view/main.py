from flask import Blueprint, flash, jsonify, make_response, redirect, render_template, request,session
from model.mysql import MYSQL_CONN
from control.user_mgmt import USER
from control import login_mgmt

main_bp = Blueprint('main',__name__,url_prefix='/main')

@main_bp.route('/index', methods = ['GET','POST'])
def index():
    if request.method == 'POST':
        id = request.form['myid']
        password = request.form['mypw']
        
        if not login_mgmt.login_possible:
            alarm = '사용 불가능한 아이디입니다.'
            return render_template('sign_in.html',input_id = request.form['myid'],available_id = False, statement = alarm)
        if not login_mgmt.validate_username(id):
            alarm = '아이디는 영어와 숫자로만 구성되고, 띄어쓰기는 불가능하며 길이는 4에서 20 사이여야 합니다.'
            return render_template('sign_in.html',input_id = request.form['myid'],available_id = False, statement = alarm)
        if not login_mgmt.validate_password(password):
            print('비밀번호는 최소 8자 이상이어야 하며, 영어와 숫자로만 구성되어야 합니다')
            alarm = '비밀번호는 최소 8자 이상이어야 하며, 영어와 숫자로만 구성되어야 합니다.'
            return render_template('sign_in.html',input_id = request.form['myid'],available_id = False, statement = alarm)
        else:
            hashed_pw = login_mgmt.hash_password(password)
            print(len(hashed_pw))
            print(hashed_pw)
            USER.create(id,hashed_pw)
            return render_template('index.html')
    else:
        if 'userid' in session:            
            return render_template('index.html',login_complete = True)
        return render_template('index.html')
    

@main_bp.route('/check_id', methods = ['POST'])
def check_id():
    if not login_mgmt.validate_username(request.form['myid']):
        login_mgmt.login_possible = False
        alarm = '사용 불가능한 아이디입니다.'
        return render_template('sign_in.html',input_id = request.form['myid'],available_id = False, statement = alarm)
    elif USER.find(request.form['myid']) != None:
        login_mgmt.login_possible = False
        alarm = '이미 사용중인 아이디입니다.'
        return render_template('sign_in.html',input_id = request.form['myid'], user = USER.find(request.form['myid']), statement = alarm)
    else:
        login_mgmt.login_possible = True
        alarm = '사용 가능한 아이디입니다.'
        return render_template('sign_in.html',input_id = request.form['myid'], user = USER.find(request.form['myid']), statement = alarm)

@main_bp.route('/sign_in', methods = ['POST'])
def sign_in(id = None):
    return render_template('sign_in.html', available_id = True)

@main_bp.route('/login', methods = ['POST'])
def login():
    id = request.form['myid']
    password = request.form['mypw']
    if USER.find(id) != None:
        if login_mgmt.verify_password(password,USER.find(id).user_pw):
            if 'userid' not in session:
                session['userid'] = id
            return render_template('index.html', login_complete = True)
    return render_template('index.html')

@main_bp.route('/logout')
def logout():
    session.pop('userid', None)
    flash('로그아웃 되었습니다.', 'success')
    return render_template('index.html')
    
@main_bp.route('/mypage')
def mypage():
    if 'userid' in session:
        id = session['userid']
        return render_template('mypage.html', userid = id)
    return render_template('index.html')

@main_bp.before_request
def before_request():
    if request.endpoint == 'main.mypage' and 'userid' not in session:
        flash('로그인이 필요합니다.', 'error')
