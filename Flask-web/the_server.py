from flask import Flask,url_for,render_template,request,flash
from abm_sql import mysql_insert,mysql_select,mysql_updata
import time

def server_wo():
    try:
        c = []
        param = []
        param.append(request.args.get('serversn'))
        param.append(request.args.get('servername'))
        param.append(request.args.get('serverasn'))
        param.append(request.args.get('serverip'))
        param.append(time.strftime('%Y%m%d%H%M%S', time.localtime(time.time())))
        param.append(request.args.get('Row'))
        param.append(request.args.get('column'))
        param.append(request.args.get('U_Number'))
        c_data = {}
        c_data['ge_id'] = request.args.get('g_id')
        sql_cmd = "insert into abm.the_server (server_sn,server_name,asset_sn,server_ip,server_date,server_p,server_l,server_u) VALUES (%s,%s,%s,%s,%s,%s,%s,%s);"
        param = tuple(param)
        mysql_insert(sql_cmd,param)
        date = {}
        date['server_sn'] = param[0]
        date['server_ip'] = param[3]
        select_cmd = "select server_id from abm.the_server where server_sn=%(server_sn)s AND server_ip=%(server_ip)s;"
        server_id = mysql_select(sql_query=select_cmd, param=date)
        #print(server_id[0][0])
        if len(server_id) > 0:
            c_data['server_id'] = server_id[0][0]
            #print(c_data['server_id'])
            sql_insert = "insert into abm.server_geography (ge_id,server_id) value (%(ge_id)s,%(server_id)s)"
            mysql_insert(sql_cmd=sql_insert, param=c_data)
            return ('录入完成')
        else:
            return ("录入失败")
    except TypeError :
        return ("录入错误")

def server_ro():
    try:
        param = {}
        param['server_sn'] = request.args.get('serversn')
        param['server_name'] = request.args.get('servername')
        param['asset_sn'] = request.args.get('serverasn')
        param['server_ip'] = request.args.get('serverip')
        param['server_p'] = request.args.get('Row')
        param['server_l'] = request.args.get('column')
        param['server_u'] = request.args.get('U_Number')

        if param['server_sn'] == 'ALL':
            param['server_sn'] = '.*'
        if param['server_name'] == 'ALL':
            param['server_name'] = '.*'
        if param['asset_sn'] == 'ALL':
            param['asset_sn'] = '.*'
        if param['server_ip'] == 'ALL':
            param['server_ip'] = '.*'
        if param['server_p'] == 'ALL':
            param['server_p'] = '.*'
        if param['server_l'] == 'ALL':
            param['server_l'] = '.*'
        if param['server_u'] == 'ALL':
            param['server_u'] = '.*'
        #print(param)
        sql_query = "SELECT server_id,server_sn,server_name,asset_sn,server_ip,server_date,server_p,server_l,server_u FROM abm.the_server where server_sn regexp %(server_sn)s and server_name regexp %(server_name)s and asset_sn regexp %(asset_sn)s and server_ip regexp %(server_ip)s and server_p regexp %(server_p)s and server_l regexp %(server_l)s and server_u regexp %(server_u)s;"
        service_select = mysql_select(sql_query, param)
        #print (service_select)
        return render_template('serverr.html',service_select=service_select)
    except TypeError:
        return ("查询错误")


def server_updata():
    try:
        param = {}
        param['server_id'] = request.args.get('serverid')
        param['server_sn'] = request.args.get('serversn')
        param['server_name'] = request.args.get('servername')
        param['asset_sn'] = request.args.get('serverasn')
        param['server_ip'] = request.args.get('serverip')
        param['server_p'] = request.args.get('Row')
        param['server_l'] = request.args.get('column')
        param['server_u'] = request.args.get('U_Number')
        #print (param)
        uodata_sql = """ update abm.the_server set server_sn=%(server_sn)s,server_name=%(server_name)s,asset_sn=%(asset_sn)s,server_ip=%(server_ip)s,server_p=%(server_p)s,server_l=%(server_l)s,server_u=%(server_u)s where server_id=%(server_id)s """
        mysql_updata(sql_cmd=uodata_sql, param=param)
        sql_query = "SELECT server_id,server_sn,server_name,asset_sn,server_ip,server_date,server_p,server_l,server_u FROM abm.the_server where server_id=%(server_id)s"
        service_select = mysql_select(sql_query, param)
        return render_template('serverr.html',service_select=service_select)
    except TabError as e:
        return e