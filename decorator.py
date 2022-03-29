
def decor(func):
    def inner(*args, **kwargs):
        inner.count += 1
        result = func(inner.count, *args, **kwargs)
        return result
    # use function as object
    inner.count = 0
    return inner

@decor
def running_function(count):
    return count

print(running_function())
print(running_function())
print(running_function())


