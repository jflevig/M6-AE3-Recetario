from django.shortcuts import render
from .models import Receta


RECETA = [
    Receta(
        nombre= "Antipasto",
        descripcion="Los italianos comienzan su comida con antipasto, una entrada o aperitivo antes del plato principal.",
        ingredientes= [
    "Cebollitas en vinagre",
    "Zanahoria en vinagre",
    "Pepinillos en vinagre",
    "Coliflor en vinagre",
    "Aceitunas rellenas de anchoa",
    "Alcaparras",
    "Atún",
    "Anchoas",
    "Aceite de oliva"
],
        preparacion= [
    "Picar más o menos la misma cantidad de cebollitas, zanahoria, pepinillos, coliflor, aceitunas rellenas, alcaparras, atún y anchoas. Esta proporción se puede modificar al gusto.",
    "Poner en un bote o bol y cubrir con aceite. Se puede preparar con antelación.",
    "Servir acompañado de tostaditas o con cualquier pan plano para que cada cual les vaya poniendo la insalatina encima."
],
        imagen = "img/antipasto.jpg",
    ),
    Receta(
        nombre="Spaguetti a la Carbonara",
        descripcion="Auténtica, cremosa y tradicional receta de la cocina italiana",
        ingredientes = [
    "3 Yemas de huevo",
    "1 Huevo",
    "100 g Panceta (Mejor si es Guanciale)",
    "50 g Queso Pecorino",
    "Pimienta negra molida al gusto",
    "Sal",
    "Agua",
    "320 g Espaguetis"
],

        preparacion = [
    "No utilices bacon o bacon ahumado para hacer esta receta. Busca el auténtico guanciale italiano, hecho con la papada del cerdo y si no, utiliza en su lugar una buena panceta fresca, retirando la piel. Córtala en trocitos de pequeño tamaño y fríe esos trocitos hasta que comiencen a dorarse.",
    "Por otro lado, bate las 3 yemas de huevo con el huevo y el queso pecorino recién rallado hasta hacer una mezcla algo espesa. Dale unos toques de pimienta negra a esa mezcla.",
    "Entre tanto, pon la pasta a cocer en agua abundante con sal, y sácala cuando falten un par de minutos para que esté al dente.",
    "En la sartén donde habíamos reservado la panceta o el guanciale salteado, agregaremos la pasta escurrida a la que añadimos la mezcla de huevos, queso y pimienta, mezclando bien.",
    "Agregamos también un cucharón del agua de cocción de la pasta."
],
        imagen = "img/spaguetti.jpg",
    ),

    Receta(
        nombre="Risotto",
        descripcion="Descubre cómo preparar el risotto italiano más cremoso y delicioso con nuestra receta tradicional paso a paso. Sabores intensos y textura perfecta garantizado",
        ingredientes = [
    "320 g Arroz Arborio o Carnaroli",
    "1.2 l Caldo de Verduras",
    "1 Cebolla Mediana (100 g)",
    "2 dientes Ajo (10 g)",
    "80 ml Vino Blanco Seco",
    "60 g Mantequilla",
    "60 g Queso Parmesano rallado",
    "2 cucharadas Aceite de Oliva (30 ml)",
    "Sal y pimienta negra al gusto",
    "2 cucharadas Perejil Fresco picado (10 g)"
],

       preparacion = [
    "En una olla grande, calienta el aceite de oliva a fuego medio. Añade la cebolla y el ajo, sofríe hasta que estén transparentes.",
    "Agrega el arroz y remueve durante 1-2 minutos hasta que esté ligeramente tostado.",
    "Vierte el vino blanco y cocina hasta que se evapore, removiendo constantemente.",
    "Comienza a añadir el caldo caliente, un cucharón a la vez, removiendo frecuentemente. Espera a que el líquido sea absorbido antes de añadir más.",
    "Continúa este proceso durante 18-20 minutos, hasta que el arroz esté al dente y cremoso.",
    "Retira del fuego y añade la mantequilla y el queso parmesano. Mezcla bien.",
    "Sazona con sal y pimienta al gusto. Deja reposar tapado durante 2 minutos.",
    "Sirve inmediatamente, espolvoreado con perejil fresco.",
    "Consejo adicional: Para un risotto más cremoso, agrega un poco más de caldo al final y remueve enérgicamente para liberar el almidón del arroz."
],
    imagen = "img/Risotto-italiano.jpg",
    ),
    Receta(
    nombre="Lasagna Bolognesa",
    descripcion="Capas de pasta, carne y salsa bechamel que definen el corazón de la cocina italiana.",
    ingredientes=[
        "12 láminas de pasta para lasagna",
        "500 g carne molida de res",
        "1 cebolla picada",
        "2 dientes de ajo",
        "400 g tomate triturado",
        "200 ml salsa bechamel",
        "100 g queso parmesano rallado",
        "Aceite de oliva, sal y pimienta"
    ],
    preparacion=[
        "Sofríe la cebolla y el ajo en aceite de oliva. Agrega la carne y cocina hasta dorar.",
        "Añade el tomate triturado, sal y pimienta. Cocina a fuego lento 20 minutos.",
        "En una fuente, alterna capas de pasta, carne y bechamel. Termina con queso.",
        "Hornea a 180°C durante 30 minutos hasta que esté dorada y burbujeante."
    ],
    imagen="img/lasagna.jpg",
),

Receta(
    nombre="Tiramisú Clásico",
    descripcion="El postre italiano por excelencia, con capas de mascarpone, café y cacao.",
    ingredientes=[
        "250 g queso mascarpone",
        "3 huevos",
        "100 g azúcar",
        "200 g bizcochos de soletilla",
        "200 ml café fuerte",
        "Cacao en polvo para espolvorear"
    ],
    preparacion=[
        "Separa las claras y las yemas. Bate las yemas con el azúcar hasta que estén cremosas.",
        "Agrega el mascarpone y mezcla bien. Bate las claras a punto de nieve y añade suavemente.",
        "Remoja los bizcochos en café y forma capas alternadas con la crema.",
        "Refrigera al menos 4 horas. Espolvorea con cacao antes de servir."
    ],
    imagen="img/tiramisu.jpg",
),

Receta(
    nombre="Focaccia al Romero",
    descripcion="Pan italiano esponjoso con aceite de oliva y aroma a romero fresco.",
    ingredientes=[
        "500 g harina de trigo",
        "300 ml agua tibia",
        "10 g levadura seca",
        "10 g sal",
        "50 ml aceite de oliva",
        "Romero fresco",
        "Sal gruesa"
    ],
    preparacion=[
        "Mezcla la harina con la levadura, sal y agua. Amasa hasta obtener una masa suave.",
        "Deja reposar 1 hora hasta que duplique su tamaño.",
        "Extiende en una bandeja, haz hoyuelos con los dedos y rocía con aceite, romero y sal gruesa.",
        "Hornea a 200°C durante 25 minutos hasta que esté dorada."
    ],
    imagen="img/focaccia.jpg",
),
]

#Inicio o Home
def home(request):
    return render(request, 'home.html', {"recetas": RECETA})

def receta_detalle(request, nombre):
    receta = next((r for r in RECETA if r.nombre == nombre), None)

    if receta is None:
        return render(request, 'RecNA.html')

    return render(request, 'recetas.html', {'receta': receta})

def contacto(request):
    return render(request, 'contacto.html')

def Error(request):
    return render(request, 'RecNA.html')

