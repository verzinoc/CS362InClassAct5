#Author: Caden Verzino
#Date: January 30th, 2021
#Class: CS 362 Software Engineering II
#Assignment: Assignment 3
#Program name: caden_verzino_hw3.py
#
#Description: accepts user input of a year, and determines if year is a leap year
#
#How to use: used on OSU flip servers with BASH shell
#	   : run command line "python caden_verzino_hw3.py" 
#	     to execute; the program will ask for input; input is NOT a command line argument



#this function will just output results
def print_no(year):
   print year, "is NOT a leap year."


#this function will just output results
def print_yes(year):
   print year, "is a leap year."


#main function will calculate if year is a leap year
def main():
   user_input = raw_input("Enter your year: ") #GET USER INPUT AS A STRING

   for i in range(len(user_input)):	#FOR EACH CHARACTER IN THE STRING
      if ord(user_input[i]) < 48 or ord(user_input[i]) > 57:	#CHECK IF ASCII VALUES ARE IN BETWEEN 48-57,
	 							#48-57 ARE 0-9 ASCII VALUES
	 print "Invalid input entered. Program ended."
	 quit()							#QUIT IF THERE IS A NON-NUMBER
   
   year = int(user_input)	#COVERT TO TYPE INT TO PERFORM MATHEMATICAL OPERATIONS LATER

   if year < 0: #YEAR IS A NEGATIVE NUMBER, CANT BE LEAP YEAR
      print_no(year)
      quit()

   if (year % 4) == 0: #YEAR IS DIVISIBLE BY 4
      if (year % 100) == 0: #YEAR IS DIVISIBLE BY 100
	 if (year % 400) == 0: #YEAR IS DIVISIBLE BY 400
	    print_yes(year)
	 else:
	    print_no(year) #YEAR IS NOT DIVISIBLE BY 400
      else:
	 print_yes(year) #YEAR IS NOT DIVISIBLE BY 100
   else: #YEAR IS NOT DIVISIBLE BY 4
      print_no(year)


if __name__ == '__main__':
   main()
