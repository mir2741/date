from flask import Flask,url_for,render_template,request,flash
from abm_sql import mysql_insert,mysql_select
import time

def geography_w():
    try:
        param = {}
        param['ge_name'] = request.args.get('ge_name')
        param['ge_addr'] = request.args.get('ge_addr')
        sql_cmd = "insert into abm.geography (ge_name,ge_addr) VALUES (%(ge_name)s,%(ge_addr)s);"
        mysql_insert(sql_cmd, param)
        return ("录入OK")
    except TypeError:
        return ("录入错误")

def geography_r():
    try:
        gid_data = {}
        gid_data['ge_id'] = request.args.get('g_id')
        print(gid_data)
        select_cmd = "select server_sn,server_name,asset_sn,server_ip,server_date,server_p,server_l,server_u,ge_name from abm.the_server as a join abm.server_geography as ag join abm.geography as g where ag.ge_id=g.ge_id and a.server_id=ag.server_id and ag.ge_id=%(ge_id)s;"
        server_data = mysql_select(sql_query=select_cmd, param=gid_data)
        print(server_data)
        param = (".*",)
        sql_query = "select ge_id,ge_name,ge_addr from abm.geography where ge_name regexp %s;"
        f = mysql_select(sql_query, param)
        return render_template('gh.html',service_select=server_data,gname=f,g_Total=len(server_data))

    except TypeError:
        return ("错误")

