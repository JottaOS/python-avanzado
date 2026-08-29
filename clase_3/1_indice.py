# 1- Agregar al programa de índice números de página y línea punteada.
# Poner el número de página como otro atributo de las secciones y niveles del índice
# Crear una clase para imprimir un índice, usando context managers anidados


class Indice:
    ANCHO = 60

    def __init__(self):
        self.nivel = []
        self.lineas = []

    def __enter__(self):
        self.nivel.append(0)
        return self

    def __exit__(self, exc_type, exc_value, traceback):
        self.nivel.pop()
        return False

    def seccion(self, titulo, pagina=1):
        return Seccion(self, titulo, pagina)

    def item(self, titulo, pagina=1):
        self.nivel[-1] += 1
        numero = ".".join(str(n) for n in self.nivel)
        self.lineas.append(self._formatear(numero, titulo, pagina))

    def _formatear(self, numero, titulo, pagina):
        texto = f"{numero} {titulo} "
        pagina_str = str(pagina)
        cantidad_puntos = self.ANCHO - len(texto) - len(pagina_str)
        puntos = "." * max(3, cantidad_puntos)
        return f"{texto}{puntos} {pagina_str}"

    def imprimir(self):
        for linea in self.lineas:
            print(linea)


class Seccion:
    def __init__(self, indice, titulo, pagina=1):
        self.indice = indice
        self.titulo = titulo
        self.pagina = pagina

    def __enter__(self):
        self.indice.nivel[-1] += 1
        numero = ".".join(str(n) for n in self.indice.nivel)
        self.indice.lineas.append(
            self.indice._formatear(numero, self.titulo, self.pagina)
        )
        self.indice.nivel.append(0)
        return self

    def __exit__(self, exc_type, exc_value, traceback):
        self.indice.nivel.pop()
        return False


if __name__ == "__main__":
    with Indice() as indice:
        with indice.seccion("Sistemas Operativos", pagina=1):
            indice.item("Windows", pagina=2)
            indice.item("MacOS", pagina=3)
            with indice.seccion("Distribuciones Linux", pagina=4):
                indice.item("Debian y derivados", pagina=5)
                indice.item("Arch y derivados", pagina=6)
        with indice.seccion("Lenguajes de programación", pagina=8):
            indice.item("Definición", pagina=9)
            with indice.seccion("Lenguajes compilados", pagina=10):
                indice.item("C y C++", pagina=11)
            with indice.seccion("Lenguajes interpretados", pagina=13):
                indice.item("Python", pagina=14)
                indice.item("JavaScript", pagina=15)
    indice.imprimir()
