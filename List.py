# simple list program
import sys

'''

commands: 
1. help
2. add 
3. remove
4. check index
5. max value
6. min value
7. clear list
8. arrange list
9. remove duplicate items 
10. exit program

'''

list = []

state_clear = True

while True:
  command = input("> ").lower()
  if command == "help":
    print(
      "\nThese are my commands: \n"
      "view - displays the current list\n"
      "add - adds number to the list: \n"
      "rm - removes number from the list\n"
      "chk index - returns the index of the number\n"
      "max - returns the max value from the list\n"
      "min - returns the min value from the list\n"
      "clr - clears the list\n"
      "sort - asks the user for the type of arrangement and does accordingly\n"
      "rm duplicate - duplicate numbers from list\n"
      "exit - exits the program\n"
    )

  elif command == "view":
    if list == []:
      print(f"\nList: {list}")
      print('List is empty\n'
            'use "add" to add values to the list\n')
    else:
      print(f"\nList: {list}\n")
  
  elif command == "add":
    try: 
      add_range = int(input("how many numbers do you want to add: "))
      state_clear = False
      a = 1 
      while a <= add_range:
        try:
          added = int(input(f"| {a} | Enter the value to add to the list: "))
          list.append(added)
          a += 1
        
        except ValueError:
          pass
          print("\n ❗ |Invalid Input| : Please enter a valid number\n")
          

      print(
        "\n✅ number were added\n"
        "the new list is\n"
        f"{list}\n"
      )
    
    except ValueError:
      pass
      print("\n ❗ |Invalid Input| : Please enter a valid number\n")
   
  elif command == "rm":
    if state_clear == True:
      print("\n❗ The list is empty\n")
      continue

    else:
      remove_range = int(input("how many numbers do you want to remove: "))
      r = 1 
      while r<= remove_range:
        removed = int(input("Enter the value to remove from the list: "))
        r += 1
        list.remove(removed)
        print(
        "✅ number was removed\n"
        "the new list is\n"
        f"{list}\n"
        )

  elif command == "rm duplicate":
    if state_clear == True:
      print("\n❗ The list is empty\n")
      continue

    else:
      unique_list = []
      previous_list = list.copy()
      for duplicates in list: 
        if duplicates not in unique_list:
          unique_list.append(duplicates)
      list.clear()
      list = unique_list
      
      print(
        "\n✅ duplicated were removed\n"
        f"previous list = {previous_list}\n"
        "the new list is:\n"
        f"{list}\n"
      )

  elif command == "sort":
    if state_clear == True:
      print("\n❗ The list is empty\n")
      continue

    else:
      type_of_arrangement = input(
        "\nenter\n" 
        "a for assending\n"
        "d for descending: "  
      ).lower()

      if type_of_arrangement == "a":
        list.sort()
        print("\n✅ list was sorted in ascending order\n")
        print(f"{list}\n")
        continue
      
      elif type_of_arrangement == "d":
        list.sort()
        list.reverse()
        print("\n✅ list was sorted in descending order\n")
        print(f"{list}\n")
        continue

      else:
        print("\n❗ Invalid choice\n")
        continue

  elif command == "chk index":
    if state_clear == True:
      print("\n❗ The list is empty\n")
      continue

    else:
      chk_index = int(input("\nEnter the value to see the index of: "))
      
      try:
        found = list.index(chk_index)
        print(
          f"\n🔍 Search Result:\n "
          f"First {chk_index} was found in index [{found}]\n"
        )
        
      except ValueError:
        pass  
        print("The number you searched for was not found in the list\n")
  
  elif command == "max":
    if state_clear == True:
      print("\n❗ The list is empty\n")
      continue
    else:
      print(f"\nMAX: {max(list)}\n")
  
  elif command == "min":
    if state_clear == True:
      print("\n❗ The list is empty\n")
      continue
    else:
      print(f"\nMIN: {min(list)}\n")

  elif command == "clr":
    if state_clear == False:
      print("\n⚠  This will clear the entire list  ⚠\n")
      authorize = input("Do you wish to proceed (y/n): ").lower()
      if authorize == "yes" or authorize == "y":
        list.clear()
        state_clear = True
        print(
          "\n✅ List is now cleared\n"
          f"the new list is {list}\n"
        )
      else:
        print("\nNO action were performed\n")
    else:
      print("\n❗The list is already cleared... NO actions performed\n")
  
  
  elif command == "exit":
    break

  else:
    print(
      "\n⚠ no such commands was found\n"
      "----------------------------\n"
      "Check your spelling\n"
      "DO NOT add space after command\n"
      'Type "help" to see my commands list\n'
    )

