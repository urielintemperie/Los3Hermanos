from django.shortcuts import render
from django.views.generic import View

# Create your views here.
'''
class NuevoPedidoView(request):

    producto = request.POST("producto")
    cantidad = request.POST("cantidad")
    pedido = Pedido.object.create(producto=producto,cantidad=cantidad,precio=producto.precio,date=date.date.today()
'''

class HomeController(View):

    def get(self, request):
        return render(request,'home.html')