import multiprocessing
import os
import datetime

deploy_start_time = datetime.datetime.now()
print "deploy_start_time:", str(deploy_start_time)

size = int(os.getenv("SIZE", 1))
print "size=", size

# Maximum 5 worker per 128MB
workers = min(multiprocessing.cpu_count() * 2 + 1, size * 5)
# workers = 4

timeout = 720
graceful_timeout = 240

print "workers=", workers, "timeout=", timeout