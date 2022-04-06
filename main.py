from typing import List


class StringCalculator:
    def __init__(self,values:str):
        self.values = self._extract_numbers(values)

    def _extract_numbers(self,values:str)->List:
        if values=="":
            return  []

        return values.split(",")
        
    def get_sum(self)->int:
        sum = 0
        for item in self.values:
            if item:
                sum += int(item)
        return sum

