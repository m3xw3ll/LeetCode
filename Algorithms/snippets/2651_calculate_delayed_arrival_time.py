def find_delayed_arrival_time(arrival_time, delayed_time):
    return (arrival_time + delayed_time) % 24


print(find_delayed_arrival_time(arrival_time=13, delayed_time=11))