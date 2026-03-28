import os
from openai import OpenAI
import pandas as pd
from datetime import datetime
from dotenv import load_dotenv

# 🔹 Cargar variables de entorno
load_dotenv()

# 🔹 Inicializar cliente OpenAI
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

# 🔹 Crear carpeta CSV si no existe
if not os.path.exists("data"):
    os.makedirs("data")

csv_file = "data/conversaciones.csv"
if not os.path.exists(csv_file):
    df = pd.DataFrame(columns=["fecha", "hora", "cliente", "respuesta", "tema"])
    df.to_csv(csv_file, index=False)

# 🔹 Función para mostrar comandos de ayuda
def mostrar_ayuda():
    print("\nComandos disponibles:")
    print("- salir / exit / quit → cerrar el bot")
    print("- ayuda → mostrar este mensaje")
    print("- resumen → mostrar últimas 5 conversaciones guardadas\n")

# 🔹 Función principal del bot
def main():
    print("🤖 AI Customer Support Bot")
    print("Escribe 'ayuda' para ver los comandos disponibles.\n")

    while True:
        mensaje = input("Cliente: ").strip()

        if mensaje.lower() in ["salir", "exit", "quit"]:
            print("Cerrando el bot... 👋")
            break
        elif mensaje.lower() == "ayuda":
            mostrar_ayuda()
            continue
        elif mensaje.lower() == "resumen":
            if os.path.exists(csv_file):
                df = pd.read_csv(csv_file)
                print("\nÚltimas 5 conversaciones:")
                print(df.tail(5)[["fecha", "hora", "cliente", "respuesta"]].to_string(index=False))
                print()
            else:
                print("No hay conversaciones guardadas todavía.\n")
            continue

        try:
            # 🔹 Llamada a la API de OpenAI
            response = client.chat.completions.create(
                model="gpt-4o-mini",
                messages=[
                    {"role": "system", "content": "Eres un asistente de atención al cliente profesional."},
                    {"role": "user", "content": mensaje}
                ]
            )

            respuesta = response.choices[0].message.content
            print("IA:", respuesta)

            # 🔹 Guardar conversación en CSV con fecha, hora y tema
            ahora = datetime.now()
            nuevo = pd.DataFrame([{
                "fecha": ahora.date(),
                "hora": ahora.strftime("%H:%M:%S"),
                "cliente": mensaje,
                "respuesta": respuesta,
                "tema": "general"
            }])
            nuevo.to_csv(csv_file, mode="a", header=False, index=False)

        except Exception as e:
            print(f"⚠️ Error al contactar con la IA: {e}\n")
            print("Revisa tu conexión o tu crédito disponible en OpenAI.\n")

if __name__ == "__main__":
    main()