class FizzBuzz:
    def call(number: int)-> str:
        if Rules.is_multiple_of_three(number) and Rules.is_multiple_of_five(number):
            return Rules.result_of_three() + Rules.result_of_five()

        if Rules.is_multiple_of_three(number):
            return Rules.result_of_three()
        
        if Rules.is_multiple_of_five(number):
            return Rules.result_of_five()

        return str(number)

class Rules:
    def is_multiple_of_three(number: int)-> bool:
        return (number % 3) == 0

    def is_multiple_of_five(number: int)-> bool:
        return (number % 5) == 0

    def result_of_three()-> str:
        return 'FIZZ'

    def result_of_five()-> str:
        return 'BUZZ'