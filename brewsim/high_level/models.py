from django.db import models

class Departement(models.Model):
    numero = models.CharField(max_length=10)
    prix_par_metre_carre = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return f"Departement {self.numero}"

class Recette(models.Model):
    nom = models.CharField(max_length=100)
    actions = models.ManyToManyField('Action')
    
    def __str__(self):
        return self.nom

class Action(models.Model):
    machine = models.ForeignKey('Machine', on_delete=models.PROTECT)
    commande = models.CharField(max_length=100)
    duree = models.IntegerField()
    action = models.CharField(max_length=100)
    ingredients = models.ManyToManyField('Ingredient')

    def __str__(self):
        return f"Action {self.action}"

class Ingredient(models.Model):
    nom = models.CharField(max_length=100)

    def __str__(self):
        return self.nom

class Usine(models.Model):
    departement = models.ForeignKey(Departement, on_delete=models.PROTECT)
    taille = models.DecimalField(max_digits=10, decimal_places=2)
    machines = models.ManyToManyField('Machine')
    stock = models.ForeignKey('QuantiteIngredient', on_delete=models.PROTECT)
    recette_biere = models.ForeignKey(Recette, on_delete=models.PROTECT)
    

    def __str__(self):
        return f"Usine {self.id}"
        
    def calculate_charge(self):
        # Calcul du prix de charge de l'usine
        prix_machines = sum(machine.get_prix_machine() for machine in self.machines.all())
        prix_stock = self.stock.get_prix_ingredient()
        return prix_machines + prix_stock

class Machine(models.Model):
    nom = models.CharField(max_length=100)
    prix = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return self.nom

class Prix(models.Model):
    ingredients = models.ForeignKey(Ingredient, on_delete=models.PROTECT)
    departement = models.ForeignKey(Departement, on_delete=models.PROTECT)
    prix = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return f"Prix pour {self.ingredients} dans {self.departement}"

class QuantiteIngredient(models.Model):
    ingredient = models.ForeignKey(Ingredient, on_delete=models.CASCADE)
    quantite = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return f"{self.quantite} de {self.ingredient}"
        
    def __str__(self):
        return Prix.objets.get(Departement_numero=Departement,ingredients=self,ingredient),prix * self,quantite 

