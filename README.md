Batalla de Pokémon 🔥

¡Bienvenido a Batalla de Pokémon Este proyecto es un simulador de batallas Pokémon creado en Python. Permite que dos Pokémon luchen entre sí, considerando sus tipos, movimientos y estadísticas.

## Características

- **Tipos de Pokémon**: Compatible con los tipos básicos de Pokémon (fuego, agua, planta).
- **Movimientos**: Cada Pokémon tiene una lista de movimientos con diferentes efectos.
- **Sistema de batalla**: Implementa la lógica de batalla, incluyendo la ventaja de tipos y el cálculo de daño.

## Requisitos

- Python 3.x
- Numpy (`pip install numpy`)

AQUI TIENES PARA EJEMPLO,  DE INICIAR LAS BATALLAS...

# Crear Pokémon
charizard = pokemon('charizard', 'fuego', ['lanzallamas', 'pirotecnia', 'Giro fuego', 'Ascuas'], {'ataque': 12, 'defensa': 8})
blastoise = pokemon('Blastoise', 'agua', ['pistola agua', 'burbujas', 'hidropulso', 'hidrobomba'], {'ataque': 10, 'defensa': 10})

# Iniciar batalla
charizard.lucha(blastoise)
