import pymysql

import os
import requests
import json


class CommentResource:

    def __int__(self):
        pass

    @staticmethod
    def _get_connection():
        usr = os.environ.get("DBUSER")
        pw = os.environ.get("DBPW")
        h = os.environ.get("DBHOST")

        conn = pymysql.connect(
            user=usr,
            password=pw,
            host=h,
            cursorclass=pymysql.cursors.DictCursor,
            autocommit=True
        )
        return conn

    @staticmethod
    def get_by_key(key):
        sql = "SELECT * FROM f22_databases.comment where post_id=%s";
        conn = CommentResource._get_connection()
        cur = conn.cursor()
        res = cur.execute(sql, args=key)
        result = cur.fetchall()
        return result

    @staticmethod
    def post_by_input(comment, cid, date, likes):
        sql = "INSERT INTO f22_databases.comment (comment_id,date,likes,text,user_id,post_id,poster_id,username) " \
              "VALUES (%s,%s,%s,%s,%s,%s,%s,%s)";
        val = (cid, date, likes, comment['text'], comment['user_id'], comment['post_id'], comment['poster_id'],
               comment['username'])
        conn = CommentResource._get_connection()
        cursor = conn.cursor()
        res = cursor.execute(sql, val)
        conn.commit()
        cursor.close()
