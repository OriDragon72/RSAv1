import math
import random
import sympy


#Alice P1
def GLP1():
  prime_num = sympy.randprime(10 ** 150, 10 ** 151)
  return prime_num 

#Alice P2
def GLP2():
  prime_num = sympy.randprime(10 ** 150, 10 ** 151)
  return prime_num 

#Public Lock
def Lock(P1, P2):
  n = P1 * P2
  return n

#The Phi of number
def Phi(P1, P2):
  Phi_n = (P1 - 1) * (P2 - 1)
  return Phi_n

#Generates an odd small exponents that has no common factors with Phi_n
def GON(phi_n):
  while True:
    odd_num = sympy.randprime(1, 25)
    if math.gcd(odd_num, phi_n) == 1:
      return odd_num

#Alice's private key
def compute_d(k, phi_n, e):
  d = (k * phi_n + 1) / e
  return d

#Computes c^d mod n
def Decryption(c, d, n):
  m = c**d % n
  return m

def A2S(nums):
  chars = [chr(int(num)) for num in nums.split()]
  return "".join(chars)

#Generates a random integer between 1 and 20
def GRI():
  return random.randint(1, 20)
