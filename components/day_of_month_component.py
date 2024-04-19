from components.time_component import TimeComponent

class DayOfMonthComponent(TimeComponent):
    NUMERAL_RANGE=[1,31]
    def __init__(self, current_expression):
        TimeComponent.__init__(self, numeral_range=DayOfMonthComponent.NUMERAL_RANGE)
        super().parse(current_expression)
        
    def get_values(self):
        return ["DayOfMonth", super().get_values()]
