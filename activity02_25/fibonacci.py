def calc_fibo(index):
   if index == 0:
      return 0
   if index == 1 or index == 2:
      return 1
   current = 2
   left = 0
   right = 1
   result = 0
   while current <= index:
      current += 1
      result = left + right
      left = right
      right = result
   
   return result 

def calc_factorial(num):
   result = num
   num_times = num - 1
   for i in range(num_times):
      num -= num
      result = result * num
   
   return result

