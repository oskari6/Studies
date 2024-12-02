def get_station_data(filename):    
    with open(filename) as file:
        locations = {}
        next(file)
        for line in file:
            formatted = line.strip().split(";")
            locations[formatted[3]] = (float(formatted[0]), float(formatted[1]))
    return locations

def distance(stations, station1, station2):
    import math

    longitude1 = stations[station1][0]
    latitude1 = stations[station1][1]
    longitude2 = stations[station2][0]
    latitude2 = stations[station2][1]

    x_km = (longitude1 - longitude2) * 55.26
    y_km = (latitude1 - latitude2) * 111.2
    distance_km = math.sqrt(x_km**2 + y_km**2)

    return distance_km

def greatest_distance(stations):
    greatest = 0
    station1 = ""
    station2 = ""

    import math

    keys = list(stations.keys())

    for i in range(len(stations)):
        key1 = keys[i]
        longitude1, latitude1 = stations[key1]

        for j in range(i+1, len(keys)):
            key2 = keys[j]
            longitude2, latitude2 = stations[key2]

            x_km = (longitude1 - longitude2) * 55.26
            y_km = (latitude1 - latitude2) * 111.2
            distance_km = math.sqrt(x_km**2 + y_km**2)
            if distance_km > greatest:
                greatest = distance_km
                station1 = key1
                station2 = key2

    return station1, station2, greatest

if __name__ == "__main__":
    stations = get_station_data('stations1.csv')
    d = distance(stations, "Designmuseo", "Hietalahdentori")
    print(d)
    d = distance(stations, "Viiskulma", "Kaivopuisto")
    print(d)
    stations = get_station_data('stations1.csv')
    station1, station2, greatest = greatest_distance(stations)
    print(station1, station2, greatest)