#coding:utf-8

# python3 不支持 MySQL-python
import sys
if sys.version_info.major == 3:
	import pymysql
	pymysql.install_as_MySQLdb()

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from conf import db

engine = create_engine(db.url) # 创建引擎

DB_Session = sessionmaker(bind = engine)
session = DB_Session()
session.execute("set names utf8")

class DbHelper:
	db_engine = None
	db_session = None

	def __init__(self):
		self.db_engine = engine
		self.db_session = session

	def getEngine(self):
		return self.db_engine

	def getSession(self):
		return self.db_session

	def load(self,mname,mclass):
		m = __import__("v1.db1." + mname, fromlist = [mclass])
		getclass = getattr(m, mclass)   #类名
		return getclass

	def do(self, methodName, obj):
		do_method = getattr(self.db_session, methodName)
		return do_method(obj)
