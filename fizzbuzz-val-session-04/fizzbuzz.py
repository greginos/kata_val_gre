class FizzBuzz:
    def call(number: int)-> str:
        input_number = Number(number)
        result = Result(input_number)

        if input_number.is_multiple_of_five() and input_number.is_multiple_of_three():
            return result.fizz() + result.buzz()
        if input_number.is_multiple_of_three():
            return result.fizz()
        if input_number.is_multiple_of_five():
            return result.buzz()

        return result.to_string()


class Number:
    def __init__(self, value: int) -> None:
        self.value = value
    
    def is_multiple_of_three(self)-> bool:
        return self.value % 3 == 0
            
    def is_multiple_of_five(self)-> bool:
        return self.value % 5 == 0

class Result:
    def __init__(self, number: Number) -> None:
        self.number = number

    def fizz(self)-> str:
        return 'FIZZ'

    def buzz(self)-> str:
        return 'BUZZ'

    def to_string(self)-> str:
        return str(self.number.value)