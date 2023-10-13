class YearlyWeatherAnalyzer:
    def __init__(self):
        self.analysis_results = {
            "max_temperature": float('-inf'),
            "pkt_max_temp": '',
            "min_temperature": float('inf'),
            "pkt_min_temp": '',
            "max_humidity": 0,
            "min_humidity": float('inf'),
            "mean_humidity": 0,
            "pkt_humidity": ''
        }

    def analyzer(self, data_list):
        for month_data in data_list:
            if month_data is None:
                continue

            for day_data in month_data:
                if day_data['Max TemperatureC'] == '' or day_data['Min TemperatureC'] == '' or day_data['Max Humidity'] == '':
                    continue

                max_temp = float(day_data['Max TemperatureC'])
                min_temp = float(day_data['Min TemperatureC'])
                humidity = int(day_data['Max Humidity'])

                if max_temp > self.analysis_results["max_temperature"]:
                    self.analysis_results["max_temperature"] = max_temp
                    self.analysis_results["pkt_max_temp"] = self.get_pkt_value(day_data)

                if min_temp < self.analysis_results["min_temperature"]:
                    self.analysis_results["min_temperature"] = min_temp
                    self.analysis_results["pkt_min_temp"] = self.get_pkt_value(day_data)

                if humidity > self.analysis_results["max_humidity"]:
                    self.analysis_results["max_humidity"] = humidity
                    self.analysis_results["min_humidity"] = int(day_data[' Min Humidity'])
                    self.analysis_results["mean_humidity"] = int(day_data[' Mean Humidity'])
                    self.analysis_results["pkt_humidity"] = self.get_pkt_value(day_data)

        return self.analysis_results

    def percentage_humidity(self, mean_humidity, max_humidity, min_humidity):
        try:
            percentage_humidity = (mean_humidity - min_humidity) / (max_humidity - min_humidity) * 100
            return percentage_humidity
        except ZeroDivisionError:
            return False

    def get_pkt_value(self, day_data):
        if 'PKT' in day_data:
            return day_data['PKT']
        elif 'PKST' in day_data:
            return day_data['PKST']
        return "Pkt not available"
