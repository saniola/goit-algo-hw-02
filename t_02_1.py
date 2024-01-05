import queue
import time

### Task 2.1
q = queue.Queue()

def generate_request():
    request = f"Request-{time.time()}"
    q.put(request)

    print(f"Generated request: {request}")

def process_request():
    if not q.empty():
        request = q.get()
        print(f"Processing request: {request}")
    else:
        print("Queue is empty. No requests to process.")

def task1():
    while True:
        generate_request()
        process_request()

        time.sleep(1)

task1()




