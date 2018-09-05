import mysql.connector as sql


config = {
        'host': '127.0.0.1',
        'user': 'abmadmin',
        'password': 'W&e7Mysl',
        'port': 3306,
        'database': 'abm',
        'charset': 'utf8'
    }

def login_sql(user_name,user_password):
    try:
        conn = sql.connect(**config)
    except sql.Error as e:
        print('connect fails!{}'.format(e))
    cursor = conn.cursor()
    try:
        sql_query = """SELECT user_Number,user_name,user_state FROM abm.user where user_Number="%s" and user_password="%s" and user_state!="n" """%(user_name,user_password)
        cursor.execute(sql_query)
        if cursor == None:
            return ("userError")
        else:
            for user_Number,user_name,user_state in cursor:
                return (user_Number,user_name,user_state)
    except sql.Error as e:
        print('query error!{}'.format(e))
    finally:
        cursor.close()
        conn.close()

def mysql_insert(sql_cmd,param):
    """
        :param sql_cmd sql 命令
        :param param 参数
        """
    try:
        conn = sql.connect(**config)
    except sql.Error as e:
        print('connect fails!{}'.format(e))
    cursor = conn.cursor()
    try:
        cursor.execute(sql_cmd, param)
        conn.commit()#提交sql
    except sql.Error as e:
        print('connect fails!{}'.format(e))
    finally:
        cursor.close()
        conn.close()

def mysql_select(sql_query,param):
    try:
        conn = sql.connect(**config)
    except sql.Error as e:
        print('connect fails!{}'.format(e))
    cursor = conn.cursor()
    try:
        cursor.execute(sql_query,param)
        if cursor == None:
            return ("userError")
        else:
            sql_list = []
            for n in cursor:
                sql_list.append(n)
        #print(sql_list)
        return (sql_list)
    except sql.Error as e:
        print('query error!{}'.format(e))
    finally:
        cursor.close()
        conn.close()

def mysql_updata(sql_cmd,param):
    """
        :param sql_cmd sql 命令
        :param param 参数
        """
    try:
        conn = sql.connect(**config)
    except sql.Error as e:
        print('connect fails!{}'.format(e))
    cursor = conn.cursor()
    try:
        cursor.execute(sql_cmd, param)
        conn.commit()#提交sql
    except sql.Error as e:
        print('connect fails!{}'.format(e))
    finally:
        cursor.close()
        conn.close()