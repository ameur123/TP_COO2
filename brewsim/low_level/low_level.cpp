#include <iostream>
#include <cstdlib>
#include <cpr/cpr.h>
#include <nlohmann/json.hpp>

using namespace std;
using json = nlohmann::json;

//les classes en c++
class Departement
{
	private:
		int numero;
		int prixparMcarre;

	public:

		Departement(int id)
		{
			cpr::Response r = cpr::Get(cpr::Url{"http://localhost:8000/departement/"+to_string(id)});
			json m = json::parse(r.text);

			numero = m["numero"];
			prixparMcarre = m["prixparMcarre"];
		}

		
};
class Machine
{
	private:
		string nom;
		int prix;

	public:
	
	Machine(int id)
		{
			cpr::Response r = cpr::Get(cpr::Url{"http://localhost:8000/machine/"+to_string(id)});
			json m = json::parse(r.text);

			nom = m["nom"];
			prix = m["prix"];
		}

		

};
class Ingredient
{
	private:
		string nom;

	public:

		Ingredient(int id)
		{
			cpr::Response r = cpr::Get(cpr::Url{"http://localhost:8000/ingredient/"+to_string(id)});
			json m = json::parse(r.text);

			nom = m["nom"];
		}

		

};


class QuantiteIngredient
{
	private:
		unique_ptr<Ingredient> ingredient;
		int quantite;

	public:

		QuantiteIngredient(int id)
		{
			cpr::Response r = cpr::Get(cpr::Url{"http://localhost:8000/quantiteingredient/"+to_string(id)});
			json m = json::parse(r.text);

			ingredient = make_unique<Ingredient>(m["ingredient"]);
			quantite = m["quantite"];
		}
		
};








class Action
{
	private:
		
		unique_ptr<Machine> machine;
		string commande;
		int duree;
		vector<unique_ptr<Ingredient>> ingredients;
		string action;

	public:

		Action(int id)
		{
			int n;

			cpr::Response r = cpr::Get(cpr::Url{"http://localhost:8000/action/"+to_string(id)});
			json m = json::parse(r.text);

			duree = m["duree"];
			machine = make_unique<Machine>(m["machine"]);
			commande = m["commande"];

			for(const auto &i: m["ingredients"])
				ingredients.push_back(make_unique<Ingredient>(i));
			action = m["action"];


		}
		
};


class Recette
{
	private:
	  string nom;
	  unique_ptr<Action> action ;

	public:

		Recette(int id)
		{
			cpr::Response r = cpr::Get(cpr::Url{"http://localhost:8000/recette/"+to_string(id)});
			json m = json::parse(r.text);

			action = make_unique<Action>(m["action"]);
			nom = m["nom"];
		}
		
};

class Usine
{
	private:
		unique_ptr<Departement> departement;
		int t;
		vector<unique_ptr<Machine>> machines;
		vector<unique_ptr<Recette>> recettes;
		vector<unique_ptr<QuantiteIngredient>> stocks;

	public:

		Usine(int id)
		{
			cpr::Response r = cpr::Get(cpr::Url{"http://localhost:8000/usine/"+to_string(id)});
			json m = json::parse(r.text);

			departement = make_unique<Departement>(m["departement"]);
			t = m["taille"];

			for(const auto i: m["machines"])
				machines.push_back(make_unique<Machine>(i));

			for(const auto i: m["recettes"])
				recettes.push_back(make_unique<Recette>(i));

			for(const auto i: m["stocks"])
				stocks.push_back(make_unique<QuantiteIngredient>(i));



		}
		
};

class Prix
{
	private:
		unique_ptr<Ingredient> ingredient;
		unique_ptr<Departement> departement;
		int prix;

	public:

		Prix(int id)
		{
			cpr::Response r = cpr::Get(cpr::Url{"http://localhost:8000/prix/"+to_string(id)});
			json m = json::parse(r.text);

			ingredient = make_unique<Ingredient>(m["ingredient"]);
			departement = make_unique<Departement>(m["departement"]);
			prix = m["prix"];
		}
		
};
auto dispaly() {//Fonction pour effectuer une requête et afficher les détails des classees
	cout << "pour la classe departement"<< endl;
	cpr::Response r = cpr::Get(cpr::Url{"http://localhost:8000/departement/1"});
	json a = json::parse(r.text);
	cout << a << endl;
	
	cout << "pour la classe usine"<< endl;
	cpr::Response t = cpr::Get(cpr::Url{"http://localhost:8000/usine/1"});
	json m = json::parse(t.text);
	cout << m << endl;
	
	cout << "pour la classe machine"<< endl;
	cpr::Response c = cpr::Get(cpr::Url{"http://localhost:8000/machine/1"});
	json j = json::parse(c.text);
	cout << j << endl;
	
	cout << "pour la classe ingredients"<< endl;
	cpr::Response I = cpr::Get(cpr::Url{"http://localhost:8000/ingredient/3"});
	json In = json::parse(I.text);
	cout << In << endl;
	//meme chose pour les autres classes
	
	
}
auto main() -> int
{


	dispaly();

}






