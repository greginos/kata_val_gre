MULTIPLE_OF_THREE_RESULT = 'FIZZ'
MULTIPLE_OF_FIVE_RESULT = 'BUZZ'
MULTIPLE_OF_SEVEN_RESULT = 'WIZZ'

class FizzBuzz:
    def call(int: int)-> str:
        result = ''
        result += MULTIPLE_OF_THREE_RESULT if Rules.is_multiple_of_three(int) else ''
        result += MULTIPLE_OF_FIVE_RESULT if Rules.is_multiple_of_five(int) else ''
        result += MULTIPLE_OF_SEVEN_RESULT if Rules.is_multiple_of_seven(int) else ''

        result = str(int) if result == '' else result
        return result


class Rules:
    def is_multiple_of_three(int: int)-> bool:
        return int % 3 == 0

    def is_multiple_of_five(int: int)-> bool:
        return int % 5 == 0

    def is_multiple_of_seven(int: int)-> bool:
        return int % 7 == 0