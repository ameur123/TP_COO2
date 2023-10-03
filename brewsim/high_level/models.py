from django.db import models

# Create your models here.
class Departement(models.Model):
        numero = models.IntegerField()
        prixparMcarre = models.IntegerField()
        def __str__(self):
                return f"{self.numero} {self.prixparMcarre}"

class Machine(models.Model):
        nom = models.CharField(max_length=100)
        prix = models.IntegerField()
        def __str__(self):
                return f"{self.nom} {self.prix}"
        def __cost__(self):
                return self.prix

class Ingredient(models.Model):
        nom = models.CharField(max_length=100)
        def __str__(self):
                return f"{self.nom}"

class QuantiteIngredient(models.Model):
        ingredient = models.ForeignKey(Ingredient, on_delete=models.PROTECT)
        quantite = models.IntegerField()
        def __str__(self):
                return f"{self.ingredient} {self.quantite}"
        def __cost__(self, departement):
                return self.ingredient.prix_set.get(departement__numero=departement).prix * self.quantite

class Action(models.Model):
        machine = models.ForeignKey(Machine, on_delete=models.PROTECT)
        commande = models.IntegerField()
        duree = models.IntegerField()
        ingredients = models.ManyToManyField(QuantiteIngredient)
        action = models.CharField(max_length=100)
        def __str__(self):
                return f"{self.machine} {self.commande} {self.duree} {self.ingredients} {self.action}"

class Recette(models.Model):
        nom = models.CharField(max_length=100)
        action = models.ForeignKey(Action, on_delete=models.PROTECT)
        def __str__(self):
                return f"{self.nom} {self.action}"

class Usine(models.Model):
        departement = models.ForeignKey(Departement, on_delete=models.PROTECT)
        taille = models.IntegerField()
        machines = models.ManyToManyField(Machine)
        recettes = models.ManyToManyField(Recette)
        stocks = models.ManyToManyField(QuantiteIngredient)
        def  costMachines(self):
            total=0
            for m in self.machines.all():
                total= total + m.prix
            return total
        def __str__(self):
                return f"{self.departement} {self.taille} {self.machines} {self.recettes} {self.stocks}"
        def __cost__(self):
                return (self.taille * self.departement.prixparMcarre ) + (self.costMachines())


class Prix(models.Model):
        ingredient = models.ForeignKey(Ingredient, on_delete=models.PROTECT)
        departement = models.ForeignKey(Departement, on_delete=models.PROTECT)
        prix = models.IntegerField()
        def __str__(self):
                return f"{self.ingredient} {self.departement} {self.prix}"

#Création des objets pour chaque classe

departement=Departement()
machine=Machine()
ingredient=Ingredient()
quantiteingredient=QuantiteIngredient()
action=Action()
recette=Recette()
usine=Usine()
prix=Prix()
