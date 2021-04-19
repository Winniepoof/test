import redis

pool=redis.ConnectionPool(
    host='localhost',
    port=6379,
    password='root',
    db=3,
    max_connections=20
)