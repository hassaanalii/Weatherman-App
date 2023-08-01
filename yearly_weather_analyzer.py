class YearlyWeatherAnalyzer:
    def __init__(self):
        # Initialize any instance variables here if needed
        pass

    def analyzer(self, data_list):
    # Initialize max_temperature and min_temperature to reasonable starting values
        max_temperature = float('-inf')
        pkt_max_temp = ''

        min_temperature = float('inf')
        pkt_min_temp = ''

        max_humidity = 0
        min_humidity = float('inf')
        mean_humidity = 0
        pkt_humidity = ''

        for month_data in data_list:
            if month_data is None:
                continue

            for day_data in month_data:

                if day_data['Max TemperatureC'] == '' or day_data['Min TemperatureC'] == '' or day_data['Max Humidity'] == '':
                    continue

                max_temp = float(day_data['Max TemperatureC'])
                min_temp = float(day_data['Min TemperatureC'])
                humidity = int(day_data['Max Humidity'])

                if max_temp > max_temperature:
                    max_temperature = max_temp
                    if 'PKT' in day_data:
                        pkt_max_temp = day_data['PKT']
                    elif 'PKST' in day_data:
                        pkt_max_temp = day_data['PKST']
                    else:
                        pkt_max_temp = "Pkt not available"
                

                if min_temp < min_temperature:
                    min_temperature = min_temp
                    if 'PKT' in day_data:
                        pkt_min_temp = day_data['PKT']
                    elif 'PKST' in day_data:
                        pkt_min_temp = day_data['PKST']
                    else:
                        pkt_min_temp = "Pkt not available"    

                if humidity > max_humidity:
                    max_humidity = humidity
                    min_humidity = int(day_data[' Min Humidity'])
                    mean_humidity = int(day_data[' Mean Humidity'])
                    if 'PKT' in day_data:
                        pkt_humidity = day_data['PKT']
                    elif 'PKST' in day_data:
                        pkt_humidity = day_data['PKST']
                    else:
                        pkt_humidity = "Pkt not available"

        return max_temperature, pkt_max_temp, min_temperature, pkt_min_temp, max_humidity, pkt_humidity, min_humidity, mean_humidity


    def percentage_humidity(self, mean_humidity, max_humidity, min_humidity):
        try:
            percentage_humidity = (mean_humidity - min_humidity) / (max_humidity - min_humidity) * 100
            return percentage_humidity
        except ZeroDivisionError:
            return False
