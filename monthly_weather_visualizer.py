from datetime import datetime

class MonthlyWeatherVisualizer:
    def __init__(self, data_list):
        self.data_list = data_list

    def PKT_PKST(self, month):
        if 'PKT' in self.data_list[month - 1][0]:
            return False
        else:
            return True

    def visualizer(self, month, bool_bonus):
        if self.data_list[month - 1] is None:
            return "No data is available for this month"

        # Check if the attribute is PKT or PKST
        check = self.PKT_PKST(month)
        attribute = "PKT"
        if check:
            attribute = "PKST"

        print("\n")
        for day_data in self.data_list[month - 1]:
            if day_data['Max TemperatureC'] == '' or day_data['Min TemperatureC'] == '':
                continue

            if attribute in day_data:
                date = day_data[attribute]
                parsed_date = datetime.strptime(date, '%Y-%m-%d')
                day = parsed_date.day

                if not bool_bonus:
                    self.visualizer_implementation(day, day_data)
                else:
                    self.bonus_task(day, day_data)

            else:
                continue

    def visualizer_implementation(self, day, day_data):
        highest_temp_bar = str(day) + " "
        lowest_temp_bar = str(day) + " "

        for i in range(int(day_data['Max TemperatureC'])):
            highest_temp_bar += "\033[31m" + "+" + "\033[0m"

        for i in range(int(day_data['Min TemperatureC'])):
            lowest_temp_bar += "\033[34m" + "+" + "\033[0m"

        highest_temp_bar += " " + str(int(day_data['Max TemperatureC'])) + "C"
        lowest_temp_bar += " " + str(int(day_data['Min TemperatureC'])) + "C"

        print(highest_temp_bar)
        print(lowest_temp_bar)
        print("\n")

    def bonus_task(self, day, day_data):
        date_bar = str(day) + " "

        for i in range(int(day_data['Max TemperatureC'])):
            date_bar += "\033[31m" + "+" + "\033[0m"

        for i in range(int(day_data['Min TemperatureC'])):
            date_bar += "\033[34m" + "+" + "\033[0m"

        date_bar += " " + str(int(day_data['Max TemperatureC'])) + "C"
        date_bar += " " + str(int(day_data['Min TemperatureC'])) + "C"

        print(date_bar)
        print("\n")
