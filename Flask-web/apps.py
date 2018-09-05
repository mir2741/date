from flask import Flask,url_for,render_template,request,flash
from abm_sql import mysql_insert,mysql_select,mysql_updata
import time

def apps_w():
    try:
        param = {}
        param['app_name'] = request.args.get('appname')#应用名
        param['app_mod_name'] = request.args.get('appsname')#模块名
        param['app_loser_name'] = request.args.get('username')#负者人
        param['app_middleware'] = request.args.get('middleware')#中间件
        param['app_jdkn'] = request.args.get('jdkn')#java版本
        param['app_ojdbcn'] = request.args.get('ojdbcn')#ojdbc版本
        param['app_prd_domain'] = request.args.get('domain_name')#域名
        param['app_prd_ip'] = request.args.get('prd_ip')#生产环境IP
        param['app_prd_ojdbc'] = request.args.get('prd_ojdbc')#生产数据源
        param['app_dev_domain'] = request.args.get('dev_domain')#测试域名
        param['app_dev_ip'] = request.args.get('dev_ip')#测试环境IP
        param['app_dev_ojdbc'] = request.args.get('dev_ojdbc')#测试数据源
        t_date = time.strftime('%Y%m%d%H%M%S', time.localtime(time.time()))
        param['app_date'] = t_date  # 录入时间
        print (param)
        insert_sql = "insert into abm.application (app_name,app_mod_name,app_loser_name,app_middleware,app_jdkn,app_date,app_prd_domain,app_prd_ip,app_dev_domain,app_dev_ip,app_prd_ojdbcip,app_dev_ojdbcip,app_ojdbcn) values (%(app_name)s,%(app_mod_name)s,%(app_loser_name)s,%(app_middleware)s,%(app_jdkn)s,%(app_date)s,%(app_prd_domain)s,%(app_prd_ip)s,%(app_dev_domain)s,%(app_dev_ip)s,%(app_prd_ojdbc)s,%(app_dev_ojdbc)s,%(app_ojdbcn)s)"
        app = mysql_insert(sql_cmd=insert_sql,param=param)
        select_sql = "SELECT app_name,app_mod_name,app_loser_name,app_middleware,app_jdkn,app_ojdbcn,app_date,app_prd_domain,app_prd_ip,app_prd_ojdbcip,app_dev_domain,app_dev_ip,app_dev_ojdbcip FROM abm.application where app_name=%(app_name)s and app_mod_name=%(app_mod_name)s and app_name!=''"
        app_aelect = mysql_select(sql_query=select_sql,param=param)
        return render_template('appw.html',appslist=app_aelect,pyError=app)
        #return render_template('appw.html',appslist=app_aelect)
    except TypeError as e:
        return ("录入错误:"+e)

def apps_r():
    try:
        param ={}
        param['app_name'] = request.args.get('appname')#应用名
        if param['app_name'] == 'ALL':
            param['app_name'] = '.*'
        param['app_mod_name'] = request.args.get('appsname')#模块名
        if param['app_mod_name'] == 'ALL':
            param['app_mod_name'] = '.*'
        param['app_loser_name'] = request.args.get('username')#负者人
        if param['app_loser_name'] == 'ALL':
            param['app_loser_name'] = '.*'
        param['app_middleware'] = request.args.get('middleware')#中间件
        if param['app_middleware'] == 'ALL':
            param['app_middleware'] = '.*'
        param['app_jdkn'] = request.args.get('jdkn')#java版本
        if param['app_jdkn'] == 'ALL':
            param['app_jdkn'] = '.*'
        param['app_ojdbcn'] = request.args.get('ojdbcn')#ojdbc版本
        if param['app_ojdbcn'] == 'ALL':
            param['app_ojdbcn'] = '.*'

        select_sql = 'SELECT app_id,app_name,app_mod_name,app_loser_name,app_middleware,app_jdkn,app_ojdbcn,app_date,app_prd_domain,app_prd_ip,app_prd_ojdbcip,app_dev_domain,app_dev_ip,app_dev_ojdbcip FROM abm.application where app_name regexp %(app_name)s and app_mod_name regexp %(app_mod_name)s and app_loser_name regexp %(app_loser_name)s and app_middleware regexp %(app_middleware)s and app_jdkn regexp %(app_jdkn)s and app_ojdbcn regexp %(app_ojdbcn)s and app_name!="" '
        sql_data = mysql_select(sql_query=select_sql,param=param)
        print (sql_data)
        return render_template('appr.html', data=sql_data)
    except TabError as e:
        return ("错误："+e)

def apps_rw():
    try:
        param = {}
        param['app_name'] = request.args.get('appname')  # 应用名
        param['app_mod_name'] = request.args.get('appsname')  # 模块名
        param['app_loser_name'] = request.args.get('username')  # 负者人
        param['app_middleware'] = request.args.get('middleware')  # 中间件
        param['app_jdkn'] = request.args.get('jdkn')  # java版本
        param['app_ojdbcn'] = request.args.get('ojdbcn')  # ojdbc版本
        param['app_prd_domain'] = request.args.get('domain_name')  # 域名
        param['app_prd_ip'] = request.args.get('prd_ip')  # 生产环境IP
        param['app_prd_ojdbc'] = request.args.get('prd_ojdbc')  # 生产数据源
        param['app_dev_domain'] = request.args.get('dev_domain')  # 测试域名
        param['app_dev_ip'] = request.args.get('dev_ip')  # 测试环境IP
        param['app_dev_ojdbc'] = request.args.get('dev_ojdbc')  # 测试数据源
        #t_date = time.strftime('%Y%m%d%H%M%S', time.localtime(time.time()))
        #param['app_date'] = t_date  # 录入时间
        param['app_id'] = request.args.get('app_id')
        uodata_sql = """ update abm.application set app_name=%(app_name)s,app_mod_name=%(app_mod_name)s,app_loser_name=%(app_loser_name)s,app_middleware=%(app_middleware)s,app_jdkn=%(app_jdkn)s,app_prd_domain=%(app_prd_domain)s,app_prd_ip=%(app_prd_ip)s,app_dev_domain=%(app_dev_domain)s,app_dev_ip=%(app_dev_ip)s,app_prd_ojdbcip=%(app_prd_ojdbc)s,app_dev_ojdbcip=%(app_dev_ojdbc)s,app_ojdbcn=%(app_ojdbcn)s where app_id = %(app_id)s """
        mysql_updata(sql_cmd=uodata_sql,param=param)
        select_sql = 'SELECT app_id,app_name,app_mod_name,app_loser_name,app_middleware,app_jdkn,app_ojdbcn,app_date,app_prd_domain,app_prd_ip,app_prd_ojdbcip,app_dev_domain,app_dev_ip,app_dev_ojdbcip FROM abm.application where app_id=%(app_id)s  and app_name!="" '
        sql_data = mysql_select(sql_query=select_sql, param=param)
        return render_template('appr2.html', data=sql_data)
    except TabError as e:
        return ("错误："+e)