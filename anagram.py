NO_OF_CHARS=256
def anagram(str1,str2):
    
    count1 =[0] * NO_OF_CHARS
    count2 = [0] * NO_OF_CHARS
    
    if len(str1) != len(str2):
        return False
    
    for i in str1:
        count1[ord(i)]+=1
        
    for i in str2:
        count2[ord(i)]+=1
        
    for i in range(NO_OF_CHARS):
        if count1[i] != count2[i]:
            return False
            
    return True
    
def panagram(str1):
    
     count= [0] * 256
     str1=str1.strip("")
     print(str1)
     
     for i in str1: 
         count[ord(i)]+=1
     
     
         
    
str1="hello"
str2="elloh"

if anagram(str1,str2):
    print(str1,"and",str2,"are anagrams")
else:
    print("Not anagrams")
    
panagram("Hello hui")