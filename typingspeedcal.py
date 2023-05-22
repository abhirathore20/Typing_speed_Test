from time import *
import random as r
def mistake(partest,usertest):
    error = 0
    for i in range(len(partest)):
        try:
            if partest[i]!= usertest[i]:
                error+=1
        except:
            error+=1
    return error

def speed_time(time_s,time_e,userinput):
    time = time_e -time_s
    time_r = round(time,2)
    speed = len(userinput)/time_r
    return round(speed)
    
test = ["The quick brown fox jumps over the lazy dog.","The five boxing wizards jump quickly.",
        "Two driven jocks help fax my big quiz."]
test1 = r.choice(test)
print("**** typing speed ****")
print(test1)
print()
print()
time1 = time()
testinput = input(" Enter : ")
time2 =time()


print('Speed : ',speed_time(time1,time2,testinput),"W/Sec")
print("Error : ", mistake(test1,testinput))