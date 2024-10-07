##FROM YOUTUBE(TELUSKO CHANNEL)
for i in range(4): #i represents the row
    for j in range(4): #j represents the column
         print("# ",end="") #end="" stops the print function to go to the next line.
    print()

##For triangle the number patterns depend on the row(i).
#
##
###
####
for i in range(4): #i represents the row
    for j in range(i+1): #j represents the column
         print("# ",end="")
    print()

##CREATIVE
for i in range(4,-1,-1): #i represents the row
    for j in range(i+1): #j represents the column
         print("# ",end="")
    print()

##PRINTING IT BACKWARDS
print("UPSIDE DOWN TRIANGLE: ")
for i in range(4,-1,-1): #i represents the row
    for j in range(i): #j represents the column
         print("# ",end="")
    print()