from components.time_component import TimeComponent

class HourComponent(TimeComponent):
    NUMERAL_RANGE=[0,23]
    def __init__(self, current_expression):
        TimeComponent.__init__(self, numeral_range=HourComponent.NUMERAL_RANGE)
        super().parse(current_expression)
        
    def get_values(self):
        return ["Hour", super().get_values()]
