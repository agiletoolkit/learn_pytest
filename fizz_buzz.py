def buzzy_boy(i):
    
    ret=''
    if(i % 3 ==0):
       ret += 'Fizz'
    if(i % 5 ==0):
        ret += 'Buzz'
    if(ret == ''):
        ret = str(i)    
    
    return ret

