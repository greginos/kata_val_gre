class FizzBuzz:
    def call(number: int)-> str:
        value = (number, 'FIZZ')[Result.multiple_of_three(number)]
        value = (value, 'BUZZ')[Result.multiple_of_five(number)]
        value = (value, 'FIZZBUZZ')[Result.multiple_of_three(number) and Result.multiple_of_five(number)]

        return str(value)

class Result:
    def multiple_of_three(number: int)-> bool:
        return (number % 3) == 0
    def multiple_of_five(number: int)-> bool:
        return (number % 5) == 0