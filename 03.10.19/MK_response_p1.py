#1

def common_items():
  first_input = input("Please input a list separated by spaces: ")
  #asking user for list input. Sorry, I couldn't figure out the random list in time. I'll step it up for next week
  first_list = first_input.split()
  second_input = input("Please input another list separated by spaces: ")
  second_list = second_input.split()
  
  common_list = []
  #an empty list generated to store common elements
  
  #comparing the 2 lists with a nested loops
  
 for first_pos in range(0, len(first_list)):
  for second_pos in range(0, len(second_list)):
    if first_list[first_pos]] == second_list[second_pos]:
      common_list.append(first_list[first_pos])

  common_list = list(dict.fromkeys(common_list))
  #turned into a dictionary and back into a list to reduce duplicate values
  common_list.sort()
  #sorting, although this won't actually sort to the best extent... fuck
  
  for i in range(0, len(common_list)):
    try:
      common_list[i] = int(common_list[i])
    except:
      continue
  
  return(common_list)

#2

def palindrome_check():
  initial_response = input("Please input a word or phrase to be checked: ")
  #stores the response by the user
  modified_response = initial_response.strip()
  #ensures that any stray spaces are not counted
  palindrome_status = True
  #sets the status default to True

  #for loop to check each character in the string with the character in its reciprocal index
  for i in range(0,len(modified_response)):
    if modified_response[i] != modified_response[len(modified_response)-1-i]:
      palindrome_status = False
      #if a single letter does not match the entire string is not a palindrome
      break
      #immediately breaks the loop
  
  return(palindrome_status)

#3

def evens_only(list):
  evens_list = []
  #creates a new list to store all even variables

  for i in range(0,len(list)):
    if list[i]%2 == 0:
      evens_list.append(list[i])
      #if a variable from the original list is even then it is added to the end of the even list

  return(evens_list)

#4A

def read_n_lines(filename, num):
	new_file = open(filename)
	#opens a new file with the file name given

	for x in range (0,num):
		print(new_file.readline())
