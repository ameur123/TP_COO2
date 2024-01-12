from django.test import TestCase

from .models import (
    Action,
    Departement,
    Ingredient,
    Machine,
    Prix,
    QuantiteIngredient,
    Recette,
    Usine,
)

# class MachineModelTests(TestCase):
#    def test_usine_creation(self):
#        self.assertEqual(Machine.objects.count(), 0)
#        Machine.objects.create(nom="four",prix=1_000)
#        self.assertEqual(Machine.objects.count(), 1)


class UsineModelTests(TestCase):
    def test_usine_creation(self):
        self.assertEqual(Usine.objects.count(), 0)
        self.assertEqual(Machine.objects.count(), 0)
        self.assertEqual(Prix.objects.count(), 0)
        self.assertEqual(Departement.objects.count(), 0)
        self.assertEqual(Ingredient.objects.count(), 0)

        four = Machine.objects.create(nom="four", prix=5_000)
        barboteur = Machine.objects.create(nom="barboteur", prix=10_000)
        moul = Machine.objects.create(nom="moul", prix=1_000)
        malt = Ingredient.objects.create(nom="malt")
        avoine = Ingredient.objects.create(nom="avoine")
        orge = Ingredient.objects.create(nom="orge")
        haute_garonne = Departement.objects.create(numero=31, prixparMcarre=100_000)
        strasbourg = Departement.objects.create(numero=67, prixparMcarre=100_000)
        Prix.objects.create(ingredient=avoine, departement=haute_garonne, prix=100)
        Prix.objects.create(ingredient=orge, departement=haute_garonne,prix=20)
        orge50 = QuantiteIngredient.objects.create(ingredient=orge, quantite=30)
        avoine20 = QuantiteIngredient.objects.create(ingredient=avoine, quantite=20)
    

        moulage = Action.objects.create(machine=moul, commande="mouler", duree=30)
        moulage.ingredients.add(avoine20)
        blonde = Recette.objects.create(nom="blonde", action=moulage)

        usine = Usine.objects.create(departement=haute_garonne, taille=100)
        usine2 = Usine.objects.create(departement=strasbourg, taille=100)

        usine.machines.add(four)
        usine.machines.add(barboteur)
        usine.stocks.add(avoine20)
        usine.recettes.add(blonde)

       
        for i in usine.stocks.all():
            print(i)
       

        #usine.rspr(usine.recettes.first(), 10)

        self.assertEqual(Usine.objects.first().costMachines(), 100_17000)

        
        print("Recette = ", usine.recettes.first())
        

        for i in usine.stocks.all():
            print(i)

        print("Prix Usine = ", usine.costMachines())

