# Ejercicio 3: Lista de reproducción de música usando la linker list proveida
from recursos.lista_enlazada import ListaEnlazada


class Utils:
    @staticmethod
    def sanitize(value: str | None) -> str:
        if value is None:
            return ""

        return value.lower().strip()


class MusicPlayer:
    def __init__(self):
        self.playlists: dict[str, ListaEnlazada] = {}

    def _validate_playlist_name(self, name: str | None) -> str | None:
        playlist_name = Utils.sanitize(name)

        if not playlist_name:
            print("El nombre de la playlist no puede estar vacío")
            return None

        return playlist_name

    def _validate_song_name(self, name: str | None) -> str | None:
        song_name = Utils.sanitize(name)

        if not song_name:
            print("El nombre de la canción no puede estar vacío")
            return None

        return song_name

    def _get_playlist(self, name: str) -> ListaEnlazada | None:
        playlist = self.playlists.get(name)

        if playlist is None:
            print("La playlist no existe")

        return playlist

    def create_playlist(self, name: str):
        playlist_name = self._validate_playlist_name(name)

        if playlist_name is None:
            return

        if playlist_name in self.playlists:
            print("Error: No puedes agregar una nueva playlist con el mismo nombre")
            return

        self.playlists[playlist_name] = ListaEnlazada()
        print("Playlist creada con éxito")

    def play_playlist(self, name: str):
        playlist_name = self._validate_playlist_name(name)
        if playlist_name is None:
            return

        found_playlist = self._get_playlist(playlist_name)
        if found_playlist is None:
            return

        print(f"Reproduciendo playlist {playlist_name}")
        found_playlist.recorrer()

    def add_song(self, playlist: str, song: str):
        playlist_name = self._validate_playlist_name(playlist)
        if playlist_name is None:
            return

        song_name = self._validate_song_name(song)
        if song_name is None:
            return

        found_playlist = self._get_playlist(playlist_name)
        if found_playlist is None:
            return

        if found_playlist.buscar(song_name):
            print("La canción ya está en esta playlist")
            return

        found_playlist.insertar_final(song_name)
        print("Canción agregada con éxito")

    def play_song(self, playlist: str, song: str):
        playlist_name = self._validate_playlist_name(playlist)
        if playlist_name is None:
            return

        song_name = self._validate_song_name(song)
        if song_name is None:
            return

        found_playlist = self._get_playlist(playlist_name)
        if found_playlist is None:
            return

        if found_playlist.buscar(song_name) is None:
            print("La canción no está en esta playlist")
            return

        print(f"Reproduciendo {song_name} de la playlist {playlist_name}")

    def list_playlists(self):
        if not self.playlists:
            print("No hay playlists disponibles")
            return

        print("Playlists disponibles:")
        for playlist_name in self.playlists:
            print(f"- {playlist_name}")


def main():
    player = MusicPlayer()
    while True:
        print("\nOpciones:")
        print("0. Listar playlists")
        print("1. Crear playlist")
        print("2. Agregar canción a playlist")
        print("3. Reproducir playlist")
        print("4. Reproducir canción de playlist")
        print("5. Salir")

        opcion = input("> ")
        match opcion:
            case "0":
                player.list_playlists()
            case "1":
                playlist_name = input("Ingrese el nombre de la playlist: ")
                player.create_playlist(playlist_name)
            case "2":
                playlist_name = input("Ingrese el nombre de la playlist: ")
                song_name = input("Ingrese el nombre de la canción: ")
                player.add_song(playlist_name, song_name)
            case "3":
                playlist_name = input("Ingrese el nombre de la playlist: ")
                player.play_playlist(playlist_name)
            case "4":
                playlist_name = input("Ingrese el nombre de la playlist: ")
                song_name = input("Ingrese el nombre de la canción: ")
                player.play_song(playlist_name, song_name)
            case "5":
                print("Saliendo del programa...")
                break
            case _:
                print("Opción inválida. Intente nuevamente.")


if __name__ == "__main__":
    main()
