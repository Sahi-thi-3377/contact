def simple_interest(principal,rate,time):
    return((principal*rate*time)/100)
if __name__=="__main__":
    p=1000
    r=5
    t=2
    result=simple_interest(p,r,t)
    print(result)