#!/usr/bin/python
# -*- coding: latin-1 -*-

"""
Rigoberto Sáenz Imbacuán
Desarrollador para Dispositivos Móviles - Colombia Games
Ingeniero de Sistemas y Computación - Universidad Nacional de Colombia
http://www.rigobertosaenz.com/
"""
from src.Controller import eActivityId, ResourceController, eQuestionAnswer, \
    GlobalsController, eGameDifficulty


class Activity:

    def __init__(self, id):
        
        self.id = id
        
        self.description = list()
        self.description.append("")
        self.description.append("")
        self.description.append("")
        self.description.append("")
        self.description.append("")
        self.description.append("")
        self.description.append("")
        self.description.append("")
        self.description.append("")
        self.description.append("")
        self.description.append("")
        self.description.append("")
        
        self.question = list()
        self.question.append("")
        self.question.append("")
        self.question.append("")
        self.question.append("")
        
        self.optionA = list()
        self.optionA.append("")
        self.optionA.append("")
        
        self.optionB = list()
        self.optionB.append("")
        self.optionB.append("")
        
        self.optionC = list()
        self.optionC.append("")
        self.optionC.append("")
        
        if id == eActivityId._01_BICICROS:
            self.name = "Bicicrós"
            self.image = ResourceController.game_Activity01Bicicros
            self.answer = eQuestionAnswer.ANSWER_B
            
            self.description[0] = "El Bicicrós se originó"
            self.description[1] = "en California en 1.970,"
            self.description[2] = "cuando los jóvenes"
            self.description[3] = "intentaban imitar a"
            self.description[4] = "los campeones de otro"
            self.description[5] = "deporte usando sus"
            self.description[6] = "bicicletas."
            
            self.question[0] = "¿Cuál de estos deportes sería?"
            
            self.optionA[0] = "Ciclismo profesional"
            self.optionB[0] = "Motocross"
            self.optionC[0] = "Ciclismo de montaña"
            
        elif id == eActivityId._02_PATINAJE:
            self.name = "Patinaje"
            self.image = ResourceController.game_Activity02Patinaje
            self.answer = eQuestionAnswer.ANSWER_B
            
            self.description[0] = "El patinaje puede ser"
            self.description[1] = "de dos tipos: El"
            self.description[2] = "clásico que se"
            self.description[3] = "realiza con patines de"
            self.description[4] = "4 ruedas, y el patinaje"
            self.description[5] = "en línea que se realiza"
            self.description[6] = "con patines que tienen"
            self.description[7] = "entre 3 y cinco ruedas"
            self.description[8] = "ubicadas en línea recta."
            
            self.question[0] = "¿Cuál de estos crees que es?"
            
            self.optionA[0] = "Skateboard"
            self.optionB[0] = "Patinaje"
            self.optionC[0] = "Carreras de cuatrimotos"
            
        elif id == eActivityId._03_FUTSAL:
            self.name = "Futsal"
            self.image = ResourceController.game_Activity03Futsal
            self.answer = eQuestionAnswer.ANSWER_B

            self.description[0] = "El fútbol de salón es"
            self.description[1] = "un deporte colectivo"
            self.description[2] = "de pelota practicado"
            self.description[3] = "entre dos equipos de 5"
            self.description[4] = "jugadores cada uno,"
            self.description[5] = "dentro de una cancha"
            self.description[6] = "de suelo duro."
            
            self.question[0] = "¿Con qué otro nombre se"
            self.question[1] = "conoce este deporte?"
            
            self.optionA[0] = "Balón mano"
            self.optionB[0] = "Microfútbol"
            self.optionC[0] = "Bochas"
            
        elif id == eActivityId._04_FUTBOL:
            self.name = "Fútbol"
            self.image = ResourceController.game_Activity04Futbol
            self.answer = eQuestionAnswer.ANSWER_A
            
            self.description[0] = "El fútbol es el deporte"
            self.description[1] = "más popular del mundo"
            self.description[2] = "que además favorece la"
            self.description[3] = "realización de"
            self.description[4] = "actividad física."
            self.description[5] = "Durante un partido de"
            self.description[6] = "fútbol profesional de"
            self.description[7] = "90 minutos, un jugador"
            self.description[8] = "recorre entre 6 y 11"
            self.description[9] = "kilómetros."
            
            self.question[0] = "¿Sabes en cuál país se realizó"
            self.question[1] = "el primer mundial de fútbol?"
            
            self.optionA[0] = "Uruguay"
            self.optionB[0] = "Brasil"
            self.optionC[0] = "Inglaterra"
            
        elif id == eActivityId._05_PORRISMO:
            self.name = "Porrismo"
            self.image = ResourceController.game_Activity05Porrismo
            self.answer = eQuestionAnswer.ANSWER_C
            
            self.description[0] = "El porrismo consiste en"
            self.description[1] = "el uso organizado de"
            self.description[2] = "música, baile y"
            self.description[3] = "gimnasia para hacer que"
            self.description[4] = "los aficionados animen"
            self.description[5] = "a sus equipos en los"
            self.description[6] = "partidos."

            self.question[0] = "¿En cuál de estos deportes"
            self.question[1] = "no se hace animación con"
            self.question[2] = "porras?"
            
            self.optionA[0] = "Fútbol"
            self.optionB[0] = "Baloncesto"
            self.optionC[0] = "Ajedrez"
            
        elif id == eActivityId._06_ATLETISMO:
            self.name = "Atletismo"
            self.image = ResourceController.game_Activity06Atletismo
            self.answer = eQuestionAnswer.ANSWER_B

            self.description[0] = "Es el arte de superar"
            self.description[1] = "el rendimiento de los"
            self.description[2] = "adversarios en"
            self.description[3] = "velocidad, resistencia,"
            self.description[4] = "distancia o  altura."
            self.description[5] = "Contiene un gran"
            self.description[6] = "conjunto de disciplinas"
            self.description[7] = "agrupadas en carreras,"
            self.description[8] = "saltos, lanzamientos,"
            self.description[9] = "pruebas combinadas y"
            self.description[10]= "marcha."

            
            self.question[0] = "¿Sabes cuál es la carrera"
            self.question[1] = "más corta que pueden correr"
            self.question[2] = "los atletas?"
            
            self.optionA[0] = "100 metros"
            self.optionB[0] = "60 metros"
            self.optionC[0] = "200 metros"
            
        elif id == eActivityId._07_BALONCESTO:
            self.name = "Baloncesto"
            self.image = ResourceController.game_Activity07Baloncesto
            self.answer = eQuestionAnswer.ANSWER_A
            
            self.description[0] = "Es un deporte de equipo,"
            self.description[1] = "en el que dos conjuntos"
            self.description[2] = "de 5 jugadores cada uno,"
            self.description[3] = "intentan anotar puntos,"
            self.description[4] = "introduciendo un balón"
            self.description[5] = "en un aro colocado a"
            self.description[6] = "3,05 metros del suelo."
            
            self.question[0] = "¿Cuánto dura cada uno de"
            self.question[1] = "los tiempos de juego?"
            
            self.optionA[0] = "15 minutos"
            self.optionB[0] = "10 minutos"
            self.optionC[0] = "12 minutos"
            
        elif id == eActivityId._08_KARATE_DO:
            self.name = "Karate Do"
            self.image = ResourceController.game_Activity08KarateDo
            self.answer = eQuestionAnswer.ANSWER_B
            
            self.description[0] = "El Karate Do no solo trata"
            self.description[1] = "sobre el acondicionamiento"
            self.description[2] = "físico, el estudio de"
            self.description[3] = "los katas y el combate"
            self.description[4] = "real o deportivo. "
            self.description[5] = "También va de la"
            self.description[6] = "mano con el desarrollo "
            self.description[7] = "vivencial de la parte "
            self.description[8] = "humana y la parte "
            self.description[9] = "espiritual, el "
            self.description[10] = "crecimiento como"
            self.description[11] = "personas y ciudadanos."
            
            self.question[0] = "¿Además del componente deportivo,"
            self.question[1] = "qué otro componente tiene el"
            self.question[2] = "karate Do?"
            
            self.optionA[0] = "Empresarial"
            self.optionB[0] = "Espiritual"
            self.optionC[0] = "Individual"
            
        elif id == eActivityId._09_LEVANTAMIENTO_DE_PESAS:
            self.name = "Levantamiento de Pesas"
            self.image = ResourceController.game_Activity09LevantamientoDePesas
            self.answer = eQuestionAnswer.ANSWER_A
            
            self.description[0] = "Es un deporte que "
            self.description[1] = "consiste en el "
            self.description[2] = "levantamiento de la "
            self.description[3] = "mayor cantidad de peso"
            self.description[4] = "posible en una barra en"
            self.description[5] = "cuyos extremos se fijan"
            self.description[6] = "varios discos, los "
            self.description[7] = "cuales determinan el "
            self.description[8] = "peso final que se "
            self.description[9] = "levanta."
            
            self.question[0] = "¿Qué otro nombre recibe el"
            self.question[1] = "levantamiento de pesas?"
            
            self.optionA[0] = "Halterofilia"
            self.optionB[0] = "Skeleton"
            self.optionC[0] = "Biatlón"
            
        elif id == eActivityId._10_TAEKWON_DO:
            self.name = "Taekwon Do"
            self.image = ResourceController.game_Activity10TaekwonDo
            self.answer = eQuestionAnswer.ANSWER_B
            
            self.description[0] = "El Taekwon Do se destaca"
            self.description[1] = "por la variedad y"
            self.description[2] = "espectacularidad de sus"
            self.description[3] = "técnicas de patada, se"
            self.description[4] = "basa fundamentalmente"
            self.description[5] = "en artes marciales como el"
            self.description[6] = "Kung fu o Wu Shu Chino."
            
            self.question[0] = "¿Cuáles de estos tres son los"
            self.question[1] = "colores correctos de algunos"
            self.question[2] = "grados básicos del taekwon do?"
            
            self.optionA[0] = "Verde, naranja, negro"
            self.optionB[0] = "Verde, azul, negro"
            self.optionC[0] = "Verde, amarillo, negro"
            
        elif id == eActivityId._11_BADMINTON:
            self.name = "Bádminton"
            self.image = ResourceController.game_Activity11Badminton
            self.answer = eQuestionAnswer.ANSWER_A
            
            self.description[0] = "A diferencia de otros "
            self.description[1] = "deportes de raqueta, en"
            self.description[2] = "el bádminton no se juega"
            self.description[3] = "con pelota, sino con un"
            self.description[4] = "proyectil llamado "
            self.description[5] = "volante, plumilla "
            self.description[6] = "o gallito."
            
            self.question[0] = "Cada partido de bádminton se"
            self.question[1] = "juega a:"
            
            self.optionA[0] = "21 puntos"
            self.optionB[0] = "18 puntos"
            self.optionC[0] = "25 puntos"
            
        elif id == eActivityId._12_TENIS_DE_MESA:
            self.name = "Tenis de Mesa"
            self.image = ResourceController.game_Activity12TenisDeMesa
            self.answer = eQuestionAnswer.ANSWER_B

            self.description[0] = "El tenis de mesa, es un"
            self.description[1] = "deporte de raqueta, que"
            self.description[2] = "se disputa entre dos"
            self.description[3] = "jugadores o dos parejas"
            self.description[4] = "(dobles)"

            self.question[0] = "¿Con qué otro nombre se conoce"
            self.question[1] = "al tenis de mesa?"
            
            self.optionA[0] = "Golf"
            self.optionB[0] = "Ping pong"
            self.optionC[0] = "Bádminton"
            
        elif id == eActivityId._13_ESGRIMA:
            self.name = "Esgrima"
            self.image = ResourceController.game_Activity13Esgrima
            self.answer = eQuestionAnswer.ANSWER_B

            self.description[0] = "La esgrima es un deporte"
            self.description[1] = "de combate en el que se"
            self.description[2] = "enfrentan dos "
            self.description[3] = "contrincantes que deben"
            self.description[4] = "intentar tocarse con un"
            self.description[5] = "arma especial, sin"
            self.description[6] = "hacerse ningún daño."
            
            self.question[0] = "¿Cuáles de estos crees que son"
            self.question[1] = "los nombres de las armas con"
            self.question[2] = "las que se practica la"
            self.question[3] = "esgrima?"
            
            self.optionA[0] = "Espada, sable, lanza"
            self.optionB[0] = "Espada, sable, florete"
            self.optionC[0] = "Espada, sable, bayoneta"
            
        elif id == eActivityId._14_GIMNASIA_ARTISTICA:
            self.name = "Gimnasia Artística"
            self.image = ResourceController.game_Activity14GimnasiaArtistica
            self.answer = eQuestionAnswer.ANSWER_C
            
            self.description[0] = "Las presentaciones en la"
            self.description[1] = "gimnasia artística son"
            self.description[2] = "generalmente"
            self.description[3] = "individuales y tienen"
            self.description[4] = "una duración promedio"
            self.description[5] = "entre treinta y noventa"
            self.description[6] = "segundos, que se"
            self.description[7] = "realizan en diferentes"
            self.description[8] = "aparatos o en el suelo"
            self.description[9] = "usando elementos como"
            self.description[10]= "balones o cintas."
            
            self.question[0] = "¿Cuál de estas ideas sobre"
            self.question[1] = "la gimnasia es correcta?"
            
            self.optionA[0] = "La gimnasia es muy difícil"
            self.optionA[1] = "para los hombres"
            self.optionB[0] = "Para practicar gimnasia solo"
            self.optionB[1] = "hay que ser flexible"
            self.optionC[0] = "La gimnasia puede ser practicada"
            self.optionC[1] = "por hombres y por mujeres"
            
        elif id == eActivityId._15_AJEDREZ:
            self.name = "Ajedrez"
            self.image = ResourceController.game_Activity15Ajedrez
            self.answer = eQuestionAnswer.ANSWER_B
            
            self.description[0] = "El ajedrez es un juego "
            self.description[1] = "competitivo entre dos "
            self.description[2] = "personas, cada una de "
            self.description[3] = "las cuales dispone de"
            self.description[4] = "16 piezas móviles que "
            self.description[5] = "se colocan sobre un "
            self.description[6] = "tablero dividido en "
            self.description[7] = "64 partes."
            
            self.question[0] = "¿Cuáles de las siguientes son"
            self.question[1] = "piezas del ajedrez?"
            
            self.optionA[0] = "Dama, caballo, lacayo"
            self.optionB[0] = "Dama, alfil, caballo"
            self.optionC[0] = "Dama, caballo, sainete"
            
        elif id == eActivityId._16_AEROBICOS:
            self.name = "Aeróbicos"
            self.image = ResourceController.game_Activity16Aerobicos
            self.answer = eQuestionAnswer.ANSWER_B
            
            self.description[0] = "El ejercicio aeróbico "
            self.description[1] = "mejora la función "
            self.description[2] = "cardiovascular, reduce"
            self.description[3] = "grasa corporal, baja los"
            self.description[4] = "niveles de colesterol "
            self.description[5] = "total en la sangre y"
            self.description[6] = "mejora la capacidad "
            self.description[7] = "pulmonar, la circulación"
            self.description[8] = "en general y el "
            self.description[9] = "aprovechamiento del "
            self.description[10] = "oxígeno."
            
            self.question[0] = "¿Cuál de los siguientes"
            self.question[1] = "beneficios es generado"
            self.question[2] = "al prácticar aeróbicos?"
            
            self.optionA[0] = "Mejora la digestión"
            self.optionB[0] = "Mejora la capacidad pulmonar"
            self.optionC[0] = "Mejora la capacidad de pensar"
            
        elif id == eActivityId._17_NATACION:
            self.name = "Natación"
            self.image = ResourceController.game_Activity17Natacion
            self.answer = eQuestionAnswer.ANSWER_A
            
            self.description[0] = "La natación es el "
            self.description[1] = "movimiento y/o "
            self.description[2] = "desplazamiento a través"
            self.description[3] = "del agua mediante el uso"
            self.description[4] = "de los brazos y las"
            self.description[5] = "piernas y por lo "
            self.description[6] = "general sin utilizar"
            self.description[7] = "ningún instrumento "
            self.description[8] = "artificial."
            
            self.question[0] = "¿Cuáles de estos son los"
            self.question[1] = "estilos de natación?"
            
            self.optionA[0] = "Pecho, mariposa y espalda"
            self.optionB[0] = "Mariposa, espalda y relevos"
            self.optionC[0] = "Pecho, mariposa y subacuático"
            
        elif id == eActivityId._18_BOXEO:
            self.name = "Boxeo"
            self.image = ResourceController.game_Activity18Boxeo
            self.answer = eQuestionAnswer.ANSWER_B
            
            self.description[0] = "Es un deporte de combate"
            self.description[1] = "en el que dos "
            self.description[2] = "contrincantes luchan"
            self.description[3] = "utilizando únicamente "
            self.description[4] = "sus puños con guantes,"
            self.description[5] = "golpeando a su "
            self.description[6] = "adversario de la cintura"
            self.description[7] = "hacia arriba, dentro de "
            self.description[8] = "un cuadrilátero, en "
            self.description[9] = "breves secuencias de "
            self.description[10] = "lucha."
            
            self.question[0] = "¿Cómo se llaman las secuencias"
            self.question[1] = "de lucha en un combate de boxeo?"
            
            self.optionA[0] = "Momentos o tiempos"
            self.optionB[0] = "Asaltos o rounds"
            self.optionC[0] = "Saltos o esperas"
            
        elif id == eActivityId._19_EQUITACION:
            self.name = "Equitación"
            self.image = ResourceController.game_Activity19Equitacion
            self.answer = eQuestionAnswer.ANSWER_C
            
            self.description[0] = "La equitación es el arte"
            self.description[1] = "de mantener el control "
            self.description[2] = "preciso sobre un caballo,"
            self.description[3] = "así como los diferentes"
            self.description[4] = "modos de manejarlo. La "
            self.description[5] = "equitación implica "
            self.description[6] = "también los "
            self.description[7] = "conocimientos para "
            self.description[8] = "cuidar caballos y el uso"
            self.description[9] = "del equipo apropiado."
            
            self.question[0] = "El equipo para montar a"
            self.question[1] = "caballo se llama:"
            
            self.optionA[0] = "Silla"
            self.optionB[0] = "Montura"
            self.optionC[0] = "Aparejos o arreos"
            
        elif id == eActivityId._20_GOLF:
            self.name = "Golf"
            self.image = ResourceController.game_Activity20Golf
            self.answer = eQuestionAnswer.ANSWER_B
            
            self.description[0] = "El golf es un deporte de"
            self.description[1] = "precisión cuyo objetivo "
            self.description[2] = "es introducir una bola "
            self.description[3] = "en los hoyos que están "
            self.description[4] = "distribuidos en el campo"
            self.description[5] = "con el menor número de"
            self.description[6] = "golpes."
            
            self.question[0] = "Si vas a practicar golf el"
            self.question[1] = "equipo que necesitas es:"
            
            self.optionA[0] = "Pelota y guantes"
            self.optionB[0] = "Palos y pelota"
            self.optionC[0] = "Pelota y bate"
            
        elif id == eActivityId._21_JUDO:
            self.name = "Judo"
            self.image = ResourceController.game_Activity21Judo
            self.answer = eQuestionAnswer.ANSWER_A
            
            self.description[0] = "El Judo es uno de los "
            self.description[1] = "cuatro estilos "
            self.description[2] = "principales de lucha"
            self.description[3] = "deportiva más "
            self.description[4] = "practicados hoy en día "
            self.description[5] = "en todo el mundo. Los "
            self.description[6] = "practicantes de este "
            self.description[7] = "arte son denominados "
            self.description[8] = "Judocas."
            
            self.question[0] = "¿Por cuál de esas razones crees"
            self.question[1] = "que el judo es un deporte muy"
            self.question[2] = "bueno para niños y jóvenes?"
            
            self.optionA[0] = "Incluye ejercicios como"
            self.optionA[1] = "saltar, rodar y arrastrarse"
            self.optionB[0] = "Es más fácil practicarlo"
            self.optionB[1] = "en estas edades"
            self.optionC[0] = "Es muy seguro y da"
            self.optionC[1] = "buena salud"
            
        elif id == eActivityId._22_RUGBY:
            self.name = "Rugby"
            self.image = ResourceController.game_Activity22Rugby
            self.answer = eQuestionAnswer.ANSWER_B
            
            self.description[0] = "Es un deporte de equipo"
            self.description[1] = "jugado por dos equipos "
            self.description[2] = "de 13 jugadores, el "
            self.description[3] = "objetivo del juego "
            self.description[4] = "consiste en apoyar un"
            self.description[5] = "balón ovalado en el "
            self.description[6] = "suelo con las manos "
            self.description[7] = "sobre o tras la línea"
            self.description[8] = "de ensayo."
            
            self.question[0] = "¿Cuál de estas es una"
            self.question[0] = "diferencia entre el rugby"
            self.question[0] = "y el fútbol americano?"
            
            self.optionA[0] = "En el rugby se mete gol en un arco y en el"
            self.optionA[1] = "fútbol americano se hace gol son postes"
            self.optionB[0] = "El partido de rugby dura 80 minutos y el"
            self.optionB[1] = "de fútbol americano 60 minutos"
            self.optionC[0] = "El material de la cancha de rugby es pasto y del"
            self.optionC[1] = "fútbol americano es césped artificial"
            
        elif id == eActivityId._23_TENIS:
            self.name = "Tenis"
            self.image = ResourceController.game_Activity23Tenis
            self.answer = eQuestionAnswer.ANSWER_B
            
            self.description[0] = "El tenis se practica en"
            self.description[1] = "un terreno rectangular,"
            self.description[2] = "dividido por una red "
            self.description[3] = "intermedia. Se disputa"
            self.description[4] = "entre dos jugadores "
            self.description[5] = "o entre dos parejas"
            self.description[6] = "y consiste en golpear"
            self.description[7] = "la pelota con la"
            self.description[8] = "raqueta para que vaya de"
            self.description[9] = "un lado al otro del"
            self.description[10] = "campo pasando por"
            self.description[11] = "encima de la red."

            self.question[0] = "¿Qué forma tiene el terreno"
            self.question[1] = "donde se practica tenis?"
            
            self.optionA[0] = "Redonda"
            self.optionB[0] = "Rectangular"
            self.optionC[0] = "Cuadrada"
            
        elif id == eActivityId._24_VOLEIBOL:
            self.name = "Voleibol"
            self.image = ResourceController.game_Activity24Voleibol
            self.answer = eQuestionAnswer.ANSWER_A
            
            self.description[0] = "Es un deporte donde dos"
            self.description[1] = "equipos se enfrentan "
            self.description[2] = "separados por una red "
            self.description[3] = "central, tratando de "
            self.description[4] = "pasar el balón por "
            self.description[5] = "encima de la red hacia "
            self.description[6] = "el suelo del campo "
            self.description[7] = "contrario. Cada equipo"
            self.description[8] = "dispone de un número "
            self.description[9] = "limitado de toques para"
            self.description[10] = "devolver el balón hacia"
            self.description[11] = "el campo contrario."
            
            self.question[0] = "¿Qué otro nombre tiene el"
            self.question[1] = "voleibol?"
            
            self.optionA[0] = "Balonvolea"
            self.optionB[0] = "Volei de playa"
            self.optionC[0] = "Mintonette"
            
        elif id == eActivityId._25_HOCKEY:
            self.name = "Hockey"
            self.image = ResourceController.game_Activity25Hockey
            self.answer = eQuestionAnswer.ANSWER_C
            
            self.description[0] = "Es un deporte en el que "
            self.description[1] = "dos equipos compiten "
            self.description[2] = "para llevar una pelota "
            self.description[3] = "de un material duro o un"
            self.description[4] = "disco de caucho a la "
            self.description[5] = "portería contraria para "
            self.description[6] = "anotar un tanto con la "
            self.description[7] = "ayuda de un bastón largo"
            self.description[8] = "o Palo de Hockey."
            
            self.question[0] = "¿Cuáles de estas son"
            self.question[1] = "modalidades del hockey?"
            
            self.optionA[0] = "Césped, hielo y granito"
            self.optionB[0] = "Hielo, en línea y"
            self.optionB[1] = "superficie lisa"
            self.optionC[0] = "Césped, hielo y en línea"
            
        elif id == eActivityId._26_TEATRO:
            self.name = "Teatro"
            self.image = ResourceController.game_Activity26Teatro
            self.answer = eQuestionAnswer.ANSWER_B
            
            self.description[0] = "El teatro es la rama"
            self.description[1] = "del arte relacionada"
            self.description[2] = "con la actuación, que"
            self.description[3] = "representa historias"
            self.description[4] = "frente a una audiencia"
            self.description[5] = "usando una combinación"
            self.description[6] = "de discurso, gestos,"
            self.description[7] = "escenografía, música,"
            self.description[8] = "sonido y espectáculo."
            
            self.question[0] = "¿A cuál de estas ramas del"
            self.question[1] = "arte pertenece el teatro?"
            
            self.optionA[0] = "Literario"
            self.optionB[0] = "Escénico"
            self.optionC[0] = "Romano"
            
        elif id == eActivityId._27_MUSICA:
            self.name = "Música"
            self.image = ResourceController.game_Activity27Musica
            self.answer = eQuestionAnswer.ANSWER_A
            
            self.description[0] = "La música, como toda"
            self.description[1] = "manifestación artística,"
            self.description[2] = "es un producto cultural."
            self.description[3] = "El fin de este arte es "
            self.description[4] = "suscitar una experiencia"
            self.description[5] = "estética en el oyente, y"
            self.description[6] = "expresar sentimientos, "
            self.description[7] = "circunstancias, "
            self.description[8] = "pensamientos o ideas."
            
            self.question[0] = "¿Si quiero aprender música"
            self.question[1] = "a dónde debo ir?"
            
            self.optionA[0] = "A la Casa de la Cultura"
            self.optionA[1] = "o a una academia"
            self.optionB[0] = "Al coliseo o al teatro"
            self.optionC[0] = "A la Alcaldía o a la"
            self.optionC[1] = "Secretaría de Educación"
            
        elif id == eActivityId._28_DANZA_FOLCLORICA:
            self.name = "Danza Folclórica"
            self.image = ResourceController.game_Activity28DanzaFolclorica
            self.answer = eQuestionAnswer.ANSWER_B
            
            self.description[0] = "El término Danza "
            self.description[1] = "Folclórica se aplica a"
            self.description[2] = "determinados bailes que "
            self.description[3] = "resultan importantes "
            self.description[4] = "para la cultura y la "
            self.description[5] = "historia de un país."
            
            self.question[0] = "¿Cuáles de estos son bailes"
            self.question[1] = "típicos del folclor de"
            self.question[2] = "Colombia?"
            
            self.optionA[0] = "Jazz, flamenco, porro"
            self.optionB[0] = "Bambuco, joropo, cumbia"
            self.optionC[0] = "Bambuco, porro y contradanza"
            
        elif id == eActivityId._29_BREAK_DANCE:
            self.name = "Break Dance"
            self.image = ResourceController.game_Activity29BreakDance
            self.answer = eQuestionAnswer.ANSWER_B
            
            self.description[0] = "Esta danza urbana forma"
            self.description[1] = "parte de la cultura "
            self.description[2] = "HipHop, cuando la "
            self.description[3] = "practican hombres estos"
            self.description[4] = "se hacen llamar Bboys, "
            self.description[5] = "cuando la practican "
            self.description[6] = "mujeres se hacen "
            self.description[7] = "llamar Bgirls."
            
            self.question[0] = "¿Cómo se hacen llamar los"
            self.question[1] = "hombres que practican el"
            self.question[2] = "Breakdance?"
            
            self.optionA[0] = "Rockers"
            self.optionB[0] = "Bboys"
            self.optionC[0] = "Bgirls"
            
        elif id == eActivityId._30_BALLET:
            self.name = "Ballet"
            self.image = ResourceController.game_Activity30Ballet
            self.answer = eQuestionAnswer.ANSWER_A
            
            self.description[0] = "Es una forma concreta"
            self.description[1] = "de danza altamente"
            self.description[2] = "técnica a la que"
            self.description[3] = "también se le llama"
            self.description[4] = "danza clásica. Esta"
            self.description[5] = "expresión artística"
            self.description[6] = "puede incluir: danza,"
            self.description[7] = "mímica, y teatro."
            
            self.question[0] = "¿Cuáles de estos implementos"
            self.question[1] = "están en la vestimenta propia"
            self.question[2] = "del ballet?"
            
            self.optionA[0] = "Mallas, tutú y zapatillas"
            self.optionB[0] = "Mallas, tutú y cintas"
            self.optionC[0] = "Tutú, zapatillas y"
            self.optionC[1] = "pantalones cortos"
            
        elif id == eActivityId._31_HIP_HOP:
            self.name = "Hip Hop"
            self.image = ResourceController.game_Activity31HipHop
            self.answer = eQuestionAnswer.ANSWER_B
            
            self.description[0] = "El hip-hop surgió en "
            self.description[1] = "Estados Unidos a "
            self.description[2] = "finales de los sesenta."
            self.description[3] = "Se compone de cuatro "
            self.description[4] = "pilares: MC (quien "
            self.description[5] = "canta), DJ (que mezcla "
            self.description[6] = "la música), Breakdance "
            self.description[7] = "(quien baila) y Grafiti "
            self.description[8] = "(quien pinta las paredes)"
            
            self.question[0] = "¿En qué país surgio"
            self.question[1] = "el hip hop?"
            
            self.optionA[0] = "Inglaterra"
            self.optionB[0] = "Estados Unidos"
            self.optionC[0] = "Africa"
            
        elif id == eActivityId._32_FOTOGRAFIA:
            self.name = "Fotografía"
            self.image = ResourceController.game_Activity32Fotografia
            self.answer = eQuestionAnswer.ANSWER_A
            
            self.description[0] = "La fotografía es el arte"
            self.description[1] = "y la técnica para "
            self.description[2] = "obtener imágenes "
            self.description[3] = "duraderas debidas a la"
            self.description[4] = "acción de la luz. En la"
            self.description[5] = "actualidad, lo más común"
            self.description[6] = "es la fotografía digital,"
            self.description[7] = "en esta se emplean "
            self.description[8] = "sensores y memorias "
            self.description[9] = "digitales."
            
            self.question[0] = "¿Qué habilidades desarrollas"
            self.question[1] = "cuando aprendes fotografía?"
            
            self.optionA[0] = "Creatividad y observación"
            self.optionB[0] = "Agilidad con las manos"
            self.optionC[0] = "Planear y organizar"
            
        elif id == eActivityId._33_CANTO:
            self.name = "Canto"
            self.image = ResourceController.game_Activity33Canto
            self.answer = eQuestionAnswer.ANSWER_B
            
            self.description[0] = "El canto es la emisión"
            self.description[1] = "controlada de sonidos de"
            self.description[2] = "la voz humana, siguiendo"
            self.description[3] = "una composición musical."
            
            self.question[0] = "¿Cuál de los siguientes"
            self.question[1] = "elementos sirve para escuchar"
            self.question[2] = "más fuertemente el canto de"
            self.question[3] = "una persona?"
            
            self.optionA[0] = "Luces"
            self.optionB[0] = "Micrófono"
            self.optionC[0] = "Sintetizador"
            
        elif id == eActivityId._34_DIBUJO_ARTISTICO:
            self.name = "Dibujo Artístico"
            self.image = ResourceController.game_Activity34DibujoArtistico
            self.answer = eQuestionAnswer.ANSWER_C
            
            self.description[0] = "Se requieren aptitudes "
            self.description[1] = "personales y naturales"
            self.description[2] = "para realizar dibujos "
            self.description[3] = "artísticos. A través de"
            self.description[4] = "ellos el artista expresa"
            self.description[5] = "su manera de ver la "
            self.description[6] = "realidad."
            
            self.question[0] = "¿Cuáles elementos necesitas"
            self.question[1] = "para realizar dibujo artístico?"
            
            self.optionA[0] = "Compás, reglas y papeles"
            self.optionB[0] = "Compás, pegante y lápices"
            self.optionC[0] = "Carboncillos, papeles,"
            self.optionC[1] = "borradores"
            
        elif id == eActivityId._35_CERAMICA:
            self.name = "Cerámica"
            self.image = ResourceController.game_Activity35Ceramica
            self.answer = eQuestionAnswer.ANSWER_B
            
            self.description[0] = "La ceramica es el arte "
            self.description[1] = "de fabricar recipientes,"
            self.description[2] = "vasijas y otros objetos"
            self.description[3] = "de arcilla, u otro "
            self.description[4] = "material cerámico."
            
            self.question[0] = "¿Qué elemento se necesita para"
            self.question[1] = "fabricar objetos en arcilla?"
            
            self.optionA[0] = "Luz"
            self.optionB[0] = "Calor"
            self.optionC[0] = "Viento"
            
        elif id == eActivityId._36_ACUARELA:
            self.name = "Acuarela"
            self.image = ResourceController.game_Activity36Acuarela
            self.answer = eQuestionAnswer.ANSWER_C
            
            self.description[0] = "La acuarela es una "
            self.description[1] = "pintura sobre papel o"
            self.description[2] = "cartulina con colores"
            self.description[3] = "diluidos en agua. Los"
            self.description[4] = "colores utilizados son"
            self.description[5] = "transparentes (según la"
            self.description[6] = "cantidad de agua en la "
            self.description[7] = "mezcla) y a veces dejan"
            self.description[8] = "ver el fondo del papel "
            self.description[9] = "(blanco)."
            
            self.question[0] = "Para modificar el color de"
            self.question[1] = "la acuarela necesitas:"
            
            self.optionA[0] = "Trementina y color blanco"
            self.optionB[0] = "Agua y trementina"
            self.optionC[0] = "Agua y pinceles"
            
        elif id == eActivityId._37_REALIZACION_AUDIOVISUAL:
            self.name = "Realización Audiovisual"
            self.image = ResourceController.game_Activity37RealizacionAudiovisual
            self.answer = eQuestionAnswer.ANSWER_B
            
            self.description[0] = "Es todo el proceso "
            self.description[1] = "mediante el cuál se "
            self.description[2] = "realizan producciones"
            self.description[3] = "audiovisuales (que son"
            self.description[4] = "las que se ven y se oyen)"
            self.description[5] = "como programas de"
            self.description[6] = "televisión."
            
            self.question[0] = "¿Cuál de los siguientes es otro"
            self.question[1] = "ejemplo de producción"
            self.question[2] = "audiovisual?"
            
            self.optionA[0] = "Una canción"
            self.optionB[0] = "Una película"
            self.optionC[0] = "Un dibujo"
            
        elif id == eActivityId._38_CREACION_NARRATIVA:
            self.name = "Creación Narrativa"
            self.image = ResourceController.game_Activity38CreacionNarrativa
            self.answer = eQuestionAnswer.ANSWER_B
            
            self.description[0] = "La creación narrativa es"
            self.description[1] = "el arte de inventar "
            self.description[2] = "historias y cuentos, "
            self.description[3] = "puedes hacerlo solo o"
            self.description[4] = "con otras personas."
            
            self.question[0] = "¿La creación narrativa es"
            self.question[1] = "el arte de inventar?"
            
            self.optionA[0] = "Dibujos"
            self.optionB[0] = "Historias y cuentos"
            self.optionC[0] = "Canciones"
            
        elif id == eActivityId._39_POESIA_Y_DECLAMACION:
            self.name = "Poesía y Declamación"
            self.image = ResourceController.game_Activity39PoesiaYDeclamacion
            self.answer = eQuestionAnswer.ANSWER_B
            
            self.description[0] = "No todos los poetas se"
            self.description[1] = "dedicaron a escribir "
            self.description[2] = "poemas para adultos, "
            self.description[3] = "algunos escribian "
            self.description[4] = "también para niños."
            
            self.question[0] = "¿Cuál de los siguientes"
            self.question[1] = "personajes es un famoso"
            self.question[2] = "poeta infantil?"
            
            self.optionA[0] = "Mario Benedetti"
            self.optionB[0] = "Rafael Pombo"
            self.optionC[0] = "Pablo Neruda"
            
        elif id == eActivityId._40_BANDA_MARCIAL:
            self.name = "Banda Marcial"
            self.image = ResourceController.game_Activity40BandaMarcial
            self.answer = eQuestionAnswer.ANSWER_A
            
            self.description[0] = "Una banda marcial se "
            self.description[1] = "compone de un grupo de"
            self.description[2] = "musicos que marchando"
            self.description[3] = "tocan diferentes "
            self.description[4] = "instrumentos y que"
            self.description[5] = "generalmente se "
            self.description[6] = "presentan en vivo y al "
            self.description[7] = "aire libre."
            
            self.question[0] = "¿En una banda marcial,"
            self.question[1] = "los músicos van?"
            
            self.optionA[0] = "Marchando"
            self.optionB[0] = "Corriendo"
            self.optionC[0] = "Hablando"
            
        elif id == eActivityId._41_MUSICA_ANDINA:
            self.name = "Música Andina"
            self.image = ResourceController.game_Activity41MusicaAndina
            self.answer = eQuestionAnswer.ANSWER_B
            
            self.description[0] = "Música andina es un "
            self.description[1] = "término que se aplica a"
            self.description[2] = "diversos generos "
            self.description[3] = "músicales originados en"
            self.description[4] = "los Andes sudamericanos,"
            self.description[5] = "particularmente en Perú."
            
            self.question[0] = "¿Música andina es un término"
            self.question[1] = "que se aplica a diversos"
            self.question[2] = "generos músicales originados"
            self.question[3] = "en?"
            
            self.optionA[0] = "Europa"
            self.optionB[0] = "Los Andes sudamericanos"
            self.optionC[0] = "Asia"
            
        elif id == eActivityId._42_GUITARRA:
            self.name = "Guitarra"
            self.image = ResourceController.game_Activity42Guitarra
            self.answer = eQuestionAnswer.ANSWER_C
            
            self.description[0] = "Es un instrumento "
            self.description[1] = "músical de seis cuerdas,"
            self.description[2] = "utilizado en la música"
            self.description[3] = "colombiana y en ritmos "
            self.description[4] = "como el rock, el "
            self.description[5] = "flamenco y la música de"
            self.description[6] = "cantautor."
            
            self.question[0] = "¿Cuántas cuerdas tiene"
            self.question[1] = "una guitarra?"
            
            self.optionA[0] = "Siete"
            self.optionB[0] = "Cinco"
            self.optionC[0] = "Seis"
            
        elif id == eActivityId._43_TITERES:
            self.name = "Títeres"
            self.image = ResourceController.game_Activity43Titeres
            self.answer = eQuestionAnswer.ANSWER_B
            
            self.description[0] = "Actividad artística que"
            self.description[1] = "consiste en la"
            self.description[2] = "manipulación de muñecos"
            self.description[3] = "en escenarios decorados"
            self.description[4] = "con cortinas."
            
            self.question[0] = "¿Los títeres también se"
            self.question[1] = "conocen cómo?"
            
            self.optionA[0] = "Teatro de muñecos"
            self.optionB[0] = "Teatro de marionetas"
            self.optionC[0] = "Teatro para niños"
            
        elif id == eActivityId._44_FLAUTAS:
            self.name = "Flautas"
            self.image = ResourceController.game_Activity44Flautas
            self.answer = eQuestionAnswer.ANSWER_A
            
            self.description[0] = "Es un instrumento"
            self.description[1] = "músical de viento,"
            self.description[2] = "que tiene una serie de"
            self.description[3] = "orificios y una"
            self.description[4] = "boquilla."
            
            self.question[0] = "Algunos tipos de flautas"
            self.question[1] = "son:"
            
            self.optionA[0] = "Traversa, dulce, ocarina"
            self.optionB[0] = "Larga, corta, traversa"
            self.optionC[0] = "Ocarina, larga, quena"
            
        elif id == eActivityId._45_CLUB_DE_LECTURA:
            self.name = "Club de lectura"
            self.image = ResourceController.game_Activity45ClubDeLectura
            self.answer = eQuestionAnswer.ANSWER_C
            
            self.description[0] = "En el club de lectura "
            self.description[1] = "las personas se reunen a"
            self.description[2] = "leer cuentos e historias."
            
            self.question[0] = "Si quieres participar en un"
            self.question[1] = "club de lectura puedes ir a:"
            
            self.optionA[0] = "El teatro"
            self.optionB[0] = "El coliseo"
            self.optionC[0] = "La Casa de la Cultura"
            
        elif id == eActivityId._46_GRUPO_DE_ROCK:
            self.name = "Grupo de Rock"
            self.image = ResourceController.game_Activity46GrupoDeRock
            self.answer = eQuestionAnswer.ANSWER_B
            
            self.description[0] = "El rock es un genero"
            self.description[1] = "músical del siglo XX"
            self.description[2] = "que se originó en"
            self.description[3] = "Estados Unidos. Su"
            self.description[4] = "sonido se basa"
            self.description[5] = "principalmente en la"
            self.description[6] = "guitarra eléctrica."
            
            self.question[0] = "¿Además de la guitarra cuáles"
            self.question[1] = "de los siguientes instrumentos"
            self.question[2] = "se utilizan en un grupo de rock?"
            
            self.optionA[0] = "La flauta y el piano"
            self.optionB[0] = "La batería y el bajo eléctrico"
            self.optionC[0] = "El violin y el piano"
            
        elif id == eActivityId._47_BANDA_SINFONICA:
            self.name = "Banda Sinfónica"
            self.image = ResourceController.game_Activity47BandaSinfonica
            self.answer = eQuestionAnswer.ANSWER_B
            
            self.description[0] = "Una banda sinfónica está"
            self.description[1] = "compuesta por "
            self.description[2] = "instrumentos de viento y"
            self.description[3] = "percusión, y también, "
            self.description[4] = "por algunos instrumentos"
            self.description[5] = "de cuerda, como el "
            self.description[6] = "violonchelo, el "
            self.description[7] = "contrabajo, el piano "
            self.description[8] = "y el arpa."
            
            self.question[0] = "Cuando en una banda se usan"
            self.question[1] = "instrumentos de viento y percusión,"
            self.question[2] = "y además instrumentos de cuerda,"
            self.question[3] = "esta se llama:"
            
            self.optionA[0] = "Banda de música"
            self.optionB[0] = "Banda sinfónica"
            self.optionC[0] = "Banda popular"
            
        elif id == eActivityId._48_GAITAS_Y_TAMBORES:
            self.name = "Gaitas y Tambores"
            self.image = ResourceController.game_Activity48GaitasYTambores
            self.answer = eQuestionAnswer.ANSWER_A
            
            self.description[0] = "La gaita es un"
            self.description[1] = "instrumento musical de"
            self.description[2] = "viento. El tambor es un"
            self.description[3] = "instrumento de"
            self.description[4] = "percusión. La unión de"
            self.description[5] = "estos dos instrumentos"
            self.description[6] = "permite interpretar"
            self.description[7] = "música del Caribe"
            self.description[8] = "colombiano."
            
            self.question[0] = "¿Cuál de los siguientes grupos"
            self.question[1] = "colombianos es famoso por"
            self.question[2] = "interpretar gaitas y tambores?"
            
            self.optionA[0] = "Los Gaiteros de San Jacinto"
            self.optionB[0] = "Los corraleros de Majagual"
            self.optionC[0] = "Lucho Bermúdez y su orquesta"
            
        elif id == eActivityId._49_MUSICA_CARRANGUERA:
            self.name = "Música Carranguera"
            self.image = ResourceController.game_Activity49MusicaCarranguera
            self.answer = eQuestionAnswer.ANSWER_B
            
            self.description[0] = "Es un tipo de música"
            self.description[1] = "folclórica colombiana"
            self.description[2] = "que nació en la región"
            self.description[3] = "andina. Uno de los"
            self.description[4] = "grupos más"
            self.description[5] = "representativos de este"
            self.description[6] = "género musical es Los"
            self.description[7] = "Carrangueros de Ráquira"
            
            self.question[0] = "¿Cuál de los siguientes cantantes"
            self.question[1] = " es famoso por interpretar"
            self.question[2] = "música carranguera?"
            
            self.optionA[0] = "Pipe Peláez"
            self.optionB[0] = "Jorge Veloza"
            self.optionC[0] = "Darío Gómez"
            
        elif id == eActivityId._50_PIANO:
            self.name = "Piano"
            self.image = ResourceController.game_Activity50Piano
            self.answer = eQuestionAnswer.ANSWER_C
            
            self.description[0] = "El piano es un "
            self.description[1] = "instrumento musical"
            self.description[2] = "clasificado como "
            self.description[3] = "instrumento de teclado "
            self.description[4] = "de cuerdas percutidas."
            self.description[5] = "Es muy utilizado en "
            self.description[6] = "hermosas melodias de "
            self.description[7] = "música clásica."
            
            self.question[0] = "Los siguientes son los dos"
            self.question[1] = "colores de las teclas del"
            self.question[2] = "piano:"
            
            self.optionA[0] = "Negro y azul"
            self.optionB[0] = "Blanco y gris metalizado"
            self.optionC[0] = "Blanco y negro"
            
        elif id == eActivityId._51_INSTITUTO_COLOMBIANO_DE_BIENESTAR_FAMILIAR:
            self.name = "Instituto Colombiano de Bienestar Familiar (ICBF)"
            self.nameToShow1 = "Instituto colombiano de"
            self.nameToShow2 = "bienestar familiar (ICBF)"
            self.image = ResourceController.game_Activity51InstitutoColombianoDeBienestarFamiliar
            self.answer = eQuestionAnswer.ANSWER_B
            
            self.description[0] = "El ICBF trabaja por el "
            self.description[1] = "desarrollo y la "
            self.description[2] = "protección integral de "
            self.description[3] = "la primera infancia, la"
            self.description[4] = "niñez, la adolescencia y"
            self.description[5] = "el bienestar de las "
            self.description[6] = "familias colombianas. "
            self.description[7] = "Se puede acudir a esta"
            self.description[8] = "institución cuando un niño,"
            self.description[9] = "niña o adolescente esté"
            self.description[10] = "siendo abusado física,"
            self.description[11] = "laboral o sexualmente."
            
            self.question[0] = "¿Por qué trabaja el ICBF?"
            
            self.optionA[0] = "Para generar ingresos"
            self.optionB[0] = "Para el desarrollo y la"
            self.optionB[1] = "protección de las familias"
            self.optionC[0] = "Para la seguridad de"
            self.optionC[1] = "los municipios"
            
        elif id == eActivityId._52_POLICIA_NACIONAL:
            self.name = "Policía Nacional"
            self.image = ResourceController.game_Activity52PoliciaNacional
            self.answer = eQuestionAnswer.ANSWER_B
            
            self.description[0] = "La Policía Nacional"
            self.description[1] = "mantiene las condiciones"
            self.description[2] = "necesarias para el"
            self.description[3] = "ejercicio de los"
            self.description[4] = "derechos y libertades"
            self.description[5] = "públicas, y para"
            self.description[6] = "asegurar que Colombia"
            self.description[7] = "viva en paz. Se puede"
            self.description[8] = "acudir a ella cuando"
            self.description[9] = "una persona está siendo"
            self.description[10] = "sometida a maltrato"
            self.description[11] = "físico o verbal."
            
            self.question[0] = "¿Cuándo se debe acudir"
            self.question[1] = "a la policía?"
            
            self.optionA[0] = "Si una persona no pagó"
            self.optionA[1] = "una deuda"
            self.optionB[0] = "Si una persona le está"
            self.optionB[1] = "haciendo daño a otra"
            self.optionC[0] = "Si a una persona se le"
            self.optionC[1] = "está incendiando su casa"
            
        elif id == eActivityId._53_COMISARIA_DE_FAMILIA:
            self.name = "Comisaría de Familia"
            self.image = ResourceController.game_Activity53ComisariaDeFamilia
            self.answer = eQuestionAnswer.ANSWER_B
            
            self.description[0] = "Es una entidad que ayuda"
            self.description[1] = "orienta a las familias,"
            self.description[2] = "las ayuda a reflexionar"
            self.description[3] = "y a establecer acuerdos"
            self.description[4] = "cuando tienen"
            self.description[5] = "dificultades. Busca que"
            self.description[6] = "los derechos de todos"
            self.description[7] = "los miembros de la"
            self.description[8] = "familia sean reconocidos"
            self.description[9] = "y respetados."
            
            self.question[0] = "¿En cuál de estas situaciones"
            self.question[1] = "un niño o una familia puede"
            self.question[2] = "acudir a la comisaría de"
            self.question[3] = "familia?"
            
            self.optionA[0] = "Cuando uno de los miembros de la"
            self.optionA[1] = "familia tiene problemas de salud"
            self.optionB[0] = "Cuando los padres maltratan a sus hijos"
            self.optionB[1] = "o cuando los padres se golpean"
            self.optionC[0] = "Cuando un miembro de la"
            self.optionC[1] = "familia está perdido"
            
        elif id == eActivityId._54_CASA_DE_LA_JUSTICIA:
            self.name = "Casa de la Justicia"
            self.image = ResourceController.game_Activity54CasaDeLaJusticia
            self.answer = eQuestionAnswer.ANSWER_C
            
            self.description[0] = "La casa de justicia fue "
            self.description[1] = "creada para asesorar, "
            self.description[2] = "apoyar y fortalecer la "
            self.description[3] = "gestión de las "
            self.description[4] = "autoridades "
            self.description[5] = "territoriales, con el"
            self.description[6] = "objetivo de garantizar "
            self.description[7] = "el derecho del acceso a"
            self.description[8] = "la justicia de todos los"
            self.description[9] = "ciudadanos."
            
            self.question[0] = "¿Qué derecho garantizan las"
            self.question[1] = "casas de justicia?"
            
            self.optionA[0] = "El derecho a la salud"
            self.optionB[0] = "El derecho a la vivienda"
            self.optionC[0] = "El derecho a la justicia"
            
        elif id == eActivityId._55_ALCALDIA:
            self.name = "Alcaldía"
            self.image = ResourceController.game_Activity55Alcaldia
            self.answer = eQuestionAnswer.ANSWER_B
            
            self.description[0] = "Desde allí se ejerce la "
            self.description[1] = "administración política "
            self.description[2] = "de una ciudad, municipio"
            self.description[3] = "o pueblo, en nuestro "
            self.description[4] = "país quien ejerce esta"
            self.description[5] = "función se denomina "
            self.description[6] = "Alcalde y es elegido a "
            self.description[7] = "través del voto."
            
            self.question[0] = "La máxima autoridad de un"
            self.question[1] = "municipio se llama:"
            
            self.optionA[0] = "Edil"
            self.optionB[0] = "Alcalde"
            self.optionC[0] = "Concejal"
            
        elif id == eActivityId._56_SERVICIO_NACIONAL_DE_APRENDIZAJE:
            self.name = "Servicio Nacional de Aprendizaje (SENA)"
            self.nameToShow1 = "Servicio nacional de"
            self.nameToShow2 = "aprendizaje (SENA)"
            self.image = ResourceController.game_Activity56ServicioNacionalDeAprendizaje
            self.answer = eQuestionAnswer.ANSWER_B
            
            self.description[0] = "El SENA ofrece formación"
            self.description[1] = "profesional para jóvenes"
            self.description[2] = "y adultos en actividades"
            self.description[3] = "productivas que les"
            self.description[4] = "permiten conseguir"
            self.description[5] = "empleo o formar su"
            self.description[6] = "propia empresa."
            
            self.question[0] = "¿Qué ofrece el SENA?"
            
            self.optionA[0] = "Clases de baile"
            self.optionB[0] = "Formación profesional"
            self.optionB[1] = "para jóvenes y adultos"
            self.optionC[0] = "Servicios de salud"
            
        elif id == eActivityId._57_CASA_DE_LA_CULTURA:
            self.name = "Casa de la Cultura"
            self.image = ResourceController.game_Activity57CasaDeLaCultura
            self.answer = eQuestionAnswer.ANSWER_B
            
            self.description[0] = "Las Casa de la Cultura"
            self.description[1] = "tiene como objetivo"
            self.description[2] = "brindar un espacio"
            self.description[3] = "permanente para que"
            self.description[4] = "todas las personas"
            self.description[5] = "accedan a las"
            self.description[6] = "diferentes"
            self.description[7] = "manifestaciones del"
            self.description[8] = "arte, la cultura y el"
            self.description[9] = "patrimonio."
            
            self.question[0] = "¿Cuál es el objetivo de la"
            self.question[1] = "casa de la cultura?"
            
            self.optionA[0] = "Brindar un espacio"
            self.optionA[1] = "para la relajación"
            self.optionB[0] = "Brindar un espacio para las"
            self.optionB[1] = "manifestaciones culturales"
            self.optionC[0] = "Dar clases para manejar"
            self.optionC[1] = "computadores"
            
        elif id == eActivityId._58_INSTITUTO_MUNICIPAL_DE_RECREACION_Y_DEPORTE:
            self.name = "Instituto Municipal de Recreación y Deporte (IMRD)"
            self.nameToShow1 = "Instituto municipal de"
            self.nameToShow2 = "recreación y deporte"
            self.image = ResourceController.game_Activity58InstitutoMunicipalDeRecreacionYDeport
            self.answer = eQuestionAnswer.ANSWER_C
            
            self.description[0] = "El IMRD promueve el "
            self.description[1] = "ejercicio y goce pleno"
            self.description[2] = "del derecho al deporte,"
            self.description[3] = "la recreación, la "
            self.description[4] = "actividad física, el "
            self.description[5] = "aprovechamiento del "
            self.description[6] = "tiempo libre y el buen"
            self.description[7] = "uso de parques y "
            self.description[8] = "escenarios para todos"
            self.description[9] = "los ciudadanos."
            
            self.question[0] = "¿Qué opciones le puede ofrecer"
            self.question[1] = "el IMRD a una persona que quiera"
            self.question[1] = "usar bien su tiempo libre?"
            
            self.optionA[0] = "Conocer los mejores"
            self.optionA[1] = "programas de televisión"
            self.optionB[0] = "Informa las películas que"
            self.optionB[1] = "hay en cartelera"
            self.optionC[0] = "Actividades culturales, deportes y"
            self.optionC[1] = "espectáculos para diferentes edades"
            
        elif id == eActivityId._59_HOSPITAL:
            self.name = "Hospital"
            self.image = ResourceController.game_Activity59Hospital
            self.answer = eQuestionAnswer.ANSWER_B
            
            self.description[0] = "Un hospital es un"
            self.description[1] = "lugar donde se atiende"
            self.description[2] = "a los enfermos para"
            self.description[3] = "diagnosticar su"
            self.description[4] = "enfermedad y brindarles"
            self.description[5] = "el tratamiento que"
            self.description[6] = "necesitan."
            
            self.question[0] = "¿A quién se atiende"
            self.question[1] = "en un hospital?"
            
            self.optionA[0] = "A los artistas"
            self.optionB[0] = "A los enfermos"
            self.optionC[0] = "A los deportistas"
            
        elif id == eActivityId._60_CASA_UNIDOS:
            self.name = "Casa UNIDOS"
            self.image = ResourceController.game_Activity60CasaUnidos
            self.answer = eQuestionAnswer.ANSWER_C
            
            self.description[0] = "Es un lugar de encuentro"
            self.description[1] = "para las familias que"
            self.description[2] = "pertenecen a la"
            self.description[3] = "estrategia UNIDOS, en el"
            self.description[4] = "que pueden hablar con"
            self.description[5] = "los cogestores y a la"
            self.description[6] = "vez que enterarse de las"
            self.description[7] = "ofertas que existen en"
            self.description[8] = "el municipio para"
            self.description[9] = "atender las"
            self.description[10]= "necesidades de la"
            self.description[11]= "población."
            
            self.question[0] = "¿Quiénes asisten a la"
            self.question[1] = "casa UNIDOS?"
            
            self.optionA[0] = "Los niños y jóvenes"
            self.optionA[1] = "en general"
            self.optionB[0] = "Los deportistas"
            self.optionC[0] = "Las familias UNIDOS"

        elif id == eActivityId._61_COMODIN:
            self.name = "Comodin Estrella"
            self.image = ResourceController.game_Activity61Comodin
            self.answer = eQuestionAnswer.ANSWER_A
            
            self.description[0] = "Es un espacio de "
            self.description[1] = "encuentro para las "
            self.description[2] = "familias que pertenecen"
            self.description[3] = "a la estrategia UNIDOS,"
            self.description[4] = "en el que pueden "
            self.description[5] = "interactuar con los "
            self.description[6] = "cogestores, a la vez que"
            self.description[7] = "enterarse de las ofertas"
            self.description[8] = "que existen en el "
            self.description[9] = "municipio para las "
            self.description[10] = "necesidades de la "
            self.description[11] = "población."
            
            self.question[0] = ""
            self.question[1] = ""
            
            self.optionA[0] = ""
            self.optionB[0] = ""
            self.optionC[0] = ""

            
class Card:

    def __init__(self, activityId, indexes):
        
        # Position
        row = indexes[0]
        column = indexes[1]
        
        self.__xPos = 0
        self.__yPos = 0
        
        if GlobalsController.GAME_DIFFICULTY == eGameDifficulty.EASY:
            self.__xPos = 190 + (170 * column)
            self.__yPos = 120 + (175 * row)
                
        elif GlobalsController.GAME_DIFFICULTY == eGameDifficulty.NORMAL:
            self.__xPos = 110 + (170 * column)
            self.__yPos = 120 + (175 * row)
            
        elif GlobalsController.GAME_DIFFICULTY == eGameDifficulty.HARD:
            self.__xPos = 10 + (148 * column)
            self.__yPos = 120 + (175 * row)
                    
        # Identification
        self.activityId = activityId
        self.__isOpen = False
        self.__image = InformationActivities.allActivities[self.activityId].image
        
    def doPaint(self, displaySurface):
        
        if self.__isOpen == True:
            displaySurface.blit(ResourceController.game_CardOpen, (self.__xPos, self.__yPos))
            displaySurface.blit(self.__image, (self.__xPos, self.__yPos))
        else:
            displaySurface.blit(ResourceController.game_CardClose, (self.__xPos, self.__yPos))

    def isOpen(self):
        return self.__isOpen

    def flipToShow(self):
        self.__isOpen = True
        
        
    def flipToHide(self):
        self.__isOpen = False
        

class InformationActivities:
    
    # ----------------------------
    # Contenedores
    # ----------------------------
    allActivities = dict()
    
    # ----------------------------
    # Referencias unicas
    # ----------------------------
    act01 = Activity(eActivityId._01_BICICROS)
    act02 = Activity(eActivityId._02_PATINAJE)
    act03 = Activity(eActivityId._03_FUTSAL)
    act04 = Activity(eActivityId._04_FUTBOL)
    act05 = Activity(eActivityId._05_PORRISMO)
    act06 = Activity(eActivityId._06_ATLETISMO)
    act07 = Activity(eActivityId._07_BALONCESTO)
    act08 = Activity(eActivityId._08_KARATE_DO)
    act09 = Activity(eActivityId._09_LEVANTAMIENTO_DE_PESAS)
    act10 = Activity(eActivityId._10_TAEKWON_DO)
    act11 = Activity(eActivityId._11_BADMINTON)
    act12 = Activity(eActivityId._12_TENIS_DE_MESA)
    act13 = Activity(eActivityId._13_ESGRIMA)
    act14 = Activity(eActivityId._14_GIMNASIA_ARTISTICA)
    act15 = Activity(eActivityId._15_AJEDREZ)
    act16 = Activity(eActivityId._16_AEROBICOS)
    act17 = Activity(eActivityId._17_NATACION)
    act18 = Activity(eActivityId._18_BOXEO)
    act19 = Activity(eActivityId._19_EQUITACION)
    act20 = Activity(eActivityId._20_GOLF)
    act21 = Activity(eActivityId._21_JUDO)
    act22 = Activity(eActivityId._22_RUGBY)
    act23 = Activity(eActivityId._23_TENIS)
    act24 = Activity(eActivityId._24_VOLEIBOL)
    act25 = Activity(eActivityId._25_HOCKEY)
    act26 = Activity(eActivityId._26_TEATRO)
    act27 = Activity(eActivityId._27_MUSICA)
    act28 = Activity(eActivityId._28_DANZA_FOLCLORICA)
    act29 = Activity(eActivityId._29_BREAK_DANCE)
    act30 = Activity(eActivityId._30_BALLET)
    act31 = Activity(eActivityId._31_HIP_HOP)
    act32 = Activity(eActivityId._32_FOTOGRAFIA)
    act33 = Activity(eActivityId._33_CANTO)
    act34 = Activity(eActivityId._34_DIBUJO_ARTISTICO)
    act35 = Activity(eActivityId._35_CERAMICA)
    act36 = Activity(eActivityId._36_ACUARELA)
    act37 = Activity(eActivityId._37_REALIZACION_AUDIOVISUAL)
    act38 = Activity(eActivityId._38_CREACION_NARRATIVA)
    act39 = Activity(eActivityId._39_POESIA_Y_DECLAMACION)
    act40 = Activity(eActivityId._40_BANDA_MARCIAL)
    act41 = Activity(eActivityId._41_MUSICA_ANDINA)
    act42 = Activity(eActivityId._42_GUITARRA)
    act43 = Activity(eActivityId._43_TITERES)
    act44 = Activity(eActivityId._44_FLAUTAS)
    act45 = Activity(eActivityId._45_CLUB_DE_LECTURA)
    act46 = Activity(eActivityId._46_GRUPO_DE_ROCK)
    act47 = Activity(eActivityId._47_BANDA_SINFONICA)
    act48 = Activity(eActivityId._48_GAITAS_Y_TAMBORES)
    act49 = Activity(eActivityId._49_MUSICA_CARRANGUERA)
    act50 = Activity(eActivityId._50_PIANO)
    act51 = Activity(eActivityId._51_INSTITUTO_COLOMBIANO_DE_BIENESTAR_FAMILIAR)
    act52 = Activity(eActivityId._52_POLICIA_NACIONAL)
    act53 = Activity(eActivityId._53_COMISARIA_DE_FAMILIA)
    act54 = Activity(eActivityId._54_CASA_DE_LA_JUSTICIA)
    act55 = Activity(eActivityId._55_ALCALDIA)
    act56 = Activity(eActivityId._56_SERVICIO_NACIONAL_DE_APRENDIZAJE)
    act57 = Activity(eActivityId._57_CASA_DE_LA_CULTURA)
    act58 = Activity(eActivityId._58_INSTITUTO_MUNICIPAL_DE_RECREACION_Y_DEPORTE)
    act59 = Activity(eActivityId._59_HOSPITAL)
    act60 = Activity(eActivityId._60_CASA_UNIDOS)
    act61 = Activity(eActivityId._61_COMODIN)
    
    # ----------------------------
    # Diccionario de todas las actividades
    # ----------------------------
    allActivities[eActivityId._01_BICICROS] = act01
    allActivities[eActivityId._02_PATINAJE] = act02
    allActivities[eActivityId._03_FUTSAL] = act03
    allActivities[eActivityId._04_FUTBOL] = act04
    allActivities[eActivityId._05_PORRISMO] = act05
    allActivities[eActivityId._06_ATLETISMO] = act06
    allActivities[eActivityId._07_BALONCESTO] = act07
    allActivities[eActivityId._08_KARATE_DO] = act08
    allActivities[eActivityId._09_LEVANTAMIENTO_DE_PESAS] = act09
    allActivities[eActivityId._10_TAEKWON_DO] = act10
    allActivities[eActivityId._11_BADMINTON] = act11
    allActivities[eActivityId._12_TENIS_DE_MESA] = act12
    allActivities[eActivityId._13_ESGRIMA] = act13
    allActivities[eActivityId._14_GIMNASIA_ARTISTICA] = act14
    allActivities[eActivityId._15_AJEDREZ] = act15
    allActivities[eActivityId._16_AEROBICOS] = act16
    allActivities[eActivityId._17_NATACION] = act17
    allActivities[eActivityId._18_BOXEO] = act18
    allActivities[eActivityId._19_EQUITACION] = act19
    allActivities[eActivityId._20_GOLF] = act20
    allActivities[eActivityId._21_JUDO] = act21
    allActivities[eActivityId._22_RUGBY] = act22
    allActivities[eActivityId._23_TENIS] = act23
    allActivities[eActivityId._24_VOLEIBOL] = act24
    allActivities[eActivityId._25_HOCKEY] = act25
    allActivities[eActivityId._26_TEATRO] = act26
    allActivities[eActivityId._27_MUSICA] = act27
    allActivities[eActivityId._28_DANZA_FOLCLORICA] = act28
    allActivities[eActivityId._29_BREAK_DANCE] = act29
    allActivities[eActivityId._30_BALLET] = act30
    allActivities[eActivityId._31_HIP_HOP] = act31
    allActivities[eActivityId._32_FOTOGRAFIA] = act32
    allActivities[eActivityId._33_CANTO] = act33
    allActivities[eActivityId._34_DIBUJO_ARTISTICO] = act34
    allActivities[eActivityId._35_CERAMICA] = act35
    allActivities[eActivityId._36_ACUARELA] = act36
    allActivities[eActivityId._37_REALIZACION_AUDIOVISUAL] = act37
    allActivities[eActivityId._38_CREACION_NARRATIVA] = act38
    allActivities[eActivityId._39_POESIA_Y_DECLAMACION] = act39
    allActivities[eActivityId._40_BANDA_MARCIAL] = act40
    allActivities[eActivityId._41_MUSICA_ANDINA] = act41
    allActivities[eActivityId._42_GUITARRA] = act42
    allActivities[eActivityId._43_TITERES] = act43
    allActivities[eActivityId._44_FLAUTAS] = act44
    allActivities[eActivityId._45_CLUB_DE_LECTURA] = act45
    allActivities[eActivityId._46_GRUPO_DE_ROCK] = act46
    allActivities[eActivityId._47_BANDA_SINFONICA] = act47
    allActivities[eActivityId._48_GAITAS_Y_TAMBORES] = act48
    allActivities[eActivityId._49_MUSICA_CARRANGUERA] = act49
    allActivities[eActivityId._50_PIANO] = act50
    allActivities[eActivityId._51_INSTITUTO_COLOMBIANO_DE_BIENESTAR_FAMILIAR] = act51
    allActivities[eActivityId._52_POLICIA_NACIONAL] = act52
    allActivities[eActivityId._53_COMISARIA_DE_FAMILIA] = act53
    allActivities[eActivityId._54_CASA_DE_LA_JUSTICIA] = act54
    allActivities[eActivityId._55_ALCALDIA] = act55
    allActivities[eActivityId._56_SERVICIO_NACIONAL_DE_APRENDIZAJE] = act56
    allActivities[eActivityId._57_CASA_DE_LA_CULTURA] = act57
    allActivities[eActivityId._58_INSTITUTO_MUNICIPAL_DE_RECREACION_Y_DEPORTE] = act58
    allActivities[eActivityId._59_HOSPITAL] = act59
    allActivities[eActivityId._60_CASA_UNIDOS] = act60
    allActivities[eActivityId._61_COMODIN] = act61
