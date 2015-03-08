
import random 

r = 1 if random.randint(0,1) else -1
print(r)
r = 1 if random.choice([0,1]) else -1
print(r)
r = random.sample([-1,1],1)[0]
print(r)
r = random.permutations('01')[0][0]
print(r)
