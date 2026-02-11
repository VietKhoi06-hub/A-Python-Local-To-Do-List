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

    def __str__(self):
        li  = []
        li.append(f"TO-DO-LIST: {self.name}")
        for i in range (len(self.array)):
            li.append(f"{i}. {self.array[i].getContent()}")
        return "\n".join(li)
