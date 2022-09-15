input_list = []
f = open("crime_scene.txt","r")             #all data in input_list
for line in f:
    input_list.append(line.split())
f.close()

w = int(input_list[0][0])
t = int(input_list[0][1])
n = int(input_list[1][0])
evidences = input_list[2:]

# SOLUTION PART 1
weight_dict={}
time_dict={}
def weight(lst,dct):                        #weight dictionary
    if len(lst) == 0:
        return
    dct[lst[0][0]] = lst[0][1]
    a = lst.pop(0)
    weight(lst[0:], dct)
    lst.insert(0,a)
def time(lst,dct):
    if len(lst) == 0:
        return
    dct[lst[0][0]] = lst[0][2]
    a = lst.pop(0)
    time(lst[0:], dct)
    lst.insert(0,a)
weight(evidences, weight_dict)
time(evidences, time_dict)

weights = list(weight_dict.values())
time = list(time_dict.values())
def weightlimit(weightlim,k):
    if k == n:
        return 0, []
    if weightlim - int(weights[k]) >= 0:           # if he can collect
        totalevidvalue , evidid = weightlimit(weightlim-int(weights[k]), k+1)
        totalevidvalue += int(evidences[k][3])
        evidid.append(int(evidences[k][0]))
    else:                                     #if he cant collect
        totalevidvalue = 0
        evidid = []

    totalvaluenottake, evididnottake = weightlimit(weightlim, k+1)          #not take this evidence
    if totalvaluenottake > totalevidvalue:
        return totalvaluenottake, evididnottake
    else:
        return totalevidvalue, evidid

part1value = (weightlimit(w, 0))[0]
part1list = (weightlimit(w, 0))[1]

#SOLUTION PART 2

def timelimit(timelim, k):
    if k == n:
        return 0, []
    if timelim - int(time[k]) >= 0:  # if he can collect
        timetotvalue, evididtime = timelimit(timelim - int(time[k]), k + 1)
        timetotvalue += int(evidences[k][3])
        evididtime.append(int(evidences[k][0]))
    else:  # if he cant collect
        timetotvalue = 0
        evididtime = []

    timevaluenottake, evididnottime = timelimit(timelim, k + 1)  # not take this evidence
    if timevaluenottake > timetotvalue:
        return timevaluenottake, evididnottime
    else:
        return timetotvalue, evididtime

part2value = (timelimit(t, 0))[0]
part2list = (timelimit(t, 0))[1]

# SOLUTION PART 3

def alllimit(timelim, weightlim, k):
    if k == n:
        return 0, []
    if timelim - int(time[k]) >= 0 and weightlim - int(weights[k]) >= 0:  # if he can collect
        totvalue, evidid = alllimit(timelim - int(time[k]),  weightlim - int(weights[k]), k + 1)
        totvalue += int(evidences[k][3])
        evidid.append(int(evidences[k][0]))
    else:  # if he cant collect
        totvalue = 0
        evidid = []

    valuenottake, evididnot = alllimit(timelim,weightlim, k + 1)  # not take this evidence
    if valuenottake > totvalue:
        return valuenottake, evididnot
    else:
        return totvalue, evidid

part3value = alllimit(t, w, 0)[0]
part3list = alllimit(t, w, 0)[1]

# SORTING IDS
x = 0
def sort_lst(lst):
    global x
    for i in range(len(lst)):
        for k in range(len(lst)-1):
            if (lst[k]>lst[k+1]):
                lst[k],lst[k+1] = lst[k+1],lst[k]
                x += 1
    return lst
part1list=sort_lst(part1list)
part2list=sort_lst(part2list)
part3list=sort_lst(part3list)
#Part 1 writing file
file1=open("solution_part1.txt","w")
file1.write(str(part1value)+"\n")
stri=""
for i in part1list:
    if i==part1list[-1]:
        stri += str(i)
    else:
        stri+= str(i)+" "
file1.write(stri)
file1.close()

#Part 2 writing file
file2=open("solution_part2.txt","w")
file2.write(str(part2value)+"\n")
stri=""
for i in part2list:
    if i==part2list[-1]:
        stri += str(i)
    else:
        stri+= str(i)+" "
file2.write(stri)
file2.close()

#Part 3 writing file
file3=open("solution_part3.txt","w")
file3.write(str(part3value)+"\n")
stri=""
for i in part3list:
    if i==part3list[-1]:
        stri += str(i)
    else:
        stri+= str(i)+" "
file3.write(stri)
file3.close()












