# -*- coding=UTF-8 -*-
import sys
import pymysql


def ssrlink_input(link):
    j = 0
    while j <= len(link) - 5:
        if link[j:j+4] == 'link':
            return link[j+5:j+21]
        j+=1
    
def mysql_connect(db_name):
    try:
        conn = pymysql.connect(host = '127.0.0.1', user = 'root', passwd = 'XST111077a', db = db_name, port = 3306)
        return conn
    except:
        print('数据库连接出错')
        conn.close()
        sys.exit()

def creat_table(db_name):
    mysql = mysql_connect(db_name)
    cur = mysql.cursor()  #数据库指向游标
    sql = "create table if not exists python.`user` \
                (id int not null primary key AUTO_INCREMENT, \
                name char(10) not null, \
                email char(15) not null, \
                token text not null);"
    try:
        cur.execute(sql)
        mysql.commit()
    except:
        print('建表出错！')
        mysql.close()
        sys.exit()
    finally:
        cur.close()
        mysql.close()

def insert_info(db_name):
    mysql = mysql_connect(db_name)
    cur = mysql.cursor()  #数据库指向游标
    sql = "INSERT INTO python.`user` (name,email,token) VALUES ('xiao','123@qq.com','jfajfajf');"
    try:
        cur.execute(sql)
        mysql.commit()
    except:
        print('插入数据失败')
        mysql.close()
        sys.exit()
    finally:
        cur.close()
        mysql.close()

def delete_info(db_name):
    mysql = mysql_connect(db_name)
    cur = mysql.cursor()  #数据库指向游标
    sql = "DELETE FROM python.`user` WHERE id > 3"
    try:
        cur.execute(sql)
        mysql.commit()
        mysql.close()
    except:
        print('信息删除失败！')
        mysql.close()
        sys.exit()
    finally:
        cur.close()
        mysql.close()

def update_info(db_name,id):
    mysql = mysql_connect(db_name)
    cur = mysql.cursor()  #数据库指向游标

    sql = "UPDATE python.`user` SET name = 'xiu' WHERE id = " + str(id)
    try:
        cur.execute(sql)
        mysql.commit()
    except:
        print('信息更新失败！')
        mysql.close()
        sys.exit()
    finally:
        cur.close()
        mysql.close()

def get_info(db_name,table = "`user`"):
    mysql = mysql_connect(db_name)
    cur = mysql.cursor()  #数据库指向游标
    sql = "SELECT * FROM "+ db_name + '.' + table + ";"
    try:
        cur.execute(sql)
        all = cur.fetchall()
        return all
    except:
        print('数据获取失败！')
        mysql.close()
        sys.exit()
    finally:
        cur.close()
        mysql.close()

def search_info(db_name,search_key,table = "`user`",table_field = "id"):
    mysql = mysql_connect(db_name)
    cur = mysql.cursor()  #数据库指向游标
    sql = "SELECT * FROM " + db_name + "." + table + " WHERE " + str(table_field) + " = \'" + str(search_key) + "\'"
    try:
        cur.execute(sql)
        all = cur.fetchall()
        return all
    except:
        print('数据获取失败！')
        mysql.close()
        sys.exit()
    finally:
        cur.close()
        mysql.close()

def display_tk(user,tree):
    j = len(user)-1
    i = 0
    while j >= 0:
        tree.insert("",0,text = j+1,values = (user[j][0],user[j][2]))
        j-=1
        i+=1
def search_FLG(db_name):
    mysql = mysql_connect(db_name)
    cur = mysql.cursor()  #数据库指向游标
    sql = "SELECT u.id, u.email, COUNT(*) num \
        FROM super.detect_log l INNER JOIN super.`user` u \
            ON l.user_id = u.id \
                WHERE l.list_id IN (3,13) \
                    GROUP BY l.user_id \
                        ORDER BY num DESC "
    try:
        cur.execute(sql)
        all = cur.fetchall()
        return all
    except:
        print('数据获取失败！')
        mysql.close()
        sys.exit()
    finally:
        cur.close()
        mysql.close()

def search_BT(db_name):
    mysql = mysql_connect(db_name)
    cur = mysql.cursor()  #数据库指向游标
    sql = "SELECT u.id, u.email, COUNT(*) num \
        FROM super.detect_log l INNER JOIN super.`user` u \
            ON l.user_id = u.id \
                WHERE l.list_id IN (4,11) \
                    GROUP BY l.user_id \
                        ORDER BY num DESC "
    try:
        cur.execute(sql)
        all = cur.fetchall()
        return all
    except:
        print('数据获取失败！')
        mysql.close()
        sys.exit()
    finally:
        cur.close()
        mysql.close()
