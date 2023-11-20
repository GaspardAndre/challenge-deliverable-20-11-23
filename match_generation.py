#!/usr/bin/env python3
# -*- coding: utf-8 -*-



import numpy as np
import json
from marc import MarkovChain



with open('/Users/gaspardandre/Documents/challenge-deliverable-20-11-23/data/match_1.json') as mon_fichier:
    match_1 = json.load(mon_fichier)
with open('/Users/gaspardandre/Documents/challenge-deliverable-20-11-23/data/match_2.json') as mon_fichier:
    match_2 = json.load(mon_fichier)

t = 1/50



def generate_match(match_train, duration):
    '''Generate a new football game.

        Parameters
        ----------
        match_train : list, 
            List of dictionaries where each dictionary
            include two keys: norm and label.

        duration : int, 
           Total duration (in seconds) that the user want.

        Returns
        -------
        gen_match : list
            The generated game in the same format as match_train.
        '''
    
    actions_chain = [el["label"] for el in match_train]
    markov = MarkovChain(actions_chain)
    predict_chain = ['walk']
    
    actions_categories = ['shot', 'cross', 'pass', 'rest',
                          'walk', 'run', 'dribble','tackle']
    
    if 'no action' in actions_chain:
        actions_categories.append('no action')
    
    actions_norms = {el:[] for el in actions_categories}
    for action in match_train:
        for category in actions_categories:
            if action['label'] == category:
                actions_norms[category].append(action['norm'])
                
    alphas = {'shot':0.1, 'cross':0.1, 'pass':0.1, 'rest':0.05,
              'walk':0.05, 'run':0.1, 'dribble':0.1,'tackle':0.1}
    
    if 'no action' in actions_chain:
        alphas['no action'] = 0.1
    
    time_spent = 0
    
    predict_match = []
    
    norms_train = actions_norms["walk"]
    ind = np.random.randint(len(norms_train))
    while (t*(len(norms_train[ind])-1)<= 0.1) or (t*
          (len(norms_train[ind])-1) >= 3):
        ind = np.random.randint(len(norms_train))
    noise = np.random.normal(0, alphas["walk"]
    *np.min(norms_train[ind]), len(norms_train[ind]))
    predict_norm = norms_train[ind] + noise

    predict_match.append({'label':"walk", 'norm': list(predict_norm)})

    time_spent += t * (len(norms_train[ind])-1)
    
    while time_spent < duration:
        
        predict_action = markov.next(predict_chain[-1])
        predict_chain.append(predict_action)
        
        
        norms_train = actions_norms[predict_action]
        ind = np.random.randint(len(norms_train))
        while (t*(len(norms_train[ind])-1)<= 0.1) or (t*
              (len(norms_train[ind])-1) >= 3):
            ind = np.random.randint(len(norms_train))
        noise = np.random.normal(0, alphas[predict_action]
        *np.min(norms_train[ind]), len(norms_train[ind]))
        predict_norm = norms_train[ind] + noise
        
        predict_match.append({'label':predict_action,
                              'norm': list(predict_norm)})
        
        time_spent += t * (len(norms_train[ind])-1)
    
    return predict_match





gen_match = generate_match(match_1, 900)      #15 minutes
gen_match_2 = generate_match(match_1, 1800)   #30 minutes
gen_match_3 = generate_match(match_1, 3600)   #60 minutes

gen_match_4 = generate_match(match_2, 900)

match_test = generate_match(match_1, 60)

print([el["label"] for el in match_test])