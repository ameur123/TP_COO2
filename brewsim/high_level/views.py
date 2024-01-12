from django.shortcuts import render
from django.views.generic import DetailView
from django.http import HttpResponse
from json import dumps
from .models import Departement, Machine, Ingredient, QuantiteIngredient, Action, Recette, Usine, Prix


class DepartementDetailView(DetailView):
    model = Departement
    template_name = 'departement_detail.html'
    context_object_name = 'departement'

    def render_to_response(self, context, **response_kwargs):
        response_kwargs.setdefault("content_type", self.content_type)
        return HttpResponse(dumps(self.object.json()))

class MachineDetailView(DetailView):
    model = Machine
    template_name = 'machine_detail.html'
    context_object_name = 'machine'

    def render_to_response(self, context, **response_kwargs):
        response_kwargs.setdefault("content_type", self.content_type)
        return HttpResponse(dumps(self.object.json()))

class IngredientDetailView(DetailView):
    model = Ingredient
    template_name = 'ingredient_detail.html'
    context_object_name = 'ingredient'

    def render_to_response(self, context, **response_kwargs):
        response_kwargs.setdefault("content_type", self.content_type)
        return HttpResponse(dumps(self.object.json()))

class QuantiteIngredientDetailView(DetailView):
    model = QuantiteIngredient
    template_name = 'quantite_ingredient_detail.html'
    context_object_name = 'qantite_ingredient'

    def render_to_response(self, context, **response_kwargs):
        response_kwargs.setdefault("content_type", self.content_type)
        return HttpResponse(dumps(self.object.json()))

class UsineDetailView(DetailView):
    model = Usine
    template_name = 'usine_detail.html'
    context_object_name = 'usine'

    def render_to_response(self, context, **response_kwargs):
        response_kwargs.setdefault("content_type", self.content_type)
        return HttpResponse(dumps(self.object.json()))

class PrixDetailView(DetailView):
    model = Prix
    template_name = 'prix_detail.html'
    context_object_name = 'prix'

    def render_to_response(self, context, **response_kwargs):
        response_kwargs.setdefault("content_type", self.content_type)
        return HttpResponse(dumps(self.object.json()))
class ActionDetailView(DetailView):
    model = Action
    template_name = 'action_detail.html'
    context_object_name = 'action'

    def render_to_response(self, context, **response_kwargs):
        response_kwargs.setdefault("content_type", self.content_type)
        return HttpResponse(dumps(self.object.json()))

class RecetteDetailView(DetailView):
    model = Recette
    template_name = 'recette_detail.html'
    context_object_name = 'recette'

    def render_to_response(self, context, **response_kwargs):
        response_kwargs.setdefault("content_type", self.content_type)
        return HttpResponse(dumps(self.object.json()))


