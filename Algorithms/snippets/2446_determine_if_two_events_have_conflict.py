def have_conflict(event1, event2):
    start_first_event = int(event1[0].replace(':', ''))
    end_first_event = int(event1[1].replace(':', ''))
    start_second_event = int(event2[0].replace(':', ''))
    end_second_event = int(event2[1].replace(':', ''))
    return True if start_second_event <= end_first_event and start_first_event <= end_second_event else False


print(have_conflict(event1=["14:13","22:08"], event2=["02:40","08:08"]))
