import math
import turtle

span=float(input("Enter Total Span of the loaded Beam : "))

UDL_dict={}
if (input("Do you have any UDL Loaded span :  (Y/n): ") == "n"):
    print("There are no UDL loaded span present in the given Beam")
    pass
else:
    UDL_count=int(input("How many UDL  Loaded spans do you have in the Beam : "))
    for i in range(1,UDL_count+1):
        UDL_range=input("Enter The " + str(i) + " UDL span lenght : (format : a-b)")
        UDL_load=float(input("Enter the " + str(i) + " UDL span load "))
        UDL_dict[UDL_range]=UDL_load


UVL_dict={}
if(input("do you have UVL loaded span : (y/n):") == "n"):
    print("There are no UVL loaded span present in the given Beam")
    pass
else:
    UVL_count=int(input("How many UVL Loaded span do you have in the Beam : "))
    for i in range(1,UVL_count+1):
        UVL_range=input("Enter the  "  + str(i) +  "  UVL span lenght:(format : a-b) ")
        UVL_load=float(input("Enter the " + str(i) + " UVL span load "))
        UVL_dict[UVL_range]=UVL_load


UDL_ans={}
def calculate_UDL(udlRange, load):
    w = load
    a, b = udlRange.split('-')
    l = float(b) - float(a)
    ans = (w*(l*l))/8 
    UDL_ans[udlRange] = ans

for udlRange,load in UDL_dict.items():
    calculate_UDL(udlRange,load)

UVL_ans={}
def calculate_UVL(uvlRange,load):
    w = load
    a, b = uvlRange.split('-')
    l = float(b) - float(a)
    ans = (w*l)/(9*math.sqrt(3))
    UVL_ans[uvlRange] = ans


for uvlRange,load in UVL_dict.items():
    calculate_UVL(uvlRange,load)

single_PL_ans={}
def calculate_single_PL(load,entire,first_span):
    entireNew = float(entire.split('-')[1]) - float(entire.split('-')[0])
    first_span = float(first_span.split('-')[1]) - float(first_span.split('-')[0])
    if (entireNew % first_span == 0):
        ans = (load*entireNew)/4
    else:
        ans = (load*first_span*(entireNew-first_span))/entireNew
        
    single_PL_ans[entire] = ans

multiple_PL_ans={}
def calculate_multiple_PL(a,b,entire_mul,F_span_mul,S_span_mul,T_span_mul):
    a = int(a)
    b = int(b)
    E = float(entire_mul.split('-')[1]) - float(entire_mul.split('-')[0])
    F = float(F_span_mul.split('-')[1]) - float(F_span_mul.split('-')[0])
    S = float(S_span_mul.split('-')[1]) - float(S_span_mul.split('-')[0])
    T = float(T_span_mul.split('-')[1]) - float(T_span_mul.split('-')[0])
    ans_1 = ( ((a*(S+T))/E) + ((b*T)/E) )*F 
    ans_2 = ( ((a*F)/E) + ((b*(F+S))/E) )*T
    
    multiple_PL_ans[entire_mul] = [ans_1,ans_2]

# POINT LOAD
Point_dict={}
if input("Do you have any Point loads present in the Beam : (y/n)") == "n":
    print("There are no Point loaded span present in the given Beam")
    pass
else:
    Point_count = int(input("How many Point Loaded spans are present :"))
    for i in range(1,Point_count+1):
        No_PL=int(input("Enter the number of Loads in " + str(i)+ " Point Load span"))
        if No_PL == 1 :
            load=float(input("Enter the Load Value :"))
            entire=input("Enter the lenght of Entire span in (format : a-b) : ")
            first_span=input("Enter the lenght of first span  (format : a-b) :")
            calculate_single_PL(load,entire,first_span)
        else:
            a,b = input("Enter Multiple Loads that are present in the span  in a , b format ").split(",")
            entire_mul = input("Enter the Lenght of Entire span in format (a-b) : ")
            F_span_mul = input("Enter the Lenght of first span in format (a-b) : ")
            S_span_mul = input("Enter the Lenght of second span in format (a-b) : ")
            T_span_mul = input("Enter the Lenght of third span in format (a-b) : ")
            calculate_multiple_PL(a,b,entire_mul,F_span_mul,S_span_mul,T_span_mul)

if ( UDL_ans ):
    print("The answer for the given UDL Loaded values are :- ",UDL_ans)
else:
    pass

if ( UVL_ans ):
    print("The answer for the given UVL Loaded values are :- ",UVL_ans)
else:
    pass

if (single_PL_ans):
    print("The answer for the given single Point loaded span are ",single_PL_ans)
else:
    pass

if (multiple_PL_ans):
    print("The answer for the given multiple Point loaded span are",multiple_PL_ans)
else:
    pass


if (UDL_ans,UVL_ans,single_PL_ans,multiple_PL_ans):
    print("The above are the ansers")
else:
    print("the Beam is not subjected to any kind of loads")
    pass
          
#drawing part


