with open('/tmp/exmaples/log.txt', "r") as file:
    time_stamp = []
    for line in file:
        status_code = line.split(" ")[1]
        if status_code == "ERROR":
            time_stamp.append(line.split(" ")[0])

    start_time = time_stamp[0]
    end_time = time_stamp[-1]
    total_messages = len(time_stamp)
    error_rate = len(time_stamp)/(int(end_time) - int(start_time))

    print(error_rate)
