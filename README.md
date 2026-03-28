# AI Customer Support Bot

Bot de atención al cliente usando OpenAI GPT-4o-mini.

## Características

- Chat interactivo en bucle.
- Comandos disponibles:
  - `ayuda` → muestra la lista de comandos
  - `resumen` → muestra las últimas 5 conversaciones
  - `salir` → cierra el bot
- Guardado automático de conversaciones en CSV (`fecha`, `hora`, `cliente`, `respuesta`, `tema`).
- Manejo de errores cuando no hay crédito disponible.

## Requisitos

- Python 3.10 o superior
- Librerías: `openai`, `pandas`, `python-dotenv`

## Instalación

1. Clonar el repositorio:

```bash
git clone https://github.com/tu_usuario/AI_Customer_Support.git
cd AI_Customer_Support