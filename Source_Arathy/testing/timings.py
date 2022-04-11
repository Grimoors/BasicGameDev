# its all the timing

import time

start_time=time.time()
time.sleep(1)
print("Sleeping time "+str(time.time()-start_time))

print(time.time())
time.sleep(0.5)
print(time.time())
