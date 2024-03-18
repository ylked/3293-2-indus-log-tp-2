# Industrialisation du logiciel TP 2 - Réponses

## Exercice 1

### b)

#### 1. Quelles étapes (steps) sont réalisées par cette action ?

1. checkout du repository 
2. installation de python, ajout dans le path 
3. installation des dépendances (selon `requirements.txt`) 
4. Linting 
5. Exécution des tests 

#### 2. Une étape est définie au minimum par 2 éléments, lesquels sont-ils et à quoi servent-ils ?

- `uses` permet de déterminer l'action à utiliser 
- `name` (pas obligatoire) permet de déterminer le nom de l'action
- `with` (pas obligatoire) permet de donner les paramètres de l'action 
- `run` permet de déterminer les commandes à lancer 

#### 3. La première étape contient le mot-clé `with`, a quoi sert-il ?

Cela sert à fournir un paramètre à une action. En l'occurrence, on dit à l'action `setup-python` que l'on veut installer la version `3.10` de python. 

## Exercice 2 

### a)

#### 1. Sur l’onglet Summary d’une analyse de code, SonarCloud fournit 4 in- dicateurs. Quels sont-ils et quelles sont leurs utilités ?

#### 2. À quoi sert l’indicateur Quality Gate ?

### b)

#### 1. Quelle est la différence entre les sections New code et Overall Code dans l’onglet Summary ?

#### 2. Y a-t-il des Code Smells ? Si oui, combien et pour quelle(s) raisons(s) ?

#### 3. Y a-t-il des Security Hotspots ? Si oui, combien et pour quelle(s) raison(s) ?

## Exercice 3

### a)

#### 1. Que fait le job pytest ?

#### 2. Que fait le job image-creation ?

#### 3. Que fait le job package-creation ?

#### 4. Dans quel ordre les différents jobs s’executent-ils et pourquoi ?

#### 5. Le stage 2 génère une image Docker. Où est-elle stockée et com- ment pouvez-vous la retrouver ?

#### 6. Le stage 3 génère un wheel Python. Où est-il stocké et comment pouvez-vous le retrouver ?

### c)

#### 1. A quel moment de la pipeline ce job s’execute-t-il et pourquoi ?

#### 2. Que fait le job wheel-testing ?