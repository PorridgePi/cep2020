
########################
# Q1 - Circular Primes #
########################

from math import *

#################
# Q1a - Warm Up #
#################

# def rotations(n):
#     result = []
#     n = str(n)
#     if len(n) == 1:
#         if n not in result:
#             result.append(int(n))
#     else:
#         for i in range(len(n)):
#             newstr = n[:i] + n[i+1:]
#             for a in rotations(int(newstr)):
#                 if int(n[i]+str(a)) not in result:
#                     result.append(int(n[i]+str(a)))
#     print(result)
#     return result

def rotations(n):
    result = []
    n = str(n)

    for i in range(len(n)):
        newstr = n[i:] + n[:i] 
        if int(newstr) not in result:
            result.append(int(newstr))
    return result

def test1a():
    print('Q1a')
    print(sorted(rotations(1))==sorted([1]))
    print(sorted(rotations(11))==sorted([11]))
    print(sorted(rotations(101))==sorted([101, 11, 110]))
    print(sorted(rotations(123))==sorted([123, 231, 312]))
    print(sorted(rotations(221))==sorted([221, 212, 122]))
    print(sorted(rotations(1231))==sorted([1231, 2311, 3112, 1123]))
    print(sorted(rotations(1212))==sorted([1212, 2121]))

# test1a()


###############################
# Q1b - Count Circular Primes #
###############################

def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n**0.5)):
        if n % i == 0:
            return False
    return True


def is_prime(n):
    # https://en.wikipedia.org/wiki/Primality_test#Pseudocode

    if n <= 3:
        return n > 1
    elif n % 2 == 0 or n % 3 == 0:
        return False

    i = 5

    while i ** 2 <= n:
        if n % i == 0 or n % (i + 2) == 0:
            return False
        i += 6

    return True


def count_circular_primes(n):
    num = 0
    for i in range(n+1):
        prime = True
        for a in rotations(i):
            if is_prime(a):
                pass
            else:
                prime = False
                break
        if prime:
            num += 1
    return num

def test1b():
    print('Q1b')
    print(count_circular_primes(2)==1)
    print(count_circular_primes(4)==2)
    print(count_circular_primes(13)==6)
    print(count_circular_primes(57)==9)
    print(count_circular_primes(100)==13)

# test1b()

##############################
# Q2 - Tyrion's Flight Mania #
##############################
# DATA Reference : quantquote.com
import csv

def import_csv(filename):
    with open(filename, 'r') as f:
        lines = csv.reader(f, delimiter=',')
        return tuple(lines)

#########################
# Q2a - Get Num Flights #
#########################
def get_num_flights(src, dst, filename):
    data = import_csv(filename)
    num = 0
    for i in data:
        if i[1] == src and i q[2] == dst:
            num += 1
    return num


def test2a():
    print('Q2a')
    print(get_num_flights('VIE','HAM','flight_routes.csv')==1)
    print(get_num_flights('SIN','MNL','flight_routes.csv')==3)
    print(get_num_flights('SIN','HAV','flight_routes.csv')==0)

test2a()

#####################
# Q2b  - Top K Hubs #
#####################

def get_top_k_hubs(k, filename):
    # Write your solution here
    pass

def test2b():
    print('Q2b')
    print(get_top_k_hubs(1,'flight_routes.csv')==[('SIN', 224)])
    print(get_top_k_hubs(2,'flight_routes.csv')==[('SIN', 224), ('MNL', 144)])
    print(get_top_k_hubs(3,'flight_routes.csv')==[('SIN', 224), ('MNL', 144), ('CGN', 134)])
    print(get_top_k_hubs(4,'flight_routes.csv')==[('SIN', 224), ('MNL', 144), ('CGN', 134), ('CTU', 122)])

#test2b()

#######################
# Q2c - Flight Search #
#######################

def search_routes(src, dest, filename, n):
    # Write your solution here
    pass

def test2c():
    print('Q2c')

    def order_not_increasing(lst): # returns True if routes are NOT arranged in increasing order
        curr_size = 0
        for i in lst:
            if curr_size <= len(i):
                curr_size = len(i)
            else:
                return True
        return False

    ans1 = search_routes('LED','NBC','flight_routes.csv',1)
    model_ans1 = [['LED','NBC']]
    ans2 = search_routes('LED','NBC','flight_routes.csv',2)
    model_ans2 = [['LED', 'NBC'], ['LED', 'DME', 'NBC']]
    ans3 = search_routes('LED','NBC','flight_routes.csv',3)
    model_ans3 = [['LED', 'NBC'], ['LED', 'DME', 'NBC'], ['LED', 'KZN', 'DME', 'NBC'], ['LED', 'KZN', 'SVX', 'NBC'], ['LED', 'UUA', 'DME', 'NBC'], ['LED', 'ASF', 'DME', 'NBC'], ['LED', 'SCW', 'SVX', 'NBC'], ['LED', 'OVB', 'SVX', 'NBC'], ['LED', 'DYU', 'DME', 'NBC'], ['LED', 'DYU', 'SVX', 'NBC'], ['LED', 'LBD', 'DME', 'NBC'], ['LED', 'CSY', 'DME', 'NBC'], ['LED', 'MCX', 'DME', 'NBC'], ['LED', 'SKX', 'DME', 'NBC'], ['LED', 'VOZ', 'DME', 'NBC']]

    if order_not_increasing(ans1):
        print(False)
    else:
        print(sorted(ans1)==sorted(model_ans1))
    if order_not_increasing(ans2):
        print(False)
    else:
        print(sorted(ans2)==sorted(model_ans2))
    if order_not_increasing(ans3):
        print(False)
    else:
        print(sorted(ans3)==sorted(model_ans3))

#test2c()


########################
# Q3 - Tech Tree Mania #
########################

class TechTree:
    # Write your solution here
    pass

def test3():
    print("Q3")
    tt = TechTree("civilization")
    tt.add_tech("metal working")
    tt.add_tech("stone working")
    tt.add_tech("bronze working")
    tt.add_tech("iron working")
    tt.add_tech("construction")
    tt.add_tech("mining")
    tt.add_tech("craftsmanship")
    tt.add_dependency("metal working","bronze working")
    tt.add_dependency("bronze working","iron working")
    tt.add_dependency("iron working","construction")
    tt.add_dependency("stone working","mining")
    tt.add_dependency("stone working","craftsmanship")
    tt.add_dependency("craftsmanship","construction")
    tt.add_dependency("stone working","construction")


    print(sorted(tt.get_parents("mining"))==sorted(['stone working']))
    print(sorted(tt.get_ancestors("mining"))==sorted(['stone working']))
    print(sorted(tt.get_parents("construction"))==sorted(['iron working', 'craftsmanship', 'stone working']))
    print(sorted(tt.get_ancestors("construction"))==sorted(['stone working', 'craftsmanship', 'iron working', 'bronze working', 'metal working']))
    print(tt.is_unlocked("stone working")==False)
    print(tt.unlock("stone working")==True)
    print(tt.is_unlocked("stone working")==True)
    print(tt.is_unlocked("construction")==False)
    print(tt.unlock("construction")==False)
    print(tt.is_unlocked("construction")==False)
    print(tt.has_loop()==False)
    tt.add_dependency("construction","stone working")
    print(tt.has_loop()==True)

#test3()
