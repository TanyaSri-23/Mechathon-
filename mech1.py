AnnualDemand = 10000 #Assume Annual demand

def solve():
    Nameofproduct = input()
    
    date = int(input())
    Interestratechargedperunitperyear = int(input())
    Numberofproductionrunsperyear = int(input())

    orderingcost = int(input())
    holdingcost = int(input())
    #Economic Order Quantity(EOQ)(Q*)
    Q = ((2*AnnualDemand*orderingcost)/holdingcost)**0.5
    #optimum lot size(N*)
    N = AnnualDemand/Q
    return Q,N

T = int(input()) #How many products you have 
for case in range(1, T+1):
    print('ProductNo. #{}:(Q, N) = {}'.format(case,solve()))


c = 1
while c != 0:
    print("press 1 if you want to place an order otherwise press 0")
    d = int(input())
    if d == 1:
        c = d
        print("Enter the quantity if order to be placed")
        qu = int(input()) #quantity
        costperitem = int(input())
        total_cost = qu*costperitem
        print(total_cost)

    else:
        c = d
        print("Exit")

