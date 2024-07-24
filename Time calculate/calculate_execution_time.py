import time

start = time.time()

for i in range(1000000):
    pass

end = time.time()

execution_time = end-start

print(f"Execution time: {execution_time} seconds")