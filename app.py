"""Main module"""

def add_numbers(first, second):
    """Add two numbers"""

    return first + second

def main():
    """Main code"""

    first_number = 1
    second_number = 2

    #pylint: disable=line-too-long
    print(f'Hello world! {first_number} + {second_number} = {add_numbers(first_number, second_number)}')

if __name__ == '__main__':
    main()
