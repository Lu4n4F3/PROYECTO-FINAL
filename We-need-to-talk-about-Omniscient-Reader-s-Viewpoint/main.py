from flask import Flask, render_template

app = Flask(__name__)

PAGINAS = [
    """<h1>Cap&iacute;tulo 1: El inicio del caos</h1>
    <p>Kim Dokja es un oficinista común y corriente que ha encontrado consuelo en algo que parece insignificante para los dem&aacute;s: una novela web llamada <i>Three Ways to Survive in a Ruined World</i> (TWSA). Durante años, ha sido el único lector fiel de esta historia, siguiendo cada capítulo sin falta. Para él, la novela es más que entretenimiento; es su escape de la realidad.</p>
    <p>Un día, su rutina cotidiana da un giro inesperado. Mientras viaja en el metro, recibe una notificación en su teléfono: el capítulo final de TWSA ha sido publicado. Emocionado, comienza a leerlo, sin saber que su vida está a punto de cambiar para siempre.</p>
    <p>De repente, una transmisión interrumpe el ambiente tranquilo del tren. Aparece una criatura conocida como Dokkaebi, que anuncia que el mundo tal como lo conocen ha terminado. A partir de ese momento, los pasajeros son forzados a participar en una serie de escenarios de supervivencia. Sin previo aviso, el mundo empieza a convertirse en un lugar apocalíptico, muy similar al que Dokja ha leído durante años.</p>
    <p>Pero Kim Dokja tiene algo que nadie más posee: el conocimiento completo de los eventos que están por suceder. Él es el único que ha leído hasta el final de la novela, y ahora esa información podría ser su única herramienta para sobrevivir en un mundo que se está derrumbando.</p>
    <p>El capítulo termina con Dokja dándose cuenta de que ya no es un simple lector pasivo. Ahora, él es parte de la historia.</p>
    """,

    """<h1>Capítulo 2: El primer escenario</h1>
    <p>El caos estalla en el tren mientras los pasajeros, desconcertados, intentan comprender lo que sucede. La criatura llamada Dokkaebi flota en el aire, sonriendo con una malicia inquietante. Anuncia que el primer escenario ha comenzado: los pasajeros deben matar a una persona antes de que pasen veinte minutos. Si no lo hacen, todos morirán.</p>
    <p>El ambiente se torna tenso. Nadie quiere creer que es real, pero pronto la realidad golpea con fuerza. Una pantalla flotante muestra un cronómetro que comienza la cuenta regresiva. La histeria y el miedo se apoderan de los pasajeros. Algunos intentan negociar con el Dokkaebi, pero la criatura simplemente se ríe. "Esto no es un juego", les dice. "Es una historia, y ustedes son los personajes secundarios".</p>
    <p>Kim Dokja, sin embargo, mantiene la calma. A diferencia de los demás, él sabe exactamente lo que está ocurriendo. Todo esto es parte del prólogo de Three Ways to Survive in a Ruined World. Conoce las reglas de los escenarios y entiende que no todos tienen que morir… si juegan bien sus cartas.</p>
    <p>A medida que los minutos pasan, un hombre desesperado intenta atacar a otro pasajero, pero Dokja interviene antes de que se desate la violencia. Utilizando su conocimiento de la novela, manipula la situación a su favor. Se acerca a un anciano que había quedado aislado del grupo y le ofrece un trato: "Si confías en mí, ambos podremos sobrevivir".</p>
    <p>El anciano, asustado pero sin otra opción, acepta. Dokja guía al hombre en el cumplimiento de la condición del escenario de una manera inesperada: en lugar de matar a una persona, sacrifican un animal que viajaba en el tren. Con ello, logran completar el objetivo sin derramar sangre humana, algo que nunca se había hecho en la novela original.</p>
    <p>El capítulo termina con Dokja reflexionando sobre una realidad inquietante: aunque conoce la historia, los eventos que están ocurriendo ya empiezan a desviarse del curso original. ¿Hasta qué punto su conocimiento lo ayudará a sobrevivir? ¿Y qué pasará cuando lo inesperado tome el control?</p>
    <p>Ahora, Dokja no solo es un lector omnisciente. También es un protagonista, y el mundo que creía conocer ha dejado de ser predecible.</p>""",
   
    """<h1>Capítulo 3: El despertar de Kim Dokja</h1>
    <p>El primer escenario ha terminado, pero el tren sigue sumido en un aire de incertidumbre y miedo. Los pasajeros que lograron sobrevivir apenas comprenden lo que acaba de suceder, pero Kim Dokja no pierde tiempo en procesar. Sabe que esto es solo el comienzo. El mundo ya no será el mismo.</p>
    <p>Mientras el Dokkaebi desaparece temporalmente, una pantalla flotante aparece frente a cada persona, mostrando su atributo personal. Es un sistema de estadísticas similar a los videojuegos, que mide habilidades como fuerza, agilidad e inteligencia. Sin embargo, cuando Dokja ve sus propios atributos, algo inesperado ocurre: en lugar de las habilidades tradicionales, aparece una habilidad única llamada "Lector Omnisciente".</p>
    <p>Esta habilidad le permite saber lo que los demás personajes piensan y sienten, siempre y cuando estén dentro de su "narrativa". Dokja entiende que su capacidad especial proviene de su conocimiento de Three Ways to Survive in a Ruined World. Él es el único que ha leído la novela completa, y su habilidad refleja eso: puede "leer" la historia del mundo como si aún fuera un lector.</p>
    <p>Pero hay un problema. La habilidad tiene un límite. No puede prever todo lo que ocurre, especialmente cuando los eventos se desvían del curso original de la novela. Dokja se da cuenta de que la historia está cambiando, y lo que parecía una ventaja ahora se siente como un riesgo constante.</p>
    <p>Mientras tanto, los demás pasajeros comienzan a organizarse. Algunos toman decisiones desesperadas, queriendo imponer su autoridad para sobrevivir. Uno de ellos, un hombre llamado Yoo Sangah, se acerca a Dokja. Ella parece confiar en él, pero también lo cuestiona: "¿Por qué no pareces tan sorprendido como los demás? ¿Sabías que esto iba a pasar?"</p>
    <p>Dokja no responde directamente. En lugar de eso, se prepara para lo que viene: el segundo escenario. Según la novela, debería ser un reto mucho más difícil y peligroso. Pero algo en su interior le dice que esta vez, incluso sus conocimientos podrían no ser suficientes.</p>
    <p>El capítulo termina con una pregunta que ronda en la mente de Dokja: "¿Y si yo también soy solo un personaje más de esta historia?"</p>""",

    """<h1>Capítulo 4: El segundo escenario</h1>
    <p>Tras sobrevivir al primer escenario, los pasajeros apenas tienen tiempo para recuperarse antes de que el Dokkaebi reaparezca con una sonrisa burlona. “Felicidades por seguir vivos… por ahora”, dice mientras anuncia el segundo escenario: los participantes deben cruzar un puente en ruinas que conecta dos edificios antes de que un enjambre de monstruos los alcance. El tiempo es limitado, y los que no lo logren serán devorados.</p>

    <p>Kim Dokja, observando las reacciones de pánico, sabe que el segundo escenario está diseñado para sembrar desesperación. Sin embargo, su conocimiento de la novela le da una ventaja. Él sabe que los monstruos no aparecen inmediatamente y que los primeros minutos son clave para planear una estrategia.</p>

    <p>Mientras los demás dudan, Dokja toma la iniciativa. Guía a un pequeño grupo de personas, incluyendo a Yoo Sangah y un hombre corpulento llamado Lee Hyunsung, un soldado que podría ser útil en futuros escenarios. Aunque Hyunsung está inicialmente desconfiado de Dokja, este logra ganarse su confianza al demostrar que sabe lo que está haciendo.</p>

    <p>Mientras cruzan el puente, los monstruos finalmente aparecen: bestias humanoides con ojos rojos y mandíbulas afiladas, moviéndose con una velocidad aterradora. Algunos participantes entran en pánico y caen al vacío, mientras otros intentan luchar, pero son rápidamente superados.</p>

    <p>Dokja, en cambio, mantiene la calma. Utiliza su habilidad Lector Omnisciente para prever los movimientos de los monstruos y guiar a su grupo con precisión. Sin embargo, pronto se da cuenta de algo alarmante: los monstruos son más fuertes y rápidos de lo que recordaba en la novela. Esto confirma lo que temía: los eventos se están desviando del curso original.</p>

    <p>Finalmente, logran cruzar el puente, pero no sin bajas. Dokja observa en silencio cómo los sobrevivientes restantes, agotados y traumatizados, intentan procesar lo que acaba de suceder. Sabe que esto es solo el principio de un viaje mucho más largo y peligroso.</p>"""
]

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/webtoon")
def webtoon():
    return render_template("webtoon.html")

@app.route("/personajes")
def personajes():
    return render_template("personajes.html")

@app.route("/galeria")
def galeria():
    return render_template("galeria.html")

@app.route("/conceptos")
def conceptos():
    return render_template("conceptos.html")

@app.route("/opinion")
def opinion():
    return render_template("opinion.html")

@app.route("/dokkaebis")
def dokkaebis():
    return render_template("Dokkaebis_Demonios_y_Dioses_Externos.html")

@app.route("/pagina/<int:numero>")
def mostrar_pagina(numero):
    if 1 <= numero <= len(PAGINAS):
        contenido = PAGINAS[numero - 1]
        return render_template(
            "pagina.html",
            contenido=contenido,
            pagina=numero,
            total=len(PAGINAS)
        )
    else:
        return "Página no encontrada", 404

if __name__ == "__main__":
    print("Ejecutando la aplicación principal...")
    app.run(debug=True)