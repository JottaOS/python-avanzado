from database import engine
from models import Character, CharacterType, Difficulty
from seed import seed
from sqlalchemy import select
from sqlalchemy.orm import Session


def queries():
    #  Un insert que inserte datos de un archivo de datos con formato de su preferencia
    #  con al menos 10 filas
    seed()

    # Un select filtrado
    with Session(engine) as session:
        print("\n======= Personajes SHOTO =======")
        statement = select(Character).where(Character.type == CharacterType.SHOTO)
        characters = session.execute(statement).all()

        for character in characters:
            print(character[0])
            print("=================")

    # Un update donde se cambian varios atributos de varios elementos de la tabla
    with Session(engine) as session:
        print("\n======= Actualizando personajes con dificultad EASY =======")
        statement = select(Character).where(Character.difficulty == Difficulty.EASY)
        characters = session.execute(statement).all()

        for character in characters:
            character_obj = character[0]
            # simulando que soy capcom
            character_obj.health += 250
            character_obj.max_damage_combo += 100
            session.add(character_obj)

        session.commit()
        print("Actualización completada.")

    # Eliminar algún dato sin sentido
    with Session(engine) as session:
        print("\n======= Eliminando a Ingrid del juego =======")
        statement = select(Character).where(Character.name == "Ingrid")
        characters = session.execute(statement).all()

        for character in characters:
            character_obj = character[0]
            session.delete(character_obj)

        session.commit()
        print("Juego mejorado.")
