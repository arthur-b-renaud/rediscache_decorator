from datetime import datetime
from time import sleep
from redis import StrictRedis
from random import random
from redis_cache_decorator import Cache


### Comment this section if you don't have redis instance ###
redis = StrictRedis(decode_responses=True)
cache = Cache(redis)


@cache.ttl(300)
def pseudo_calc():
    sleep(1)
    print("Computation in progress")
    return str(datetime.now())


for i in range(10):
    print(pseudo_calc())


@cache.ttl(123)
def another():
    return "hello"

# Example: redis_cache_decorator dict

@cache.dict(60)
def return_a_dict(*args, **kwargs):
    sleep(1)
    print("Computation in progress")
    return {"now": str(datetime.now())}


for i in range(5):
    print(return_a_dict())


# Example: redis_cache_decorator float number


@cache.float(60)
def return_a_float(*args, **kwargs):
    return random()


for i in range(5):
    print(return_a_float())
