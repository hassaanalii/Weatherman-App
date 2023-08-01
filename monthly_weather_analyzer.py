class MonthlyWeatherAnalyzer:
    def __init__(self, data_list):
        self.data_list = data_list

    def analyzer(self, month, key):
        if self.data_list[month - 1] is None:
            return  
        
        value_count = 0
        sum = 0
        for day_data in self.data_list[month - 1]:
            if day_data[key] == '':
                continue
            else:
                value_count += 1
                sum += float(day_data[key])
        
        return self.calculate_average(sum, value_count)

    def calculate_average(self, sum, count):
        return sum / count