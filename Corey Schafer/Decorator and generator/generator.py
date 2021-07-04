def square_number(nums):
    for i in nums:
        yield (i*i) #yield command makes generator

my_nums = square_number([1,2,3,4,5])
#print(my_nums)

#print(next(my_nums))
#print(next(my_nums))
#print(next(my_nums))
#print(next(my_nums))
#print(next(my_nums))

for num in my_nums:
    print(num)

