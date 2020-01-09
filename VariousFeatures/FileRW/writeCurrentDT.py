import time
import datetime
currentDT=datetime.datetime.now()
log=open("log","w")
log.write(str(currentDT))
log.close()