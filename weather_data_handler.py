class WeatherDataHandler:
    def __init__(self):
        self.months = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']

    def extracting_data(self, year, month):
        try:
            file_path = f"./weatherfiles/Murree_weather_{year}_{month}.txt"
            with open(file_path, "r") as file:
                raw_data = []
                for values in file:
                    raw_data.append(values)

                columns = raw_data[0].split(',')
                data_dict_list = []

                for line in raw_data[1:]:
                    values = line.strip().split(',')
                    data_dict = dict(zip(columns, values))
                    data_dict_list.append(data_dict)
                return data_dict_list
        except FileNotFoundError:
            return None

    def list_initialization(self, year):
        monthly_data_list = []
        for month in self.months:
            data = self.extracting_data(year, month)
            if data is not None:
                monthly_data_list.append(data)

        with open("output.txt", "w") as output_file:
            output_file.write(str(monthly_data_list))

        return monthly_data_list
