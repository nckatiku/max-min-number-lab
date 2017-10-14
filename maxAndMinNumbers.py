input_set = list()
num = input("Enter how many elements you want:")
print("Enter numbers in array:")
for i in range(int(num)):
    n = int(input("input number :"))
    input_set.append(int(n))
print ("ARRAY: ", input_set)
largest = input_set[0]
for i in range(len(input_set)):

    if input_set[i] > largest:
        greatest = input_set[i]

print("Largest number is :", greatest)

smallest = input_set[0]
for i in range(len(input_set)):

    if input_set[i] < largest:
        smallest = input_set[i]

print("Smallest number is :", smallest)