#Turns the letters in a string into numbers
def S2A(inp):
  s = CS(inp)
  ascii_nums = [str(ord(char)) for char in s]
  return "".join(ascii_nums)

#Turns the letters in a string -> capital
def CS(input_string):
  return input_string.upper()

#Computes m^e mod n
def Ecryption(m, e, n):
  c = m**e % n
  return c