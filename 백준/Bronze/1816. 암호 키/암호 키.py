import sys
import math

def get_primes(limit):
    is_prime = [True] * (limit + 1)
    is_prime[0] = is_prime[1] = False
    for i in range(2, int(math.sqrt(limit)) + 1):
        if is_prime[i]:
            for j in range(i * i, limit + 1, i):
                is_prime[j] = False
    return [i for i, val in enumerate(is_prime) if val]

def is_valid_key(s, primes):
    for prime in primes:
        if prime * prime > s:
            break
        if s % prime == 0:
            return "NO"
    return "YES"

def main():
    input = sys.stdin.readline
    N = int(input())
    primes = get_primes(10**6)
    for _ in range(N):
        S = int(input())
        print(is_valid_key(S, primes))

if __name__ == "__main__":
    main()
