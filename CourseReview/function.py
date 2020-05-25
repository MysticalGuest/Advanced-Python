s = "This is my uncle."
print(s)
print(s.replace("This", "That"))
print(s.lower())
print(s.upper())
s1 = s.upper()
print(s1.replace("IS", "was"))


def check_if_prime(N):
    for x in range(2, N):
        if N % x == 0:
            return False
    return True


print(check_if_prime(3))
print(check_if_prime(4))
print(check_if_prime(5))
print(check_if_prime(6))
print(check_if_prime(7))


