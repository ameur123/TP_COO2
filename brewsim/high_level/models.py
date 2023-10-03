from django.db import models

class Departement(models.Model):
    numero = models.IntegerField()
    prix_par_mcarre = models.IntegerField()  # Changer le nom du champ pour être conforme aux conventions Python
    def __str__(self):
        return f"{self.numero} {self.prix_par_mcarre}"

class Machine(models.Model):
    nom = models.CharField(max_length=100)
    prix = models.IntegerField()
    def __str__(self):
        return f"{self.nom} {self.prix}"
    def cost(self):
        return self.prix  # Renommer la méthode en "cost" (sans les double underscores)

class Ingredient(models.Model):
    nom = models.CharField(max_length=100)
    def __str__(self):
        return f"{self.nom}"

class QuantiteIngredient(models.Model):
    ingredient = models.ForeignKey(Ingredient, on_delete=models.PROTECT)
    quantite = models.IntegerField()
    def __str__(self):
        return f"{self.ingredient} {self.quantite}"
    def cost(self, departement):
        return self.ingredient.prix_set.get(departement__numero=departement).prix * self.quantite

class Action(models.Model):
    machine = models.ForeignKey(Machine, on_delete=models.PROTECT)
    commande = models.IntegerField()
    duree = models.IntegerField()
    ingredients = models.ManyToManyField(QuantiteIngredient)
    action = models.CharField(max_length=100)
    def __str__(self):
        return f"{self.machine} {self.commande} {self.duree} {self.action}"

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
    
    def costMachines(self):
        total = 0
        for m in self.machines.all():
            total += m.prix
        return total
    
    def __str__(self):
        return f"{self.departement} {self.taille} {self.machines} {self.recettes} {self.stocks}"
    
    def cost(self):
        return (self.taille * self.departement.prix_par_mcarre) + (self.costMachines())

class Prix(models.Model):
    ingredient = models.ForeignKey(Ingredient, on_delete=models.PROTECT)
    departement = models.ForeignKey(Departement, on_delete=models.PROTECT)
    prix = models.IntegerField()
    def __str__(self):
        return f"{self.ingredient} dans le {self.departement} {self.prix} euros/kg"

# Création des objets pour chaque classe
departement = Departement(numero=1, prix_par_mcarre=2000)
departement.save()

machine = Machine(nom="Machine 1", prix=5000)
machine.save()

ingredient = Ingredient(nom="Ingrédient 1")
ingredient.save()

quantiteingredient = QuantiteIngredient(ingredient=ingredient, quantite=10)
quantiteingredient.save()

action = Action(machine=machine, commande=1, duree=30, action="Action 1")
action.save()

recette = Recette(nom="Recette 1", action=action)
recette.save()

usine = Usine(departement=departement, taille=1000)
usine.save()

prix = Prix(ingredient=ingredient, departement=departement, prix=5)
prix.save()

