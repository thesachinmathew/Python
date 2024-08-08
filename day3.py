#1st and 2nd max in list
n=[1,3,4,5,6,2]
print(max(n))
second_max=sorted(set(n))[-2]
print(second_max)

#deci to bin
decimal_number=18
binary_number=1010
binary_number = print(decimal_number)
print(binary_number)
decimal_number = print(binary_number, 2)
print(decimal_number) 

#diagonal sum
n= 3*3
matrix = [[1,2,3],[4,5,6],[7,8,9]]
diag_elements = [matrix[i][i] for i in range(len(matrix))]
sum_diagonal=sum(diag_elements)
print(f"Diagonal elements: {diag_elements}, Sum: {sum_diagonal}")

#insert element
arr = [1,2,3]
arr.insert(1,7)
print(arr)

#least and most significant
n=123406
msd,lsd=str(n)[0],str(n)[-1]
print(f"most signifact digit:{msd}, least significant digit:{lsd}")

#min and max
a,b,c=2,5,7
print(max(a,b,c))
print(min(a,b,c))

#merge 2 arrays
arr1=[1,2,3,4,5,6]
arr2=[7,8,9,10,11]
merged=arr1+arr2
print(merged)

#multiplication table
num=4
for i in range(1,11):
    print(num, 'x', i, '=', num*i)

#simple interest
def simple_intrest(p, r=5, t=2):
    return(p*r*t)/100
p=200
print(f"simple intrest:{simple_intrest(p)}")













