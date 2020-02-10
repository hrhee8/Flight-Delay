import numpy as np
import csv

# NEED TO:
# - Handwrite Exercise 1
# - Correct print() statement at end
#   - line 231, in <module>
#     "Is the flight delayed? = " + SFO_ORD_WN )
#     TypeError: can only concatenate str (not "numpy.float64") to str


# # Exercise 1
#
p = 0.5
# m = 4
# z = m*p
#
# seatn = 4
# seatY = 3
# seatN = 1
# ProbSeaY = (seatY + z)/(seatn+m)
# ProbSeaN = (seatN + z)/(seatn+m)
# atln = 3
# atlY = 1
# atlN = 2
# ProbAtlY = (atlY + z)/(atln+m)
# ProbAtlN = (atlN + z)/(atln+m)
# goodn = 3
# goodY = 1
# goodN = 2
# ProbGoodY = (goodY + z)/(goodn+m)
# ProbGoodN = (goodN + z)/(goodn+m)
# swn = 3
# swY = 2
# swN = 1
# ProbswY = (swY + z)/(swn+m)
# ProbswN = (swN + z)/(swn+m)
#
#
# ansY = 0.5*ProbSeaY*ProbAtlY*ProbGoodY*ProbswY
# ansN = 0.5*ProbSeaN*ProbAtlN*ProbGoodN*ProbswN
#
# yhat = numpy.argmax(ansY,ansN)

# Exercise 2

inFile = open("FlightTime.csv","r")

myReader = csv.reader(inFile, delimiter = ",")

n_delay = 0
n_onTime = 0

myData = []

next(myReader)
for line in myReader:
    if int(line[9]) >= 230 and line[5] and line[7]:
        myData.append(line)

for line in myData:
    arr_delay = int(line[6])
    dep_delay = int(line[8])
    total_delay = arr_delay + dep_delay
    line.append(total_delay)
    if total_delay > 15:
        line.append("Y")
        n_delay += 1
    else:
        line.append("N")
        n_onTime += 1

# Exercise 3

carrier = []
origin = []
dest = []

# Set m

m = 3

# Calculate p values

for line in myData:
    if line[0] not in carrier:
        carrier.append(line[0])
    if line[1] not in origin:
        origin.append(line[1])
    if line[2] not in dest:
        dest.append(line[2])

p_c = 1/len(carrier)
p_o = 1/len(origin)
p_d = 1/len(dest)

# Increment n and n_hat values

n_AA, n_AAdelay, n_AAonTime, n_JFKdelay, n_JFKonTime, n_LASdelay, n_LASonTime, n_B6delay, n_B6onTime, n_SFOdelay, n_SFOonTime, n_ORDdelay, n_ORDonTime, n_VXdelay, n_VXonTime, n_WNdelay, n_WNonTime = np.zeros(17)


for line in myData:
    # carrier
    if line[0] == "AA":
        n_AA += 1
        if line[11] == "Y":
            n_AAdelay += 1
        elif line[11] == "N":
            n_AAonTime += 1
    elif line[0] == "B6":
        n_B6 += 1
        if line[11] == "Y":
            n_B6delay += 1
        elif line[11] == "N":
            n_B6onTime += 1
    elif line[0] == "VX":
        n_VX += 1
        if line[11] == "Y":
            n_VXdelay += 1
        elif line[11] == "N":
            n_VXonTime += 1
    elif line[0] == "WN":
        n_WN += 1
        if line[11] == "Y":
            n_WNdelay += 1
        elif line[11] == "N":
            n_WNonTime += 1
    # origin
    if line[1] == "JFK":
        n_JFK += 1
        if line[11] == "Y":
            n_JFKdelay +=1
        elif line[11] == "N":
            n_JFKonTime +=1
    elif line[1] == "SFO":
        n_SFO += 1
        if line[11] == "Y":
            n_SFOdelay +=1
        elif line[11] == "N":
            n_SFOonTime +=1
    # destination
    if line[2] == "LAS":
        n_LAS += 1
        if line[11] == "Y":
            n_LASdelay +=1
        elif line[11] == "N":
            n_LASonTime +=1
    elif line[2] == "ORD":
        n_ORD += 1
        if line[11] == "Y":
            n_ORDdelay += 1
        elif line[11] == "N":
            n_ORDonTime += 1



# if n_JFK != n_JFKdelay + n_JFKonTime:
#     print("Error JFK")

# Calculate constituent probabilities

# (1)
P_JFKgDelay = (n_JFKdelay + m*p_o)/(n_delay + m)
P_JFKgOnTime = (n_JFKonTime + m*p_o)/(n_onTime + m)
P_LASgDelay = (n_LASdelay + m*p_d)/(n_delay + m)
P_LASgOnTime = (n_LASonTime + m*p_d)/(n_onTime + m)
P_AAgDelay = (n_AAdelay + m*p_c)/(n_delay + m)
P_AAgOnTime = (n_AAonTime + m*p_c)/(n_onTime + m)

# (2)
P_B6gDelay = (n_B6delay + m*p_c)/(n_delay + m)
P_B6gOnTime = (n_B6onTime + m*p_c)/(n_onTime + m)

# (3)
P_SFOgDelay = (n_SFOdelay + m*p_o)/(n_delay + m)
P_SFOgOnTime = (n_SFOonTime + m*p_o)/(n_onTime + m)
P_ORDgDelay = (n_ORDdelay + m*p_d)/(n_delay + m)
P_ORDgOnTime = (n_ORDonTime + m*p_d)/(n_onTime + m)
P_VXgDelay = (n_VXdelay + m*p_c)/(n_delay + m)
P_VXgOnTime = (n_VXonTime + m*p_c)/(n_onTime + m)

# (4)
P_WNgDelay = (n_WNdelay + m*p_c)/(n_delay + m)
P_WNgOnTime = (n_WNonTime + m*p_c)/(n_onTime + m)

# Calculate actual P(A|X,Y,Z)

P_JFK_LAS_AA_delay = p*P_JFKgDelay*P_LASgDelay*P_AAgDelay
P_JFK_LAS_AA_onTIme = p*P_JFKgOnTime*P_LASgOnTime*P_AAgOnTime

P_JFK_LAS_B6_delay = p*P_JFKgDelay*P_LASgDelay*P_B6gDelay
P_JFK_LAS_B6_onTIme = p*P_JFKgOnTime*P_LASgOnTime*P_B6gOnTime

P_SFO_ORD_VX_delay = p*P_SFOgDelay*P_ORDgDelay*P_VXgDelay
P_SFO_ORD_VX_onTIme = p*P_SFOgOnTime*P_ORDgOnTime*P_VXgOnTime

P_SFO_ORD_WN_delay = p*P_SFOgDelay*P_ORDgDelay*P_WNgDelay
P_SFO_ORD_WN_onTIme = p*P_SFOgOnTime*P_ORDgOnTime*P_WNgOnTime

# Determine if flight is delayed

if P_JFK_LAS_AA_delay > 0.5:
    JFK_LAS_AA = "Yes"
else:
    JFK_LAS_AA = "No"
if P_JFK_LAS_B6_delay > 0.5:
    JFK_LAS_B6 = "Yes"
else:
    JFK_LAS_B6 = "No"
if P_SFO_ORD_VX_delay > 0.5:
    SFO_ORD_VX = "Yes"
else:
    SFO_ORD_VX = "No"
if P_SFO_ORD_WN_delay > 0.5:
    SFO_ORD_WN = "Yes"
else:
    SFO_ORD_WN = "No"

print(
"P(Y|JFK,LAS,AA) = " + P_JFK_LAS_AA_delay + "\n" +
"P(N|JFK,LAS,AA) = " + P_JFK_LAS_AA_onTime + "\n" +
"Is the flight delayed? = " + JFK_LAS_AA + "\n\n" +
"P(Y|JFK,LAS,B6) = " + P_JFK_LAS_B6_delay + "\n" +
"P(N|JFK,LAS,B6) = " + P_JFK_LAS_B6_onTIme + "\n" +
"Is the flight delayed? = " + JFK_LAS_B6 + "\n\n" +
"P(Y|SFO,ORD,VX) = " + P_SFO_ORD_VX_delay + "\n" +
"P(N|SFO,ORD,VX) = " + P_SFO_ORD_VX_onTIme + "\n" +
"Is the flight delayed? = " + SFO_ORD_VX + "\n\n" +
"P(Y|SFO,ORD,WN) = " + P_SFO_ORD_WN_delay + "\n" +
"P(N|SFO,ORD,WN) = " + P_SFO_ORD_WN_onTIme + "\n" +
"Is the flight delayed? = " + SFO_ORD_WN )