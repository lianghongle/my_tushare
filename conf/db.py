arr = {
    "host": '',
    "user": '',
    "password": '',
    "db": '',
    "charset": ''
}

url = "mysql+pymysql://" \
      + arr['user'] + ":" + arr['password'] + "@" + arr['host'] + "/" + arr['db'] + "?charset=" + arr['charset']