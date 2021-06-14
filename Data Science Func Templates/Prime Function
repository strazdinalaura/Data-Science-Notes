def is_prime(x):

    if x == 1:
        return False
    elif x == 2:
        return True

    divisor = int(x/2) 

    while divisor >= 2:
        if x % divisor == 0:
            return False
        divisor -= 1 # -= because we are iterating backwards from let's say 50 to 2 to see what's the biggest divisor 

    return True

#PART 2

def find_primes(n):

    # 1. define counter 
    num = 2 

    # 2. define collector (accumulator)
    list_ = []
    
    # 3. define exit condition
    while num <= n:
        # 5. Collect / filter values that we want 
        if is_prime(num) == True:
            list_.append(num)
            
        # 4. increment the counter (mutate the variable that #controls the exit condition)
        num += 1
        
    # 6. return collection
    return list_

# print(find_primes(1000))
```

```python

def is_prime(num):

  prime = True

  if num < 2:
      return False

  for divisor in range(2, num):
      if num % divisor == 0:
       prime = False
    
  return prime

#for i in range(2, 10):
    #print(i, is_prime(i))

def next_prime(n):
  counter = n
  while True:
    counter += 1
    if is_prime(counter):
      return counter
```

```python
for i in range(20):
    print(i, is_prime(i))
'''
0 False
1 False
2 True
3 True
4 False
5 True
6 False
7 True
8 False
9 False
10 False
11 True
12 False
13 True
14 False
15 False
16 False
17 True
18 False
19 True
'''
```
