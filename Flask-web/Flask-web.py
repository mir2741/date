from flask import Flask,url_for,render_template,request

app = Flask(__name__)

@app.route('/')
def hello_world():
    return render_template('index.html')

from login import user_login
app.add_url_rule('/login',view_func=user_login)

####物理机信息录入
from abm_sql import mysql_select
@app.route('/server/wh')
def server_w():
    param = (".*",)
    sql_query = "select ge_id,ge_name from abm.geography where ge_name regexp %s;"
    f = mysql_select(sql_query, param)
    return render_template('serverw.html',gname=f)

from the_server import server_wo
app.add_url_rule('/server/wo',view_func=server_wo)
####物理机信息查询
@app.route('/server/rh')
def server_r():
    return render_template('serverr.html')

from the_server import server_ro
app.add_url_rule('/server/ro',view_func=server_ro)

####物理机信息修改
from the_server import server_updata
app.add_url_rule('/server/uo',view_func=server_updata)


####deploy
#@app.route('/server/deploy')
#def deploy_r():
#    return render_template('appr.html')

#/newserver/newdeploy  初始化
from NewServer import newserver_html
app.add_url_rule("/newserver/newdeploy",view_func=newserver_html)

#/newserver/newdeploy  初始化服务器

#/newserver/newzabbix 安装zabbix

# /newserver/newmiddleware 进入部署容器页面

####硬件信  息录入

####应用信  息录入
@app.route('/apps/wh')
def apps_h():
    return render_template('appw.html')
from apps import apps_w
app.add_url_rule("/apps/appsw",view_func=apps_w)

@app.route('/apps/rh')
def apps_hr():
    return render_template('appr2.html')
from apps import apps_r
app.add_url_rule("/apps/appsr",view_func=apps_r)
from apps import apps_rw
app.add_url_rule("/apps/appsrw",view_func=apps_rw)

####机房信  息录入
@app.route("/server/gh")
def g_r():
    param = (".*",)
    sql_query = "select ge_id,ge_name,ge_addr from abm.geography where ge_name regexp %s;"
    f = mysql_select(sql_query, param)
    return render_template('gh.html',gname=f)

from geography import geography_w
app.add_url_rule("/server/gw",view_func=geography_w)
####机房信息 查询
from geography import geography_r
app.add_url_rule("/server/grh",view_func=geography_r)

if __name__ == '__main__':
    #app.run(debug = True)
    app.run(host='127.0.0.1',port=5000,debug = True)




