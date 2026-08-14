class Nodo:
    def __init__(self, valor):
        self.valor = valor
        self.siguiente = None  # nos permite movernos hacia la derecha
        self.anterior = None   # nos permite movernos hacia la izquierda


class ListaDoblemente:
    def __init__(self):
        self.cabeza = None  # inicio de la lista
        self.cola = None    # final de la lista
        self.tamano = 0     # cantidad de nodos en la lista

    def listaVacia(self):
        return self.cabeza is None  # determina si la cabeza es None

    def insertarAlInicio(self, valor):
        nuevo_nodo = Nodo(valor)
        if self.listaVacia():
            self.cabeza = nuevo_nodo
            self.cola = nuevo_nodo
        else:
            nuevo_nodo.siguiente = self.cabeza
            self.cabeza.anterior = nuevo_nodo
            self.cabeza = nuevo_nodo
        self.tamano += 1

    def imprimiratras(self):
        if self.listaVacia():
            print("La lista esta vacia")
            return
        actual = self.cola
        while actual: #mientras que atras no es NULL
            print(actual.valor,end="->")
            actual = actual.anterior
        print("None")

    def imprimirAdelante(self):
        if self.listaVacia():
            print("La lista esta vacia")
            return
        actual = self.cabeza
        while actual: #mientras que adelante no es NULL
            print(actual.valor,end="->")
            actual = actual.siguiente
        print("None")

    def cantidadElementos(self):
        return self.tamano

    def eliminarFinal(self):
        if self.listaVacia():
            print("La lista esta vacia")
            return
        if self.cabeza != self.cola: #si hay ub solo nodo en la lista
            self.cola = self.cola.anterior
            self.cola.siguiente = None
            self.tamano -= 1
        else:
            self.cabeza = None
            self.cola = None
            self.tamano -= 1

    def buscarElemento(self, valor):
        if self.listaVacia():
            print("La lista esta vacia")
            return False
        actual = self.cabeza
        pocicion = 0
        while actual:
            if actual.valor == valor:
                return None
            actual = actual.siguiente
            pocicion += 1
        return -1 #El elemento no se encontro.

    def insertarAlFinal(self, valor):
        nuevo_nodo = Nodo(valor)
        if self.listaVacia():
            self.cabeza = nuevo_nodo
            self.cola = nuevo_nodo
        else:
            nuevo_nodo.anterior = self.cola
            self.cola.siguiente = nuevo_nodo
            self.cola = nuevo_nodo
        self.tamano += 1

    def insertarAlMedio(self, valor, posicion):

        #verificar si la posicion es valida 
        if posicion<0 or posicion>self.tamano:
            print("Posicion invalida")
            return

        #si la pocicion es 0, insertar al inicio
        if posicion == 0:
            self.agregarAlInicio(valor)
            return

        #si la poscion corresponde al final
        if posicion == self.tamano:
            self.agregarAlFinal(valor)
            return

        nuevo_nodo = Nodo(valor)

        actual=self.cabeza
         #Llegar al nodo que actualmente ocupa la posicion 
        for i in range(posicion):
            actual = actual.siguiente

        #Conectar el nuevo nodo
        anterior = actual.anterior

        nuevo_nodo.anterior = anterior
        nuevo_nodo.siguiente = actual

        anterior.siguiente = nuevo_nodo
        actual.anterior = nuevo_nodo

        self.tamano += 1

    def eliminarAlInicio(self):
        if self.estaVacia():
            print("No se puede eliminar ya que la lista esta vacia")
            return None

        valorEliminado = self.cabeza.valor

        #Caso solamente existe un nodo en la lista
        if self.cabeza == self.cola:
            self.cabeza = None
            self.cola = None

        else:
            self.cabeza = self.cabeza.siguiente
            self.cabeza.anterior = None

        self.tamano-= 1
        return valorEliminado


    def eliminarAlMedio(self, posicion):
        if self.estaVacia():
            print("No se puede eliminar ya que la lista esta vacia")
            return None

        #verificar posicion valida
        if posicion <0 or posicion >=self.tamano:
            print("Posicion invalida")
            return None

        #si es el primer elemento
        if posicion == 0:
            return self.eliminarAlInicio()

        #si es el ultimo elemento
        if posicion == self.tamano - 1:
            return self.eliminarFinal()

        actual =self.cabeza

        #Buscae el nodo que se desea eliminar
        for i in range(posicion):
            actual = actual.siguiente

        valorEliminado = actual.valor

        #Guardar nodos anterior y siguiente 
        anterior = actual.anterior
        siguiente = actual.siguiente

        #reconectar los nodos
        anterior.siguiente = siguiente
        siguiente.anterior = anterior

        self.tamano -= 1
        return valorEliminado
    


        
       
if __name__ == "__main__":
    lista = ListaDoblemente()
    lista.insertarAlInicio(10)
    lista.insertarAlInicio(20)
    lista.insertarAlInicio(30)
    lista.imprimiratras()
    lista.imprimirAdelante()
    print("Cantidad de elementos:", lista.cantidadElementos())
    lista.eliminarFinal
    lista.imprimirAdelante()
    lista.imprimiratras()
    print(lista.buscarElemento(20))

    print("Hola Mundo ")
    