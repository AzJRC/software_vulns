from threading import Thread

global_var = 0

class IncrementThread(Thread):
    def run(self):
        global global_var
        read_value = global_var
        print(f"global_var in {self.name} is {read_value}")
        global_var = read_value + 1
        print(f"global_var in {self.name} after increment is {global_var}")

def use_increment_thread():
    threads = []
    for i in range(50):
        thread = IncrementThread()
        threads.append(thread)
        thread.start()
    for i in threads:
        thread.join()
        print()
        print(f"After 50 modifications, global_var should be 50")
        print(f"But after 50 modifications, global_var is {global_var}")

if __name__ == "__main__":
    use_increment_thread()