from django.db import models

class Departement(models.Model):
    numero = models.CharField(max_length=10)
    prix_par_metre_carre = models.CharField(max_digits=10, decimal_places=2)
    
class Recette(models.Model):
    nom = models.CharField(max_length=100)
    actions = models.Foreignkey(Action)
    on_delete=models.PORTECT

class Action(models.Model):
    machine = models.Foreignkey(Machine, on_delete=models.PORTECT)
    commande = models.CharField(max_length=100)
    duree = models.IntegerField()
    action = models.CharField(max_length=100)
    ingerdient = models.ManyToManyFild(Ingredient)

class Ingredient(models.Model):
    nom = models.CharField(max_length=100)
    
    
class Usine(models.Model):
    departement = models.Foreignkey(Departement, on_delete=models.PORTECT)
    taille = models.DecimalField(max_digits=10, decimal_places=2)
    machines = models.Foreignkey(Machine, on_delete=models.PORTECT)
    stock = models.ForeignKey(QuantiteIngredient, on_delete=models.PORTECT)
    recette_biere = models.ForeignKey(Recette, on_delete=models.PORTECT)

class Machine(models.Model):
    nom= models.CharField(max_length=100)
    prix = models.DecimalField(max_digits=10, decimal_places=2)



class Prix(models.Model):
    ingredients = models.Foreignkey(Ingredient, on_delete=models.PORTECT))
    departement = models.ForeignKey(Departement, on_delete=models.PORTECT)
    prix = models.DecimalField(max_digits=10, decimal_places=2)

class QuantiteIngredient(models.Model):
    ingredient = models.ForeignKey(Ingredient, on_delete=models.CASCADE)
    quantite = models.DecimalField(max_digits=10, decimal_places=2)

