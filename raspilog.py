import os 
from time import sleep, strftime, time
#CPUtemperature                                  
def getCPUtemperature():
    res = os.popen('vcgencmd measure_temp').readline()
    return(res.replace("temp=","").replace("'C\n",""))
# CPU User                               
def getCPUuse():
    return(str(os.popen("top -n1 | awk '/Cpu\(s\):/ {print $2}'").readline().strip(\
)))
def main():
     with open("cpu_temp.csv", "a") as log:
          while True:
              CPU_temp = getCPUtemperature()
              CPU_usage = getCPUuse()
              log.write("{0},{1}\n".format(strftime("%Y-%m-%d %H:%M:%S"),str(CPU_temp),"\n\n"))
			  log.write("{0},{1}\n".format(strftime("%Y-%m-%d %H:%M:%S"),str(CPU_usage),"\n\n"))
              sleep(1)
    
if __name__ == '__main__':
main()

