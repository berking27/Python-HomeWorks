from functools import reduce

def calculate(total, blood_glucose_values):
  
  reduction_per_unit = 1800 / total
  
  insulin_needed = [ (value - 120) / reduction_per_unit for value in blood_glucose_values ]
  return insulin_needed


patients = {}


for i in range(5):

  name = input("Enter the patient's name: ")
  blood_glucose_values = [int(x) for x in input("Enter the patient's 12-hour blood glucose values: ").split()]


  high_values = list(filter(lambda x: x > 120, blood_glucose_values))
  print("Glucose values over 120 mg/dl : %s" %high_values)


  insulin_count = int(input("How many times did you take insulin in 12 hours?"))
  insulin_doses = [int(x) for x in input("Enter insulin doses: ").split()]


  total = reduce(lambda x, y: x + y, insulin_doses)


  insulin_needed = calculate(total, high_values)


  patients[name] = {
    "blood_glucose_values": blood_glucose_values,
    "high_values": high_values,
    "insulin_needed": insulin_needed
  }


print(patients)

for name, data in patients.items():
  i = 0
  print(f"\n{name} should take:")
  while(i < 5):
    print(f"{data['insulin_needed'][i]} unit insulin for {data['high_values'][i]} mg/dl")
    i = i + 1