class Range:
    def __init__(self, start, end):
        self.start=start
        self.end=end

class TimeComponent:
    def __init__(self, numeral_range=[], string_values=[]):
        self.numeral_range= Range(numeral_range[0], numeral_range[1])
        self.string_values= string_values
        self.current_values=[]

    # star, number, string, slash, comma, hyphen
    def parse(self, expression):
        if expression == "*":
            self.star_expression()
        elif expression.find("/")!=-1:
            self.slash_expression(expression)
        elif expression.find(",")!=-1:
            self.comma_expression(expression)
        elif expression.find("-")!=-1:
            self.hyphen_expression(expression)
        else:
            try:
                numeral = int(expression)
                self.numeral_expression(expression)
            except:
                self.string_expression(expression)
    
    def star_expression(self):
        self.current_values = [x for x in range(self.numeral_range.start, self.numeral_range.end+1)]
    
    def slash_expression(self,expression):
        values = expression.split("/")
        if len(values)!=2:
            raise Exception(f"Invalid slash expression: {expression}")
        
        try:
            val = int(values[1])
            self.validate_correct_values(val)
        except:
            raise Exception(f"Invalid slash expression: {expression}")


        if values[0]=="*":
            self.current_values = [x for x in range(self.numeral_range.start, self.numeral_range.end+1, int(values[1]))]
        else:
            self.current_values = [x for x in range(int(values[0]), self.numeral_range.end+1, int(values[1]))]
            
    def comma_expression(self, expression):
        values = expression.split(",")

        is_integer = self.validate_all_same_value(values,expression)

        if is_integer:
            validate = [self.validate_correct_values(int(x)) for x in values] 
            self.current_values = [int(x) for x in values]
        else:
            validate = [self.validate_correct_values(x) for x in values] 
            self.current_values = [x for x in values]
    
    def hyphen_expression(self, expression):
        values = expression.split("-")
        try:
            val_start = int(values[0])
            val_end = int(values[1])
            self.validate_correct_values(val_start)
            self.validate_correct_values(val_end)
        except:
            raise Exception(f"Invalid hyphen expression: {expression}")
        
        if len(values)!=2:
            raise Exception(f"Invalid hyphen expression: {expression}")
        
        start = int(values[0])
        end = min(int(values[1]), self.numeral_range.end)
        self.current_values = [x for x in range(start,end+1) ]
    
    def numeral_expression(self, expression):
        self.validate_correct_values(int(expression))
        self.current_values = [int(expression)]
    
    def string_expression(self, expression):
        self.validate_correct_values(expression)
        self.current_values = [expression]
    
    def get_values(self):
        return self.current_values

    def validate_correct_values(self, value):
        if isinstance(value, int):
            if not (self.numeral_range.start <= value and  self.numeral_range.end >=value):
                raise Exception(f'Values out of bound: {value}')
        else:
            if not value in self.string_values:
                raise Exception(f'Values out of bound: {value}')
    
    def validate_all_same_value(self, values, expression):
        is_integer = -1
        is_error=False
        for value in values:
            try:
                val = int(value)                
                if is_integer==0:
                    is_error=True
                    raise Exception(f"Only integer or only string value required: {expression}")
                self.validate_correct_values(val)
                is_integer = 1
            except Exception as ex:
                if is_error:
                    raise Exception(ex)
                if is_integer==1:
                    raise Exception(f"Only integer or only string value required: {expression}")
                self.validate_correct_values(value)
                is_integer = 0
        return is_integer
