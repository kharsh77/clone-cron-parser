from components.time_component import TimeComponent

class MinuteComponent(TimeComponent):
    NUMERAL_RANGE=[0,59]
    def __init__(self, current_expression):
        TimeComponent.__init__(self, numeral_range=MinuteComponent.NUMERAL_RANGE)
        super().parse(current_expression)
        
    def get_values(self):
        return ["Minute", super().get_values()]
