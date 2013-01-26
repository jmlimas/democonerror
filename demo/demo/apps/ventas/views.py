from django.shortcuts import render_to_response
from django.template import RequestContext
from demo.apps.ventas.forms import addProductForm
from demo.apps.ventas.models import producto

def add_product_view(request):
	if request.method == "POST":
		form  = addProductForm(request.POST)
		info = "Inicializando"
		if form.is_valid():
		    nombre = form.cleaned_data['nombre']
		    descripcion = form.cleaned_data['descripcion']
		    p = producto()
		    p.nombre = nombre
		    p.descripcion = descripcion
		    p.status = True
		    p.save() # Guardar la  Informacion
		    info = "Se Guardo Satisfactoriamente.!!"
		else:
		        info = "Informacion con datos incorrectos...."
	        form = addProductForm()
	        ctx = {'form':form, 'informacion':info}
	        return render_to_response('ventas/addProducto.html',ctx,context_instance=render_to_response(request))    	
	else:  
	    		form = addProductForm()
			ctx = {'form':form}
			return  render_to_response('ventas/addProducto.html',ctx,context_instance=RequestContext(request))