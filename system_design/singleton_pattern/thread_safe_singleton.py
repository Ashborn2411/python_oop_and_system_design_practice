import threading

class Logger:
    _instance=None
    _lock=threading.Lock()
    def __new__(cls):
        if cls._instance is None:
            with cls._lock:
                if cls._instance is None:
                    cls._instance=super().__new__(cls)
                    cls._instance.logs=[]
        return cls._instance
    def log(self,message):
        with self._lock:
            self.logs.append(message)
            print(f"Log:{message}")
    def get_logs(self):
        return self.logs.copy()
def test_logger(thread_id):
    logger=Logger()
    logger.log(thread_id)
threads=[]
for i in range(5):
    t=threading.Thread(target=test_logger,args=(i,))
    threads.append(t)
    t.start()
for t in threads:
    t.join()


