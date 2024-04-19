from components.time_component import TimeComponent

class MonthComponent(TimeComponent):
    NUMERAL_RANGE=[1,12]
    STRING_VALUES=["JAN","FEB","MAR","APR","MAY","JUN","JUL","AUG","SEP","OCT","NOV","DEC"]
    def __init__(self, current_expression):
        TimeComponent.__init__(self, numeral_range=MonthComponent.NUMERAL_RANGE,string_values=MonthComponent.STRING_VALUES)
        super().parse(current_expression)
        
    def get_values(self):
        return ["Month", super().get_values()]
