# Miles Philips
# Prog 260
# 8/19/19
# An implementation of a binary heap: a reservation system based on a priority queue & order of creation.

from binheap import BinHeap

# create Guest class
class Guest:

    # initialize with atributes name, priority, & insertionOrder
    def __init__(self, name, priority, insertionOrder):
        self.name = name
        self.insertionOrder = insertionOrder
        self.priority = priority

    # define comparitive function
    def __gt__(self,other):
        return (self.priority,self.insertionOrder) > (other.priority, other.insertionOrder)

# define main program
def main():

    # greeting
    print("Welcome to Alice's Restaurant") 
    print("Open everyday except Thanksgiving.")

    # display command list
    print('Enter "a" to add a guest to the waiting list.' )
    print('Enter "s" to remove the next guest from the waiting list once they have been seated.')
    print('Enter "q" to quit.')

    # initialize reservation list & guest tracking number
    reservationList = BinHeap()
    guestnumber = 0

    # get user imput
    command = input("Command: ")
    while command.lower() != "q":

        # add guest
        if command.lower() == "a":
            name = input("Guest name: ")
            priority = input("Guest priority: ")
            guestnumber += 1
            newguest = Guest(name, priority, guestnumber)
            reservationList.insert(newguest)
            print("A reservation for",newguest.name,"has been made.")
            print("They have been assigned a priority of", newguest.priority+".")
            print("They are currently", reservationList._heap.index(newguest), "in line for a table.") 
            command = input("Command: ")

        # get next guest from list
        elif command.lower() == "s":
            serving = reservationList.pop()

            # check if there are guests on list 
            if serving:
                print("Now serving", serving.name)
                command = input("Command: ")

            # warn if no guests on list
            else:
                print("There are no customers on the waiting list")
                command = input("Command: ")

        # control for invalid commands
        elif command.lower() != "a" or "s":
            print("Unrecognised command! Please try again.")
            command = input("Command: ")

    # exit program
    else:
        print("Goodbye!")
        exit()
        
if __name__ == "__main__":
    main()

