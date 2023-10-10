

def sum_of_divisors(n):

    # Calculates the sum of proper divisors for a given number 'n'

    divisors_sum = 1

    #Starting the factoring algorithm

    for i in range(2, int(n**0.5) + 1):

        if n % i == 0:

            divisors_sum += i
            #A fall back mechnism to avoid prime numbers
            if i != n // i:

                divisors_sum += n // i
                
    ## Algorithm Ended

    return divisors_sum

#Initializing the amicable numbers function

def find_amicable_numbers(limit):

    amicable_numbers = []

    for num in range(2, limit + 1):
        

        sum_a = sum_of_divisors(num)

        sum_b = sum_of_divisors(sum_a)

        if num == sum_b and num != sum_a:
            #to check for correlation and evade prime numbers

            amicable_numbers.append((num, sum_a))
            
            #print((num, sum_a))

            ## Uncoment the print statement above for verbosity
            ## i.e giving result in real time

    return amicable_numbers

##===================================================

limit = 10000  # Set the upper limit for the range of numbers to check
## Feel free to modify the limit. - but dont set it too high to consume
## you CPU resources; 10000 is gentlemanly enough TONY.

amicable_nums = find_amicable_numbers(limit)

print("Amicable numbers:")

for index, pair in enumerate(amicable_nums):

    print(index, '\t', pair)

 # Set the upper limit for the range of numbers to check amicable_nums = find_amicable_numbers(limit) print("Amicable numbers:") for pair in amicable_nums: print(pair)
