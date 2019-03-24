import random

def question4a():
    with open("justin_test.txt") as my_file:
        file_contents = my_file.read()
    return file_contents

def question3():
    list = [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]
    return list[::2]

def question2():
    print('Enter string to check for palindrome: ')
    check_string = input()
    return str(check_string) == str(check_string[::-1])

def question1():
    # generate random non duplicate values for both lists
    list1 = random.sample(range(30), 10)
    list2 = random.sample(range(30), 10)
    return set(list1) & set(list2)

def main():
    print('Question 1:')
    duplicates = question1()
    print(duplicates)

    print('\nQuestion 2:')
    is_palindrome = question2()
    print(is_palindrome)

    print('\nQuestion 3:')
    even_indices = question3()
    print(even_indices)

    print('\nQuestion 4a:')
    first_n_lines = question4a()
    print(first_n_lines)

if __name__ == "__main__":
    main()