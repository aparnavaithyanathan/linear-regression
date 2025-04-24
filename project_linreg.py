def file():
    import csv
    f=open('data.csv','w',newline='')
    obj=csv.writer(f)
    while True:
        field1=eval(input("Enter values of field 1:"))
        field2=eval(input("Enter values of field 2:"))
        obj.writerow(field1)
        obj.writerow(field2)
        if len(field1)!=len(field2):
            print('Check your data')
        else:
            break
    f.close()
def simplinreg():
    import csv
    f=open('data.csv','r')
    read=csv.reader(f)
    l=[]
    x=[]
    y=[]
    for i in read:
        l.append(i)
    for value in l[0]:
        j=int(value)
        x.append(j)
    for value in l[1]:
        k=int(value)
        y.append(k)
    f.close()
    n=0
    sumx=0
    sumy=0
    for i,j in zip(x,y):
        n+=1
        sumx+=i
        sumy+=j
    meanx=sumx/n
    meany=sumy/n
#beta coeff
    num=0
    den=0
    for i,j in zip(x,y):
        num+=(i-meanx)*(j-meany)
        den+=(i-meanx)**2
    b1=num/den
    b0=meany-b1*meanx
#predicted y
    y_hats=[]
    errors=[]
    for i,j in zip(x,y):
        yhat=b0+b1*i
        error=j-yhat
        y_hats.append(yhat)
        errors.append(error)
#r square and adjusted r square
    SSE=0
    SSR=0
    SST=0
    for i,j in zip(y,y_hats):
        SSE+=(i-j)**2
        SSR+=(j-meany)**2
        SST+=(i-meany)**2
    r_square=SSR/SST

#f value and residual standard error
    f_value=(SSR/1)/(SSE/(n-2))
    from scipy import stats
    p_value_f=1-stats.f.cdf(f_value,1,(n-2))

#output
    print('\nThe value of beta0         :%.4f'%b0)
    print('\nThe value of beta1         :%.4f'%b1)
    print('\nR square value             :%.4f'%r_square)
    print('\nF statistics value         :%.4f'%f_value)
    print('\nOverall P value            :%.4f'%p_value_f)
    print('\nInterpretation for significance of the model:')
    if p_value_f>0.05:
        print('\nThe model is not significant')
    else:
        print('\nThe model is significant')
if __name__ == "__main__":
    file()
    simplinreg()