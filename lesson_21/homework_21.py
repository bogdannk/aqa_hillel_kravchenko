from datetime import datetime

def heartbeat_analyze(log_file, key, output_log_file):
    filtered_log = []

    with open(log_file, 'r') as file:
        lines = file.readlines()
        for line in lines:
            if key in line:
                filtered_log.append(line)

    with open(output_log_file, 'w') as log_output:
        previous_time = None

        for line in filtered_log:
            timestamp_index = line.find("Timestamp ")
            if timestamp_index != -1:
                time_str = line[timestamp_index + 10:timestamp_index + 18]
                current_time = datetime.strptime(time_str, "%H:%M:%S")

                if previous_time:
                    time_difference = (previous_time - current_time).total_seconds()

                    if 31 < abs(time_difference) < 33:
                        message = f"WARNING: Time difference is {abs(time_difference)} seconds at {time_str}"
                        print(message)
                        log_output.write(message + '\n')
                    elif abs(time_difference) >= 33:
                        message = f"ERROR: Time difference is {abs(time_difference)} seconds at {time_str}"
                        print(message)
                        log_output.write(message + '\n')

                previous_time = current_time


heartbeat_analyze('hblog.txt', 'Key TSTFEED0300|7E3E|0400', 'hb_test.log')
