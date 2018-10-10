#coding=utf-8

# https://tushare.pro/document/2?doc_id=25

import sys

sys.path.append('..')

import tushare as ts
from lib.my_tushare.db.DbHelper import DbHelper
from conf.tushare import token

ts.set_token(token)
pro = ts.pro_api()

# 股票列表
fields='ts_code,symbol,name,fullname,enname,exchange_id,curr_type,list_status,list_date,delist_date,is_hs'
df = pro.stock_basic(fields=fields)

# 所有股票表的表名
# stock表除了本脚本更新,应该尽量只有读操作
all_stock_table_name = 'stock_basic'

db = DbHelper()

session = db.getSession()
engine = db.getEngine()

# 把表清空
# 因为我们需要修改表结构,所以to_sql的if_exists='replace'会把表删除,从新建立.
# 所以我们自己删除数据,保留表,使用if_exists='append'
session.execute('TRUNCATE ' + all_stock_table_name)

# 写入数据库
res = df.to_sql(all_stock_table_name, engine, if_exists='append')

# 三元表达式
# true_part if condition else false_part。
msg = 'ok' if res == None else res
print(msg)