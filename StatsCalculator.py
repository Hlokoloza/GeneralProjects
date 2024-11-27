import math

def calculate_average():
        user_input=input('input numbers sepearated by space :')
        mylist=[int(i) for i in user_input.split()]
        avarage=sum(mylist)/len(mylist)
        print(f'your avarage is: {avarage}')

def calculate_FiveNumberSummary():
    user_input=input('input your value seperated by a space: ')
    our_list=[int(i) for i in user_input.split()]
    print(our_list)
    our_list=sorted(our_list)
    Q_1=int(0.25*len(our_list))
    Q_2=int(0.5*len(our_list))
    Q_3=int(0.75*len(our_list))

    IQR=our_list[Q_3]-our_list[Q_1]
    semi_IQR=IQR/int(2)
    mid_IQR=(our_list[Q_3]+our_list[Q_1])/int(2)

    print(f'The lower quartile is: {our_list[Q_1]}')
    print(f'The median is: {our_list[Q_2]}')
    print(f'The upper quartile is: {our_list[Q_3]}')
    print(f'The IQR is: {IQR}')
    print(f'The semi-IQR is: {semi_IQR}')
    print(f'The mid-IQR is: {mid_IQR}')

def calculate_measuresOfDispersion():
    user_input=input('input values seperated by space: ')
    mylist=[int(i) for i in user_input.split()]
    mylist=sorted(mylist)

    myrange = max(mylist) - min(mylist)
    print(myrange)

    mean=sum(mylist)/len(mylist)

    squared_values=sum((x-mean)**2 for x in mylist)
    Var=squared_values/len(mylist)
    StD=math.sqrt(Var)

    print(f'The mean of your values is: {mean}')
    print(f'The varience of your values is: {Var}')
    print(f'The standard deviation of your values is: {StD}')

#user_stats=input('input your data: ')
user_choice=input('What would you like to calculate: 1-FiveNumberSummary or 2-measuresOfDispersion ')
if user_choice=='1':
    calculate_FiveNumberSummary()
elif user_choice=='2':
    calculate_measuresOfDispersion()
else:
    print('invalid input!')
