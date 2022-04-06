from typing import List


class StringCalculator:
    def __init__(self,values:str):
        self.negative_numbers = []
        self.delimiter = self._get_custom_delimiter(values)
        delimiter_hint_removed = self._trim_delimiter_hint(values)  # delimeter_hint_removed is for Hidden Temporal Coupling
        delimiter_processed = self._process_delimiter(delimiter_hint_removed)
        self.values = self._extract_numbers(delimiter_processed)
    
    def _get_custom_delimiter(self,values:str)->str:
        raw_string = '%r'%values
        if raw_string[1:3]=="//" and raw_string[4:6]==r"\n":
            return raw_string[3:4]
        else:
            return ","

    def _trim_delimiter_hint(self,values:str)->str:
        raw_string = '%r'%values
        if raw_string[1:3]=="//" and raw_string[4:6]==r"\n":
            return raw_string[6:-1]
        return values

    def _process_delimiter(self,values:str)->str:
        delimiter_processed = values.replace(self.delimiter,",")
        return delimiter_processed

    def _extract_numbers(self,values:str)->List:
        if values=="":
            return  []

        return values.split(",")
        
    def get_sum(self)->int:
        sum = 0
        for item in self.values:
            if int(item) < 0:
                self.negative_numbers.append(item)
            if item:
                sum += int(item)
        if self.negative_numbers:
            negative_numbers = " ".join(self.negative_numbers)
            raise ValueError(f"Negative numbers are not allowed, It contains {negative_numbers}")
        return sum

