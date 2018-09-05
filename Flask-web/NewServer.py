from flask import Flask,url_for,render_template,request,flash
from abm_sql import mysql_insert,mysql_select,mysql_updata
import time


def newserver_html():
    try:
        param = {}
        param['app_id'] = request.args.get('app_id')#应用ID
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
        param['geology'] = request.args.get('geology')#环境选择
        print (param)
        if param['geology'] == 'dev':  #测试
            server_ip = str(param['app_dev_ip']).split(',')
            return render_template('newserver_html.html',newserver_slist=param,
                                   server_ip=server_ip,
                                   jdkn=param['app_jdkn'],
                                   middleware=param['app_middleware'],
                                   geology=param['geology'],
                                   appsname=param['app_mod_name'],
                                   app_name=param['app_name'],
                                   app_loser_name=param['app_loser_name'])
        elif param['geology'] == 'prd':  #生产
            server_ip = str(param['app_prd_ip']).split(',')
            return render_template('newserver_html.html', newserver_slist=param,
                                   server_ip=server_ip,
                                   jdkn=param['app_jdkn'],
                                   middleware=param['app_middleware'],
                                   geology=param['geology'],
                                   appsname=param['app_mod_name'],
                                   app_name=param['app_name'],
                                   app_loser_name=param['app_loser_name'])
        else:
            return ("没有选择环境")
    except TypeError as e:
        return ("录入错误:"+e)

def install_newzabbix():
    try:
        param = {}
        param['app_id'] = request.args.get('app_id')#应用ID
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
        param['geology'] = request.args.get('geology')#环境选择
        print (param)
        if param['geology'] == 'dev':  # 测试
            server_ip = str(param['app_dev_ip']).split(',')
            pass

        elif param['geology'] == 'prd':  # 生产
            server_ip = str(param['app_prd_ip']).split(',')
            pass

        else:
            return ("没有选择环境")
    except TypeError as e:
        return ("录入错误:"+e)