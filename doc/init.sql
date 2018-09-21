-- auto-generated definition
create table stock_basic
(
  `index`     INT(10)      null,
  ts_code     VARCHAR(10)  null
  comment 'TS代码',
  symbol      VARCHAR(6)   null
  comment '股票代码',
  name        VARCHAR(10)  null
  comment '股票名称',
  fullname    VARCHAR(30)  null
  comment '股票全称',
  enname      VARCHAR(100) null
  comment '英文全称',
  exchange_id VARCHAR(5)   null
  comment '交易所代码',
  curr_type   VARCHAR(3)   null
  comment '交易货币',
  list_status CHAR(1)      null
  comment '上市状态 L上市 D退市 P暂停上市',
  list_date   INT(10)      null
  comment '上市日期',
  delist_date INT(10)      null
  comment '退市日期',
  is_hs       CHAR(1)      null
  comment '是否沪深港通标的，N否 H沪股通 S深股通'
);

