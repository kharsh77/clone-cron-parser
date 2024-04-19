from components.minute_component import MinuteComponent
from components.hour_component import HourComponent
from components.day_of_month_component import DayOfMonthComponent
from components.month_component import MonthComponent
from components.day_of_week_component import DayOfWeekComponent
from components.command_component import CommandComponent

class ExpressionParser:
    EXPRESSION_SUPPORTED = [MinuteComponent, HourComponent, DayOfMonthComponent, MonthComponent, DayOfWeekComponent, CommandComponent]
    def __init__(self, expression):
        self.raw_expression = expression
        self.expression = [None for _ in range(len(ExpressionParser.EXPRESSION_SUPPORTED))]
        self.parse_expression(expression)

    def parse_expression(self, exp):
        is_debug = False
        if is_debug:
            exp_arr = exp.split(" ")
            for i in range(len(ExpressionParser.EXPRESSION_SUPPORTED)):
                self.expression[i]=ExpressionParser.EXPRESSION_SUPPORTED[i](exp_arr[i])
        else:
            try:
                exp_arr = exp.split(" ")
                for i in range(len(ExpressionParser.EXPRESSION_SUPPORTED)):
                    self.expression[i]=ExpressionParser.EXPRESSION_SUPPORTED[i](exp_arr[i])
            except Exception as ex:
                print(f'Exception: {str(ex)}')
                self.expression = [None for _ in range(len(ExpressionParser.EXPRESSION_SUPPORTED))]     

    def expand(self):
        out = []
        for exp in self.expression:
            if not exp:
                return {}
            out.append(exp.get_values())
        return dict(out)
    
    def print_values(self):
        print(f'\nExpression: {self.raw_expression}\n')

        res = self.expand()
        if not res:
            print("No values to print")
            return

        for k,v in res.items():
            key_spaces = 15
            values = v
            if type(v)==list:
                values = ", ".join([str(x) for x in v])
            print(f'{k}' + ' '*(key_spaces-len(k) )+ str(values))
