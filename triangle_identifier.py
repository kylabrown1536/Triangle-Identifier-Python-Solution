a = int(input("What is the measure of the first angle? "))
b = int(input("What is the measure of second angle? "))

c = 180 - (a + b) 
print("The third angle must be ", c, "degrees.")

def triangle_identifier(a, b, c):
  if a == 90 or b == 90 or c == 90:
    return "This is a right triangle"
  elif a < 90 and b < 90 and c < 90:
    return "This is an acute triangle"
  elif a > 90 or b > 90 or c > 90:
    return "This is an obtuse triangle"
  else:
    print ("Error.")
    
triangle_identifier(a, b, c)