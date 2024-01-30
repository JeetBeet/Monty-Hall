# -*- coding: utf-8 -*-
"""
Created on Fri Nov 24 14:14:29 2023

@author: Administrator

Monty Hall, with N doors
M goats
and P Rounds

version 0.2

"""



import numpy as np
from argparse import ArgumentParser
from argparse import RawDescriptionHelpFormatter



intro_text=     """ Monty_Hall_N_M_S
    Monte Carlo simulation of  a more universal 
    version of the Monty hall problem.
    
    The Rules of the game are as follows:
    
    There Are N doors, behind M doors there is a price, like a car,
    behind the other ones there is a dummy price like a goat.*
    
    In the first round the candidate chooses a door. 
    The game show host (that knows where the prices are) than opens 
    one door that has a goat behind it
    The candidate than has the option to change their choice or 
    to keep  with the original choice. 
    
    Intuitively most people would expect that changing doors after a goat 
    has been revealed would not change the chances of winning a price. 
    However in 1975 Steve Savant showed that for the case N=3 and M=1
    The chance of winning the car doubles when changing doors after the reveal
    of a goat. An explanation can be found at
    https://en.wikipedia.org/wiki/Monty_Hall_problem
    
    This program checks the outcomes experimentally. The program randomly 
    picks a door, than randomly reveals a goat behind one of the other doors.
    After that one of the remaining doors is randomly choosen.
    
    This proces is repeated S times. At the end it is counted how often
    the first choice selected a price, and how often the second choice
    selected a price.
    
    * which is actually a great price on it's own
    
    """
    


def Easter_Egg(nrofdoor,nrofprices,nrofsamples):
    # Monty Python's Flying Circus" first aired on British 
    # television on October 5, 1969
    
    if (nrofdoors == 11) and (nrofprices == 5 ) and ( nrofsamples == 1969):
    
        Egg_text=('This Monte Carlo simulation of the Monty Hall Problem  ',
              'needs a Monty Python reference.\nWe therefore interrupt this '
              'program to annoy you and make things generally more ',
              'irritating.\n\n')
    
        print(Egg_text)
        input('Press enter to continue')
        


def random_choice_except(values_pool, *except_values_vectors):
    """
    
   randomly chooses a value from a given base set after removal of 
    
    Args:
        values_pool: 1 dim numpy array
            base set of unique values that can be choosen from
            
        except_values_vectors: variable number of 1dim numpy arrays 
            These contain values that should be excluded
            from the original values pool, i.e. values that cannot be drawn.
            The number of drawings equals the length of the 
            except_values_vectors. For each drawing the corresponding elements 
            of all except_values_vectors are removed from the values_pool
                       
            * the length of each vector should be the same,
            * values of the except_values_vectors must be an element in 
              values_pool
            * corresponding elements in the vectors cannot be the same
            
    Returns          
        result_vector, 1 dim numpy array
            contains the randomly choosen values from 
            it has the same length as the except_values_vectors
    
    
    """
    
    nrof_rows = except_values_vectors[0].size
    nrof_cols = values_pool.size  
    nrof_except_vecs = len(except_values_vectors) 
    nrof_remaining_vals =  nrof_cols - nrof_except_vecs     
        
    values_pool_row = values_pool.reshape(1,-1)
    values_pool_matrix = np.tile(values_pool_row,(nrof_rows,1))
    
    values2keep_mask=np.ones((nrof_rows,nrof_cols), dtype=bool)
    
    for except_values_vec in except_values_vectors:
        
         except_values_col = except_values_vec.reshape(-1,1)    
         except_values_matrix=np.tile(except_values_col,(1,nrof_cols))
    
         values2keep_mask[values_pool_matrix == except_values_matrix] = False
    
    
    reduced_values_pool=values_pool_matrix[values2keep_mask].reshape(nrof_rows,
                                                           nrof_remaining_vals)
    
    
    rand_generator = np.random.default_rng()
    
    random_col_indices = rand_generator.integers(low=0, 
                                                 high=nrof_remaining_vals,
                                                 size=nrof_rows)
     
    
    result_vector=reduced_values_pool[np.arange(0,nrof_rows),
                                      random_col_indices]
    
    return result_vector
    




def Monty_hall_NMP_vector(nrofdoors=3, nrofprices=1,  nrofsamples=100000):#nrofrounds
    
   
    """
    Monte Carlo calculation of  a more universal 
    version of the Monty hall problem.
    The Rules of the game are as follows:
    
    There Are N doors, behind M doors   there is a price, like a car,
    behind the other ones there is a dummy price like a goat. *
    
    In the first round the candidate chooses a door. 
    The game show host (that knows where the prices are) than opens 
    one door that has a goat behind it
    The candidate than has the option to chance their choice or 
    to keep  with the original choice. 
    
    This Monte Carlo simulation
    
    
    * which is actually a great price on it's own
    

    """
    
    
    
    # There are N doors and M prices, the prices are always behind the
    # first M doors. This can be done because the candidate's choice is 
    # random. You could also make the placement of the prices random, and than 
    # create a function mapping them to the function placed here. 
    
       
    doors = np.arange(0,nrofdoors) #index to all doors    
    goats = np.arange(nrofprices,nrofdoors) #index to the door with goats

          

    # vertical vector with the first guess of the candidate 
    # each element corresponds with a random sample
    rand_generator = np.random.default_rng()
    
    firstguess = rand_generator.integers(low=0, high=nrofdoors,
                                                 size=nrofsamples)
      
    price_guessed_mask=(firstguess<nrofprices)
    
    
    # the host of the show can only reveal a goat (non-price) that has not
    # been selected by the candidate
    
    goat_revealed=-1*np.ones(firstguess.shape)   #initialisation    
    
    ## first deal with the cases where the candidate selected a price   
    ## in these casse the host can reveal any goat   
    
    goat_revealed_when_price_guessed = np.random.randint(low=nrofprices, 
                                                         high=nrofdoors, 
                                               size=np.sum(price_guessed_mask))    
    goat_revealed[price_guessed_mask] = goat_revealed_when_price_guessed
    
    ## now deal with the cases where the candidate guessed a goat
    ## in this case the host can reveal only one of the remaining goats

    goatsguessed = firstguess[~price_guessed_mask]             
    goat_revealed_when_goat_guessed=random_choice_except(goats, 
                                                   goatsguessed)
    goat_revealed[~price_guessed_mask] = goat_revealed_when_goat_guessed
    
    # after a goat is revealed the candidate gets the chance to 
    # choose another door, for this second guess the candidate cannot
    # choose their previous choice, and also not the revealed goat
       
    second_guess = random_choice_except(doors, firstguess, goat_revealed)
                                                         
    #calculate statistics
    first_guess_wins = (firstguess<nrofprices)    
    perc_firstguess_wins = 100*np.sum(first_guess_wins)/nrofsamples
    
    second_guess_wins = (second_guess < nrofprices)

    perc_secondguess_wins = 100*np.sum(second_guess_wins)/nrofsamples
    
    return nrofdoors, nrofprices, nrofsamples,\
           perc_firstguess_wins, perc_secondguess_wins
         
       
def print_results(nrofdoors, nrofprices, nrofsamples,
                  perc_firstguess_wins, perc_secondguess_wins):
    
    print('Results of Monte Carlo simulation of the Monty Hall Problem with',
          f'{nrofdoors} doors and {nrofprices} after {nrofsamples} samples: \n',
          'percentage of wins without changing doors: ',
          f'{perc_firstguess_wins:.2f} \n',
          'percentage of wins after changing doors  : '
          f'{perc_secondguess_wins:.2f}')


if __name__=='__main__':
    
    # read the inputs from the commandline and 
    # call the function doing the actual work
    
    arg_parser = ArgumentParser(description=intro_text,
                                formatter_class=RawDescriptionHelpFormatter)

    # Define positional arguments
    arg_parser.add_argument('nrofdoors', type=int, nargs='?', default=None, 
                            help='Number of doors')
    arg_parser.add_argument('nrofprices', type=int, nargs='?', default=None,
                            help='Number of prices')
    arg_parser.add_argument('nrofsamples', type=int, nargs='?', default=None,
                            help='Number of times the scenario is played')
    
    args = arg_parser.parse_args()
    
    #only pass the arguments for which a value was given
    keys2pass = {key: value for key, value in vars(args).items()\
                                               if value is not None}
        
    nrofdoors, nrofprices, nrofsamples, perc_firstguess_wins,\
                   perc_secondguess_wins = Monty_hall_NMP_vector(**keys2pass)
                   
    print_results(nrofdoors, nrofprices, nrofsamples,
                      perc_firstguess_wins, perc_secondguess_wins)               
    

