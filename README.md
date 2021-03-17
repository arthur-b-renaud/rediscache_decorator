## Important Note :

This repo is widely based on https://github.com/louisLouL/louisPy
Yet, for deployment purposes (esp. AWS Lambda), it relies too heavily on pandas.

## Quick start

### Install
```bash
pip install rediscache_decorator
```

### Initialize
```python
from rediscache_decorator import Cache
from redis import StrictRedis
redis = StrictRedis(decode_responses=True)
cache = Cache(redis)
```
## Examples
Make sure you have redis up and running.(https://redis.io/)

### Example1 : Cache string return

```python
from time import sleep
from datetime import datetime
@cache.ttl(300)
def pseudo_calc():
    sleep(1)
    print("Computation in progress")
    return str(datetime.now())

for i in range(10):
    print(pseudo_calc())
```

#### Example 3: Cache dict
```python

@cache.dict(60)
def return_a_dict(*args, **kwargs):
    sleep(1)
    print("Computation in progress")
    return {"now": str(datetime.now())}


for i in range(5):
    print(return_a_dict())
```

#### Example 4: Cache float number
```python
@cache.float(60)
def return_a_float(*args, **kwargs):
    return random()


for i in range(5):
    print(return_a_float())
```

#### Delete Cache
```python
# Delete cache by function and signature
cache.delete_cache(return_a_float, 2, b=3) 
# Delete cache by function
cache.delete_cache(return_a_float)
# Delete all caches
cache.delete_cache()
```