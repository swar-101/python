# Python Lambda

A lambda is a small anonymous function.

A lambda function can take any number of arguments, but only can have one expression.

## Syntax

lambda *arguments* : expression

The expression is executed and the result is returned.
e.g.

```python
    x = lambda a: a + 10
    print(x(5))
```

## Why use Lambda Functions?

The power of lambda can be seen when you use an anonymous function inside another function.
for e.g. 

```python
def myfunc(n):
  return lambda a: a * n

# making an x2 multiplier
my_doubler = myfunc(2)

print(my_doubler(2)) 

# making an x3 multiplier
my_tripler = myfunc(3)

print(my_tripler(11))
```



