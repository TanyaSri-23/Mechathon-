AnnualDemand = 10000 #Assume Annual demand

def solve():
    Nameofproduct = input()
    quantity = int(input())
    costperitem = int(input())
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


