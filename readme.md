# Monty_Hall_N_M_S

## General Description

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

## How to use

The module can be used as a library to be used in other software, or be run as
a stand-alone program.

for help on use of the stand-alone program type in terminal or shell:

```
python(.exe) Monty_Hall_N_M_S.py -h
```


Copyright Jethro Betcke 2024
    
    