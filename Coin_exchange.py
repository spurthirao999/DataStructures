#Coin Exchange problem
# c(P)=(1..i)min(c(P-Vi)) + 1
def coin_exchange(coins, val):
    MAX = float('inf')
    #coin_dict={}
    
    coin_val=[MAX for i in range(val + 1)]
    coin_val[0]=0
    for i in range(1, val + 1):
        
        for j in coins:
            
            if (i - j) >= 0:
                coin_val[i]=min(coin_val[i-j]+1,coin_val[i])
                
    print(coin_val[val])
    
   
    
  
coins=[1,2,3,10]
val=27
coin_exchange(coins,val)