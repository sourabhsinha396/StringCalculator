from typing import Union,Tuple


str_or_int = Union[str,int]

class StringCalculator:
    def __init__(self,value:str):
        self.first,self.second = self._extract_numbers(value)

    def _extract_numbers(self,value:str)->Tuple[str_or_int,str_or_int]:
        if value=="":
            return  0,0

        if len(value.rstrip(","))==1:
            return value.rstrip(","),0

        values = value.split(",")
        return values[0],values[1]
        
    def get_sum(self)->int:
        return int(self.first) + int(self.second)

