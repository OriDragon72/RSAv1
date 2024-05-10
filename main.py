from Alice import *
from Bob import *
import os

def Master_C0De():
  a = "the number of step|what A does"
  b = " |\n"
  q = "N/A"
  print("Master C0De: " + a + "|what an evesdropper can see|what B does|")
  print("Order: Step|Alice|Eve|Bob\n")

  One_m = "TheQuickBrownFoxJumpsOverTheLazyDog"
  print("1.| " + q + " | " + q + " | " + One_m + b)
  Two_m = S2A(One_m)
  print("2.| " + q + " | " + q + " | " + str(Two_m) + b)
  ThreeP1 = GLP1()
  ThreeP2 = GLP2()
  print("3.| " + str(ThreeP1) + ", " + str(ThreeP2)+ " | " + q + " | " + q + b)
  Four_n = Lock(ThreeP1, ThreeP2)
  print("4.| " + str(Four_n) + " | " + q + " | " + q + b)
  Five_phi_n = Phi(ThreeP1, ThreeP2)
  print("5.| " + str(Five_phi_n) + " | " + q + " | " + q + b)
  Six_e = GON(Five_phi_n)
  print("6.| " + str(Five_phi_n) + " | " + q + " | " + q + b)
  Seven_d = compute_d(GRI(), Five_phi_n, Six_e)
  print("7.| " + str(Seven_d) + " | " + q + " | " + q + b)
  Eight_PK = "(" + str(Four_n) + ", " + str(Six_e) + ")"
  print("8.| " + Eight_PK + " | " + q + " | " + q + b)
  print("9.| " + Eight_PK + " | " + Eight_PK + " | " + Eight_PK + b)
  Ten_c = Ecryption(int(Two_m), Six_e, Four_n)
  print("10.| " + q + " | " + q + " | " + str(Ten_c) + b)
  print("11.| " + str(Ten_c) + " | " + str(Ten_c) + " | " + str(Ten_c) + b)
  Twelve_m = Two_m
  print("12.| " + str(Twelve_m) + " | " + q + " | " + q + b)
  Thirteen_m = One_m
  print("13.| " + str(Thirteen_m) + " | " + q + " | " + One_m + b)

print("Welcome to RSA version 1.0")
print("[aka. an asymmetrical ecryption method]\n")
print("Its a simulation that shows how the RSA Protocol works\n")

print("Start code?")
ANS = input("[y/n]: ")

if ANS == "y":
  os.system("clear")
  
  print("\nStarting...\n")
  print("--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--\n")
  print("Key:")
  print("1. Bob generates a message")
  print("2. Bob converts the message into a number")
  print("3. Alice generates two Prim numbers: P1 and P2")
  print("4. Alice computes n = P1 * P2")
  print("5. Alice computes Phi_n = (P1 - 1) * (P2 - 1)")
  print("6. Alice generates an odd number e that has no common factors with Phi_n")
  print("7. Alice computes d = (k * Phi_n + 1) / e")
  print("8. Alice creats a public key (n, e)")
  print("9. Alice sends the public key to Bob [EVE sees the transaction]")
  print("10. Bob computes c = m^e mod n")
  print("11. Bob sends c to Alice [EVE sees the transaction]")
  print("12. Alice computes m = c^d mod n")
  print("13. Alice coverts the number into the actual message & exchange successful\n")
  print("--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--*--\n")
  Master_C0De()

elif ANS == "n":
  os.system("clear")
  print("Then why did you run this code?")
  exit(784)

else:
  os.system("clear")
  print("Invalid answer")