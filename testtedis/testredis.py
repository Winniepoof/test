import redis
from pool import pool

c=redis.Redis(
    connection_pool=pool
)

c.set('country','英国')
c.set('city','伦敦')
#city=c.get('city').decode('utf-8')
#print(city)
#del c