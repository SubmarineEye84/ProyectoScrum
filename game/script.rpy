# Declare characters used by this game.
define Martín = Character('Martín', color="#f0ed54")
define Ana = Character('Ana', color="#be0049")
define Carlos = Character('Carlos', color="#0e91e9")
define María = Character('María', color="#930aee")
define Juan = Character('Juan', color="#30be30")
define Guia = Character('Guia', color="#b6118c")
# The game starts here.
label start:

    # Start by playing some music.
    play music "illurock.opus"

    scene bg start
    with fade

    "Martín y su equipo de Scrum Masters son convocados para una misión especial en un lugar remoto. La historia comienza con una introducción a la metodología Scrum y sus principales características, explicando su origen y su importancia en el desarrollo de proyectos ágiles."



    scene bg start
    with fade

    show byleth

    Martín "(Leyendo la invitación) Estimado Martín, has sido seleccionado para una misión especial. Te esperamos en un lugar remoto para embarcarte en una aventura única. Atentamente, El Guardián del Conocimiento Ágil."

    "El equipo de Scrum Masters se reúne, lleno de curiosidad y expectación. Martín les comparte la noticia y juntos comienzan a investigar sobre la misión y qué podría significar."

    "Después de una intensa discusión, llegan a la conclusión de que se trata de una oportunidad para aprender sobre una metodología ágil en particular: Scrum."


    Martín "¡Chicos, parece que nos están invitando a aprender más sobre Scrum! Sabemos que Scrum es una metodología ágil utilizada para el desarrollo de proyectos, pero no sabemos mucho más."

    Martín "¡Esta es una oportunidad emocionante para sumergirnos en el mundo de Scrum y descubrir sus secretos!"

    menu:

        "¿Quieres embarcarte en la aventura?"

        "¡Vamos allá!":

            jump si

        "No tengo ganas":

            jump no


label si:

    show byleth

    Martín "Scrum es una metodología que permite a los equipos adaptarse rápidamente a los cambios del entorno y del proyecto, promueve la colaboración y la comunicación efectiva entre los miembros del equipo, y fomenta la transparencia en todas las fases del desarrollo."

    Martín "Estoy emocionado por descubrir más sobre Scrum y cómo podemos aplicarla en nuestros proyectos para mejorar nuestros resultados."

    "Con esta introducción a Scrum y sus principales características, Martín y su equipo se preparan para embarcarse en su aventura y aprender más sobre esta metodología ágil. Están listos para enfrentar los desafíos que se les presenten y descubrir los secretos del Scrum en su viaje."
    
    "La historia está lista para continuar con el primer acto: 'El llamado a la aventura'."

    scene bg montaña
    with fade

    "Martín y su equipo de Scrum Masters llegan al lugar remoto de la reunión, ansiosos por descubrir qué les espera. Se encuentran en una cabaña en la base de una imponente montaña, rodeados por un paisaje natural y salvaje."
    
    "Aparece un guía local que los llevará en su aventura."

    show roy

    Guia "¡Bienvenidos a la montaña de los desafíos! Para llegar a su destino final y descubrir los secretos del Scrum, tendrán que escalar esta montaña."

    hide roy
    show byleth

    "El equipo se sorprende y se emociona con el desafío que les espera. Martín y su equipo intercambian miradas determinadas y aceptan el reto sin dudarlo."

    Martín "¡Vamos allá! Estamos listos para enfrentar cualquier obstáculo que se presente en nuestro camino y descubrir los secretos del Scrum en esta aventura."

    hide byleth

    "El equipo se prepara con su equipo de escalada y comienza a ascender la montaña. A medida que avanzan, enfrentan diversos obstáculos que simbolizan los retos que se presentan en un proyecto Scrum:"

    "Desprendimientos de rocas que bloquean el camino, puentes colgantes inestables que requieren trabajo en equipo para cruzar, cambios climáticos repentinos que ponen a prueba su adaptabilidad, y senderos confusos que demandan una comunicación clara y eficaz."

    "A pesar de los desafíos, el equipo de Scrum Masters muestra una gran colaboración y adaptabilidad. Trabajan juntos para superar cada obstáculo, aplicando los principios y valores de Scrum en su camino hacia la cima de la montaña."

    "Aprenden a confiar en su equipo y a utilizar la transparencia y la comunicación efectiva para superar los desafíos."


    "Después de enfrentar varios obstáculos y de un arduo esfuerzo, el equipo finalmente alcanza una plataforma en la cima de la montaña. Se encuentran agotados pero también emocionados por lo que han aprendido en su aventura."

    show bg top moun
    show byleth

    Martín "¡Lo logramos! Aprendimos mucho en este desafío. La colaboración, la adaptabilidad y la comunicación efectiva son clave para enfrentar los retos en un proyecto Scrum. Estoy orgulloso de cada uno de ustedes."

    "El equipo celebra su éxito y se prepara para continuar con su viaje hacia el destino final, ansiosos por descubrir más sobre Scrum y cómo aplicar sus enseñanzas en su trabajo diario."
    
    "La historia está lista para avanzar al siguiente acto: (El encuentro con el Guardián del Conocimiento Ágil."

    "Martín y su equipo de Scrum Masters continúan su ascenso por la montaña, enfrentándose a una serie de desafíos en el camino. A pesar de su entusiasmo inicial, pronto se dan cuenta de que no todo será fácil en esta aventura."

    "En un momento, el equipo se encuentra en un cruce de caminos confuso, donde la falta de comunicación entre ellos crea confusión y desorden."

    hide byleth
    show lucina


    Ana "Creo que debemos tomar el camino de la izquierda."

    hide lucina
    show robin

    Carlos "¡No, estoy seguro de que es el camino de la derecha!"

    hide robin

    menu:

        "¿Que camino eliges?"

        "Izquierda":

            jump izquierda

        "Derecha":

            jump derecha

        "Decidir como equipo":
            
            jump equipo

label equipo:

    "El equipo se encuentra en desacuerdo y la falta de transparencia y claridad en la comunicación crea tensión entre ellos. Martín, como líder del equipo, se da cuenta de que deben resolver este problema para seguir adelante."

    show byleth

    Martín "¡Detengámonos un momento! La comunicación es clave en Scrum. Necesitamos ser transparentes y compartir nuestras ideas y puntos de vista de manera clara y respetuosa. Escuchémonos mutuamente y encontremos una solución juntos."

    "El equipo se toma un momento para escucharse y compartir sus ideas. Finalmente, llegan a un consenso y deciden tomar el camino de la izquierda. Aprenden que la comunicación efectiva es fundamental para evitar malentendidos y mantenerse en el camino correcto en un proyecto Scrum."

    hide byleth

    show bg cave 2
    
    "Más adelante, el equipo se encuentra con la resistencia al cambio por parte de algunos miembros del equipo. Algunos Scrum Masters muestran resistencia a adoptar nuevas prácticas ágiles y a abandonar antiguas formas de trabajo."

    show corrin

    María "Pero siempre lo hemos hecho así, ¿por qué tenemos quse cambiar ahora?"

    hide corrin
    show ike

    Juan "No estoy seguro de que esta nueva forma de trabajo funcione para nosotros. Prefiero seguir con lo conocido."

    hide ike

    "Martín se da cuenta que la resistencia al cambio puede ser un obstáculo en la implementiación exitosa de Scrum y decide abordar el problema"

    show byleth

    Martín "Entiendo que el cambio puede ser difícil, pero como equipo de Scrum Masters, debemos estar dispuestos a adaptarnos y mejorar constantemente."

    Martín "Scrum es una metodología ágil que nos permite ser flexibles y adaptarnos a las necesidades del proyecto. Confíen en el proceso y trabajemos juntos para superar esta resistencia al cambio."

    
    return


    label izquierda:

        María "XD"
        return

    label derecha:

        return
    label no:

    "Decidiste no ir, no obtuviste el conocimiento de SCRUM"

    scene black
    with dissolve

    "Pero podrias cambiar esa decision..."

    "¿Estaras dispuesto a tomar el reto esta vez?"

    "Toma valor y afronta el reto..."

    "{b}Bad Ending{/b}."

    return