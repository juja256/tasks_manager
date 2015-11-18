import concurrent.futures as cc
import hashlib

class TaskManager:

    def __init__(self, max_workers=8, t=cc.ProcessPoolExecutor):
        self.__executor = t(max_workers=max_workers)
        self.__max_workers = max_workers
        self.__tasks = {}
        self.__queue = []
        self.__counter = 0
        self.__md5 = hashlib.md5()

    def add_task(self, function, *args, **kwargs):
        self.__counter += 1
        self.__md5.update(("Task#%d" % self.__counter).encode('utf-8'))
        key = self.__md5.hexdigest()[:8]
        if len(self.__tasks) < self.__max_workers:
            self.__tasks[key] = self.__executor.submit(function, *args, **kwargs)
            self.__tasks[key].add_done_callback(self.rebound_execution)
            print("Task " + key + " added to execution")
        else:
            self.__queue.append((key, function, args, kwargs))
            print("Task " + key + " added to queue")
        return key

    def force_get_result(self, key):
        if key in self.__tasks.keys():
            return self.__tasks[key].result()
        else:
            raise ValueError("key is not correct")

    def attempt_get_result(self, key):
        if key in self.__tasks.keys():
            if self.__tasks[key].done():
                res = self.__tasks[key].result()
                del self.__tasks[key]
                return res
            else:
                return None
        elif key in [i[0] for i in self.__queue]:
            print("Task " + key + " is waiting for execution")
        else:
            raise ValueError("key is not correct")
    
    def rebound_execution(self, instance):
        if len(self.__tasks) < self.__max_workers:
            d = self.__max_workers - len(self.__tasks)
            i = 0
            while i < d and len(self.__queue) > 0:
                self.__tasks[self.__queue[i][0]] = self.__executor.submit(self.__queue[i][1], self.__queue[i][2], self.__queue[i][3])
                self.__tasks[self.__queue[i][0]].add_done_callback(self.rebound_execution)
                del self.__queue[i]
                i += 1
            
    def get_all_running_tasks(self):
        return [j for j in self.__tasks.values() if not j.done()]

