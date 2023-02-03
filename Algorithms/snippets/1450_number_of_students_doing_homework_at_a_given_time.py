def busy_student(start_time, end_time, query_time):
    cnt = 0
    for i in range(len(start_time)):
        if start_time[i] <= query_time <= end_time[i]:
            cnt += 1
    return cnt


print(busy_student(start_time = [1,2,3], end_time = [3,2,7], query_time = 4))