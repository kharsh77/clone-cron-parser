
class CommandComponent:
    def __init__(self, current_expression):
        self.current_values = [current_expression]
    def get_values(self):
        return ["Command", self.current_values]