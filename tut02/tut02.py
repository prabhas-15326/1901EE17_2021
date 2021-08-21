def get_memory_score(l):  # function returns the score from memory game

    new_list = []  # creates a new list
    i = 0
    # checks whether the list contains integers or not if not it exits
    for i in range(0, len(l)):
        if type(l[i]) != int or l[i]<0 or l[i]>9:
            new_list.append(l[i])
    
    if(len(new_list)!=0):
        print("Please Enter a valid input .Invalid Input detects", new_list)
        exit()
    else:
        # If input is integer then it runs memory game and returns score
        
        l1 = []     #creates a new list to store the integers
        score = 0
        
        for i in range(0, len(l)):

            if l[i] in l1:
                score = score + 1
            else:
                l1.append(l[i])  
            x = len(l1)
            # removes 1st integer if it exceeds maximum of 5 previously calles out numbers
            if x > 5:
                l1.remove(l1[0])
    return score

   

# initial code
input_nums =[7, 5, 8, 6, 3, 5, 9, 7, 9, 7, 5, 6, 4, 1, 7, 4, 6, 5, 8, 9, 4, 8, 3, 0, 3]
print("score", get_memory_score(input_nums))