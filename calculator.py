
def add(a, b):
  return a + b
def subtract(a, b):
  return a - b
def multiply(a, b):
  return a * b

def square(a):
  return a * a
def divide(a,b):
  if b == 0:
    return None
  return a / b

if __name__ == "__main__":
  print("2 + 3 =", add(2, 3))
  print("5- 2 =", subtract(5, 2))
  print("3 * 4 =", multiply(3, 4))
  print("4 squared = ", square(4))
  print("10 / 2 =", divide(10, 2))
