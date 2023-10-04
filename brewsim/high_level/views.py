 
from django.shortcuts import render
from django.views.generic import DetailView
from .models import Departement

class DepartementDetailView(DetailView):
    model = Departement
    template_name = 'departement_detail.html'  # Créez un template HTML pour afficher les détails du département
    context_object_name = 'departement'

    def render_to_response(self, context, **response_kwargs):
        """
        Return a response, using the response_class for this view, with a
        template rendered with the given context.
        Pass response_kwargs to the constructor of the response class.
        """
        response_kwargs.setdefault("content_type", self.content_type)
        return Httpresponse(dumps(self.object.json()))  
    
