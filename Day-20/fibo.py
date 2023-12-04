def findFib(n):
    if n <= 2:
        return 1
    pre, next_fib = 1, 1

    i = 3
    while i <= n:
        i += 1
        pre, next_fib = next_fib, pre + next_fib

        # pre = next
        # next = pre + next

    return next_fib

def listFib(n):
    fib_list = [1, 1]
    if n <= 2:
        return fib_list[:n]
    pre, next_fib = 1, 1

    i = 3
    while i <= n:
        i += 1
        pre, next_fib = next_fib, pre + next_fib

        fib_list.append(next_fib)

        # pre = next
        # next = pre + next

    return fib_list

