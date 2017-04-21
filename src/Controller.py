#!/usr/bin/python
# -*- coding: latin-1 -*-

"""
Rigoberto Sáenz Imbacuán
Desarrollador para Dispositivos Móviles - Colombia Games
Ingeniero de Sistemas y Computación - Universidad Nacional de Colombia
http://www.rigobertosaenz.com/
"""
import pygame
import threading
import urllib


class eScreen:
    SPLASH_START = 1
    LOGIN = 2
    REGISTRATION = 3
    SELECT_LEVEL = 4
    BOARD = 5
    SPLASH_CLOSE = 6
    
class eLeafUserId:
    MAIN_USER = 0
    PARENTS = 1
    UNCLE = 2
    BROTHER = 3
    COUSIN = 4
    FRIEND = 5
    
class eMatchState:
    NO_LINE = 1
    LINE_1 = 2
    LINE_2 = 3
    ANSWER = 4
    
class eMatchActivityGroup:
    CULTURE = 1
    RECREATION = 2
    SOCIAL = 3
    
class eConnectionState:
    CONNECTING = 1
    SUCCESS = 2
    FAILURE = 3
    
class eConnectionMethod:
    POST = 1
    GET = 2

class eMusic:
    BOARD = 1
    MENU = 2
    
class eSound:
    BOARD_COMPLETE = 1
    OPEN_CARD = 2
    PAIR_CORRECT = 3
    PAIR_INCORRECT = 4
    TIME_OUT = 5
    TIME_RUNNING = 6
    
    HELLO_BOY = 7
    HELLO_GIRL = 8
    LEVEL_WIN = 9
    YUJU_BOY = 10
    YUJU_GIRL = 11
    
class eGameDifficulty:
    EASY = 1
    NORMAL = 2
    HARD = 3
    
class eQuestionAnswer:
    ANSWER_A = 1
    ANSWER_B = 2
    ANSWER_C = 3
    
class eBoardState:
    CAN_PICK_FIRST_CARD = 1
    CAN_PICK_SECOND_CARD = 2
    CAN_NOT_PICK = 3
    COMODIN = 4
    LEVEL_FINISHED = 5
    TIME_OUT = 6
    
class eActivityId:
    _01_BICICROS = 1
    _02_PATINAJE = 2
    _03_FUTSAL = 3
    _04_FUTBOL = 4
    _05_PORRISMO = 5
    _06_ATLETISMO = 6
    _07_BALONCESTO = 7
    _08_KARATE_DO = 8
    _09_LEVANTAMIENTO_DE_PESAS = 9
    _10_TAEKWON_DO = 10
    _11_BADMINTON = 11
    _12_TENIS_DE_MESA = 12
    _13_ESGRIMA = 13
    _14_GIMNASIA_ARTISTICA = 14
    _15_AJEDREZ = 15
    _16_AEROBICOS = 16
    _17_NATACION = 17
    _18_BOXEO = 18
    _19_EQUITACION = 19
    _20_GOLF = 20
    _21_JUDO = 21
    _22_RUGBY = 22
    _23_TENIS = 23
    _24_VOLEIBOL = 24
    _25_HOCKEY = 25
    _26_TEATRO = 26
    _27_MUSICA = 27
    _28_DANZA_FOLCLORICA = 28
    _29_BREAK_DANCE = 29
    _30_BALLET = 30
    _31_HIP_HOP = 31
    _32_FOTOGRAFIA = 32
    _33_CANTO = 33
    _34_DIBUJO_ARTISTICO = 34
    _35_CERAMICA = 35
    _36_ACUARELA = 36
    _37_REALIZACION_AUDIOVISUAL = 37
    _38_CREACION_NARRATIVA = 38
    _39_POESIA_Y_DECLAMACION = 39
    _40_BANDA_MARCIAL = 40
    _41_MUSICA_ANDINA = 41
    _42_GUITARRA = 42
    _43_TITERES = 43
    _44_FLAUTAS = 44
    _45_CLUB_DE_LECTURA = 45
    _46_GRUPO_DE_ROCK = 46
    _47_BANDA_SINFONICA = 47
    _48_GAITAS_Y_TAMBORES = 48
    _49_MUSICA_CARRANGUERA = 49
    _50_PIANO = 50
    _51_INSTITUTO_COLOMBIANO_DE_BIENESTAR_FAMILIAR = 51
    _52_POLICIA_NACIONAL = 52
    _53_COMISARIA_DE_FAMILIA = 53
    _54_CASA_DE_LA_JUSTICIA = 54
    _55_ALCALDIA = 55
    _56_SERVICIO_NACIONAL_DE_APRENDIZAJE = 56
    _57_CASA_DE_LA_CULTURA = 57
    _58_INSTITUTO_MUNICIPAL_DE_RECREACION_Y_DEPORTE = 58
    _59_HOSPITAL = 59
    _60_CASA_UNIDOS = 60
    _61_COMODIN = 61


class ResourceController:
    
    # Audio folder
    music_Board = "res/audio/Board.ogg"
    music_Menu = "res/audio/Menu.ogg"
    
    # -> sounds
    soundBoardComplete = None
    soundOpenCard = None
    soundPairCorrect = None
    soundPairIncorrect = None
    soundTimeOut = None
    
    soundHelloBoy = None
    soundHelloGirl = None
    soundLevelWin = None
    soundYujuBoy = None
    soundYujuGirl = None
        
    @staticmethod
    def doInit():
        
        # -> sounds
        ResourceController.soundBoardComplete = pygame.mixer.Sound("res/audio/sounds/BoardComplete.ogg")
        ResourceController.soundOpenCard = pygame.mixer.Sound("res/audio/sounds/OpenCard.ogg")
        ResourceController.soundPairCorrect = pygame.mixer.Sound("res/audio/sounds/PairCorrect.ogg")
        ResourceController.soundPairIncorrect = pygame.mixer.Sound("res/audio/sounds/PairIncorrect.ogg")
        ResourceController.soundTimeOut = pygame.mixer.Sound("res/audio/sounds/TimeOut.ogg")
        ResourceController.soundTimeRunning = pygame.mixer.Sound("res/audio/sounds/TimeRunning.ogg")
        
        ResourceController.soundHelloBoy = pygame.mixer.Sound("res/audio/sounds/cheers/HelloBoy.ogg")
        ResourceController.soundHelloGirl = pygame.mixer.Sound("res/audio/sounds/cheers/HelloGirl.ogg")
        ResourceController.soundLevelWin = pygame.mixer.Sound("res/audio/sounds/cheers/LevelWin.ogg")
        ResourceController.soundYujuBoy = pygame.mixer.Sound("res/audio/sounds/cheers/YujuBoy.ogg")
        ResourceController.soundYujuGirl = pygame.mixer.Sound("res/audio/sounds/cheers/YujuGirl.ogg")
    
        ResourceController.soundBoardComplete.set_volume(0.8)
        ResourceController.soundOpenCard.set_volume(0.6)
        ResourceController.soundPairCorrect.set_volume(1.0)
        ResourceController.soundPairIncorrect.set_volume(1.0)
        ResourceController.soundTimeOut.set_volume(1.0)
        ResourceController.soundTimeRunning.set_volume(1.0)
        
        ResourceController.soundHelloBoy.set_volume(1.0)
        ResourceController.soundHelloGirl.set_volume(1.0)
        ResourceController.soundLevelWin.set_volume(1.0)
        ResourceController.soundYujuBoy.set_volume(1.0)
        ResourceController.soundYujuGirl.set_volume(1.0)
    
    # Background folder
    background_Answer = pygame.image.load("res/background/Answer.png")
    background_BoardA = pygame.image.load("res/background/BoardA.png")
    background_BoardB = pygame.image.load("res/background/BoardB.png")
    background_BoardC = pygame.image.load("res/background/BoardC.png")
    background_BoardD = pygame.image.load("res/background/BoardD.png")
    background_BoardE = pygame.image.load("res/background/BoardE.png")
    background_BoardF = pygame.image.load("res/background/BoardF.png")
    background_Login = pygame.image.load("res/background/Login.png")
    background_Match = pygame.image.load("res/background/Match.png")
    background_Question = pygame.image.load("res/background/Question.png")
    background_Registration = pygame.image.load("res/background/Registration.png")
    background_SelectLevel = pygame.image.load("res/background/SelectLevel.png")
    background_Splash_1 = pygame.image.load("res/background/Splash_1.png")
    background_Splash_2 = pygame.image.load("res/background/Splash_2.png")
    background_Splash_3 = pygame.image.load("res/background/Splash_3.png")
    background_Splash_4 = pygame.image.load("res/background/Splash_4.png")
    background_Splash_5 = pygame.image.load("res/background/Splash_5.png")
    background_Standard = pygame.image.load("res/background/Standard.png")
    background_Transparent = pygame.image.load("res/background/Transparent.png")
    
    # Input folder
    input_Accept_On = pygame.image.load("res/input/Accept_On.png")
    input_Accept_Off = pygame.image.load("res/input/Accept_Off.png")
    input_AnswerA_On = pygame.image.load("res/input/AnswerA_On.png")
    input_AnswerA_Off = pygame.image.load("res/input/AnswerA_Off.png")
    input_AnswerB_On = pygame.image.load("res/input/AnswerB_On.png")
    input_AnswerB_Off = pygame.image.load("res/input/AnswerB_Off.png")
    input_AnswerC_On = pygame.image.load("res/input/AnswerC_On.png")
    input_AnswerC_Off = pygame.image.load("res/input/AnswerC_Off.png")
    input_Cancel_On = pygame.image.load("res/input/Cancel_On.png")
    input_Cancel_Off = pygame.image.load("res/input/Cancel_Off.png")
    input_CloseGame_On = pygame.image.load("res/input/CloseGame_On.png")
    input_CloseGame_Off = pygame.image.load("res/input/CloseGame_Off.png")
    input_Connecting = pygame.image.load("res/input/Connecting.png")
    input_LevelEasy_Off = pygame.image.load("res/input/LevelEasy_Off.png")
    input_LevelEasy_On = pygame.image.load("res/input/LevelEasy_On.png")
    input_LevelHard_Off = pygame.image.load("res/input/LevelHard_Off.png")
    input_LevelHard_On = pygame.image.load("res/input/LevelHard_On.png")
    input_LevelNormal_Off = pygame.image.load("res/input/LevelNormal_Off.png")
    input_LevelNormal_On = pygame.image.load("res/input/LevelNormal_On.png")
    input_Login_On = pygame.image.load("res/input/Login_On.png")
    input_Login_Off = pygame.image.load("res/input/Login_Off.png")
    input_LoginBrother = pygame.image.load("res/input/LoginBrother.png")
    input_LoginCousin = pygame.image.load("res/input/LoginCousin.png")
    input_LoginFriend = pygame.image.load("res/input/LoginFriend.png")
    input_LoginInput = pygame.image.load("res/input/LoginInput.png")
    input_LoginMainUser = pygame.image.load("res/input/LoginMainUser.png")
    input_LoginParent = pygame.image.load("res/input/LoginParent.png")
    input_LoginUncle = pygame.image.load("res/input/LoginUncle.png")
    input_NextLevel_On = pygame.image.load("res/input/NextLevel_On.png")
    input_NextLevel_Off = pygame.image.load("res/input/NextLevel_Off.png")
    input_Registration_On = pygame.image.load("res/input/Registration_On.png")
    input_Registration_Off = pygame.image.load("res/input/Registration_Off.png")
            
    # Cursor folder
    cursor_Sugar = "res/cursor/Sugar.xbm"
    cursor_SugarMask = "res/cursor/SugarMask.xbm"
    
    # Font folder
    font_BorisBlackBloxx = "res/font/BorisBlackBloxx.ttf"
    
    # Game folder
    game_Boy = pygame.image.load("res/game/Boy.png")
    game_CardClose = pygame.image.load("res/game/CardClose.png")
    game_CardOpen = pygame.image.load("res/game/CardOpen.png")
    game_ClockBig = pygame.image.load("res/game/ClockBig.png")
    game_ClockMini = pygame.image.load("res/game/ClockMini.png")
    game_MessageGoodWork = pygame.image.load("res/game/MessageGoodWork.png")
    game_MessageTryAgain = pygame.image.load("res/game/MessageTryAgain.png")
    game_MessageWrongAnswer = pygame.image.load("res/game/MessageWrongAnswer.png")
    game_MessageYouGot = pygame.image.load("res/game/MessageYouGot.png")
    
    game_Number1 = pygame.image.load("res/game/Number1.png")
    game_Number2 = pygame.image.load("res/game/Number2.png")
    game_Number3 = pygame.image.load("res/game/Number3.png")
    game_Number4 = pygame.image.load("res/game/Number4.png")
    game_Number5 = pygame.image.load("res/game/Number5.png")
    game_Number6 = pygame.image.load("res/game/Number6.png")
    game_Number7 = pygame.image.load("res/game/Number7.png")
    game_Number8 = pygame.image.load("res/game/Number8.png")
    game_Number9 = pygame.image.load("res/game/Number9.png")
    game_Number10 = pygame.image.load("res/game/Number10.png")
    game_StarBig_Off = pygame.image.load("res/game/StarBig_Off.png")
    game_StarBig_On = pygame.image.load("res/game/StarBig_On.png")
    game_StarMini = pygame.image.load("res/game/StarMini.png")
    game_StatsBackground = pygame.image.load("res/game/StatsBackground.png")
    
    # -> Match folder
    game_SelectorWhite = pygame.image.load("res/game/match/SelectorWhite.png")
    game_SelectorYellow = pygame.image.load("res/game/match/SelectorYellow.png")
    
    # -> Culture folder
    game_CultureLogo = pygame.image.load("res/game/match/culture/Logo.png")
    game_Culture_Bailar = pygame.image.load("res/game/match/culture/Bailar.png")
    game_Culture_Guitarra = pygame.image.load("res/game/match/culture/Guitarra.png")
    game_Culture_Teatro = pygame.image.load("res/game/match/culture/Teatro.png")
    
    # -> Recreation folder
    game_RecreationLogo = pygame.image.load("res/game/match/recreation/Logo.png")
    game_Recreation_Atletismo = pygame.image.load("res/game/match/recreation/Atletismo.png")
    game_Recreation_Basketball = pygame.image.load("res/game/match/recreation/Basketball.png")
    game_Recreation_Deportes = pygame.image.load("res/game/match/recreation/Deportes.png")
        
    # -> Social folder
    game_SocialLogo = pygame.image.load("res/game/match/social/Logo.png")
    game_Social_Anciano = pygame.image.load("res/game/match/social/Anciano.png")
    game_Social_Arena = pygame.image.load("res/game/match/social/Arena.png")
    game_Social_Floristeria = pygame.image.load("res/game/match/social/Floristeria.png")
    game_Social_Jovenes = pygame.image.load("res/game/match/social/Jovenes.png")
    
    # -> Lines folder
    game_Line1_1 = pygame.image.load("res/game/match/lines/line1-1.png")
    game_Line1_2 = pygame.image.load("res/game/match/lines/line1-2.png")
    game_Line1_3 = pygame.image.load("res/game/match/lines/line1-3.png")
    game_Line2_1 = pygame.image.load("res/game/match/lines/line2-1.png")
    game_Line2_2 = pygame.image.load("res/game/match/lines/line2-2.png")
    game_Line2_3 = pygame.image.load("res/game/match/lines/line2-3.png")
    game_Line3_1 = pygame.image.load("res/game/match/lines/line3-1.png")
    game_Line3_2 = pygame.image.load("res/game/match/lines/line3-2.png")
    game_Line3_3 = pygame.image.load("res/game/match/lines/line3-3.png")
    
    # -> Activities
    game_Activity01Bicicros = pygame.image.load("res/game/activities/01Bicicros.png")
    game_Activity02Patinaje = pygame.image.load("res/game/activities/02Patinaje.png")
    game_Activity03Futsal = pygame.image.load("res/game/activities/03Futsal.png")
    game_Activity04Futbol = pygame.image.load("res/game/activities/04Futbol.png")
    game_Activity05Porrismo = pygame.image.load("res/game/activities/05Porrismo.png")
    game_Activity06Atletismo = pygame.image.load("res/game/activities/06Atletismo.png")
    game_Activity07Baloncesto = pygame.image.load("res/game/activities/07Baloncesto.png")
    game_Activity08KarateDo = pygame.image.load("res/game/activities/08KarateDo.png")
    game_Activity09LevantamientoDePesas = pygame.image.load("res/game/activities/09LevantamientoDePesas.png")
    game_Activity10TaekwonDo = pygame.image.load("res/game/activities/10TaekwonDo.png")
    game_Activity11Badminton = pygame.image.load("res/game/activities/11Badminton.png")
    game_Activity12TenisDeMesa = pygame.image.load("res/game/activities/12TenisDeMesa.png")
    game_Activity13Esgrima = pygame.image.load("res/game/activities/13Esgrima.png")
    game_Activity14GimnasiaArtistica = pygame.image.load("res/game/activities/14GimnasiaArtistica.png")
    game_Activity15Ajedrez = pygame.image.load("res/game/activities/15Ajedrez.png")
    game_Activity16Aerobicos = pygame.image.load("res/game/activities/16Aerobicos.png")
    game_Activity17Natacion = pygame.image.load("res/game/activities/17Natacion.png")
    game_Activity18Boxeo = pygame.image.load("res/game/activities/18Boxeo.png")
    game_Activity19Equitacion = pygame.image.load("res/game/activities/19Equitacion.png")
    game_Activity20Golf = pygame.image.load("res/game/activities/20Golf.png")
    game_Activity21Judo = pygame.image.load("res/game/activities/21Judo.png")
    game_Activity22Rugby = pygame.image.load("res/game/activities/22Rugby.png")
    game_Activity23Tenis = pygame.image.load("res/game/activities/23Tenis.png")
    game_Activity24Voleibol = pygame.image.load("res/game/activities/24Voleibol.png")
    game_Activity25Hockey = pygame.image.load("res/game/activities/25Hockey.png")
    game_Activity26Teatro = pygame.image.load("res/game/activities/26Teatro.png")
    game_Activity27Musica = pygame.image.load("res/game/activities/27Musica.png")
    game_Activity28DanzaFolclorica = pygame.image.load("res/game/activities/28DanzaFolclorica.png")
    game_Activity29BreakDance = pygame.image.load("res/game/activities/29BreakDance.png")
    game_Activity30Ballet = pygame.image.load("res/game/activities/30Ballet.png")
    game_Activity31HipHop = pygame.image.load("res/game/activities/31HipHop.png")
    game_Activity32Fotografia = pygame.image.load("res/game/activities/32Fotografia.png")
    game_Activity33Canto = pygame.image.load("res/game/activities/33Canto.png")
    game_Activity34DibujoArtistico = pygame.image.load("res/game/activities/34DibujoArtistico.png")
    game_Activity35Ceramica = pygame.image.load("res/game/activities/35Ceramica.png")
    game_Activity36Acuarela = pygame.image.load("res/game/activities/36Acuarela.png")
    game_Activity37RealizacionAudiovisual = pygame.image.load("res/game/activities/37RealizacionAudiovisual.png")
    game_Activity38CreacionNarrativa = pygame.image.load("res/game/activities/38CreacionNarrativa.png")
    game_Activity39PoesiaYDeclamacion = pygame.image.load("res/game/activities/39PoesiaYDeclamacion.png")
    game_Activity40BandaMarcial = pygame.image.load("res/game/activities/40BandaMarcial.png")
    game_Activity41MusicaAndina = pygame.image.load("res/game/activities/41MusicaAndina.png")
    game_Activity42Guitarra = pygame.image.load("res/game/activities/42Guitarra.png")
    game_Activity43Titeres = pygame.image.load("res/game/activities/43Titeres.png")
    game_Activity44Flautas = pygame.image.load("res/game/activities/44Flautas.png")
    game_Activity45ClubDeLectura = pygame.image.load("res/game/activities/45ClubDeLectura.png")
    game_Activity46GrupoDeRock = pygame.image.load("res/game/activities/46GrupoDeRock.png")
    game_Activity47BandaSinfonica = pygame.image.load("res/game/activities/47BandaSinfonica.png")
    game_Activity48GaitasYTambores = pygame.image.load("res/game/activities/48GaitasYTambores.png")
    game_Activity49MusicaCarranguera = pygame.image.load("res/game/activities/49MusicaCarranguera.png")
    game_Activity50Piano = pygame.image.load("res/game/activities/50Piano.png")
    game_Activity51InstitutoColombianoDeBienestarFamiliar = pygame.image.load("res/game/activities/51InstitutoColombianoDeBienestarFamiliar.png")
    game_Activity52PoliciaNacional = pygame.image.load("res/game/activities/52PoliciaNacional.png")
    game_Activity53ComisariaDeFamilia = pygame.image.load("res/game/activities/53ComisariaDeFamilia.png")
    game_Activity54CasaDeLaJusticia = pygame.image.load("res/game/activities/54CasaDeLaJusticia.png")
    game_Activity55Alcaldia = pygame.image.load("res/game/activities/55Alcaldia.png")
    game_Activity56ServicioNacionalDeAprendizaje = pygame.image.load("res/game/activities/56ServicioNacionalDeAprendizaje.png")
    game_Activity57CasaDeLaCultura = pygame.image.load("res/game/activities/57CasaDeLaCultura.png")
    game_Activity58InstitutoMunicipalDeRecreacionYDeport = pygame.image.load("res/game/activities/58InstitutoMunicipalDeRecreacionYDeporte.png")
    game_Activity59Hospital = pygame.image.load("res/game/activities/59Hospital.png")
    game_Activity60CasaUnidos = pygame.image.load("res/game/activities/60CasaUnidos.png")
    game_Activity61Comodin = pygame.image.load("res/game/activities/61Comodin.png")


class FontController:

    font5 = None
    font10 = None
    font15 = None
    font16 = None
    font17 = None
    font18 = None
    font19 = None
    font20 = None
    font21 = None
    font22 = None
    font23 = None
    font24 = None
    font25 = None
    font26 = None
    font27 = None
    font28 = None
    font29 = None
    font30 = None
    font35 = None
    font40 = None
    font60 = None
    
    @staticmethod
    def doInit():
        FontController.font5 = pygame.font.Font(ResourceController.font_BorisBlackBloxx, 5)
        FontController.font10 = pygame.font.Font(ResourceController.font_BorisBlackBloxx, 10)
        FontController.font15 = pygame.font.Font(ResourceController.font_BorisBlackBloxx, 15)
        FontController.font16 = pygame.font.Font(ResourceController.font_BorisBlackBloxx, 16)
        FontController.font17 = pygame.font.Font(ResourceController.font_BorisBlackBloxx, 17)
        FontController.font18 = pygame.font.Font(ResourceController.font_BorisBlackBloxx, 18)
        FontController.font19 = pygame.font.Font(ResourceController.font_BorisBlackBloxx, 19)
        FontController.font20 = pygame.font.Font(ResourceController.font_BorisBlackBloxx, 20)
        FontController.font21 = pygame.font.Font(ResourceController.font_BorisBlackBloxx, 21)
        FontController.font22 = pygame.font.Font(ResourceController.font_BorisBlackBloxx, 22)
        FontController.font23 = pygame.font.Font(ResourceController.font_BorisBlackBloxx, 23)
        FontController.font24 = pygame.font.Font(ResourceController.font_BorisBlackBloxx, 24)
        FontController.font25 = pygame.font.Font(ResourceController.font_BorisBlackBloxx, 25)
        FontController.font26 = pygame.font.Font(ResourceController.font_BorisBlackBloxx, 26)
        FontController.font27 = pygame.font.Font(ResourceController.font_BorisBlackBloxx, 27)
        FontController.font28 = pygame.font.Font(ResourceController.font_BorisBlackBloxx, 28)
        FontController.font29 = pygame.font.Font(ResourceController.font_BorisBlackBloxx, 29)
        FontController.font30 = pygame.font.Font(ResourceController.font_BorisBlackBloxx, 30)
        FontController.font35 = pygame.font.Font(ResourceController.font_BorisBlackBloxx, 35)
        FontController.font40 = pygame.font.Font(ResourceController.font_BorisBlackBloxx, 40)
        FontController.font60 = pygame.font.Font(ResourceController.font_BorisBlackBloxx, 60)
   
class ConnectionController(threading.Thread):
    
    def __init__(self, method, url, parameters):
        threading.Thread.__init__(self)
        self.__method = method
        self.__url = url
        self.__parameters = parameters
        self.__state = None
        self.__result = None
  
    def run(self):
        
        # Comienza el proceso de conexion
        self.__state = eConnectionState.CONNECTING
        
        # Hacemos la solicitud por POST
        if self.__method == eConnectionMethod.POST:
            
            try:
                self.__result = urllib.urlopen(self.__url, self.__parameters).read()
                self.__state = eConnectionState.SUCCESS
            except: 
                self.__state = eConnectionState.FAILURE
            
    def getResult(self):
        return self.__result
        
    def getState(self):        
        return self.__state
    

class GlobalsController:
    
    # Game
    GAME_ID = 1  # 1 = ParticipAcción
    GAME_FPS = 40
    GAME_DIFFICULTY = eGameDifficulty.EASY
    
    # Info for persistence (Datos iniciales para detectar errores)
    INFO_USERNAME = "None"
    INFO_PASSWORD = "None"
    INFO_ROOT_USER_ID = -1
    INFO_LEAF_USER_ID = -1
    INFO_START_TIME = "None"
    INFO_FINISH_TIME = "None"
    INFO_STARS = 0
    
    # Audio
    AUDIO_FREQ = 44100  # same as audio CD
    AUDIO_BITSIZE = -16  # unsigned 16 bit
    AUDIO_CHANNELS = 2  # 1 == mono, 2 == stereo
    AUDIO_BUFFER = 1024  # audio buffer size in no of samples
    AUDIO_FRAMERATE = 30  # how often to check if playback has finished
    
    # Display (xo display size)
    DISPLAY_WIDTH = 1200
    DISPLAY_HEIGHT = 900 - 75
    
class MusicThread(threading.Thread):
    
    def __init__(self, musicId):
        
        threading.Thread.__init__(self)
        
        if musicId == eMusic.BOARD:
            self.__musicFile = ResourceController.music_Board
            pygame.mixer.music.set_volume(0.2)
        elif musicId == eMusic.MENU:
            self.__musicFile = ResourceController.music_Menu
            pygame.mixer.music.set_volume(0.2)
        
        self.__noRepetitions = -1  # -1 : Reproduccion continua
        self.__isPlaying = False
  
    def run(self):
        # Stream music with mixer.music module in blocking manner.
        # This will stream the sound from disk while playing.
        pygame.mixer.music.load(self.__musicFile)
        pygame.mixer.music.play(self.__noRepetitions)
        self.__isPlaying = False
        
        clock = pygame.time.Clock()
        while (self.__isPlaying == True) and (pygame.mixer.music.get_busy()):
            clock.tick(GlobalsController.AUDIO_FRAMERATE)
        
    def stop(self):
        pygame.mixer.music.stop()
        self.__isPlaying = False
          
          
class SoundThread(threading.Thread):
    
    def __init__(self, soundFile, noRepetitions):
        
        threading.Thread.__init__(self)
        self.__soundFile = soundFile
        self.__isPlaying = False
        
        if noRepetitions == 0:
            # -1 : Reproduccion continua
            self.__noRepetitions = -1
        else:
            if noRepetitions > 0:
                self.__noRepetitions = noRepetitions - 1
            else:
                self.__noRepetitions = 0
    
    def run(self):
        
        # Play sound through default mixer channel in blocking manner.
        # This will load the whole sound into memory before playback
        self.__soundFile.play(self.__noRepetitions)
        self.__isPlaying = True
        
        clock = pygame.time.Clock()
        while pygame.mixer.get_busy():
            clock.tick(GlobalsController.AUDIO_FRAMERATE)
            
        self.__isPlaying = False
    
    def stop(self):
        pygame.mixer.stop()
        self.__isPlaying = False
        
    def isPlaying(self):
        return self.__isPlaying


class AudioController:

    __musicThread = None
    
    __soundThreadBoardComplete = None
    __soundThreadOpenCard = None
    __soundThreadPairCorrect = None
    __soundThreadPairIncorrect = None
    __soundThreadTimeOut = None
    __soundThreadTimeRunning = None
    
    __soundThreadHelloBoy = None
    __soundThreadHelloGirl = None
    __soundThreadLevelWin = None
    __soundThreadYujuBoy = None
    __soundThreadYujuGirl = None
    
    @staticmethod
    def playSound(soundId, noRepetitions):
        
        # Detenemos los hilos que ya no estan reproduciendo un sonido
        AudioController.__cleanNonActiveThreads()
        
        # Detenemos el hilo que esta utilizando el sonido que se quiere reproducir
        AudioController.__stopSound(soundId)
        
        # Reproduciomos el sonido solicitado
        if soundId == eSound.BOARD_COMPLETE:
            AudioController.__soundThreadBoardComplete = SoundThread(ResourceController.soundBoardComplete, noRepetitions)
            AudioController.__soundThreadBoardComplete.start()
            
        elif soundId == eSound.OPEN_CARD:
            AudioController.__soundThreadOpenCard = SoundThread(ResourceController.soundOpenCard, noRepetitions)
            AudioController.__soundThreadOpenCard.start()
            
        elif soundId == eSound.PAIR_CORRECT:
            AudioController.__soundThreadPairCorrect = SoundThread(ResourceController.soundPairCorrect, noRepetitions)
            AudioController.__soundThreadPairCorrect.start()
            
        elif soundId == eSound.PAIR_INCORRECT:
            AudioController.__soundThreadPairIncorrect = SoundThread(ResourceController.soundPairIncorrect, noRepetitions)
            AudioController.__soundThreadPairIncorrect.start()
            
        elif soundId == eSound.TIME_OUT:
            AudioController.__soundThreadTimeOut = SoundThread(ResourceController.soundTimeOut, noRepetitions)
            AudioController.__soundThreadTimeOut.start()
            
        elif soundId == eSound.TIME_RUNNING:
            AudioController.__soundThreadTimeRunning = SoundThread(ResourceController.soundTimeRunning, noRepetitions)
            AudioController.__soundThreadTimeRunning.start()
            
            
        elif soundId == eSound.HELLO_BOY:
            AudioController.__soundThreadHelloBoy = SoundThread(ResourceController.soundHelloBoy, noRepetitions)
            AudioController.__soundThreadHelloBoy.start()
                                    
        elif soundId == eSound.HELLO_GIRL:
            AudioController.__soundThreadHelloGirl = SoundThread(ResourceController.soundHelloGirl, noRepetitions)
            AudioController.__soundThreadHelloGirl.start()
                                    
        elif soundId == eSound.LEVEL_WIN:
            AudioController.__soundThreadLevelWin = SoundThread(ResourceController.soundLevelWin, noRepetitions)
            AudioController.__soundThreadLevelWin.start()
                                    
        elif soundId == eSound.YUJU_BOY:
            AudioController.__soundThreadYujuBoy = SoundThread(ResourceController.soundYujuBoy, noRepetitions)
            AudioController.__soundThreadYujuBoy.start()
                                    
        elif soundId == eSound.YUJU_GIRL:
            AudioController.__soundThreadYujuGirl = SoundThread(ResourceController.soundYujuGirl, noRepetitions)
            AudioController.__soundThreadYujuGirl.start()

    @staticmethod
    def __cleanNonActiveThreads():
        if (AudioController.__soundThreadBoardComplete != None) and (AudioController.__soundThreadBoardComplete.isPlaying() == False):
            AudioController.__stopSound(eSound.BOARD_COMPLETE)            
        if (AudioController.__soundThreadOpenCard != None) and (AudioController.__soundThreadOpenCard.isPlaying() == False):
            AudioController.__stopSound(eSound.OPEN_CARD)            
        if (AudioController.__soundThreadPairCorrect != None) and (AudioController.__soundThreadPairCorrect.isPlaying() == False):
            AudioController.__stopSound(eSound.PAIR_CORRECT)            
        if (AudioController.__soundThreadPairIncorrect != None) and (AudioController.__soundThreadPairIncorrect.isPlaying() == False):
            AudioController.__stopSound(eSound.PAIR_INCORRECT)            
        if (AudioController.__soundThreadTimeOut != None) and (AudioController.__soundThreadTimeOut.isPlaying() == False):
            AudioController.__stopSound(eSound.TIME_OUT)            
        if (AudioController.__soundThreadTimeRunning != None) and (AudioController.__soundThreadTimeRunning.isPlaying() == False):
            AudioController.__stopSound(eSound.TIME_RUNNING)            
            
        if (AudioController.__soundThreadHelloBoy != None) and (AudioController.__soundThreadHelloBoy.isPlaying() == False):
            AudioController.__stopSound(eSound.HELLO_BOY)
        if (AudioController.__soundThreadHelloGirl != None) and (AudioController.__soundThreadHelloGirl.isPlaying() == False):
            AudioController.__stopSound(eSound.HELLO_GIRL)
        if (AudioController.__soundThreadLevelWin != None) and (AudioController.__soundThreadLevelWin.isPlaying() == False):
            AudioController.__stopSound(eSound.LEVEL_WIN)
        if (AudioController.__soundThreadYujuBoy != None) and (AudioController.__soundThreadYujuBoy.isPlaying() == False):
            AudioController.__stopSound(eSound.YUJU_BOY)
        if (AudioController.__soundThreadYujuGirl != None) and (AudioController.__soundThreadYujuGirl.isPlaying() == False):
            AudioController.__stopSound(eSound.YUJU_GIRL)

    @staticmethod
    def __stopSound(soundId):
        
        if soundId == eSound.BOARD_COMPLETE:
            if AudioController.__soundThreadBoardComplete != None:
                AudioController.__soundThreadBoardComplete.stop()
                AudioController.__soundThreadBoardComplete = None
        
        elif soundId == eSound.OPEN_CARD:
            if AudioController.__soundThreadOpenCard != None:
                AudioController.__soundThreadOpenCard.stop()
                AudioController.__soundThreadOpenCard = None
                
        elif soundId == eSound.PAIR_CORRECT:
            if AudioController.__soundThreadPairCorrect != None:
                AudioController.__soundThreadPairCorrect.stop()
                AudioController.__soundThreadPairCorrect = None
                
        elif soundId == eSound.PAIR_INCORRECT:
            if AudioController.__soundThreadPairIncorrect != None:
                AudioController.__soundThreadPairIncorrect.stop()
                AudioController.__soundThreadPairIncorrect = None
                
        elif soundId == eSound.TIME_OUT:
            if AudioController.__soundThreadTimeOut != None:
                AudioController.__soundThreadTimeOut.stop()
                AudioController.__soundThreadTimeOut = None
                
        elif soundId == eSound.TIME_RUNNING:
            if AudioController.__soundThreadTimeRunning != None:
                AudioController.__soundThreadTimeRunning.stop()
                AudioController.__soundThreadTimeRunning = None
                
                
        elif soundId == eSound.HELLO_BOY:
            if AudioController.__soundThreadHelloBoy != None:
                AudioController.__soundThreadHelloBoy.stop()
                AudioController.__soundThreadHelloBoy = None
                                
        elif soundId == eSound.HELLO_GIRL:
            if AudioController.__soundThreadHelloGirl != None:
                AudioController.__soundThreadHelloGirl.stop()
                AudioController.__soundThreadHelloGirl = None
                                
        elif soundId == eSound.LEVEL_WIN:
            if AudioController.__soundThreadLevelWin != None:
                AudioController.__soundThreadLevelWin.stop()
                AudioController.__soundThreadLevelWin = None
                                
        elif soundId == eSound.YUJU_BOY:
            if AudioController.__soundThreadYujuBoy != None:
                AudioController.__soundThreadYujuBoy.stop()
                AudioController.__soundThreadYujuBoy = None
                                
        elif soundId == eSound.YUJU_GIRL:
            if AudioController.__soundThreadYujuGirl != None:
                AudioController.__soundThreadYujuGirl.stop()
                AudioController.__soundThreadYujuGirl = None
            
    @staticmethod
    def stopSounds():
        AudioController.__stopSound(eSound.BOARD_COMPLETE)
        AudioController.__stopSound(eSound.OPEN_CARD)
        AudioController.__stopSound(eSound.PAIR_CORRECT)
        AudioController.__stopSound(eSound.PAIR_INCORRECT)
        AudioController.__stopSound(eSound.TIME_OUT)
        AudioController.__stopSound(eSound.TIME_RUNNING)
        
        AudioController.__stopSound(eSound.HELLO_BOY)
        AudioController.__stopSound(eSound.HELLO_GIRL)
        AudioController.__stopSound(eSound.LEVEL_WIN)
        AudioController.__stopSound(eSound.YUJU_BOY)
        AudioController.__stopSound(eSound.YUJU_GIRL)

    @staticmethod
    def playMusic(musicId):
        
        # Detenemos cualquier musica de fondo que se este reproduciendo
        AudioController.stopMusic()
        
        # Iniciamos la reproduccion en un Thread
        AudioController.__musicThread = MusicThread(musicId)
        AudioController.__musicThread.start()
        
    @staticmethod
    def stopMusic():
        if AudioController.__musicThread != None:
            AudioController.__musicThread.stop()
            AudioController.__musicThread = None
