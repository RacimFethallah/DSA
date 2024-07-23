import csv



    # What was the average temperature in first week of Jan
    # What was the maximum temperature in first 10 days of Jan

    # What was the temperature on Jan 9?
    # What was the temperature on Jan 4?




if __name__ == '__main__':
    arr = []
    weather_dict = {}

    with open('04_hashMaps/nyc_weather.csv', newline='') as csvfile:
        next(csvfile)
        for row in csvfile:
            tuple = row.split(",")
            arr.append(int(tuple[1]))
            weather_dict[tuple[0]] = int(tuple[1])

    print(weather_dict['Jan 9'])       
    print(weather_dict['Jan 4'])
    
    # print("1: ", sum(arr[:7]) / 7)
    # print("2: ", max(arr[:10]))