from typing import List


class StringCalculator:
    def __init__(self,values:str):
        self.delimeter = "\n"
        delimeter_processed = self._process_delimeter(values)
        self.values = self._extract_numbers(delimeter_processed)

    def _process_delimeter(self,values:str)->str:
        delimeter_processed = values.replace("\n",",")
        return delimeter_processed

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

