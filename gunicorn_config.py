import multiprocessing
import os

size = int(os.getenv("SIZE", 1))
print "size=", size

# Maximum 5 worker per 128MB
# workers = min(multiprocessing.cpu_count() * 2 + 1, size * 5)
workers = 3
timeout = 120

print "workers=", workers