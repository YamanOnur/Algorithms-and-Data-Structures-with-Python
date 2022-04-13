class MazeSolver():
    def __init__(self,path):
        self._maze=self.text_to_array(path)
        self._cellstack=Stack()
        self._explored=list()
    def text_to_array(self,path):
        file=open(path,"r")
        content=[]
        for line in file.readlines():
            line=line.strip("\n")
            line=list(line[l] for l in range(len(line)))
            content.append(line)
        file.close()
        return Maze(content)
    def get_a_neighbor(self,a_tuple):
        lst=self._maze.lst
        row=a_tuple[0]
        col=a_tuple[1]
        if col-1>=0 and (lst[row][col-1]=="O" or lst[row][col-1]=="E") and not (row,col-1) in self._explored:
            return (row,col-1)
        elif row+1<=len(lst)-1 and (lst[row+1][col]=="O" or lst[row+1][col]=="E") and not (row+1,col) in self._explored:
            return (row+1,col)
        elif col+1<=len(lst[0])-1 and (lst[row][col+1]=="O" or lst[row][col+1]=="E") and not (row,col+1) in self._explored:
            return (row,col+1)
        elif row-1>=0 and (lst[row-1][col]=="O" or lst[row-1][col]=="E") and not (row-1,col) in self._explored:
            return (row-1,col)
        else:raise Exception
    def solve_maze(self):
        self._cellstack.push(self._maze.start)
        while not self._cellstack.is_empty():
            c=self._cellstack.top()
            if not c in self._explored:
                self._explored.append(c)
            if c==self._maze.end:
                return str(self._cellstack)
            try:
                c=self.get_a_neighbor(c)
                if not c in self._explored:
                    self._cellstack.push(c)
            except:self._cellstack.pop()
        return [(-1,-1)]

class Maze():
    def __init__(self,lst):
        self.start=None
        self.end=None
        if len(lst)<3:raise Exception("InvalidMazeException")
        for l in range(len(lst)):
            if len(lst[l])<3 or len(lst[l])!=len(lst[0]):raise Exception("InvalidMazeException")
            for k in range(len(lst[l])):
                if not (lst[l][k]=="S" or lst[l][k]=="O" or lst[l][k]=="X" or lst[l][k]=="E"):
                    raise Exception("InvalidMazeExeption")
                if lst[l][k]=="S":
                    self.start=(l,k)
                if lst[l][k]=="E":
                    self.end=(l,k)
        if self.start==None or self.end==None:raise Exception("InvalidMazeException")
        self.lst=lst
    def get_start(self):
        return (self.start[0],self.start[1])
    def get_exit(self):
        return (self.end[0],self.end[1])

class Stack:
    def __init__(self):
        self._data=[]
    def __len__(self):
        return len(self._data)
    def is_empty(self):
        return len(self._data)==0
    def push(self,e):
        self._data.append(e)
    def top(self):
        if self.is_empty():
            raise Exception("Stack is empty")
        return self._data[-1]
    def pop(self):
        if self.is_empty():
            raise Exception("Stack is empty")
        return self._data.pop()
    def __str__(self):
        return str(self._data)
