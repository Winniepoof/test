import redis

pool=redis.ConnectionPool(

    host='localhost',
    port=6379,
    password='',
    db=3,
    max_connections=20
)

if __name__ == '__main__':
    pass