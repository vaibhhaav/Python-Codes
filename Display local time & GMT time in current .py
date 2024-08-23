import time
current_time = time.time()

local_time = time.localtime(current_time)
formatted_current_time = time.strftime("%Y-%m-%d %H:%M:%S", local_time)
print("Current local time: ", formatted_current_time)

gmt_time = time.gmtime(current_time)
formatted_gmt_time = time.strftime("%Y-%m-%d %H:%M:%S", gmt_time)

print("Current time in GMT:", formatted_gmt_time)
