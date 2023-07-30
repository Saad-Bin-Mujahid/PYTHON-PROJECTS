# Importing "Numpy" and "Random" library
from numpy import array
import random

#Number or Rows and Coloumns
# 900 variables
n=30

#Initializing array in order to store random generated variables

matrix=array([[0 for i in range(n)]for j in range(n)])

# Colourise - colours text in shell. Returns plain if colour doesn't exist.

def colourise(colour, text):
    if colour == "black":
        return "\033[1;30m" + str(text) + "\033[1;m"
    if colour == "red":
        return "\033[1;31m" + str(text) + "\033[1;m"
    if colour == "green":
        return "\033[1;32m" + str(text) + "\033[1;m"
    if colour == "yellow":
        return "\033[1;33m" + str(text) + "\033[1;m"
    if colour == "blue":
        return "\033[1;34m" + str(text) + "\033[1;m"
    if colour == "magenta":
        return "\033[1;35m" + str(text) + "\033[1;m"
    if colour == "cyan":
        return "\033[1;36m" + str(text) + "\033[1;m"
    if colour == "gray":
        return "\033[1;37m" + str(text) + "\033[1;m"
    return str(text)

# Highlight - highlights text in shell. Returns plain if colour doesn't exist.

def highlight(colour, text):
    if colour == "black":
        return "\033[1;40m" + str(text) + "\033[1;m"
    if colour == "red":
        return "\033[1;41m" + str(text) + "\033[1;m"
    if colour == "green":
        return "\033[1;42m" + str(text) + "\033[1;m"
    if colour == "yellow":
        return "\033[1;43m" + str(text) + "\033[1;m"
    if colour == "blue":
        return "\033[1;44m" + str(text) + "\033[1;m"
    if colour == "magenta":
        return "\033[1;45m" + str(text) + "\033[1;m"
    if colour == "cyan":
        return "\033[1;46m" + str(text) + "\033[1;m"
    if colour == "gray":
        return "\033[1;47m" + str(text) + "\033[1;m"
    return str(text)

# Function to Creating random variables and storing them on the spot in matrix

def triangle(n):
     
    # number of spaces

    k = n - 1
 
    # outer loop to handle number of rows
    
    for i in range(0, n):
     
        # inner loop to handle number spaces
        
        # values changing acc. to requirement
        
        for j in range(0, k):
            matrix[i][j]=0
     
        # decrementing k after each loop
        
        k = k - 1
     
        # inner loop to handle number of columns
        
        # values changing acc. to outer loop
        
        for j in range(0, i+1):
         
            #Creating random variables and storing them on the spot in matrix
            
            matrix[i][j]=random.randint(1,9)
            
# Defining Function namely trianle2 in order to print random generated stored variables in 3 angle triangle form

def triangle2(n):
    
    # number of spaces
    
    k = n - 1
    
    # outer loop to handle number of rows
    
    for i in range(0, n):
        
        # inner loop to handle number spaces
        
        # values changing acc. to requirement
        
        for j in range(0, k):
            
            print(end=" ")
        
        # decrementing k after each loop
        
        k = k - 1
        
        # inner loop to handle number of columns
        
        # values changing acc. to outer loop
        
        for j in range(0, i+1):
            
            # Printing varaibles in colored values
            
            print(colourise("red",(matrix[i][j])),end=" ")
        
        # ending line after each row
        
        print("\r")

# Function to Highlight selected region

#Taking input to select triangle region
row_num=int(input("Insert the number or Row of matrix to select 3 variable triangle: "))
col_num=int(input("Insert the number or Column of matrix to select 3 variable triangle: "))

stored_var_1=0
stored_var_2=0
stored_var_3=0

def highlighted_selected_region(n):
    if(row_num==n or col_num==n or row_num>n or col_num>n or row_num<0 or col_num<0):
        print("\n\nNOTE: PLEASE SELECT ROW AND COLOUMN NUMBER IN RANGE OF MATRIX....")
    else:
        stored_var_1 = matrix[row_num][col_num]
        stored_var_2 = matrix[row_num+1][col_num]
        stored_var_3 = matrix[row_num+1][col_num+1]
        print("\n\nYour selected region is from Matrix Row",row_num,"and Matrix Column",col_num,"and 2 below variables of that selected variable......")
        print("....",stored_var_1,"....")
        print("..",stored_var_2," ",stored_var_3,"..")

#Function for Formula of Heat Measurement
def Heat_Calculation():
    if(row_num==n or col_num==n or row_num>n or col_num>n or row_num<0 or col_num<0):
        print("")
    else:
        Specific_Heat_c=matrix[row_num][col_num]
        Mass_m=matrix[row_num+1][col_num]
        Change_in_Temperature_T=matrix[row_num+1][col_num+1]
        Heat_Q=(Specific_Heat_c)*(Mass_m)*(Change_in_Temperature_T)
        print("\n\nConsidering",Specific_Heat_c,"as Specific Heat....")
        print("Considering",Mass_m,"as Mass....")
        print("Considering",Change_in_Temperature_T,"as Change in Temperature ....")
        print("\n")
        print(colourise("magenta","ANSWER / HEAT / Q CALCULATED IN SELECTED TRIANGULAR REGION IS:-"))
        print(colourise("magenta",Heat_Q))

# Driver Code

# Calling trinagle function in order to create random vairables and store them in matrix 
triangle(n)

# Printing matrix of random generated stored variables
print(colourise("green","\n\nSTORED VARIABLES IN MATRIX:-\n"))
print(matrix)

# Printing random created variables in 3 angles Triangle form
print(colourise("red","\n\nSTORED VARIABLES IN 3 ANGLES TRIANGULAR FORM:-\n"))
triangle2(n)

#Calling function to print selected region
highlighted_selected_region(n)

#Calling function to print calculated heat
Heat_Calculation()
