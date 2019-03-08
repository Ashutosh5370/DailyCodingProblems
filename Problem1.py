def sum_exist(numbers , target):
    number_seen = set()

    for number in numbers:
        if target- number in number_seen:
            
            return True
        number_seen.add(number)

    return False


print(sum_exist([10,15,3,7] , 17))

#Problem  Given a list of numbers and a number k, return whether any two numbers from the list add up to k.

#For example, given [10, 15, 3, 7] and k of 17, return true since 10 + 7 is 17.

#Bonus: Can you do this in one pass?
