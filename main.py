"""
Blackjack
"""
# Provide your solution here
def calculate_score(input_list):
    for element in input_list:
        if element <= 21:
            return sum
        elif element > 21 and  11:
            return (sum-10)
        else:
            print("BUST")


my_list1 = [9, 9, 9]
my_list2 = [2, 8, 11]
my_list3 = [3, 8, 11]
my_list4 = [11, 11, 11]

print("blackjack", calculate_score(my_list1))
print(calculate_score(my_list2))
print(calculate_score(my_list3))
print(calculate_score(my_list4))
"""
Even Numbers
"""
# Provide your solution here

def even_positive_numbers(input_list):
    even_pos_nums=[num for num in input_list if num % 2 <= 0]
    return even_pos_nums


numbers1 = [1, 2, 3]
numbers2 = [10, 22, 31, 24, 35, 36]
numbers3 = [-10, -22, 31, 24, 35, 36]
# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print("Test your functions by calling them here. Use different parameter values to test them with different scenarios.")

print(even_positive_numbers(numbers1))
print(even_positive_numbers(numbers2))
print(even_positive_numbers(numbers3))
