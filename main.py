class StringCalculator:
    def __init__(self,value:str):
        self.first = self._extract_number(value)

    def _extract_number(self,value:str)->int:
        if value=="":
            return  0

    def get_sum(self)->int:
        return int(self.first)

