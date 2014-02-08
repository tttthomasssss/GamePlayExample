'''
Created on Jan 2, 2014

@author: thomas
'''
from gametree import GameNode, GameTree

class GameTreeFactory(object):
    
    @staticmethod
    def get_2011_exam_game_tree():
        
        # Root
        root = GameNode(parent=None, name='A')
        
        # 1st level children
        nodeD = GameNode(parent=root, name='D')
        nodeC = GameNode(parent=root, name='C')
        nodeB = GameNode(parent=root, name='B')
        
        root.add_child(nodeD)
        root.add_child(nodeC)
        root.add_child(nodeB)
        
        #    2nd level children (parent=B)
        nodeG = GameNode(parent=nodeB, name='G')
        nodeF = GameNode(parent=nodeB, name='F')
        nodeE = GameNode(parent=nodeB, name='E')
        
        nodeB.add_child(nodeG)
        nodeB.add_child(nodeF)
        nodeB.add_child(nodeE)
        
        #    2nd level children (parent=C)
        nodeH = GameNode(parent=nodeC, name='H')
        nodeI = GameNode(parent=nodeC, name='I')
        
        nodeC.add_child(nodeI)
        nodeC.add_child(nodeH)
        
        #    2nd level children (parent=D)
        nodeJ = GameNode(parent=nodeD, name='J')
        nodeK = GameNode(parent=nodeD, name='K')
        
        nodeD.add_child(nodeK)
        nodeD.add_child(nodeJ)
        
        #        3rd level children (parent=E)
        nodeL = GameNode(parent=nodeE, value=3, name='L')
        nodeM = GameNode(parent=nodeE, value=1, name='M')
        
        nodeE.add_child(nodeM)
        nodeE.add_child(nodeL)
        
        #        3rd level children (parent=F)
        nodeO = GameNode(parent=nodeF, value=3, name='O')
        nodeN = GameNode(parent=nodeF, value=10, name='N')
        
        nodeF.add_child(nodeO)
        nodeF.add_child(nodeN)
        
        #        3rd level children (parent=G)
        nodeP = GameNode(parent=nodeG, value=9, name='P')
        nodeQ = GameNode(parent=nodeG, value=5, name='Q')
        
        nodeG.add_child(nodeQ)
        nodeG.add_child(nodeP)
        
        #        3rd level children (parent=H)
        nodeR = GameNode(parent=nodeH, value=11, name='R')
        nodeS = GameNode(parent=nodeH, value=14, name='S')
        
        nodeH.add_child(nodeS)
        nodeH.add_child(nodeR)
        
        #        3rd level children (parent=I)
        nodeT = GameNode(parent=nodeI, value=4, name='T')
        nodeU = GameNode(parent=nodeI, value=10, name='U')
        
        nodeI.add_child(nodeU)
        nodeI.add_child(nodeT)
        
        #        3rd level children (parent=J)
        nodeV = GameNode(parent=nodeJ, value=9, name='V')
        nodeW = GameNode(parent=nodeJ, value=17, name='W')
        
        nodeJ.add_child(nodeW)
        nodeJ.add_child(nodeV)
        
        #        3rd level children (parent=K)
        nodeX = GameNode(parent=nodeK, value=8, name='X')
        nodeY = GameNode(parent=nodeK, value=10, name='Y')
        
        nodeK.add_child(nodeY)
        nodeK.add_child(nodeX)
        
        return GameTree(root=root)
    
    @staticmethod
    def get_another_mock_game_tree():
        
        # Root
        root = GameNode(parent=None, name='A')
        
        # 1st level children
        nodeD = GameNode(parent=root, name='D')
        nodeC = GameNode(parent=root, name='C')
        nodeB = GameNode(parent=root, name='B')
        
        root.add_child(nodeD)
        root.add_child(nodeC)
        root.add_child(nodeB)
        
        #    2nd level children (parent=B)
        nodeG = GameNode(parent=nodeB, name='G')
        nodeF = GameNode(parent=nodeB, name='F')
        nodeE = GameNode(parent=nodeB, name='E')
        
        nodeB.add_child(nodeG)
        nodeB.add_child(nodeF)
        nodeB.add_child(nodeE)
        
        #    2nd level children (parent=C)
        nodeH = GameNode(parent=nodeC, name='H')
        nodeI = GameNode(parent=nodeC, name='I')
        
        nodeC.add_child(nodeI)
        nodeC.add_child(nodeH)
        
        #    2nd level children (parent=D)
        nodeJ = GameNode(parent=nodeD, name='J')
        nodeK = GameNode(parent=nodeD, name='K')
        
        nodeD.add_child(nodeK)
        nodeD.add_child(nodeJ)
        
        #        3rd level children (parent=E)
        nodeL = GameNode(parent=nodeE, value=7, name='L')
        nodeM = GameNode(parent=nodeE, value=3, name='M')
        
        nodeE.add_child(nodeM)
        nodeE.add_child(nodeL)
        
        #        3rd level children (parent=F)
        nodeO = GameNode(parent=nodeF, value=12, name='O')
        nodeN = GameNode(parent=nodeF, value=8, name='N')
        
        nodeF.add_child(nodeO)
        nodeF.add_child(nodeN)
        
        #        3rd level children (parent=G)
        nodeP = GameNode(parent=nodeG, value=15, name='P')
        nodeQ = GameNode(parent=nodeG, value=2, name='Q')
        
        nodeG.add_child(nodeQ)
        nodeG.add_child(nodeP)
        
        #        3rd level children (parent=H)
        nodeR = GameNode(parent=nodeH, value=9, name='R')
        nodeS = GameNode(parent=nodeH, value=3, name='S')
        
        nodeH.add_child(nodeS)
        nodeH.add_child(nodeR)
        
        #        3rd level children (parent=I)
        nodeT = GameNode(parent=nodeI, value=11, name='T')
        nodeU = GameNode(parent=nodeI, value=8, name='U')
        
        nodeI.add_child(nodeU)
        nodeI.add_child(nodeT)
        
        #        3rd level children (parent=J)
        nodeV = GameNode(parent=nodeJ, value=5, name='V')
        nodeW = GameNode(parent=nodeJ, value=2, name='W')
        
        nodeJ.add_child(nodeW)
        nodeJ.add_child(nodeV)
        
        #        3rd level children (parent=K)
        nodeX = GameNode(parent=nodeK, value=1, name='X')
        nodeY = GameNode(parent=nodeK, value=4, name='Y')
        
        nodeK.add_child(nodeY)
        nodeK.add_child(nodeX)
        
        return GameTree(root=root)
    
    @staticmethod
    def get_russel_norvig_example_tree():
        
        # Root
        root = GameNode(parent=None, name='A')
        
        # 1st level children
        nodeB = GameNode(parent=root, name='B')
        nodeC = GameNode(parent=root, name='C')
        nodeD = GameNode(parent=root, name='D')
        
        root.add_child(nodeB)
        root.add_child(nodeC)
        root.add_child(nodeD)
        
        #    2nd level children (parent=B)
        nodeE = GameNode(parent=nodeB, name='E', value=3)
        nodeF = GameNode(parent=nodeB, name='F', value=12)
        nodeG = GameNode(parent=nodeB, name='G', value=8)
        
        nodeB.add_child(nodeE)
        nodeB.add_child(nodeF)
        nodeB.add_child(nodeG)
        
        #    2nd level children (parent=C)
        nodeH = GameNode(parent=nodeC, name='H', value=2)
        nodeI = GameNode(parent=nodeC, name='I', value=4)
        nodeJ = GameNode(parent=nodeC, name='J', value=7)
        
        nodeC.add_child(nodeH)
        nodeC.add_child(nodeI)
        nodeC.add_child(nodeJ)
        
        #    2nd level children (parent=D)
        nodeK = GameNode(parent=nodeD, name='K', value=14)
        nodeL = GameNode(parent=nodeD, name='L', value=5)
        nodeM = GameNode(parent=nodeD, name='M', value=2)
        
        nodeD.add_child(nodeK)
        nodeD.add_child(nodeL)
        nodeD.add_child(nodeM)
        
        return GameTree(root=root)
    
    @staticmethod
    def get_yet_another_mock_game_tree():
        
        # Root
        root = GameNode(parent=None, name='A')
        
        # 1st level children
        nodeD = GameNode(parent=root, name='D')
        nodeC = GameNode(parent=root, name='C')
        nodeB = GameNode(parent=root, name='B')
        
        root.add_child(nodeD)
        root.add_child(nodeC)
        root.add_child(nodeB)
        
        #    2nd level children (parent=B)
        nodeG = GameNode(parent=nodeB, name='G')
        nodeF = GameNode(parent=nodeB, name='F')
        nodeE = GameNode(parent=nodeB, name='E')
        
        nodeB.add_child(nodeG)
        nodeB.add_child(nodeF)
        nodeB.add_child(nodeE)
        
        #    2nd level children (parent=C)
        nodeH = GameNode(parent=nodeC, name='H')
        nodeI = GameNode(parent=nodeC, name='I')
        
        nodeC.add_child(nodeI)
        nodeC.add_child(nodeH)
        
        #    2nd level children (parent=D)
        nodeJ = GameNode(parent=nodeD, name='J')
        nodeK = GameNode(parent=nodeD, name='K')
        
        nodeD.add_child(nodeK)
        nodeD.add_child(nodeJ)
        
        #        3rd level children (parent=E)
        nodeL = GameNode(parent=nodeE, value=2, name='L')
        nodeM = GameNode(parent=nodeE, value=2, name='M')
        
        nodeE.add_child(nodeM)
        nodeE.add_child(nodeL)
        
        #        3rd level children (parent=F)
        nodeO = GameNode(parent=nodeF, value=9, name='O')
        nodeN = GameNode(parent=nodeF, value=4, name='N')
        
        nodeF.add_child(nodeO)
        nodeF.add_child(nodeN)
        
        #        3rd level children (parent=G)
        nodeP = GameNode(parent=nodeG, value=8, name='P')
        nodeQ = GameNode(parent=nodeG, value=6, name='Q')
        
        nodeG.add_child(nodeQ)
        nodeG.add_child(nodeP)
        
        #        3rd level children (parent=H)
        nodeR = GameNode(parent=nodeH, value=13, name='R')
        nodeS = GameNode(parent=nodeH, value=11, name='S')
        
        nodeH.add_child(nodeS)
        nodeH.add_child(nodeR)
        
        #        3rd level children (parent=I)
        nodeT = GameNode(parent=nodeI, value=10, name='T')
        nodeU = GameNode(parent=nodeI, value=4, name='U')
        
        nodeI.add_child(nodeU)
        nodeI.add_child(nodeT)
        
        #        3rd level children (parent=J)
        nodeV = GameNode(parent=nodeJ, value=10, name='V')
        nodeW = GameNode(parent=nodeJ, value=16, name='W')
        
        nodeJ.add_child(nodeW)
        nodeJ.add_child(nodeV)
        
        #        3rd level children (parent=K)
        nodeX = GameNode(parent=nodeK, value=9, name='X')
        nodeY = GameNode(parent=nodeK, value=9, name='Y')
        
        nodeK.add_child(nodeY)
        nodeK.add_child(nodeX)
        
        return GameTree(root=root)
    
    @staticmethod
    def get_selfmade_test_tree():
        
        # Root
        root = GameNode(parent=None, name='A')
        
        # 1st level children
        nodeD = GameNode(parent=root, name='D')
        nodeC = GameNode(parent=root, name='C')
        nodeB = GameNode(parent=root, name='B')
        
        root.add_child(nodeD)
        root.add_child(nodeC)
        root.add_child(nodeB)
        
        #    2nd level children (parent=B)
        nodeE = GameNode(parent=nodeB, name='E')
        nodeF = GameNode(parent=nodeB, name='F')
        
        nodeB.add_child(nodeF)
        nodeB.add_child(nodeE)
        
        #    2nd level children (parent=C)
        nodeH = GameNode(parent=nodeC, name='H')
        nodeG = GameNode(parent=nodeC, name='G')
        
        nodeC.add_child(nodeH)
        nodeC.add_child(nodeG)
        
        #    2nd level children (parent=D)
        nodeJ = GameNode(parent=nodeD, name='J')
        nodeI = GameNode(parent=nodeD, name='I')
        
        nodeD.add_child(nodeJ)
        nodeD.add_child(nodeI)
        
        #        3rd level children (parent=E)
        nodeL = GameNode(parent=nodeE, value=11, name='L')
        nodeK = GameNode(parent=nodeE, value=1, name='K')
        
        nodeE.add_child(nodeL)
        nodeE.add_child(nodeK)
        
        #        3rd level children (parent=F)
        nodeN = GameNode(parent=nodeF, value=7, name='N')
        nodeM = GameNode(parent=nodeF, value=4, name='M')
        
        nodeF.add_child(nodeN)
        nodeF.add_child(nodeM)
        
        #        3rd level children (parent=G)
        nodeP = GameNode(parent=nodeG, value=17, name='P')
        nodeO = GameNode(parent=nodeG, value=10, name='O')
        
        nodeG.add_child(nodeP)
        nodeG.add_child(nodeO)
        
        #        3rd level children (parent=H)
        nodeR = GameNode(parent=nodeH, value=11, name='R')
        nodeQ = GameNode(parent=nodeH, value=3, name='Q')
        
        nodeH.add_child(nodeR)
        nodeH.add_child(nodeQ)
        
        #        3rd level children (parent=I)
        nodeT = GameNode(parent=nodeI, value=16, name='T')
        nodeS = GameNode(parent=nodeI, value=9, name='S')
        
        nodeI.add_child(nodeT)
        nodeI.add_child(nodeS)
        
        #        3rd level children (parent=J)
        nodeV = GameNode(parent=nodeJ, value=12, name='V')
        nodeU = GameNode(parent=nodeJ, value=7, name='U')
        
        nodeJ.add_child(nodeV)
        nodeJ.add_child(nodeU)
        
        return GameTree(root=root)
    
    @staticmethod
    def get_2012_exam_game_tree():
        # Root
        root = GameNode(parent=None, name='A')
        
        # 1st level children
        nodeD = GameNode(parent=root, name='D')
        nodeC = GameNode(parent=root, name='C')
        nodeB = GameNode(parent=root, name='B')
        
        root.add_child(nodeD)
        root.add_child(nodeC)
        root.add_child(nodeB)
        
        #    2nd level children (parent=B)
        nodeG = GameNode(parent=nodeB, name='G')
        nodeF = GameNode(parent=nodeB, name='F')
        nodeE = GameNode(parent=nodeB, name='E')
        
        nodeB.add_child(nodeG)
        nodeB.add_child(nodeF)
        nodeB.add_child(nodeE)
        
        #    2nd level children (parent=C)
        nodeH = GameNode(parent=nodeC, name='H')
        nodeI = GameNode(parent=nodeC, name='I')
        
        nodeC.add_child(nodeI)
        nodeC.add_child(nodeH)
        
        #    2nd level children (parent=D)
        nodeJ = GameNode(parent=nodeD, name='J')
        nodeK = GameNode(parent=nodeD, name='K')
        
        nodeD.add_child(nodeK)
        nodeD.add_child(nodeJ)
        
        #        3rd level children (parent=E)
        nodeL = GameNode(parent=nodeE, value=2, name='L')
        nodeM = GameNode(parent=nodeE, value=3, name='M')
        
        nodeE.add_child(nodeM)
        nodeE.add_child(nodeL)
        
        #        3rd level children (parent=F)
        nodeO = GameNode(parent=nodeF, value=5, name='O')
        nodeN = GameNode(parent=nodeF, value=9, name='N')
        
        nodeF.add_child(nodeO)
        nodeF.add_child(nodeN)
        
        #        3rd level children (parent=G)
        nodeP = GameNode(parent=nodeG, value=6, name='P')
        nodeQ = GameNode(parent=nodeG, value=5, name='Q')
        
        nodeG.add_child(nodeQ)
        nodeG.add_child(nodeP)
        
        #        3rd level children (parent=H)
        nodeR = GameNode(parent=nodeH, value=12, name='R')
        nodeS = GameNode(parent=nodeH, value=15, name='S')
        
        nodeH.add_child(nodeS)
        nodeH.add_child(nodeR)
        
        #        3rd level children (parent=I)
        nodeT = GameNode(parent=nodeI, value=5, name='T')
        nodeU = GameNode(parent=nodeI, value=9, name='U')
        
        nodeI.add_child(nodeU)
        nodeI.add_child(nodeT)
        
        #        3rd level children (parent=J)
        nodeV = GameNode(parent=nodeJ, value=11, name='V')
        nodeW = GameNode(parent=nodeJ, value=18, name='W')
        
        nodeJ.add_child(nodeW)
        nodeJ.add_child(nodeV)
        
        #        3rd level children (parent=K)
        nodeX = GameNode(parent=nodeK, value=9, name='X')
        nodeY = GameNode(parent=nodeK, value=13, name='Y')
        
        nodeK.add_child(nodeY)
        nodeK.add_child(nodeX)
        
        return GameTree(root=root)