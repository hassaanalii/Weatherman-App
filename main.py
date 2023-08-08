import sys

from weather_data_handler import WeatherDataHandler
from yearly_weather_analyzer import YearlyWeatherAnalyzer
from monthly_weather_analyzer import MonthlyWeatherAnalyzer
from monthly_weather_visualizer import MonthlyWeatherVisualizer


def get_yearly_data(year):
    data_handler = WeatherDataHandler()
    monthly_data_list = data_handler.list_initialization(year)

    yearly_analyzer = YearlyWeatherAnalyzer()
    yearly_data_dict = yearly_analyzer.analyzer(monthly_data_list)

    humidity = yearly_analyzer.percentage_humidity(yearly_data_dict['mean_humidity'], yearly_data_dict['max_humidity'], yearly_data_dict['min_humidity'])

    return yearly_data_dict, humidity
   

def monthly_temperature_analyzer(year, month):
    if 1 <= month <= 12:
        data_handler = WeatherDataHandler()
        monthly_data_list = data_handler.list_initialization(year)
        monthly_analyzer = MonthlyWeatherAnalyzer(monthly_data_list)

        average_highest_temp = monthly_analyzer.monthly_weather_analyzer(month, 'Max TemperatureC')
        average_lowest_temp = monthly_analyzer.monthly_weather_analyzer(month, 'Min TemperatureC')
        average_mean_humidity = monthly_analyzer.monthly_weather_analyzer(month, ' Mean Humidity')

        print("\nHighest Average: " + str(average_highest_temp) + "C")
        print("Lowest Average: " + str(average_lowest_temp) + "C")
        print("Average Mean Humidity: " + str(average_mean_humidity) + "%")
    else:
        print("\nInvalid month value for monthly data. Month should be between 1 and 12.\n")


def monthly_temperature_visualizer(year, month):
    if 1 <= month <= 12:
        data_handler = WeatherDataHandler()
        monthly_data_list = data_handler.list_initialization(year)
        monthly_visualizer = MonthlyWeatherVisualizer(monthly_data_list)
        monthly_visualizer.monthly_weather_visualizer(month, False)
        print("\n\nBONUS TASK\n\n")
        monthly_visualizer.monthly_weather_visualizer(month, True)

    else:
        print("\nInvalid month value for visualizer. Month should be between 1 and 12.\n")


if __name__ == "__main__":
    if len(sys.argv) == 4:
        path_to_file = sys.argv[1]
        command = sys.argv[2]
        year = sys.argv[3]

        # Module 1
        if command == '-e':
            yearly_data_dict, humidity = get_yearly_data(year)

            print("\nHighest:", yearly_data_dict["max_temperature"], "on", yearly_data_dict['pkt_max_temp'])
            print("Lowest:", yearly_data_dict['min_temperature'], "on", yearly_data_dict['pkt_min_temp'])

            if humidity:
                print("Humidity: {}% on {}".format(humidity, yearly_data_dict['pkt_humidity']))
            else:
                print("Humidity data not available for the year {}".format(year))


        elif command == '-a':
            temp_lst = year.split("/")
            year = int(temp_lst[0])
            month = int(temp_lst[1])
            monthly_temperature_analyzer(year, month)

        elif command == "-c":
            temp_lst = year.split("/")
            year = int(temp_lst[0])     
            month = int(temp_lst[1])
            monthly_temperature_visualizer(year, month)

    elif len(sys.argv) == 8:
        year_month_c = sys.argv[3]
        year_month_a = sys.argv[5]
        year_e = sys.argv[7]

        temp_lst_c = year_month_c.split("/")
        year_c = int(temp_lst_c[0])
        month_c = int(temp_lst_c[1])

        temp_lst_a = year_month_a.split("/")
        year_a = int(temp_lst_a[0])
        month_a = int(temp_lst_a[1])

        monthly_temperature_visualizer(year_c, month_c)
        monthly_temperature_analyzer(year_a, month_a)


        yearly_data_dict, humidity = get_yearly_data(year_e)

        print("\nHighest:", yearly_data_dict['max_temperature'], "on", yearly_data_dict['pkt_max_temp'])
        print("Lowest:", yearly_data_dict['min_temperature'], "on", yearly_data_dict['pkt_min_temp'])

        if humidity:
            print("Humidity: {}% on {}".format(humidity, yearly_data_dict['pkt_humidity']))
        else:
            print("Humidity data not available for the year {}".format(year_e))

    else:
        print("Invalid command!")
