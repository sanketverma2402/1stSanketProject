print("-----Ex6: Finally block------")
print("Program started")
a=10
b=0
try:
  print(a / b)     #risky code
except:

  print("Generic Exception Handled")
finally:
  print("--Running finally block--")   #Irrespective of risky or normal code ,finally block will run

print("Program ended")