
#rogramme de mot de passe ^^

import random

lower = "abcdefghijklmnopqrstuvwxyz"
upper = "ABCDEFGHIJKLMOPQRSTUVWXYZ"
number = "0123456789"
special = "@#$%&*/\?!"

mdp = lower+upper+number+special
taille = 24

password = "".join(random.sample(mdp, taille))

print (password)