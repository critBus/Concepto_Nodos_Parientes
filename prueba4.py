from neomodel import StructuredNode, StringProperty, FloatProperty, RelationshipTo, RelationshipFrom

from neomodel import config
import urllib3

config.DATABASE_URL = 'bolt://neo4j:rene1234@localhost:7687'

class Persona(StructuredNode):
    nombre1 = StringProperty()
    nombre2 = StringProperty()
    apellido1 = StringProperty()
    apellido2 = StringProperty()
    estatura = FloatProperty()
    color = StringProperty()
    sexo = StringProperty()
    direccion = StringProperty()
    ci = StringProperty()

    padre = RelationshipTo('Persona', 'PADRE')
    madre = RelationshipTo('Persona', 'MADRE')
    hermanos = RelationshipTo('Persona', 'HERMANO')

    hijo_de = RelationshipFrom('Persona', 'PADRE')
    hija_de = RelationshipFrom('Persona', 'MADRE')
    hermano_de = RelationshipFrom('Persona', 'HERMANO')


#estr=EstructuraD(dato='zxc3',dato2='qwe3').save()
#juan = Persona(nombre1='Juan', apellido1='Pérez').save()
#pedro = Persona(nombre1='Pedro', apellido1='Pérez').save()
#juan.padre.connect(pedro)

#alberto=Persona(nombre1='Alberto', apellido1='Gonzales',ci="1231221331").save()
#gualberto=Persona(nombre1='Gualberto', apellido1='Armando',ci="45334234").save()
#mario=Persona(nombre1='Mario', apellido1='Prieto',ci="21543534").save()

persona = Persona.nodes.get(ci='1231221331')
if persona is not None:
    print(f"Se encontró a la persona: {persona.nombre1} {persona.apellido1}")
else:
    print("No se encontró a ninguna persona con ese CI")
print("termino")