from django.db import models

# Create your models here.


class Departement(models.Model):
    numero = models.IntegerField()
    prixparMcarre = models.IntegerField()

    def __str__(self):
        return f"{self.numero} {self.prixparMcarre}"

    def json(self):
        return {
            "numero": self.numero,
            "prixparMcarre": self.prixparMcarre,
        }

    def json_extended(self):
        return self.json()


class Machine(models.Model):
    nom = models.CharField(max_length=100)
    prix = models.IntegerField()

    def __str__(self):
        return f"{self.nom} {self.prix}"

    def cost(self):
        return self.prix

    def json(self):
        return {
            "nom": self.nom,
            "prix": self.prix,
        }

    def json_extended(self):
        return self.json()

        	


class Ingredient(models.Model):
    nom = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.nom}"

    def json(self):
        return {
            "nom": self.nom,
        }

    def json_extended(self):
        return self.json()
         



class QuantiteIngredient(models.Model):
    ingredient = models.ForeignKey(Ingredient, on_delete=models.PROTECT)
    quantite = models.IntegerField()

    def __str__(self):
        return f"{self.ingredient} {self.quantite}"

    def cost(self, departement):
        return self.ingredient.prix_set.get(departement__numero=departement).prix * self.quantite

    def json(self):
        return {
            "ingredient": self.ingredient,
            "quantite": self.quantite,
        }

    def json_extended(self):
        return self.json()



class Action(models.Model):
    machine = models.ForeignKey(Machine, on_delete=models.PROTECT)
    commande = models.CharField(max_length=100)
    duree = models.IntegerField()
    ingredients = models.ManyToManyField(QuantiteIngredient)
    action = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.machine} {self.commande} {self.duree} {self.ingredients} {self.action}"

    def json(self):
        ingredients_ids = [i.id for i in self.ingredients.all()]
        return {
            "machine": self.machine.id,
            "commande": self.commande,
            "duree": self.duree,
            "ingredients": ingredients_ids,
            "action": self.action,
        }

    def json_extended(self):
        ingredients_json_extended = [i.json_extended() for i in self.ingredients.all()]
        return {
            "machine": self.machine.json_extended(),
            "commande": self.commande,
            "duree": self.duree,
            "ingredients": ingredients_json_extended,
            "action": self.action,
        }


class Recette(models.Model):
        nom = models.CharField(max_length=100)
        action = models.ForeignKey(Action, on_delete=models.PROTECT)
        def __str__(self):
                return f"{self.nom} {self.action}"
        def json(self):                    
                 return {
        		"nom" : self.nom,
        		"action" : self.action,     		  
               		 }
	#def json_extended(self):
      		  #return self.json()                  


class Usine(models.Model):
    departement = models.ForeignKey(Departement, on_delete=models.PROTECT)
    taille = models.IntegerField()
    machines = models.ManyToManyField(Machine)
    recettes = models.ManyToManyField(Recette)
    stocks = models.ManyToManyField(QuantiteIngredient)
    
    def costMachines(self):
        pm = 0
        pi = 0
        for m in self.machines.all():
            pm += m.cost()
        pe = self.departement.prixparMcarre * self.taille
        for n in self.stocks.all():
            pi += n.cost(self.departement.numero)
        total = pm + pe + pi
        return total
    
    def __str__(self):
        return f"{self.departement} {self.taille} {self.machines} {self.recettes} {self.stocks}"
    
    # def cost(self):
    #     return (self.taille * self.departement.prixparMcarre) + (self.costMachines())
    
    def json(self):
        machines_ids = [m.id for m in self.machines.all()]
        recettes_ids = [r.id for r in self.recettes.all()]
        stocks_ids = [s.id for s in self.stocks.all()]

        return {
            "departement": self.departement.id,
            "taille": self.taille,
            "machines": machines_ids,
            "recettes": recettes_ids,
            "stocks": stocks_ids,
        }


    # def json_extended(self):
    #     return self.json()


class Prix(models.Model):
    ingredient = models.ForeignKey(Ingredient, on_delete=models.PROTECT)
    departement = models.ForeignKey(Departement, on_delete=models.PROTECT)
    prix = models.IntegerField()

    def __str__(self):
        return f"{self.ingredient} dans le {self.departement} {self.prix} euros/kg"

    def json(self):
        return {
            "ingredient": self.ingredient,
            "departement": self.departement,
            "prix": self.prix,
        }

    def json_extended(self):
        return self.json()


departement=Departement()
machine=Machine()
ingredient=Ingredient()
quantiteingredient=QuantiteIngredient()
action=Action()
recette=Recette()
usine=Usine()
prix=Prix()
