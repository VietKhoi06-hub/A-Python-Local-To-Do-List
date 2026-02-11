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
        return (f"The content: {self.getContent()}")

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
            self.array[index].setName(name)


    def __str__(self):
        li  = []
        li.append(f"TO-DO-LIST: {self.name}")
        for i in range (len(self.array)):
            li.append(f"{i}. {self.array[i].getContent()}")
        return "\n".join(li)


operator = {":add" : 0, ":remove" : 1, ":tick" : 2, ":rename" : 3, "setFileName" : 4, ":open" : 5, ":close" : 6}


class Interpreter:

    def __init__(self):
        self.to_do_list = List("")
        self.fileName = None
        
    def parser(self, command):
        parse = command.split(" ")
        op = parse[0]
        parse.pop(0)
        execute(op, parse)

    def execute(self, op, li):
        val = operator.get(op)
        match val:
            case 0: #Add a task
                self.to_do_list.addTask(" ".join.li)
            case 1: #Remove a task
                s = "".join.li
                if (s.isnumeric()):
                    self.to_do_list.removeTask(int(s))
                else:
                    print("Invalid operand to remove the task!")
            case 2: #Tick off a Task
                s = "".join.li
                if (s.isnumeric()):
                    self.to_do_list.tickOffTask(int(s))
            case 3: #Rename Task
                idx = li[0]
                li.pop(0)
                s = " ".join(li)
                self.to_do_list.renameTask(idx, s)
            case 4: #setListName
                s = " ".join.li
                self.to_do_list.setName(s)
            case 5:   #Open file
                location = " ".join.li + ".txt"
                self.fileName = location
                with open(location, 'r') as file:
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
                            task.setStatus(status)
                            self.to_do_list.append(task)

            case 6: #Close a file
                fileName = self.fileName
                with open(fileName, 'w') as file:
                    file.write(self.to_do_list.getName() + "\n")
                    for task in self.to_do_list:
                        if (task.getStatus() == False):
                            state = 0
                        else:
                            state = 1
                        file.write(f"{{state} {task.getName()}\n")

            case None:
                print("Unsupported command")


