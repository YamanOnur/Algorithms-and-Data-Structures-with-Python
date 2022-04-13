#Task-4
def reverse_string(my_string):
    my_string=my_string[::-1]
    return my_string
print(reverse_string(input("Enter a string for Task4:")))
#Task-5 R-1.2
def is_even(k):
    k_as_str=str(k)
    if k_as_str[len(k_as_str)-1] in ["1","3","5","7","9"]:
        return False
    else:return True
print(is_even(input("Enter a number for R-1.2:")))
#R-1.6
def sum_squares_oddPozitives(n):
    sum=0
    for i in range(1,n):
        if i%2==1:
            sum+=i**2
    return sum
print(sum_squares_oddPozitives(int(input("Enter a positive number for R-1.6:"))))
#R-1.7
n=int(input("Enter a positive number for R-1.7:"))
sum=sum([i**2 for i in range(n) if i%2==1])
print(sum)
#R-1.9
lst=[i for i in range(50, 90, 10)]
print("R-1.9:",lst)
#R-1.11
lst=list([2**i for i in range(0,9)])
print("R-1.11:",lst)
#C-1.19
chr_lst=list([chr(i) for i in range(ord("a"),ord("a")+26)])
print("C-1.19:",chr_lst)
#C-1.20
import random
def my_shuffle_function(x):
    index_list=list([i for i in range(len(x))])
    result_list=[]
    while len(index_list)>0:
        r=random.randint(min(index_list),max(index_list))
        if r not in index_list:
            continue
        index_list.remove(r)
        result_list.append(x[r])
    return result_list
print(my_shuffle_function(eval(input("Enter a list for C-1.20\n"
                                     "use the syntax [1,1,1]:"))))
#C-1.28
def p_norm(v):
    p=len(v)
    v=list(v)
    sum_exponent=0
    for i in range(p):
        sum_exponent+=(v[i])**p
    return sum_exponent**(1/p)
print(p_norm(eval(input("Enter a vector as list for C-1.28\n"
                        "use the syntax [1,1,1]:"))))
#Task-6 P-1.35
def birthday_paradox(n):
    count=0
    birthday_list=[]
    for i in range(n):
        birthday_list.append(random.randint(1,365))
    for i in range(n):
        person_birthday=birthday_list.pop(i)
        birthday_list.append(0)
        if person_birthday in birthday_list:
            count+=1
    return count
def birthday_paradox_withMultiples_of_5():
    result_list=[]
    for i in range(1,21):
        result_list.append(birthday_paradox(5*i)/n)
    return result_list
print("Task-6:The probability for n=5,...,100 is:",birthday_paradox_withMultiples_of_5(),"so"
      " the ratio > 1/2 when n>23")
#Task-7
print("Answer to Task_7:","This code gives l2=l1+l2 and then l1=[]")