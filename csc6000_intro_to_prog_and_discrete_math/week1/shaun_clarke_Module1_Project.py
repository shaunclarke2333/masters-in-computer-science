
def guess_my_birth_year():
      """
      This function asks the user to enter their age and the present year.
      Then guesses the year they were born
      """
      # Aksing the user for their name, age and current year
      name = input(f"Please Enter Your Name: ").title() # Making sure name is title case
      age = ""
      year = ""

      # making sure age is int or ask user to enter it again.
      while age != int:
            try:
                  if age == "exit":
                        exit 
                  
                  age = int(age)
                  break
            except ValueError:
                  # Asking user to enter age 
                  age = input(f"Please enter your age as a number: ") 


      # making sure year is a is int or ask user to enter again.
      while year != int:
            try:
                  if year == "exit":
                        exit
                  
                  year = int(year)
                  break
            except ValueError:
                  # Asking user to enter year 
                  year = input(f"Please enter the current year as a 4 digit number: ")


      # Narrowing down the birth year by subtracting age
      birth_year = year - age

      # Printing the output to screen
      print("")
      print(f"Dear {name}, you were born in {birth_year - 1} or {birth_year}")


def main():
      # Calling the guess_my_birth_year function
      guess_my_birth_year()


if __name__ == "__main__":
      main()
