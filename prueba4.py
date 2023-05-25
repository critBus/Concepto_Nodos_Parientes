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
    hermanos = RelationshipTo('Persona', 'HERMANOS')

    hijos = RelationshipTo('Persona', 'HIJOS')

    # def esHijoDe(self,padre):
    #     for hijo in padre.hijos:
    #         if hijo.id==self.id:
    #             return True
    #     return False
    def tieneComoHijoA(self,hijoABuscar):
        for hijo in self.hijos:
            if hijo.id==hijoABuscar.id:
                return True
        return False
    def getPadre(self):
        if len(self.padre)>0:
            return self.padre[0]
        return None
    def getMadre(self):
        if len(self.madre)>0:
            return self.madre[0]
        return None
    def tieneComoPadreA(self,padreABuscar):
        padre=self.getPadre()
        return padre.id==padreABuscar.id if padre is not None else False
    def tieneComoMadreA(self,madreABuscar):
        madre=self.getPadre()
        return madre.id==madreABuscar.id if madre is not None else False
    def tieneComoHermanoA(self,ABuscar):
        for hermanos in self.hermanos:
            if hermanos.id==ABuscar.id:
                return True
        return False

    @staticmethod
    def delete_all_personas():
        db.cypher_query('MATCH (n:Persona) DETACH DELETE n')
    @staticmethod
    def agregar_relacion_padre_hijo(padre, hijo):
        padre.hijos.connect(hijo)
        hijo.padre.connect(padre)
    @staticmethod
    def findById(id):
        query = "MATCH (p:Persona) WHERE ID(p) = " + str(id) + " RETURN p"
        results, meta = db.cypher_query(query)#, {"id_persona": id}
        if len(results) == 0:
            return None
        else:
            return Persona.inflate(results[0][0])

    


#estr=EstructuraD(dato='zxc3',dato2='qwe3').save()
#juan = Persona(nombre1='Juan', apellido1='Pérez').save()
#pedro = Persona(nombre1='Pedro', apellido1='Pérez').save()
#juan.padre.connect(pedro)

#alberto=Persona(nombre1='Alberto', apellido1='Gonzales',ci="1231221331").save()
#gualberto=Persona(nombre1='Gualberto', apellido1='Armando',ci="45334234").save()
#mario=Persona(nombre1='Mario', apellido1='Prieto',ci="21543534").save()

persona = Persona.nodes.get(ci='1231221331')
# persona.padre.connect(Persona.nodes.get(ci='45334234'))
if persona is not None:
    print(f"Se encontró a la persona: {persona.nombre1} {persona.apellido1}")
else:
    print("No se encontró a ninguna persona con ese CI")
print("termino")
