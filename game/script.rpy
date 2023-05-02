# Declare characters used by this game.
define Martín = Character('Martín', color="#f0ed54") #Byleth
define Ana = Character('Ana', color="#be0049") #Lucina
define Carlos = Character('Carlos', color="#0e91e9") #Roy
define María = Character('María', color="#930aee") #Corrin
define Juan = Character('Juan', color="#30be30") #Ike
define Guia = Character('Guia', color="#b6118c") #Robin
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

    menu Caminos:

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

    hide byleth

    "Con paciencia y perseverancia, Martín y su equipo logran superar la resistencia al cambio y continúan su ascenso hacia la cima de la montaña."

    "Finalmente, el equipo enfrenta un último desafío: la falta de compromiso con los objetivos del proyecto."

    "Algunos Scrum Masters muestran falta de motivación y compromiso, lo que afecta la cohesión y la eficacia del equipo."

    show byleth

    Martín "Chicos, es importante que estemos comprometidos con los objetivos del proyecto. Solo trabajando juntos y demostrando un compromiso sólido podremos llegar a la cima y alcanzar el éxito en nuestra misión. Hagamos un esfuerzo extra y mantengamos la visión clara en mente."

    hide byleth

    "El equipo reflexiona sobre la importancia del compromiso y la responsabilidad individual."

    show ike

    Juan "Tienes razón, Martín. No podemos permitirnos perder la visión del proyecto. Estoy comprometido y dispuesto a dar lo mejor de mí para alcanzar nuestros objetivos."

    hide ike
    show corrin

    María "Yo también. A veces es fácil perder de vista el panorama general, pero ahora entiendo que mi compromiso es crucial para el éxito del equipo"

    hide corrin

    "Con el compromiso renovado, el equipo de Scrum Masters continúa su ascenso con renovada energía y determinación."
    
    "Aprenden que el compromiso y la responsabilidad individual son fundamentales en un proyecto Scrum, ya que cada miembro del equipo debe estar alineado con los objetivos comunes."

    "A lo largo del camino, el equipo también se da cuenta de la importancia de la adaptabilidad. Se encuentran con situaciones inesperadas, como cambios en las condiciones climáticas, senderos bloqueados y otros obstáculos que los obligan a ajustar su plan original."

    show robin

    Carlos "Parece que el sendero que planeamos tomar está bloqueado. Tenemos que encontrar una ruta alternativa."

    hide robin
    show ike

    Juan "Sí, debemos ser flexibles y adaptarnos a las circunstancias cambiantes. ¿Qué tal si tomamos el sendero de la derecha en su lugar?"

    hide ike

    "El equipo trabaja juntos para encontrar soluciones creativas y adaptarse a los cambios en el camino, aplicando los principios ágiles de Scrum."
    
    "Aprenden que la adaptabilidad es esencial en un entorno empresarial y que deben estar dispuestos a ajustar su enfoque según las necesidades del proyecto."

    "Con cada desafío superado y cada lección aprendida, el equipo de Scrum Masters se vuelve más cohesionado y efectivo."
    
    "Han aprendido la importancia de la comunicación, la resistencia al cambio, el compromiso y la adaptabilidad en el contexto de Scrum, y han aplicado estos principios en su camino hacia la cima de la montaña."

    jump acto2

    label izquierda:
        show lucina

        Ana "Vamos por acá, ¡rápido!"

        hide lucina
        show robin

        Carlos "Te he dicho que a la derecha, ¿porque debemos hacer lo que dices tu?"

        Carlos "Yo no iré hacia ese camino"

        hide robin
        show lucina

        Ana "¡Ay por el amor de dios!"

        hide lucina
        jump Caminos

    label derecha:
        show robin

        Carlos "Como les decia, creo firmemente que la opción a elegir es ir a la derecha"

        hide robin
        show lucina

        Ana "Pero si la izquierda se mira completamente mejor que la derecha, vamos mejor allá"
        hide lucina
        show robin

        Carlos "¡No, hagan lo que yo digo!"

        hide robin
        jump Caminos

    label acto3:

    show ike

    Juan "¡Miren esto! ¡Un antiguo libro en el templo! Parece que contiene la esencia misma de la metodología Scrum."

    hide ike
    show byleth

    Martín "Increíble, ¿verdad? Vamos a explorar su contenido y descubrir lo que podemos aprender."

    hide byleth

    "El equipo de Scrum Masters se sumerge en la lectura del antiguo libro y descubre los principios fundamentales de Scrum y cómo aplicarlos en su trabajo diario."
    
    "A medida que leen, se dan cuenta de que han estado aplicando algunos de los conceptos de Scrum de manera superficial, pero que ahora tienen una comprensión más profunda y completa de la metodología"

    Scrum Master 11: "Esto es asombroso. Ahora entiendo la importancia de la inspección y adaptación continua en nuestros proyectos Scrum. También puedo ver cómo podemos mejorar nuestra transparencia y colaboración."
 
    Scrum Master 12: "Sí, definitivamente. También me doy cuenta de cómo podemos mejorar la gestión de nuestro backlog y la planificación de sprints para hacer nuestro trabajo más eficiente."
 
    "El equipo de Scrum Masters discute y comparte ideas sobre cómo aplicar los principios de Scrum de manera más efectiva en su trabajo."
    
    "Se dan cuenta de que hay áreas de mejora y oportunidades para aplicar lo que han aprendido en el antiguo libro en sus proyectos actuales y futuros."
 
    Scrum Master 13: "Creo que ahora tenemos una comprensión mucho más profunda de Scrum y cómo puede ayudarnos a enfrentar los retos en nuestros proyectos. Estoy emocionado de implementar estos cambios y ver los resultados."
 
    Scrum Master 14: "Sí, definitivamente. Creo que este descubrimiento en el templo ha sido un punto de inflexión para nuestro equipo. Estoy ansioso por compartir lo que hemos aprendido con el resto del equipo y seguir mejorando."
 
    "El equipo de Scrum Masters sale del templo con una nueva perspectiva y una comprensión más profunda de Scrum. Han superado los desafíos en su camino hacia la cima de la montaña y han descubierto el conocimiento valioso en el antiguo libro."
    
    "Ahora están preparados para aplicar lo que han aprendido en sus proyectos y llevar a su equipo a un nuevo nivel de eficiencia y colaboración."

    jump casa

    label casa:

    Scrum Master 9: "¡Ya estamos de regreso en casa! Es hora de poner en práctica todo lo que hemos aprendido en el templo y llevar nuestros proyectos Scrum al siguiente nivel."
 
    Scrum Master 10: "¡Exactamente! Vamos a compartir nuestras experiencias con nuestros equipos y comenzar a implementar los principios de Scrum en nuestros proyectos reales."
 
    "El equipo de Scrum Masters se reúne con sus respectivos equipos y comparte sus conocimientos y aprendizajes del antiguo libro. Explican los principios de Scrum y cómo pueden ser aplicados en su trabajo diario para mejorar la eficiencia y la calidad de los proyectos."
 
    Equipo de Desarrollo 1: "Esto suena realmente interesante. Creo que podemos aplicar el principio de inspección y adaptación en nuestras reuniones diarias de seguimiento del progreso del proyecto."
 
    Equipo de Desarrollo 2: "Sí, definitivamente. También podemos mejorar la transparencia compartiendo información relevante en nuestro tablero de trabajo y en nuestras reuniones de revisión del sprint."
 
    "El equipo de Scrum Masters trabaja en estrecha colaboración con sus equipos para implementar las herramientas y prácticas de Scrum en sus proyectos reales. Se enfrentan a desafíos y obstáculos en el camino, pero utilizan los principios de Scrum para adaptar la metodología a sus necesidades específicas."
 
    Scrum Master 11: "Es genial ver cómo nuestros equipos están adoptando los principios de Scrum y cómo están mejorando la colaboración y la transparencia en nuestros proyectos."
 
    Scrum Master 12: "Sí, definitivamente. También estamos entregando valor a nuestros clientes de una manera más efectiva gracias a las prácticas de Scrum que estamos implementando."
 
    "A medida que el tiempo pasa, el equipo de Scrum Masters y sus equipos experimentan una mejora en la eficiencia y la calidad de sus proyectos. Los clientes están más satisfechos con los resultados y los equipos están más comprometidos y colaborativos en su trabajo."
 
    "El guión concluye con el equipo de Scrum Masters celebrando el éxito de la implementación de Scrum en sus proyectos reales. Se dan cuenta de que la aventura en el templo fue una experiencia transformadora que les permitió mejorar su enfoque de trabajo y obtener resultados positivos en sus proyectos ágiles."

 
    Martín: "¡Y así concluye nuestra aventura con Scrum! Hemos aprendido mucho en nuestro viaje y ahora es el momento de reflexionar sobre lo que hemos aprendido."
 
    "El equipo de Scrum Masters y otros participantes se reúnen en una sesión de resumen y reflexión, donde discuten los principios fundamentales de Scrum y cómo han aplicado la metodología en sus contextos y proyectos específicos."
 
    Scrum Master 1: "Una de las cosas que más me gustó de Scrum es el enfoque en la colaboración y la transparencia. Ha mejorado nuestra comunicación interna y nos ha permitido trabajar de manera más eficiente como equipo."
 
    Scrum Master 2: "Definitivamente, ha sido una experiencia transformadora. El principio de inspección y adaptación nos ha permitido mejorar constantemente y adaptarnos a los cambios en el entorno del proyecto."
 
    Martín: "Sí, y también me ha gustado cómo Scrum nos ha ayudado a entregar valor a nuestros clientes de una manera más rápida y efectiva. Nuestros proyectos han sido más exitosos desde que implementamos Scrum en nuestra organización."
 
    Scrum Master 3: "¡Y también hemos aprendido la importancia de la adaptabilidad! Cada proyecto es diferente y Scrum nos ha brindado la flexibilidad necesaria para ajustarnos a las necesidades cambiantes de nuestros clientes y del mercado."
 
    "Se anima a los participantes a seguir aprendiendo y mejorando en su práctica de Scrum. Se destacan los beneficios de compartir experiencias y conocimientos con la comunidad de Scrum, creando un legado duradero en la implementación exitosa de la metodología en su organización"
 
    Martín: "Es importante seguir aprendiendo y mejorando en nuestra práctica de Scrum. También debemos compartir nuestras experiencias y conocimientos con la comunidad de Scrum para que más personas puedan beneficiarse de esta metodología ágil."
 
    Scrum Master 4: "Sí, definitivamente. Crear un legado duradero en la implementación exitosa de Scrum en nuestra organización es fundamental. Sigamos aprendiendo, compartiendo y mejorando juntos."


    label no:

    "Decidiste no ir, no obtuviste el conocimiento de SCRUM"

    scene black
    with dissolve

    "Pero podrias cambiar esa decision..."

    "¿Estaras dispuesto a tomar el reto esta vez?"

    "Toma valor y afronta el reto..."

    "{b}Bad Ending{/b}."

    return