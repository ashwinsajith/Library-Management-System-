
def position(): 
    user=input("Admin or Guest?-")
    return user
def startsends_number(passwd):
    if passwd[0] or passwd[-1] in '123456789':
        return True
    else:
        return False
def count_particular(fetch,particular):
    for i in fetch:
        if i[0]==particular:
            return True
            break
    else:
        return False
def whitespace(passwd):
    counter=0
    for i in passwd:
        if i==' ':
            counter=1
    if counter==1:
        return True
    else:
        return False
def leap(year):
    if year%100==0:
        if year%400==0:
            return True
        else:
            return False
    else:
        if year%4==0:
            return True
        else:
            return False
def dayofyear(y,m,d):
    #usage of leap year concept for the month of february through the leap function
    if leap(y)==True:
        if m==1:
            day=d
        elif m==2:
            day=31+d
        elif m==3:
            day=31+29+d
        elif m==4:
            day=31+29+31+d
        elif m==5:
            day=31+29+31+30+d
        elif m==6:
            day=31+29+31+30+31+d
        elif m==7:
            day=31+29+31+30+31+30+d
        elif m==8:
            day=31+29+31+30+31+30+31+d
        elif m==9:
            day=31+29+31+30+31+30+31+31+d
        elif m==10:
            day=31+29+31+30+31+30+31+31+30+d
        elif m==11:
            day=31+29+31+30+31+30+31+31+30+31+d
        elif m==12:
            day=31+29+31+30+31+30+31+31+30+31+30+d        
    else:
        if m==1:
            day=d
        elif m==2:
            day=31+d
        elif m==3:
            day=31+28+d
        elif m==4:
            day=31+28+31+d
        elif m==5:
            day=31+28+31+30+d
        elif m==6:
            day=31+28+31+30+31+d
        elif m==7:
            day=31+28+31+30+31+30+d
        elif m==8:
            day=31+28+31+30+31+30+31+d
        elif m==9:
            day=31+28+31+30+31+30+31+31+d
        elif m==10:
            day=31+28+31+30+31+30+31+31+30+d
        elif m==11:
            day=31+28+31+30+31+30+31+31+30+31+d
        elif m==12:
            day=31+28+31+30+31+30+31+31+30+31+30+d
    return day
