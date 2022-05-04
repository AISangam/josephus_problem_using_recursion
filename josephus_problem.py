def josephus_recursion(n, k):
    """
    n is the number of the persons
    k is the person to be killed
    assumption is that persons starts with index 0
    """

    if n == 1:
        return 0
    else:
        return (josephus_recursion(n - 1, k) + k) % n


print(josephus_recursion(2, 1))
    