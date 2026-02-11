#Structure of a task
class Task:
    def __init__(self, content):
        self.content = content
        self.status = False

    def setStatus(self, status):
        if((status == True) or (status == False)):
            self.status = status
        else:
            raise Exception("Task :: Incorrect value to set status!!!")

    def getStatus(self):
        return self.status

    def getContent(self):
        return self.content

    def setContent(self, content):
        self.content = content
    
    def __str__(self):
        return (f"{self.getContent()}")

#Structure of a list
class List:
    def __init__(self, name):
        self.name = name
        self.array = []

    def setName(self, name):
        self.name = name
    
    def getName(self):
        return self.name

    def addTask(self, content):
        t = Task(content)
        self.array.append(t)

    def tickOffTask(self, index):
        if(index >= len(self.array)):
            raise Exception("List :: tickOffTask : Incorrect index!")
        else:
            self.array[index].setStatus(not(self.array[index].getStatus()))
    
    def removeTask(self, index):
        if (index >= len(self.array)):
            raise Exception("List :: removeTask : Incorrect index!")
        else:
            self.array.pop(index)

    def renameTask(self, index, name):
        if (index >= len(self.array)):
            raise Exception("List :: renametask : Incorrect index!")
        else:
            self.array[index].setContent(name)


    def __str__(self):
        li  = []
        li.append("\n\n--------------------------------------------\n\n")
        li.append(f"TO-DO-LIST: {self.name}")
        li.append(f"No. \t Status \t\t Task")
        for i in range (len(self.array)):
            if (self.array[i].getStatus() == False):
                state = "Undone"
            else: 
                state = "Done"
            li.append(f"{i}. \t {state} \t\t {self.array[i].getContent()}") 
        li.append("\n\n--------------------------------------------\n\n")
        return "\n".join(li)

    def getString(self):
        li = []
        li.append(f"{self.getName()}\n")
        for task in self.array:
            if (task.getStatus() == False):
                state = 0
            else:
                state = 1
            li.append(f"{state} {task.getContent()}\n")
        return "".join(li)

operator = {":add" : 0, ":remove" : 1, ":tick" : 2, ":rename" : 3, ":setFileName" : 4, ":open" : 5, ":close" : 6}


class Interpreter:

    def __init__(self):
        self.to_do_list = List("")
        self.fileName = None
        
    def parser(self, command):
        parse = command.split(" ")
        op = parse[0]
        parse.pop(0)
        self.execute(op, parse)

    def execute(self, op, li):
        val = operator.get(op)
        match val:
            case 0: #Add a task
                self.to_do_list.addTask(" ".join(li))
            case 1: #Remove a task
                s = "".join(li)
                if (s.isnumeric()):
                    self.to_do_list.removeTask(int(s))
                else:
                    print("Invalid operand to remove the task!")
            case 2: #Tick off a Task
                s = "".join(li)
                if (s.isnumeric()):
                    self.to_do_list.tickOffTask(int(s))
            case 3: #Rename Task
                idx = li[0]
                if (li[0].isnumeric()):
                    idx = int(li[0])
                else:
                    print("Invalid index to rename Task!")
                    return
                li.pop(0)
                s = " ".join(li)
                self.to_do_list.renameTask(idx, s)
            case 4: #setListName
                s = " ".join(li)
                self.to_do_list.setName(s)
            case 5:   #Open file
                location = "".join(li) + ".txt"
                self.fileName = location
                try:
                    file = open(location, "x")
                except:
                    print(f"NOTE: File {location} already existed")
                else:
                    print(f"NOTE: File {location} has been created")
                    file.close()
                finally:
                    with open(location, "r") as file:
                        counter = 0
                        for line in file:
                            if (counter == 0):
                                self.to_do_list.setName(line.strip())
                                counter += 1
                            else:
                                state = line[0: line.find(" ")]
                                content = line[line.find(" ") + 1:]
                                if (state == "0"):
                                    state = False
                                else:
                                    state = True
                                task = Task(content)
                                task.setStatus(state)
                                self.to_do_list.addTask(task)

            case 6: #Close a file
                fileName = self.fileName
                with open(fileName, 'w') as file:
                    file.write(self.to_do_list.getString())
    
            case None:
                print("NOTE: Unsupported command")
                return
        print(self.to_do_list)    
