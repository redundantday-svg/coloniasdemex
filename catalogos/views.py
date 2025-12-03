from django.shortcuts import render,redirect, get_object_or_404
from django.http import HttpResponse
from django.db.models import Q
from .models import Estado
from .models import municipio
from .models import colonia
from .forms import EstadoForm
from .forms import municipioForm
from .forms import ColoniaForm
# Create your views here.
def hola_mundo (request):
    return HttpResponse("<h1 align= 'center'>Bienvenidos</h1>" \
    ) 

def principal(request):
    q = request.GET.get('q', '').strip()
    
    if q:
        # Search colonias
        colonias = colonia.objects.filter(
            Q(nombre__icontains=q) |
            Q(codigo_p__icontains=q)
        ).select_related('municipio_p', 'municipio_p__estadop')
        
        # Search municipios
        municipios = municipio.objects.filter(
            nombre__icontains=q
        ).select_related('estadop')
        
        # Search estados
        estados = Estado.objects.filter(
            Q(nombre__icontains=q) |
            Q(clave__icontains=q)
        )
    else:
        colonias = colonia.objects.all().select_related('municipio_p', 'municipio_p__estadop')
        municipios = municipio.objects.all().select_related('estadop')
        estados = Estado.objects.all()
    
    return render(request, 'principal.html', {
        'colonias': colonias,
        'municipios': municipios,
        'estados': estados,
        'q': q
    })
def pantalla_inicio (request):
    return render (request, 'pantalla_inicio.html')
def estado_list (request):
    estados=Estado.objects.all()
    return render(request,'estado_list.html', {'estados':estados})
def Estado_create(request):
    Form=EstadoForm(request.POST or None)
    if Form.is_valid():
        Form.save()
        return redirect('estado_list')
    return render(request,'estado_form.html',{'form':Form})
def estado_update (request, pk):
    estado = get_object_or_404(Estado, id=pk)
    form=EstadoForm(request.POST or None, instance=estado)
    if form.is_valid():
        form.save()
        return redirect ('estado_list')
    return render(request, 'estado_form.html', {'form':form})
def estado_delete (request, pk,):
    estado = get_object_or_404(Estado, id=pk)
    if request.method == 'POST':
        estado.delete()
        return redirect('estado_list')
    return render(request, 'estado_confirm_delete.html', {'estado':estado})
def municipio_list (request):
    municipios=municipio.objects.all()
    return render(request,'municipio_list.html', {'municipios':municipios})
def municipio_create(request):
    Form=municipioForm(request.POST or None)
    if Form.is_valid():
        Form.save()
        return redirect('municipio_list')
    return render(request,'municipio_form.html',{'form':Form})
def municipio_update (request, pk):
    municipio_obj    = get_object_or_404(municipio, id=pk)
    form=municipioForm(request.POST or None, instance=municipio_obj)
    if form.is_valid():
        form.save()
        return redirect ('municipio_list')
    return render(request, 'municipio_form.html', {'form':form})
def municipio_delete (request, pk,):
    municipio_obj = get_object_or_404(municipio, id=pk)
    if request.method=='POST':
        municipio_obj.delete()
        return redirect('municipio_list')
    return render(request, 'municipio_confirm_delete.html', {'municipio':municipio_obj})
def colonia_list (request):
    colonias=colonia.objects.all()
    return render(request,'colonia_list.html', {'colonias':colonias})
def colonia_create(request):
    Form=ColoniaForm(request.POST or None)
    if Form.is_valid():
        Form.save()
        return redirect('colonia_list')
    return render(request,'colonia_form.html',{'form':Form})
def colonia_update (request, pk):
    colonia_obj = get_object_or_404(colonia, id=pk)
    form=ColoniaForm(request.POST or None, instance=colonia_obj)
    if form.is_valid():
        form.save()
        return redirect ('colonia_list')
    return render(request, 'colonia_form.html', {'form':form})
def colonia_delete (request, pk,):
    colonia_obj = get_object_or_404(colonia, id=pk)
    if request.method=='POST':
        colonia_obj.delete()
        return redirect('colonia_list')
    return render(request, 'colonia_confirm_delete.html', {'colonia':colonia_obj})


