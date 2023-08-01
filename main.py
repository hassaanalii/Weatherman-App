import sys
from weather_data_handler import WeatherDataHandler
from yearly_weather_analyzer import YearlyWeatherAnalyzer
from monthly_weather_analyzer import MonthlyWeatherAnalyzer
from monthly_weather_visualizer import MonthlyWeatherVisualizer
  
def yearly_data(year):
    data_handler = WeatherDataHandler()
    monthly_data_list = data_handler.list_initialization(year)

    yearly_analyzer = YearlyWeatherAnalyzer()
    max_temperature, pkt_max_temp, min_temperature, pkt_min_temp, max_humidity, pkt_humidity, min_humidity, mean_humidity = yearly_analyzer.analyzer(monthly_data_list)
    humidity = yearly_analyzer.percentage_humidity(mean_humidity, max_humidity, min_humidity)
    print("\n Highest:", max_temperature, "on", pkt_max_temp)
    print(" Lowest:", min_temperature, "on", pkt_min_temp)

    if humidity:
        print(" Humidity:", humidity, f"% on", pkt_humidity)
    else:
        print(" Max or Min humidity is zero")

def monthly_data(year, month):
    if 1 <= month <= 12:
        data_handler = WeatherDataHandler()
        monthly_data_list = data_handler.list_initialization(year)
        monthly_analyzer = MonthlyWeatherAnalyzer(monthly_data_list)
            
        average_highest_temp = monthly_analyzer.analyzer(month, 'Max TemperatureC')
        average_lowest_temp = monthly_analyzer.analyzer(month, 'Min TemperatureC')
        average_mean_humidity = monthly_analyzer.analyzer(month, ' Mean Humidity')

        print(f"\nHighest Average: {average_highest_temp}C")
        print(f"Lowest Average: {average_lowest_temp}C")
        print(f"Average Mean Humidity: {average_mean_humidity}%")
    else:
        print("\nInvalid month value for monthly data. Month should be between 1 and 12.\n")

def visualizer(year, month):
    if 1 <= month <= 12:
        data_handler = WeatherDataHandler()
        monthly_data_list = data_handler.list_initialization(year)
        monthly_visualizer = MonthlyWeatherVisualizer(monthly_data_list)
        monthly_visualizer.visualizer(month, False)
        print("\n\n BONUS TASK \n\n")
        monthly_visualizer.visualizer(month, True)

    else: 
        print("\nInvalid month value for visualizer. Month should be between 1 and 12.\n")
if __name__ == "__main__":  

    if len(sys.argv) == 4:
        path_to_file = sys.argv[1]
        command = sys.argv[2]
        year = sys.argv[3]

    
        #Module 1
        if command == '-e':
           yearly_data(year)

        elif command == '-a':
            temp_lst = year.split("/")
            year = int(temp_lst[0])
            month = int(temp_lst[1])
            monthly_data(year, month)
            

        elif command == "-c":
            temp_lst = year.split("/")
            year = int(temp_lst[0])
            month = int(temp_lst[1])
            visualizer(year, month)
            

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

        visualizer(year_c, month_c)
    
        monthly_data(year_a, month_a)
        yearly_data(year_e)

        
    else:
        print("Invalid command!")
        
        


        



    #Module 2
    # monthly_analyzer = MonthlyWeatherAnalyzer(monthly_data_list)
    # month = int(input("Enter a month (1 - 12): "))

    # avg_highest_temp = monthly_analyzer.analyzer(month, 'Max TemperatureC')
    # avg_lowest_temp = monthly_analyzer.analyzer(month, 'Min TemperatureC')
    # avg_mean_humidity = monthly_analyzer.analyzer(month, ' Mean Humidity')

    # print("\n The average highest temperature is:", avg_highest_temp, "C")
    # print(" The average lowest temperature is:", avg_lowest_temp, "C")
    # print(" The average mean humidity is:", avg_mean_humidity, "%")

    #Module 3 and bonus task
    # monthly_visualizer = MonthlyWeatherVisualizer(monthly_data_list)

    # month = int(input("Enter a month (1 - 12): "))

    # monthly_visualizer.visualizer(month, True)
    