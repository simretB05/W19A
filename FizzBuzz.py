
def num_checker(myNum_list):

    for num in myNum_list:
        if (num%3==0 and num%5==0 ):
         print('FizzBuzz')
        elif(num % 3==0):
          print('Fizz') 
        elif(num %5==0):
              print('Buzz')  
           
myNum_list=[27,83,15,75,95,70,9,31,36,42,27,32,95,39,63]
numberChecked=num_checker(myNum_list)
print(numberChecked)  
















    

