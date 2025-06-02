import threading

class DBConnectionSingleton:
    __instance = None
    __lock = threading.Lock()

    def __new__(cls, *args, **kwargs):
        if not cls.__instance:
            with cls.__lock:
                if not cls.__instance:
                    cls.__instance = super(DBConnectionSingleton, cls).__new__(cls)
        return cls.__instance
    
d1 = DBConnectionSingleton()
d2 = DBConnectionSingleton()

print(id(d1))
print(id(d2))

# threading example
def thread_function(name):
    instance = DBConnectionSingleton()
    print(f"Thread {name}: {id(instance)}")

threads = []
print("Creating and starting threads...")
for index in range(5):
    thread = threading.Thread(target=thread_function, args=(index,), daemon=True)
    threads.append(thread)
    thread.start()

for thread in threads:
    thread.join()

print("All threads have finished execution.")

# executors & futures example
print("\nUsing ThreadPoolExecutor to create multiple threads...")
from concurrent.futures import ThreadPoolExecutor
with ThreadPoolExecutor(max_workers=5) as executor:
    futures = [executor.submit(thread_function, i) for i in range(5)]
    for future in futures:
        future.result()  # Wait for all threads to complete
