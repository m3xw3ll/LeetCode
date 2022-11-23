def distance_between_bus_stops(distance, start, destination):
    if start > destination:
        start, destination = destination, start
    tot = sum(distance)
    dis = sum(distance[start:destination])
    return min(dis, tot-dis)


print(distance_between_bus_stops(distance=[1, 2, 3, 4], start=0, destination=1))
