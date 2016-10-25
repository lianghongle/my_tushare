#coding=utf-8

"""
获取所有股票,并写入数据库
Created on 2016-10-25
@author: Liang Hong Le
@contact: lianghongle@163.com
"""

"""
code,代码
name,名称
industry,所属行业
area,地区
pe,市盈率
outstanding,流通股本
totals,总股本(万)
totalAssets,总资产(万)
liquidAssets,流动资产
fixedAssets,固定资产
reserved,公积金
reservedPerShare,每股公积金
eps,每股收益
bvps,每股净资
pb,市净率
timeToMarket,上市日期
"""

'''
第一次运行,会报错
(1170, "BLOB/TEXT column 'code' used in key specification without a key length")
[SQL: u'CREATE INDEX ix_stock_code ON stock (code)']
没有把数据插入数据库,但是表已经创建
人工修改表结构
ALTER TABLE `stock` CHANGE COLUMN `code` `code` varchar(6) NOT NULL, ADD PRIMARY KEY (`code`);
'''

from db.DbHelper import DbHelper
import tushare as ts

# 所有股票表的表名
# stock表除了本脚本更新,应该尽量只有读操作
all_stock_table_name = 'stock'

# 获取所有股票基本数据
all_stock = ts.get_stock_basics()

db = DbHelper()

session = db.getSession()
engine = db.getEngine()

# 把表清空
# 因为我们需要修改表结构,所以to_sql的if_exists='replace'会把表删除,从新建立.
# 所以我们自己删除数据,保留表,使用if_exists='append'
session.execute('TRUNCATE ' + all_stock_table_name)

# 写入数据库
res = all_stock.to_sql(all_stock_table_name, engine, if_exists='append')

# 三元表达式
# true_part if condition else false_part。
msg = 'ok' if res == None else res;
print(msg)

