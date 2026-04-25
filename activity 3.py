def fibonacci_cemi_suretli(limit):
    a, b = 2, 8
    cem = 0

    while a <= limit:
        cem += a
        a, b = b, 4 * b + a

    return cem

print(fibonacci_cemi_suretli(4_000_000))