f=open("complete.csv")
case={}
for line in f:
    data=line.rstrip("\n").split(",")
    state=data[1]
    confirmed=data[4]
    death=data[5]
    recovered=data[6]
    if state not in case:
        case[state]={"state":state,"confirmed":confirmed,"death":death,"recovered":recovered}
    else:
        case[state] = {"state": state, "confirmed": confirmed, "death": death, "recovered": recovered}

def fetchdata(**kwargs):
    state=kwargs["state"]
    if(state not in case):
        print("State does not exists")
    else:
        #print(case)
        print(case[state]["state"])
    if "para" in kwargs:
        value=kwargs["para"]
        print(case[state][value])

state=input("state")
fetchdata(state=(state),para="death")