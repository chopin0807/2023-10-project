import time, os
from multiprocess import Pool

def work_func(x):
    print("value %s is in PID : %s" % (x, os.getpid()))
    time.sleep(1)
    return x**5

def main():
    start = int(time.time())
    num_cores = 4
    pool = Pool(num_cores)
    print(pool.map(work_func, range(1,13)))
    print("***run time(sec) :", int(time.time()) - start)

if __name__ == "__main__":
    main()