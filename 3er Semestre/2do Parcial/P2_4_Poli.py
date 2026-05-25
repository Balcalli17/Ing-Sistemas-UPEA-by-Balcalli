class Cancion:
    def __init__(self, titulo, artista, duracion_segundos):
        self.titulo            = titulo
        self.artista           = artista
        self.duracion_segundos = duracion_segundos

    def __gt__(self, otra):
        return self.duracion_segundos > otra.duracion_segundos

    def __lt__(self, otra):
        return self.duracion_segundos < otra.duracion_segundos

    def __ge__(self, otra):
        return self.duracion_segundos >= otra.duracion_segundos

    def __le__(self, otra):
        return self.duracion_segundos <= otra.duracion_segundos

    def __eq__(self, otra):
        return self.duracion_segundos == otra.duracion_segundos

    def __str__(self):
        mins = self.duracion_segundos // 60
        segs = self.duracion_segundos % 60
        return f"Título: {self.titulo}, Artista: {self.artista}, Duración: {mins}:{segs:02d}"

# ── Programa principal ──
c1 = Cancion("Bohemian Rhapsody", "Queen",   354)
c2 = Cancion("Blinding Lights",   "The Weeknd", 200)
c3 = Cancion("Shape of You",      "Ed Sheeran", 234)

print(c1)
print(c2)
print(c3)

print(f"\nc1 > c2  : {c1 > c2}")
print(f"c2 < c3  : {c2 < c3}")
print(f"c1 >= c3 : {c1 >= c3}")
print(f"c2 == c3 : {c2 == c3}")

canciones = [c1, c2, c3]
mayor = max(canciones)
print(f"\nCanción más larga: {mayor.titulo}")
