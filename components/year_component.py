from components.time_component import TimeComponent

class YearComponent(TimeComponent):
    NUMERAL_RANGE=[2023,2030]
    def __init__(self, current_expression):
        super().__init__(numeral_range=YearComponent.NUMERAL_RANGE)
        self.parse(current_expression)
        
    def get_values(self):
        return ["Year", super().get_values()]
