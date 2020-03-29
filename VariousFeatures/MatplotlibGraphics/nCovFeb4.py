import pyautogui as pg
import matplotlib.pyplot as pyp
import numpy
# import matplotlib as mpl
# import threading
# import keyboard

# import time
distanceResource = {
 "wuhan": 1,            "guangzhou": 980,       "hangzhou": 772,
 "zhenzhou": 510,       "changsha": 346,        "hefei": 378,
 "nanchang": 358,       "chongqin": 867,        "nanjing": 544,
 "qingdao": 1075,       "chengdu": 1132,        "beijing": 1170,
 "shanghai": 828,       "fuzhou": 909,          "xian": 740,
 "guilin": 831,         "haerbin": 2354,        "kunming": 1556,
 "shijiazhuang": 895,   "shenyang": 1811,       "haikou": 1498,
 "taiyuan": 938,        "tianjin": 1151,        "lanzhou": 1359,
 "guiyang": 1041,       "huhehaote": 1381,      "yinchuan": 1424,
 "changchun": 2086,     "wulumuqi": 3268,       "hongkong": 1098,
 "xining": 1579,        "taibei": 1100,         "macau": 1118,
 "lasa": 3484}

patientResource = {
 "wuhan": 13522,        "guangzhou": 813,   "hangzhou": 829,
 "zhenzhou": 675,       "changsha": 593,    "hefei": 480,
 "nanchang": 476,       "chongqin": 344,    "nanjing": 308,
 "jinan": 275,        "chengdu": 282,     "beijing": 228,
 "shanghai": 219,       "fuzhou": 194,      "xian": 142,
 "guilin": 139,         "haerbin": 155,     "kunming": 114,
 "shijiazhuang": 126,   "shenyang": 77,     "haikou": 80,
 "taiyuan": 74,         "tianjin": 66,      "lanzhou": 55,
 "guiyang": 58,         "huhehaote": 35,    "yinchuan": 34,
 "changchun": 42,       "wulumuqi": 29,     "hongkong": 17,
 "xining": 34,          "taibei": 10,       "macau": 10,
 "lasa": 1
}

disRatePatient = numpy.zeros((34,2))

a = [1, 11177]
thelist = [a]

distanceList = list(distanceResource.values())
patientlist = list(patientResource.values())

sortedpati = patientlist

distancePatientDictionary = dict(zip(distanceList, patientlist))
#dictionary of distance and patient counts generated
distanceList.sort()
#x axis is distance, 0 is x
for i in range(33):
    b = list()
    b.append(distanceList[i + 1])
    b.append(distancePatientDictionary.get(distanceList[i + 1]))
    thelist.append(b)
    disRatePatient[i][0] = distanceList[i]
    disRatePatient[i][1] = distancePatientDictionary.get(distanceList[i])
    sortedpati[i] = distancePatientDictionary.get(distanceList[i])
# now the disRatePatient can be used

# pyp.plot(distanceList, sortedpati, 'r')

# pyp.title("constitude")
# pyp.xlabel("distance(Kilometer)")
# pyp.ylabel("patient(person)")

# pyp.show()