avec_soleil=True
en_semaine=False
if avec_soleil and not en_semaine:
    print("on va ala plage")
elif avec_soleil and en_semaine:
    print("on va au travail")
else:
    print("on reste a la maison")