
from django.db import models

# Create your models here.


class Departement(models.Model):
    numero = models.IntegerField()
    prixm2 = models.IntegerField()

    def __str__(self):
        return f"departement {self.numero}"


class Ingredient(models.Model):
    nom = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.nom}"


class Prix(models.Model):
    ingredient = models.ForeignKey(Ingredient, on_delete=models.PROTECT)
    departement = models.ForeignKey(Departement, on_delete=models.PROTECT)

    prix = models.IntegerField()

    def __str__(self):
        return f"{self.ingredient} dans le {self.departement} {self.prix} euros/kg"


class Machine(models.Model):
    nom = models.CharField(max_length=100)
    prix = models.IntegerField()

    def __str__(self):
        return f"{self.nom}"

    def costs(self):
        return self.prix


class QuantiteIngredient(models.Model):
    ingredient = models.ForeignKey(Ingredient, on_delete=models.PROTECT)
    quantite = models.IntegerField()

    def __str__(self):
        return f"{self.quantite} kg de {self.ingredient}"

    def costs(self, departement):
        return (
            self.quantite
            * self.ingredient.prix_set.get(departement__numero=departement.numero).prix
        )


class Action(models.Model):
    machine = models.ForeignKey(Machine, on_delete=models.PROTECT)
    commande = models.CharField(max_length=100)
    duree = models.IntegerField()
    ingredients = models.ManyToManyField(QuantiteIngredient)
    action = models.ForeignKey(
        "self", on_delete=models.PROTECT, blank=True, null=True, related_name="+"
    )

    def __str__(self):
        return f"{self.commande}"


class Recette(models.Model):
    nom = models.CharField(max_length=100)
    action = models.ForeignKey(Action, on_delete=models.PROTECT)

    def __str__(self):
        return f"{self.nom}"


class Usine(models.Model):
    departement = models.ForeignKey(Departement, on_delete=models.PROTECT)
    taille = models.IntegerField()
    machines = models.ManyToManyField(Machine)
    recettes = models.ManyToManyField(Recette)
    stocks = models.ManyToManyField(QuantiteIngredient)

    def __str__(self):
        return f"Usine de {self.taille} m2"

    def costs(self):
        prix_usine = self.departement.prixm2 * self.taille

        prix_machine = 0
        for machine in self.machines.all():
            prix_machine += machine.prix

        prix_stocks = 0
        for stock in self.stocks.all():
            prix_stocks += stock.costs(self.departement)

        return prix_usine + prix_machine + prix_stocks
