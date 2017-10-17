import os 
#CPUtemperature                                  
def getCPUtemperature():
    res = os.popen('vcgencmd measure_temp').readline()
    return(res.replace("temp=","").replace("'C\n",""))
# CPU User                               
def getCPUuse():
    return(str(os.popen("top -n1 | awk '/Cpu\(s\):/ {print $2}'").readline().strip(\
)))
def main():
     # CPU
     CPU_temp = getCPUtemperature()
     CPU_usage = getCPUuse()
     #Logging
     f = open("/log.txt","w")
     f.write("CPU Temperature :"""+CPU_temp+"\n\r")
     f.write("\n\r" + "CPU Usage:" +CPU_usage+"%"+"\n\r")
     f.close()	
if __name__ == '__main__':
    main()

