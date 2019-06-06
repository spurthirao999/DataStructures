def reverse_arr_without_splchar(string):
    l=0
    r=len(string)-1
    
    #print(l,r)
    #print(string[0])
    string=list(string)
    
    while(l<r):
        if not string[l].isalpha():
            l+=1
        if not string[r].isalpha():
            r-=1
        else:    
            string[l],string[r]=string[r],string[l]
            l+=1
            r-=1
    str1=''.join(string)
    print(str1)
    

reverse_arr_without_splchar("H^&*ell$o")