class Tree:
    def __init__(self,height=0):
        self.height = height

    def irrigate(self):
        pass

    def getHeight(self):
        return self.height

class WhitebarkPine(Tree):
    def __init__(self,height=0):
        Tree.__init__(self , height)
        self.height = height

    def irrigate(self):
        self.height += 2


class FoxtailPine(Tree):
    def __init__(self,height=0):
        Tree.__init__(self , height)
        self.height = height
    def irrigate(self):
        self.height += 2

class Lumberjack:
    def canCut(self,tree):
        if tree.height > 4:
            return True
        else:
            return False
        

class Forest:
    def __init__(self):
        self.trees =[]
    
    def add_tree(self,tree):
        self.trees.append(tree)
 
    def rain(self):
        for tree in self.trees:
            tree.irrigate()
    
    def cutTrees(self,lumberjack):
        trees_cut=[]
        for tree in self.trees:
            if lumberjack.canCut(tree):
                trees_cut.append(tree)

        
        for i in trees_cut:
            for tree in self.trees:
                if i == tree:
                    self.trees.remove(tree)
    

    def is_empty(self):
        if len(self.trees) == 0:
            return True
        else:
            return False
    
    def get_status(self):

        for tree in self.trees:
            # tree.__class__.__name__     get the current name of tree
            return f'there is a { tree.height } tall  {tree.__class__.__name__}in the forest'      


   
   
whitebarkPine = WhitebarkPine(3)
# whitebarkPine.irrigate()
foxtailPine = FoxtailPine(4)
# foxtailPine.irrigate()
# lumberjack = Lumberjack()

forest = Forest()
forest.add_tree(whitebarkPine)
forest.add_tree(foxtailPine)
# # forest.rain()
print(forest.get_status())
