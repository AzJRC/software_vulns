# race-condition homework

This repository explains the race condition bug that arises in main.py due to multiple threats accessing and modifying a shared resource `global_var` without proper synchronization.

## Code analysis

In `main.py`, a global variable its initialized.

```py
global_var = 0
```

The `IncrementThread` class, defined as a subclass of the Thread class, performs the following operations in the respective order:

- Each instance of the class reads the current value of `global_var`.
- Next, it will print the current value of that variable.
- Next, it will increment the value of `global_var` by 1.
- Finally, it will print the new value of that variable.

This application is executed ussing a threading approach. Each `IncrementThreat` would be executed within the `use_increment_thread` function sequentially. The function will perform the following operations in the respective order: 

- 50 `IncrementThread` objects will be instantiated and exectuted sequentially.
- The main thread will wait for all the threads to finish by using `thread.join()`.
- After each thread finishes, the function will print the expected and actual value of the `global_var` variable.

## Cause of race condition

A race condition is a bug or situation that arises in the software due to the relative timing of events (like threading), leading to unpredictable results.
In the code explained before, the operations of reading and writting `global_var` is not **atomic**, i.e., it is possible for multiple threads to read and write the same variable simultanously, leading to lost updates. Basically, a thread may be updating the variable while another thread is also updating the same variable, or in the worst case, a older thread delayed is writting the variable after a newer thread writed the variable.

## Solution proposal

A synchronization mechanism may solve the issue in `main.py`. The following code adds the `Lock` class to the code, that ensures that only one thread can execute the block at a time. (This essentially destroys the purpose of multithreading in the application, but in first place, by the nature of the code, multithreading was not necessary in first place).

```py
from threading import Thread, Lock

global_var = 0
lock = Lock()

class IncrementThread(Thread):
    def run(self):
        global global_var
        with lock:
            read_value = global_var
            print(f"global_var in {self.name} is {read_value}")
            global_var = read_value + 1
            print(f"global_var in {self.name} after increment is {global_var}")
```

## Conclusion

The race condition in the code is due to unsynchronized access to `global_var`, leading to lost updates when multiple threads read and write simultaneously. By introducing a lock to make the read-modify-write sequence atomic, we can eliminate the race condition and ensure `global_var` increments correctly (atomically).
