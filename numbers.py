numbers=[17, 12, 17, 19, 8, 19, 16, 15, 17, 10]

#Sum:
sum=sum(numbers)
print('Sum: ',sum )

#sort
numbers.sort()

#Median:
length = len(numbers)
middle =length // 2
if length%2==0:
   median=(numbers[middle-1]+numbers[middle])/2

else:
    median=numbers[middle]
print('Median: ',median)

#Mode:
mode= numbers[0]
#initial point of the mode

highest_count=0
for number in numbers:
    count=numbers.count(number)

    if count > highest_count:
        highest_count=count
        mode=number

print('Mode: ',mode)

#Mean:
length = len(numbers)
mean = sum/length
print('Mean: ',mean)