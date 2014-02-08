'''
Created on Jan 2, 2014

@author: thomas
'''
class GameEvaluator(object):
    
    @staticmethod
    def pruning(game_tree):
        
        l = game_tree.root.children
        
        game_tree.root.pruned = False
        
        max_score = -1
        best_nodes = list()
        
        alpha = -float('inf')
        beta = float('inf')
        
        for c in l:
            score = GameEvaluator._alphabeta_evaluation(c, False, alpha, beta)
            
            if (score == max_score):
                best_nodes.append(c)
            elif (score > max_score):
                best_nodes = list()
                best_nodes.append(c)
                max_score = score
                alpha = score
        
        stack = list()
        stack.append(game_tree.root)
        print 'Pruned Nodes:'
        while len(stack) > 0:
            node = stack.pop()
            if (node.pruned):
                print node.name
                
            if (len(node.children) > 0):
                stack.extend(node.children)
        
    
    @staticmethod
    def best_move(game_tree):
        
        l = game_tree.root.children
        
        max_score = -1
        best_nodes = list()
        
        for c in l:
            score = GameEvaluator._minimax_evaluation(c, True)
            
            if (score == max_score):
                best_nodes.append(c)
            elif (score > max_score):
                best_nodes = list()
                best_nodes.append(c)
                max_score = score
        
        print 'Found Best Move(s) with score of', max_score
        for n in best_nodes:
            print n
        
    @staticmethod
    def _minimax_evaluation(node, maximise):
        
        evaluation = None
        
        if (node.is_leaf()):
            evaluation = node.value
        else:
            l = node.children
            
            maximise = not maximise
            for n in l:
                score = GameEvaluator._minimax_evaluation(n, maximise)
                
                n.value = score
                
                if (node.value == None): # Dirty check if node has already been evaluated
                    node.value = score
                    evaluation = score
                else: # Actual MiniMax Checking
                    if (n.value > node.value and maximise):
                        node.value = score
                        evaluation = score
                    elif (n.value < node.value and (not maximise)):
                        node.value = score
                        evaluation = score
        
        return evaluation
    
    '''
    Notes:
    -------------------------------
    7.1.2014 (Damn you wikipedia page on alpha-beta pruning...)
    Check for beta <= alpha replaced by beta < alpha:
    
    Consider the case of exam tree 2011, if it would be checked for <= then the transition C -> H would be pruned,
    however this can not be done safely because at that time C is AT MOST 10, meaning, C could still drop, so the value
    of C cannot yet be reported as being 10, hence moving the game to C could turn out to be suboptimal (ie. in case S=7 and R=8)  
    '''
    @staticmethod
    def _alphabeta_evaluation(node, maximise, alpha, beta):
        
        evaluation = None
        
        l = node.children
            
        if (node.is_leaf()):
            evaluation = node.value
        else:
            if (maximise):
                maximise = not maximise
                
                for n in l:
                    score = GameEvaluator._alphabeta_evaluation(n, maximise, alpha, beta)
                
                    n.value = score
                    n.pruned = False
                    if (node.value == None): # Dirty check if node has already been evaluated
                        node.value = score
                        evaluation = score
                        alpha = score
                        node.pruned = False
                    else: # Actual MiniMax Checking
                        if (n.value > node.value):
                            node.value = score
                            evaluation = score
                            alpha = score
                            node.pruned = False
                    
                    # if (beta <= alpha):
                    if (beta < alpha):
                        break    
                
            else:
                maximise = not maximise
                
                for n in l:
                    score = GameEvaluator._alphabeta_evaluation(n, maximise, alpha, beta)
                
                    n.value = score
                    n.pruned = False
                    if (node.value == None): # Dirty check if node has already been evaluated
                        node.value = score
                        evaluation = score
                        node.pruned = False
                        beta = score
                    else: # Actual MiniMax Checking
                        if (n.value < node.value):
                            node.value = score
                            evaluation = score
                            node.pruned = False
                            beta = score
                    
                    #if (beta <= alpha):
                    if (beta < alpha):
                        break 
            
        return evaluation