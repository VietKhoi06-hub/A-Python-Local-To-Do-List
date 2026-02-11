import struct

def main():
    interpret = struct.Interpreter()
    print('''
    --------------Welcome to TO-DO-LIST-------------
    Here are the commands:
    :open fileName              : to open a to_do_list which will be saved into the fileName.txt
    :close                      : to close the to_do_list
    :add taskName               : to add a task into the to_do_list
    :rename index newTaskName   : to rename the task at index to the newTaskName
    :remove index               : to remove the task at index
    :tick index                 : to tick off the task at index
    :setFileName fileName       : to setFileName
    -------------------------------------------------
          ''')
    while(True):
        line = input("Please enter the command: ")
        if (line == ":q"):
            print("Thank you for using this product. Any contribution is welcome!!!")
            break
        else:
            interpret.parser(line)




if __name__ == "__main__":
    main()
    
