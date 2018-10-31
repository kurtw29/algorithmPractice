class Node:
    def __init__(self, val):
        self.val = val
        self.next = None
    def length(self):
        if self.next == None:
            return 1
        else:
            return 1 + self.next.length()

class SLL:
    def __init__(self):
        self.head = None

    def addNode(self, value):
        newNode = Node(value)
        if self.head == None:
            self.head = newNode
        else:
            runner = self.head
            while(runner.next != None):
                runner = runner.next
            runner.next = newNode
        return self
    
    def removeNode(self, value):
        if self.head == None:
            return self
        else:
            if(self.head.val == value):
                self.head = self.head.next
            runner = self.head
            if(runner != None):
                while(runner.next != None):
                    if(runner.next.val == value):
                        if(runner.next.next != None):
                            runner = runner.next.next
                        else:
                            runner.next = None
                    else:
                        runner = runner.next
            return self
    def display(self):
        if(self.head == None):
            print("SLL empty")
        else:
            output = "SLL Head--> "
            runner = self.head
            while(runner.next != None):
                output += str(runner.val) + "-->"
                runner = runner.next
            output += str(runner.val)+ "--*"
            print(output)
        return self


    def reverseSLL(self):
        if(self.head == None or self.head.next == None):
            return self
        elif(self.head.next.next == None):
            pointer = self.head
            self.head = self.head.next
            self.head.next = pointer
            point.next = None
            return self
        else:
            p = self.head
            r = self.head.next
            n = self.head.next.next
            self.head.next = None
            while(n.next != None):
                r.next = p
                p = r
                r = n
                n = n.next
            n.next = r
            r.next = p
            self.head = n
            return self





#Testing begings
print("***Testing begin***")
slist = SLL()
slist.addNode(1).addNode(2).addNode(3).display().reverseSLL().display()
slist.removeNode(1).display().removeNode(2).display().removeNode(3).display()
# slist.addNode(4).addNode(5).display()