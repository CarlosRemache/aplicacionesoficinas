from django.shortcuts import render,redirect

# Create your views here.
from.models import Oficina, Contratista, Reforma, Suministro, ReformaSuministro

from django.contrib import messages
from datetime import datetime



from django.utils.timezone import now



from django.http import HttpResponse
from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas



def inicio(request):
    return render(request, 'inicio.html')



def nueva_oficina(request):
    return render(request, 'nueva_oficina.html')



def listado_oficinas(request):
    oficinas = Oficina.objects.all()
    return render(request, 'listado_oficinas.html', {'oficinas': oficinas})




def guardar_oficina(request):
    nombre = request.POST['txt_nombre']
    ubicacion = request.POST['txt_ubicacion']
    responsable = request.POST['txt_responsable']
    capacidad = request.POST['txt_capacidad']
    estado = request.POST['txt_estado']

    # Validar que la capacidad no sea negativa
    if float(capacidad) < 0:
        messages.error(request, "La capacidad no puede ser un número negativo.")
        return redirect('/nueva_oficina')

    Oficina.objects.create(
        nombre=nombre, 
        ubicacion=ubicacion, 
        responsable=responsable, 
        capacidad=capacidad, 
        estado=estado
    )

    messages.success(request, "Oficina guardada exitosamente")
    return redirect('/listado_oficinas')





def eliminar_oficina(request, id):
    oficina = Oficina.objects.get(id=id)
    oficina.delete()
    messages.success(request, "Oficina eliminada exitosamente")
    return redirect('/listado_oficinas')




def editar_oficina(request, id):
    oficina = Oficina.objects.get(id=id)
    return render(request, 'editar_oficina.html', {'oficina': oficina})




def procesar_editar_oficina(request):
    oficina = Oficina.objects.get(id=request.POST['id'])
    
    nombre = request.POST['txt_nombre']
    ubicacion = request.POST['txt_ubicacion']
    responsable = request.POST['txt_responsable']
    capacidad = request.POST['txt_capacidad']
    estado = request.POST['txt_estado']

    # Validar que la capacidad no sea negativa
    if float(capacidad) < 0:
        messages.error(request, "La capacidad no puede ser un número negativo.")
        return redirect(f'/editar_oficina/{oficina.id}')

    oficina.nombre = nombre
    oficina.ubicacion = ubicacion
    oficina.responsable = responsable
    oficina.capacidad = capacidad
    oficina.estado = estado
    oficina.save()

    messages.success(request, "Oficina editada exitosamente")
    return redirect('/listado_oficinas')



#-----------------------------------------------------------contratista





def nuevo_contratista(request):
    return render(request, 'nuevo_contratista.html')




def listado_contratistas(request):
    contratistas = Contratista.objects.all()
    return render(request, 'listado_contratistas.html', {'contratistas': contratistas})




def guardar_contratista(request):
    nombre = request.POST['txt_nombre']
    empresa = request.POST['txt_empresa']
    telefono = request.POST['txt_telefono']
    correo = request.POST['txt_correo']
    especialidad = request.POST['txt_especialidad']
    fotografia = request.FILES.get('foto')  # para fotos


    Contratista.objects.create(
        nombre=nombre, 
        empresa=empresa, 
        telefono=telefono, 
        correo=correo, 
        especialidad=especialidad,
        fotografia=fotografia
    )

    messages.success(request, "Contratista guardado exitosamente")
    return redirect('/listado_contratistas')





def eliminar_contratista(request, id):
    contratista = Contratista.objects.get(id=id)
    contratista.delete()
    messages.success(request, "Contratista eliminado exitosamente")
    return redirect('/listado_contratistas')




def editar_contratista(request, id):
    contratista = Contratista.objects.get(id=id)
    return render(request, 'editar_contratista.html', {'contratista': contratista})




def procesar_editar_contratista(request):
    contratista = Contratista.objects.get(id=request.POST['id'])
    contratista.nombre = request.POST['txt_nombre']
    contratista.empresa = request.POST['txt_empresa']
    contratista.telefono = request.POST['txt_telefono']
    contratista.correo = request.POST['txt_correo']
    contratista.especialidad = request.POST['txt_especialidad']
    contratista.fotografia=request.FILES.get('foto')#para fotos
   
    contratista.save()

    messages.success(request, "Contratista editado exitosamente")
    return redirect('/listado_contratistas')




#-----------------------------------------------------------reforma


def nueva_reforma(request):
    oficinas = Oficina.objects.all()
    contratistas = Contratista.objects.all()
    return render(request, 'nueva_reforma.html', {'oficinas': oficinas, 'contratistas': contratistas})




def listado_reformas(request):
    reformas = Reforma.objects.all()
    return render(request, 'listado_reformas.html', {'reformas': reformas})





def guardar_reforma(request):
    oficina = Oficina.objects.get(id=request.POST['oficina'])
    contratista = Contratista.objects.get(id=request.POST['contratista'])
    fecha_inicio = request.POST['fecha_inicio']
    fecha_fin = request.POST['fecha_fin']
    presupuesto = request.POST['presupuesto']
    descripcion = request.POST['descripcion']
    reforma = request.POST['reforma']


    # Validar presupuesto
    try:
        presupuesto = float(presupuesto)
        if presupuesto < 0:
            messages.error(request, "El presupuesto no puede ser negativo.")
            return redirect('/nueva_reforma')
    except ValueError:
        messages.error(request, "El presupuesto debe ser un número válido.")
        return redirect('/nueva_reforma')




    # Validar fechas
    try:
        fecha_inicio = datetime.strptime(fecha_inicio, "%Y-%m-%d")
        fecha_fin = datetime.strptime(fecha_fin, "%Y-%m-%d")

        if not (datetime(2000, 1, 1) <= fecha_inicio <= datetime(2030, 12, 31)):
            messages.error(request, "La fecha de inicio debe estar entre el 2000 y el 2030.")
            return redirect('/nueva_reforma')

        if not (datetime(2000, 1, 1) <= fecha_fin <= datetime(2030, 12, 31)):
            messages.error(request, "La fecha de fin debe estar entre el 2000 y el 2030.")
            return redirect('/nueva_reforma')

    except ValueError:
        messages.error(request, "Las fechas proporcionadas no son válidas.")
        return redirect('/nueva_reforma')

    # Guardar reforma si las fechas son válidas
    Reforma.objects.create(
        oficina=oficina, 
        contratista=contratista, 
        fecha_inicio=fecha_inicio, 
        fecha_fin=fecha_fin, 
        presupuesto=presupuesto, 
        descripcion=descripcion, 
        reforma=reforma
    )

    messages.success(request, "Reforma guardada exitosamente")
    return redirect('/listado_reformas')








def eliminar_reforma(request, id):
    reforma = Reforma.objects.get(id=id)
    reforma.delete()
    messages.success(request, "Reforma eliminada exitosamente")
    return redirect('/listado_reformas')





def editar_reforma(request, id):
    reforma = Reforma.objects.get(id=id)
    oficinas = Oficina.objects.all()
    contratistas = Contratista.objects.all()
    return render(request, 'editar_reforma.html', {'reforma': reforma, 'oficinas': oficinas, 'contratistas': contratistas})




def procesar_editar_reforma(request):
    reforma = Reforma.objects.get(id=request.POST['id'])
    reforma.oficina = Oficina.objects.get(id=request.POST['oficina'])
    reforma.contratista = Contratista.objects.get(id=request.POST['contratista'])
    fecha_inicio = request.POST['fecha_inicio']
    fecha_fin = request.POST['fecha_fin']
    presupuesto = request.POST['presupuesto']
    reforma.descripcion = request.POST['descripcion']
    reforma.reforma = request.POST['reforma']


       # Validar presupuesto
    try:
        presupuesto = float(presupuesto)
        if presupuesto < 0:
            messages.error(request, "El presupuesto no puede ser negativo.")
            return redirect(f'/editar_reforma/{reforma.id}')
    except ValueError:
        messages.error(request, "El presupuesto debe ser un número válido.")
        return redirect(f'/editar_reforma/{reforma.id}')



    # Validar fechas
    try:
        fecha_inicio = datetime.strptime(fecha_inicio, "%Y-%m-%d")
        fecha_fin = datetime.strptime(fecha_fin, "%Y-%m-%d")

        if not (datetime(2000, 1, 1) <= fecha_inicio <= datetime(2030, 12, 31)):
            messages.error(request, "La fecha de inicio debe estar entre el 2000 y el 2030.")
            return redirect(f'/editar_reforma/{reforma.id}')

        if not (datetime(2000, 1, 1) <= fecha_fin <= datetime(2030, 12, 31)):
            messages.error(request, "La fecha de fin debe estar entre el 2000 y el 2030.")
            return redirect(f'/editar_reforma/{reforma.id}')

    except ValueError:
        messages.error(request, "Las fechas proporcionadas no son válidas.")
        return redirect(f'/editar_reforma/{reforma.id}')

    # Guardar reforma si las fechas son válidas
    reforma.fecha_inicio = fecha_inicio
    reforma.fecha_fin = fecha_fin
    reforma.presupuesto = presupuesto
    reforma.save()

    messages.success(request, "Reforma editada exitosamente")
    return redirect('/listado_reformas')






#-----------------------------------------------------------suministro


def nuevo_suministro(request):
    return render(request, 'nuevo_suministro.html')




def listado_suministros(request):
    suministros = Suministro.objects.all()
    return render(request, 'listado_suministros.html', {'suministros': suministros})




def guardar_suministro(request):
    nombre = request.POST['nombre']
    descripcion = request.POST['descripcion']
    cantidad = request.POST['cantidad']
    costo_unitario = request.POST['costo_unitario']
    evidencias = request.FILES.get('foto')  # para fotos


     # Validar cantidad y costo_unitario
    try:
        cantidad = float(cantidad)
        if cantidad < 0:
            messages.error(request, "La cantidad no puede ser negativa.")
            return redirect('/nuevo_suministro')
    except ValueError:
        messages.error(request, "La cantidad debe ser un número válido.")
        return redirect('/nuevo_suministro')

    try:
        costo_unitario = float(costo_unitario)
        if costo_unitario < 0:
            messages.error(request, "El costo unitario no puede ser negativo.")
            return redirect('/nuevo_suministro')
    except ValueError:
        messages.error(request, "El costo unitario debe ser un número válido.")
        return redirect('/nuevo_suministro')


    Suministro.objects.create(
        nombre=nombre,
        descripcion=descripcion,
        cantidad=cantidad,
        costo_unitario=costo_unitario,
        evidencias=evidencias
    )

    messages.success(request, "Suministro guardado exitosamente")
    return redirect('/listado_suministros')




def eliminar_suministro(request, id):
    suministro = Suministro.objects.get(id=id)
    suministro.delete()
    messages.success(request, "Suministro eliminado exitosamente")
    return redirect('/listado_suministros')




def editar_suministro(request, id):
    suministro = Suministro.objects.get(id=id)
    return render(request, 'editar_suministro.html', {'suministro': suministro})





def procesar_editar_suministro(request):
    suministro = Suministro.objects.get(id=request.POST['id'])
    suministro.nombre = request.POST['nombre']
    suministro.descripcion = request.POST['descripcion']
    cantidad = request.POST['cantidad']
    costo_unitario = request.POST['costo_unitario']
    suministro.evidencias=request.FILES.get('foto')#para fotos

      # Validar cantidad y costo_unitario
    try:
        cantidad = float(cantidad)
        if cantidad < 0:
            messages.error(request, "La cantidad no puede ser negativa.")
            return redirect(f'/editar_suministro/{suministro.id}')
    except ValueError:
        messages.error(request, "La cantidad debe ser un número válido.")
        return redirect(f'/editar_suministro/{suministro.id}')

    try:
        costo_unitario = float(costo_unitario)
        if costo_unitario < 0:
            messages.error(request, "El costo unitario no puede ser negativo.")
            return redirect(f'/editar_suministro/{suministro.id}')
    except ValueError:
        messages.error(request, "El costo unitario debe ser un número válido.")
        return redirect(f'/editar_suministro/{suministro.id}')



    suministro.cantidad = cantidad
    suministro.costo_unitario = costo_unitario
    suministro.save()

    messages.success(request, "Suministro editado exitosamente")
    return redirect('/listado_suministros')









#-----------------------------------------------------------reforma de suministro


def nuevo_reforma_suministro(request):
    reformas = Reforma.objects.all()
    suministros = Suministro.objects.all()
    return render(request, 'nuevo_reforma_suministro.html', {'reformas': reformas, 'suministros': suministros})






def listado_reforma_suministro(request):
    reformas_suministros = ReformaSuministro.objects.all()
    return render(request, 'listado_reforma_suministro.html', {'reformas_suministros': reformas_suministros})






def guardar_reforma_suministro(request):
    reforma_id = request.POST['reforma']
    suministro_id = request.POST['suministro']
    cantidad_usada = request.POST['cantidad_usada']



        # Validar cantidad_usada
    try:
        cantidad_usada = float(cantidad_usada)
        if cantidad_usada < 0:
            messages.error(request, "La cantidad usada no puede ser negativa.")
            return redirect('/nuevo_reforma_suministro')
    except ValueError:
        messages.error(request, "La cantidad usada debe ser un número válido.")
        return redirect('/nuevo_reforma_suministro')




    reforma = Reforma.objects.get(id=reforma_id)
    suministro = Suministro.objects.get(id=suministro_id)

    ReformaSuministro.objects.create(
        reforma=reforma,
        suministro=suministro,
        cantidad_usada=cantidad_usada
    )

    messages.success(request, "Reforma y suministro guardados correctamente")
    return redirect('/listado_reforma_suministro')




def eliminar_reforma_suministro(request, id):
    reforma_suministro = ReformaSuministro.objects.get(id=id)
    reforma_suministro.delete()
    messages.success(request, "Reforma y suministro eliminados correctamente")
    return redirect('/listado_reforma_suministro')



def editar_reforma_suministro(request, id):
    reforma_suministro = ReformaSuministro.objects.get(id=id)
    reformas = Reforma.objects.all()
    suministros = Suministro.objects.all()
    return render(request, 'editar_reforma_suministro.html', {
        'reforma_suministro': reforma_suministro,
        'reformas': reformas,
        'suministros': suministros
    })






def procesar_editar_reforma_suministro(request):
    reforma_suministro = ReformaSuministro.objects.get(id=request.POST['id'])
    reforma_suministro.reforma = Reforma.objects.get(id=request.POST['reforma'])
    reforma_suministro.suministro = Suministro.objects.get(id=request.POST['suministro'])
    cantidad_usada = request.POST['cantidad_usada']
    
    # Validar cantidad_usada
    try:
        cantidad_usada = float(cantidad_usada)
        if cantidad_usada < 0:
            messages.error(request, "La cantidad usada no puede ser negativa.")
            return redirect(f'/editar_reforma_suministro/{reforma_suministro.id}')
    except ValueError:
        messages.error(request, "La cantidad usada debe ser un número válido.")
        return redirect(f'/editar_reforma_suministro/{reforma_suministro.id}')



    reforma_suministro.cantidad_usada = cantidad_usada
    reforma_suministro.save()

    messages.success(request, "Reforma y suministro editados correctamente")
    return redirect('/listado_reforma_suministro')







#-----------------------------------------------------------reportes

def generar_reporte_pdf(request):
    response = HttpResponse(content_type='application/pdf')
    response['Content-Disposition'] = 'attachment; filename="reporte_reforma_suministro.pdf"'

    # Crear el PDF
    pdf = canvas.Canvas(response, pagesize=letter)
    pdf.setTitle("Reporte de Reforma y Suministros")
    
    y = 750  # Posición inicial en el PDF

    reformas = Reforma.objects.all()

    pdf.setFont("Helvetica-Bold", 14)
    pdf.drawString(200, y, "Reporte de Reformas y Suministros")
    y -= 30

    for reforma in reformas:
        pdf.setFont("Helvetica-Bold", 12)
        pdf.drawString(50, y, f"Oficina: {reforma.oficina.nombre}")
        y -= 20
        pdf.drawString(50, y, f"Contratista: {reforma.contratista.nombre}")
        y -= 20
        pdf.drawString(50, y, f"Fecha de Inicio: {reforma.fecha_inicio}")
        y -= 20
        pdf.drawString(50, y, f"Fecha de Fin: {reforma.fecha_fin if reforma.fecha_fin else 'N/A'}")
        y -= 20
        pdf.drawString(50, y, f"Presupuesto: ${reforma.presupuesto}")
        y -= 20
        pdf.drawString(50, y, f"Descripción: {reforma.descripcion}")
        y -= 20
        pdf.drawString(50, y, f"Estado: {reforma.reforma}")
        y -= 30

        # Obtener suministros relacionados con la reforma
        suministros = ReformaSuministro.objects.filter(reforma=reforma)

        if suministros.exists():
            pdf.setFont("Helvetica-Bold", 12)
            pdf.drawString(50, y, "Suministros utilizados:")
            y -= 20
            pdf.setFont("Helvetica", 10)
            pdf.drawString(50, y, "Nombre | Descripción | Cantidad | Costo Unitario")
            y -= 15

            total_costo = 0  # Variable para almacenar el costo total de los suministros

            for suministro in suministros:
                costo_total_suministro = suministro.cantidad_usada * suministro.suministro.costo_unitario
                total_costo += costo_total_suministro  # Acumular el costo total

                pdf.drawString(50, y, f"{suministro.suministro.nombre} | {suministro.suministro.descripcion} | {suministro.cantidad_usada} | ${suministro.suministro.costo_unitario}")
                y -= 15
            
            y -= 20
            pdf.setFont("Helvetica-Bold", 12)
            pdf.drawString(50, y, f"TOTAL COSTO SUMINISTROS: ${total_costo:.2f}")  # Mostrar total
            y -= 30

        # Espaciado entre reformas
        y -= 30
        if y < 100:
            pdf.showPage()
            y = 750

    pdf.save()
    return response


















