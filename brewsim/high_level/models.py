from django.db import models

class Departement(models.Model):
    numero = models.CharField(max_length=10)
    prix_par_metre_carre = models.DecimalField(max_digits=10, decimal_places=2)

class Recette(models.Model):
    nom = models.CharField(max_length=100)
    actions = models.ManyToManyField('Action')
    
class Action(models.Model):
    machine = models.ForeignKey('Machine', on_delete=models.PROTECT)
    commande = models.CharField(max_length=100)
    duree = models.IntegerField()
    action = models.CharField(max_length=100)
    ingredients = models.ManyToManyField('Ingredient')

class Ingredient(models.Model):
    nom = models.CharField(max_length=100)

class Usine(models.Model):
    departement = models.ForeignKey(Departement, on_delete=models.PROTECT)
    taille = models.DecimalField(max_digits=10, decimal_places=2)
    machines = models.ManyToManyField('Machine')
    stock = models.ForeignKey('QuantiteIngredient', on_delete=models.PROTECT)
    recette_biere = models.ForeignKey(Recette, on_delete=models.PROTECT)

class Machine(models.Model):
    nom = models.CharField(max_length=100)
    prix = models.DecimalField(max_digits=10, decimal_places=2)

class Prix(models.Model):
    ingredients = models.ForeignKey(Ingredient, on_delete=models.PROTECT)
    departement = models.ForeignKey(Departement, on_delete=models.PROTECT)
    prix = models.DecimalField(max_digits=10, decimal_places=2)

class QuantiteIngredient(models.Model):
    ingredient = models.ForeignKey(Ingredient, on_delete=models.CASCADE)
    quantite = models.DecimalField(max_digits=10, decimal_places=2)

