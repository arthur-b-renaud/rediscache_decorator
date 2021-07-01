import redis
r = redis.Redis(host='ra475940-001.dbaas.ovh.net', port=35820, password="ref1dc671e53A")
r.set('foo', 'name')
r.set('foo2', 'name3')
print(r.get('foo2'))