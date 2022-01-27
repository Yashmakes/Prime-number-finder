# author Yash
# web- Drperfect.tech

lower = int(input("Enter first no."))
upper = int(input("Enter Second no."))

print("Prime numbers between", lower, "and", upper, "are:")
for num in range(lower, upper + 1):
 if num > 1:
    for i in range(2, num):
           
        if (num % i) == 0:
            
            break