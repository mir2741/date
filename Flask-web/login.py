from flask import Flask,url_for,render_template,request,flash
from abm_sql import login_sql

def user_login():
    try:
        uaername = request.args.get('username')
        uaerpass = request.args.get('password')
        a = login_sql(uaername,uaerpass)
        return render_template('login.html', userNumber=a[0],uaername=a[1], uaerstate=a[2])
    except TypeError :
        return render_template('index.html', error="用户密码错误,账号不存在")
