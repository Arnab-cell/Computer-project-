import csv
   
def create():
    with open("student.csv", "a") as obj:
        wobj=csv.writer(obj)
        #wobj.writerow(["Student ID","Name","Class Roll Number","Batch Name"])
        while True:
            id=input("Enter Student ID ")
            name=input("Enter Name ")
            roll=input("Enter Class Roll Number ")
            batch=input("Enter Batch Name ")
            record=[id,name,roll,batch]
            wobj.writerow(record)
            ch=input("exit to exit, any other key to continue ")
            if ch=="exit":
                break

def display():
    with open("student.csv", "r") as obj:
        robj=csv.reader(obj)
        for i in robj:
            print(i)

def update():
    with open("student.csv", "r") as obj:
        robj=csv.reader(obj)    
        L=[]
        found=False
        while True:
            fid = input("Enter Student ID ")
            for i in robj:
                if i[0]==fid:
                    found=True
                    nid=input("Enter new Student ID ")
                    name=input("Enter new Name ")
                    roll=input("Enter new Class Roll Number ")
                    batch=input("Enter new Batch Name ")
                    i[0]=nid
                    i[1]=name
                    i[2]=roll
                    i[3]=batch
                else:
                    print("Student not found")
                L.append(i)
            ch = input("exit to exit, any other key to continue ")
            if ch == "exit":
                break

    if found==False:
        print("Student cannot be found")
    else:
        with open("student.csv", "w+", newline="") as obj:
            wobj=csv.writer(obj)
            wobj.writerows(L)
            obj.seek(0)
            robj=csv.reader(obj)
            for i in robj:
                print(i)



#create()
#display()
#update()
