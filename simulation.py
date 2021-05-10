

%matplotlib inline
import numpy as np
import pandas as pd

# curriculum example visualizations
import viz 

np.random.seed(29)

# 1)
# How likely is it that you roll doubles when rolling two dice?

n_trials = nrows = 10_000
n_dice = ncols = 2

rolls = np.random.choice([1, 2, 3, 4, 5, 6], n_trials * n_dice).reshape(nrows, ncols)
rolls

double = [len(np.unique(rolls[n])) for n in range(0, nrows-1) if len(np.unique(rolls[n])) ==1]

chance = len(double) / len(rolls)

chance #16.7% chance

#2) If you flip 8 coins, what is the probability of getting exactly 3 heads? What is the probability of getting more than 3 heads?
sims = rows = 10000
coin_flips = ncols = 8
heads = 1
tails = 0

three_heads = np.random.choice([0, 1], sims * coin_flips).reshape(nrows, ncols)
HHH = three_heads.sum(axis=1)
HHH_prob = (HHH == 3).mean()
HHH_prob # 22.43% chance of getting 3 heads

#3)There are approximitely 3 web development cohorts for every 1 data science cohort at Codeup. Assuming that Codeup randomly selects an alumni to put on a billboard, what are the odds that the two billboards I drive past both have data science students on them?
sims = rows = 10000
adds = ncols = 2
yes = 1
no = 0

billdata = np.random.random(rows, ncols).reshape(rows, ncols)
((billdata < 0.25).sum(axis=1) == 2).mean()
# 6.22%
 


# 4)

# Codeup students buy, on average, 3 poptart packages (+- 1.5) a day from the snack vending machine. If on monday the machine is restocked with 17 poptart packages, how likely is it that I will be able to buy some poptarts on Friday afternoon?
pop_avg = 3
pop_std = 1.5
trials = ncols = 5
simulations =  10000
poptart_trials =  np.random.normal(pop_avg, pop_std, size = (simulations, trials))
prob_poptart = (poptart_trials.sum(axis = 1) <= 16).mean()
prob_poptart

# 61.72%


# 5 Compare Heights
# Men have an average height of 178 cm and standard deviation of 8cm.
# Women have a mean of 170, sd = 6cm.
# If a man and woman are chosen at random, P(woman taller than man)?
m_mean = 178
m_stddev = 8
f_mean = 170
f_stddev = 6

m_height = np.random.normal(m_mean, m_stddev, 10000) 
f_height = np.random.normal(f_mean, f_stddev, 10000)

prob = (f_height > m_height).mean()
prob 
# 21.4 % 


