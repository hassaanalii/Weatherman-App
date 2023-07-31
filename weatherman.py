from pprint import pprint
from datetime import datetime


def extracting_data(year, month):
    try:
            
        with open(f"./weatherfiles/Murree_weather_{year}_{month}.txt", "r") as file:
            raw_data = []
            for values in file:
                raw_data.append(values)

            # print('\n\n')
            # print(raw_data)
            # print("\n\n")

            columns = raw_data[0].split(',')
            # print(columns)
            # print("\n\n")

            data_dict_list = []

            for line in raw_data[1:]:
                values = line.strip().split(',')
                data_dict = dict(zip(columns, values))
                data_dict_list.append(data_dict)
            return data_dict_list
    except: 
        pass

def list_initialization():
    temp = True
    while temp:
        year = int(input("\n Enter an year (2004 - 2016): "))
        if year < 2004 or year > 2016:
            pass
        else:
            temp = False
            

    months = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']
    monthly_data_list = []

    for month in months:
        monthly_data_list.append(extracting_data(year, month))

    # pprint(monthly_data_list)
    with open("output.txt", "w") as output_file:
        output_file.write(str(monthly_data_list)) 

    return monthly_data_list


def module_1(data_list):
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


def percentage_humidity(mean_humidity, max_humidity, min_humidity):
    try:
        percentage_humidity = (mean_humidity - min_humidity) / (max_humidity - min_humidity) * 100
        return percentage_humidity
    except ZeroDivisionError:
        return False
    

def module_2(data_list, month, key, value_count, sum):

    if data_list[month - 1] is None:
        return "Not available for this month"
    
    for day_data in data_list[month - 1]:
        if day_data[key] == '':
            continue
        else:
            value_count += 1
            sum += float(day_data[key])
    
    return(calculate_average(sum, value_count))


def calculate_average(sum, count):
    return sum / count


def PKT_PKST(data_list, month):
    if 'PKT' in data_list[month - 1][0]:
        return False
    else:
        return True
    

def module_3(data_list, month, bool_bonus):
    if data_list[month - 1] is None:
        return "No data is available for this month"
    # check if the attribute is PKT or PKST
    check = PKT_PKST(data_list, month)
    attribute = "PKT"
    if check:
        attribute = "PKST"

    print("\n")
    
    for day_data in data_list[month - 1]:
        if day_data['Max TemperatureC'] == '' or day_data['Min TemperatureC'] == '':
            continue
        if attribute in day_data:
            date = day_data[attribute]
            parsed_date = datetime.strptime(date, '%Y-%m-%d')
            day = parsed_date.day

            if not bool_bonus:
                module_3_implementation(day, day_data)
            else:
                bonus_task(day, day_data)

        else:
            continue
         
def module_3_implementation(day, day_data):
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

def bonus_task(day, day_data):
    date_bar = str(day) + " "
    for i in range(int(day_data['Max TemperatureC'])):
        date_bar += "\033[31m" + "+" + "\033[0m"

    for i in range(int(day_data['Min TemperatureC'])):
        date_bar += "\033[34m" + "+" + "\033[0m"
            
    date_bar += " " + str(int(day_data['Max TemperatureC'])) + "C"
    date_bar += " " + str(int(day_data['Min TemperatureC'])) + "C"

    print(date_bar)
    print("\n")

def month_input():
    temp = True
    while temp:
        month = int(input(" Enter a month (1 - 12): "))
        if month >= 1 and month <= 12:
            temp = False
    return month

if __name__ == '__main__':
    temp = True
  
    while temp:
        print("\n\n\t\t\t*******************************************************")
        print("\n\t\t\t\t\tWeatherman Application")
        print("\n\t\t\t*******************************************************")
        print("\n Main Menu: ")
        print("\n 1. Highest temperature and day, lowest temperature and day, most humid day and humidity. ")
        print(" 2. Average highest temperature, average lowest temperature, average mean humidity.")
        print(" 3. Horizontal bar charts for the highest and lowest temperature on each day.")
        print(" 4. BONUS TASK: Draw horizontal bar chart for the highest and lowest temperature on each day.")
        print(" 5. Exit\n")

        option = int(input(" Choose an option: "))

        if option == 1:
            monthly_data_list = list_initialization()
            max_temperature, pkt_max_temp, min_temperature, pkt_min_temp, max_humidity, pkt_humidity, min_humidity, mean_humidity = module_1(monthly_data_list)

            humidity = percentage_humidity(mean_humidity, max_humidity, min_humidity)
            print("\n Highest:", max_temperature, "on", pkt_max_temp)
            print(" Lowest:", min_temperature, "on", pkt_min_temp)

            if humidity:
                print(" Humidity:", humidity, f"% on", pkt_humidity)
            else:
                print(" Max or Min humidity is zero")
        elif option == 2:
            monthly_data_list = list_initialization()
            month = month_input()

            print("\n The average highest temperature is: ", module_2(monthly_data_list, month, 'Max TemperatureC', 0, 0))
            print(" The average lowest temperature is: ", module_2(monthly_data_list, month, 'Min TemperatureC', 0, 0))
            print(" The average mean humidity is: ", module_2(monthly_data_list, month, ' Mean Humidity', 0, 0))
        elif option == 3:
            monthly_data_list = list_initialization()
            month = month_input()
            module_3(monthly_data_list, month, False)
        elif option == 4:
            monthly_data_list = list_initialization()
            month = month_input()
            module_3(monthly_data_list, month, True)
        else:
            print("\n Thankyou!\n")
            temp = False







