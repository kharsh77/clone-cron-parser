from components.time_component import TimeComponent

class DayOfWeekComponent(TimeComponent):
    NUMERAL_RANGE=[1,7]
    STRING_VALUES=["SUN","MON","TUE","WED","THU","FRI","SAT"]
    def __init__(self, current_expression):
        TimeComponent.__init__(self, numeral_range=DayOfWeekComponent.NUMERAL_RANGE,string_values=DayOfWeekComponent.STRING_VALUES)
        super().parse(current_expression)
        
    def get_values(self):
        return ["DayOfWeek", super().get_values()]
    