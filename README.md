# randcase

## Français

### Contenu

Cette bibliothèque fournit une fonction, `rand_switch_case`, qui change
aléatoirement la casse des lettres d'une chaîne de caractères.

### Paramètres

**text (str)**: la chaîne de caractères qui subira des changements de casse
aléatoires

**probability (float)**: la probabilité pour chaque lettre dans `text` de
changer de casse. Elle doit être de 0,0 à 1,0. Par défaut, elle vaut 0,5.

### Ligne de commande

On peut exécuter le module `rand_case.py` en ligne de commande pour voir la
sortie de `rand_switch_case`. Utilisez l'argument `-h` pour obtenir la
description du module et des autres arguments.

```
python rand_case.py -h
```

Exemple d'exécution:

```
python rand_case.py -t "Les chemises de l'archiduchesse sont-elles sèches ou archisèches?" -p 0.7
```

## English

### Content

This library provides one function, `rand_switch_case`, which randomly changes
the case of the letters in a string.

### Parameters

**text (str)**: the string that will undergo random case changes

**probability (float)**: the probability for each letter in `text` to have its
case changed. It must range from 0.0 to 1.0. Defaults to 0.5.

### Command Line

It is possible to execute module `rand_case.py` in command line to see the
output of `rand_switch_case`. Use argument `-h` to obtain the description of
the module and the other arguments.

```
python rand_case.py -h
```

Execution example:

```
python rand_case.py -t "She sells seashells by the seashore." -p 0.7
```
