'''
Created on Jan 2, 2014

@author: thomas
'''
from game.gametreefactory import GameTreeFactory
from evaluation.evaluator import GameEvaluator

def run_2011_exam_tree():
    print 'Best Move Evaluation for Exam 2011 Tree...'
    GameEvaluator.best_move(GameTreeFactory.get_2011_exam_game_tree())
    print 'Finished!'
    
    print 'Pruning Evaluation for Exam 2011 Tree...'
    GameEvaluator.pruning(GameTreeFactory.get_2011_exam_game_tree())
    print 'Finished'
    
def run_2012_exam_tree():
    print 'Best Move Evaluation for Exam 2012 Tree...'
    GameEvaluator.best_move(GameTreeFactory.get_2012_exam_game_tree())
    print 'Finished!'
    
    print 'Pruning Evaluation for Exam 2012 Tree...'
    GameEvaluator.pruning(GameTreeFactory.get_2012_exam_game_tree())
    print 'Finished'
    
def run_selfmade_test_tree():
    print 'Best Move Evaluation for Selfmade test Tree...'
    GameEvaluator.best_move(GameTreeFactory.get_selfmade_test_tree())
    print 'Finished!'
    
    print 'Pruning Evaluation for Selfmade test Tree...'
    GameEvaluator.pruning(GameTreeFactory.get_selfmade_test_tree())
    print 'Finished'
    
def run_another_mockup_tree():
    print 'Best Move Evaluation for Another Mockup Tree...'
    GameEvaluator.best_move(GameTreeFactory.get_another_mock_game_tree())
    print 'Finished!'
    
    print 'Pruning Evaluation for Another Mockup Tree...'
    GameEvaluator.pruning(GameTreeFactory.get_another_mock_game_tree())
    print 'Finished'

def run_yet_another_mockup_tree():
    print 'Best Move Evaluation for yet Another Mockup Tree...'
    GameEvaluator.best_move(GameTreeFactory.get_yet_another_mock_game_tree())
    print 'Finished!'
    
    print 'Pruning Evaluation for yet Another Mockup Tree...'
    GameEvaluator.pruning(GameTreeFactory.get_yet_another_mock_game_tree())
    print 'Finished'

def run_russel_norvig_tree():
    print 'Best Move Evaluation for Russel/Norvig Tree...'
    GameEvaluator.best_move(GameTreeFactory.get_russel_norvig_example_tree())
    print 'Finished!'
    
    print 'Pruning Evaluation for Russel/Norvig Tree...'
    GameEvaluator.pruning(GameTreeFactory.get_russel_norvig_example_tree())
    print 'Finished'

def main():
    
    #run_2011_exam_tree()
    run_2012_exam_tree()
    #run_selfmade_test_tree()
    #run_another_mockup_tree()
    #run_yet_another_mockup_tree()
    #run_russel_norvig_tree()
    
if __name__ == '__main__':main()
