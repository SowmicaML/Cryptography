#initializing 5X5 matrix with 0 value
def matrix(x,y,initial):
    return [[initial for i in range(x)] for j in range(y)]

#To find the location of char in the matrix   
def locindex(c): 
    loc=list()
    if c=='J':
        c='I'
    for i ,j in enumerate(my_matrix):
        for k,l in enumerate(j):
            if c==l:
                loc.append(i)
                loc.append(k)
                return loc
 #encrypt function           
def encrypt():  
    msg=str(input("ENTER MSG : "))
    msg=msg.upper()
    msg=msg.replace(" ", "")             
    i=0
    for s in range(0,len(msg)+1,2):
        if s<len(msg)-1:
            if msg[s]==msg[s+1]:
                msg=msg[:s+1]+'Z'+msg[s+1:]
    if len(msg)%2!=0:
        msg=msg[:]+'Z'
    print(msg)
    print("CIPHER TEXT:",end=' ')
    while i<len(msg):
        loc=list()
        loc=locindex(msg[i])
        loc1=list()
        loc1=locindex(msg[i+1])
        #characters in same column
        if loc[1]==loc1[1]: 
            print("{}{}".format(my_matrix[(loc[0]+1)%5][loc[1]],my_matrix[(loc1[0]+1)%5][loc1[1]]),end=' ')
        #characters in same row
        elif loc[0]==loc1[0]:
            print("{}{}".format(my_matrix[loc[0]][(loc[1]+1)%5],my_matrix[loc1[0]][(loc1[1]+1)%5]),end=' ')  
        #characters in diff row and diff column
        else:
            print("{}{}".format(my_matrix[loc[0]][loc1[1]],my_matrix[loc1[0]][loc[1]]),end=' ')    
        i=i+2        
#decrypt function                
def decrypt():  
    msg=str(input("ENTER CIPHER TEXT:"))
    msg=msg.upper()
    msg=msg.replace(" ", "")
    print("PLAIN TEXT:",end=' ')
    i=0
    while i<len(msg):
        loc=list()
        loc=locindex(msg[i])
        loc1=list()
        loc1=locindex(msg[i+1])
         #characters in same column
        if loc[1]==loc1[1]:
            print("{}{}".format(my_matrix[(loc[0]-1)%5][loc[1]],my_matrix[(loc1[0]-1)%5][loc1[1]]),end=' ')
        #characters in same row
        elif loc[0]==loc1[0]:
            print("{}{}".format(my_matrix[loc[0]][(loc[1]-1)%5],my_matrix[loc1[0]][(loc1[1]-1)%5]),end=' ')  
        #characters in diff row and diff column
        else:
            print("{}{}".format(my_matrix[loc[0]][loc1[1]],my_matrix[loc1[0]][loc[1]]),end=' ')    
        i=i+2

        
key=input("Enter key : ")
key=key.replace(" ", "")
key=key.upper()

#Initializing list with key and rest of the alphabets
result=[]
for c in key: 
    if c not in result:
        if c=='J':
            result.append('I')  #I and J are of same frequency
        else:
            result.append(c)

alphabet="ABCDEFGHIKLMNOPQRSTUVWXYZ"
for ch in alphabet: 
    if ch not in result:
        result.append(ch)

           
k=0
my_matrix=matrix(5,5,0)

#Initializing matrix
for i in range(0,5): 
    for j in range(0,5):
        my_matrix[i][j]=result[k]
        k+=1
while(1):
    choice=int(input("\n 1.Encryption \n 2.Decryption: \n 3.EXIT \n Enter Your Choice: "))
    
    if choice==1:
        encrypt()
    elif choice==2:
        decrypt()
    elif choice==3:
        exit()
    else:
        print("Choose correct choice")
