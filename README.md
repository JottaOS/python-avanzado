# python-avanzado
Clases del curso Python Avanzado en la UAA

Utiliza [Ruff](https://docs.astral.sh/ruff/) como linter y formatter.

[uv](https://docs.astral.sh/uv/) para manejo de dependencias.

## Estructura
La estructura de las carpetas es la siguiente:

```t
.
├── README.md
└── clase_[n] # Cada clase tiene su propia carpeta
    ├── 1_tarea.py # Solución ejercicio 1
    ├── 2_tarea.py 
    └── recursos # Recursos proveídos por el profesor
        └── original.py
```

## Ejecución
Los scripts se ejecutan de la siguiente manera:
```bash
uv run python {filepath}
```
