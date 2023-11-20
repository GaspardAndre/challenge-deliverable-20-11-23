# challenge-deliverable-20-11-23
This repository contains the project files due by November 20, 2023

## Requirements

It is necessary to install the ``` marc ``` and ```mchmm``` libraries to correctly run the repository files.

to do this you can use the following commands in a python environment:
```bash
pip install marc
pip install mchmm

```
This repository also uses ```numpy 1.19.5```, ```pandas 0.25.1```and ```matplotlib 3.1.1```.

## Import data
To execute the files it is necessary to import the match json data by replacing "path_to_file" (as in the following cell) with your own path and place it in the corresponding cell of the notebook <https://github.com/GaspardAndre/projet-test/blob/main/Project.ipynb> and in begining of the python file <https://github.com/GaspardAndre/projet-test/blob/main/match_generation.py>:
```bash
with open('path_to_file/match_1.json') as mon_fichier:
    match_1 = json.load(mon_fichier)
with open('path_to_file/match_2.json') as mon_fichier:
    match_2 = json.load(mon_fichier)
```

## Description
The notebook <https://github.com/GaspardAndre/projet-test/blob/main/Project.ipynb> answers the project's questions and the python file <https://github.com/GaspardAndre/projet-test/blob/main/match_generation.py> more specifically contains the python function ```generate_match``` which allows you to generate new match data as requested in the statement. The python file also contains some new game creations from the ```generate_match``` function in the variables ```gen_match```, ```gen_match_2```, ```gen_match_3``` and ```gen_match_4```.



