from datetime import date, datetime

today = date.today()

with open("today.txt", "w") as file:
	file.write(str(today))
	
	


with open("today.txt", "r") as file:
	today_string = file.read()
	
print(today_string)



from datetime import datetime

today_date = datetime.strptime(today_string, "%Y-%m-%d").date()

print(today_date)




import multiprocessing
import time
import random
from datetime import datetime

def print_time():
    time.sleep(random.uniform(0, 1))  
    print(f"{multiprocessing.current_process().name}: {datetime.now()}")
    #sys.stdout.flush()  

if __name__ == "__main__":  
    processes = []
    for _ in range(3):  
        p = multiprocessing.Process(target=print_time)
        p.start()
        processes.append(p)

    for p in processes:
        p.join()  
