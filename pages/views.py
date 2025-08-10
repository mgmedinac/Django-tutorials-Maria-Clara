from django.shortcuts import render
from django.views.generic import TemplateView
from django.views import View

class homePageView(TemplateView):
    template_name= 'pages/home.html'
    


class aboutPageView(TemplateView):
    template_name = 'pages/about.html'


    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context.update({
        "title": "About us - Online Store",
        "subtitle": "About us",
        "description": "This is an about page ...",
        "author": "Developed by: Maria Clara Medina Gómez",
        })
        return context
    

class Product:
    products = [
    {"id":"1", "name":"TV", "description":"Best TV"},
    {"id":"2", "name":"iPhone", "description":"Best iPhone"},
    {"id":"3", "name":"Chromecast", "description":"Best Chromecast"},
    {"id":"4", "name":"Glasses", "description":"Best Glasses"}
    ]

class productIndexView(View):
    template_name = 'products/index.html'

    def get(self, request):
        viewData = {}
        viewData["title"] = "Products - Online Store"
        viewData["subtitle"] = "List of products"
        viewData["products"] = Product.products

        return render(request, self.template_name, viewData)


class productShowView(View):
    template_name = 'products/show.html'

    def get(self, request, id):
        viewData = {}
        product = Product.products[int(id)-1]
        viewData["title"] = product["name"] + " - Online Store"
        viewData["subtitle"] = product["name"] + " - Product information"
        viewData["product"] = product
        return render(request, self.template_name, viewData)