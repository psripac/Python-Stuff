import math #so i can use math.sqrt for euclidian distance

print("Hello, welcome to the overlapping geometry analysis tool.")

run_again = True #default the user to always run again

while run_again == True: #checks if the user entered "no"

    print("Choose which analysis mode you would like to use.")
    shape_mode = input("(rectangle/circle): ")
    another = "" #records a blank choice until the user types in "yes" or "no" when asked to run again
    
    if shape_mode == "rectangle": #if the user types in rectangle
        #initialized all sides of rectangle A
        ra_left = 0.0
        ra_right = 0.0      
        ra_top = 0.0        
        ra_bottom = 0.0
        #initialized all sides of rectangle B
        rb_left = 0.0       
        rb_right = 0.0
        rb_top = 0.0
        rb_bottom = 0.0

        #gets all the positions of each side from the user for A
        ra_left = input("Enter rectangle A's left coordinate: ")
        ra_right = input("Enter rectangle A's right coordinate: ")
        ra_top = input("Enter rectangle A's top coordinate: ")
        ra_bottom = input("Enter rectangle A's bottom coordinate: ")
        #gets all the positions of each side from the user for B
        rb_left = input("Enter rectangle B's left coordinate: ")
        rb_right = input("Enter rectangle B's right coordinate: ")
        rb_top = input("Enter rectangle B's top coordinate: ")
        rb_bottom = input("Enter rectangle B's bottom coordinate: ")

        #find the coordinates for the center of rectangle A
        ra_center_x = float(ra_left + ra_right) / 2.0
        ra_center_y = float(ra_top + ra_bottom) / 2.0
        #find the coordinates for the center of rectangle B
        rb_center_x = float(ra_left + ra_right) / 2.0
        rb_center_y = float(ra_top + ra_bottom) / 2.0

        #if the rectangles have the same sides
        if ra_left == rb_left and ra_right == rb_right and ra_top == rb_top and ra_bottom == rb_bottom:
            print("The rectangles are the same.")
        elif ra_center_x < rb_center_x:                             #if yes, rectangle A is to the left of B
            if ra_center_y < rb_center_y:                           #if yes, A is to the left and below B
                if ra_right < rb_left:                              #if the right side of A is less than the left side of B
                    if ra_top < rb_bottom:                          #check if the top of A is under the bottom of B
                        print("The rectangles do not overlap.")     #if yes, no overlap
                    else:                                           #or else the rectangles overlap or touch sides
                        print("The rectangles overlap.")
                else:                                               #if the left side of B is less than the right side of A
                    print("The rectangles overlap.")                #then they overlap
            else:                                                   #A is to the left and above B
                if ra_right < rb_left:                              #if the right side of A is less than the left side of B
                    if rb_top < ra_bottom:                          #check if the top of B is under the bottom of A
                        print("The rectangles do not overlap.")     #if yes, no overlap
                    else:                                           #or else the rectangles overlap or touch sides
                        print("The rectangles overlap.")    
                else:                                               #if the left side of B is less than the right side of A
                    print("The rectangles overlap.")                #then they overlap
        else:                                                       #rectangle A is to the right of B
            if ra_center_y < rb_center_y:                           #A is to the right and below B
                if rb_right < ra_left:                              #if the right side of B is less than the left of A
                    if ra_top < rb_bottom:                          #then check if top of A is below bottom of B
                        print("The rectangles do not overlap.")     #if yes, no overlap
                    else:                                           #or else the rectangles overlap or touch sides
                        print("The rectangles overlap.")
                else:                                               #if the left of A is less than the right of B
                    print("The rectangles overlap.")                #then they overlap
            else:                                                   #A is to the right and above B
                if rb_right < ra_left:                              #if the right side of B is less than the left side of A
                    if rb_top < ra_bottom:                          #check if the top of B is below the bottom of A
                        print("The rectangles do not overlap.")     #if yes, no overlap
                    else:                                           #or else the rectangles overlap or touch sides
                        print("The rectangles overlap.")
                else:                                               #if the right side of B is less than the left of A
                    print("The rectangles overlap.")                #then they overlap
            
        
        another = input("Would you like to run another analysis (yes/no)? ") #asks the user to run another analysis
        if another == "yes":        #if user types "yes", run_again is True
            run_again = True
        elif another == "no":       #if user types "no", run_again is False
            run_again = False

    elif shape_mode == "circle":
        #blank circle A
        ca_x = 0.0
        ca_y = 0.0
        ca_rad = 0.0
        #blank circle B
        cb_x = 0.0
        cb_y = 0.0
        cb_rad = 0.0

        #user defined circle A
        ca_x = input("Enter circle A's center's x coordinate: ")
        ca_y = input("Enter circle A's center's y coordinate: ")
        ca_rad = input("Enter circle A's radius: ")
        #user defined circle B
        cb_x = input("Enter circle B's center's x coordinate: ")
        cb_y = input("Enter circle B's center's y coordinate: ")
        cb_rad = input("Enter circle B's radius: ")

        #euclidian distance formula sqrt((x_2 - x_1)^2 + (y_2 - y_1)^2), distance between the circles origins
        distance = math.sqrt(((float(cb_x) - float(ca_x))**2)+((float(cb_y) - float(ca_y))**2))

        if ca_x == cb_x and ca_y == cb_y and ca_rad == cb_rad:  #if the circles have the same origin and radii
            print("The circles are the same.")
        elif (float(ca_rad) + float(cb_rad)) < distance:        #if the circles combined radii is less than the distance
            print("The circles do not overlap.")                #no overlap
        else:                                                   #or if the circles combined radii is equal to or greater
            print("The circles overlap.")                       #than the distance, they overlap

        another = input("Would you like to run another analysis (yes/no)? ")
        if another == "yes":        #if user types "yes", run_again is True
            run_again = True
        elif another == "no":       #if user types "no", run_again is False
            run_again = False

    else:
        print("Sorry, you did not enter a supported mode. Please try again.") #the user enters anything other than rectangle/circle
