#!/usr/bin/python
# -*- coding: latin-1 -*-

"""
Rigoberto Sáenz Imbacuán
Desarrollador para Dispositivos Móviles - Colombia Games
Ingeniero de Sistemas y Computación - Universidad Nacional de Colombia
http://www.rigobertosaenz.com/
"""
from src.Controller import ResourceController, GlobalsController, \
    AudioController, FontController, ConnectionController, eScreen, eBoardState, \
    eGameDifficulty, eMusic, eQuestionAnswer, eSound, eActivityId, eConnectionState, \
    eConnectionMethod, eLeafUserId, eMatchState, eMatchActivityGroup
from src.Model import InformationActivities, Card
from random import randrange
import datetime
import olpcgames
import os
import pygame
import random
import urllib


class View:
    
    __clock = None
    __displaySurface = None
    __currentScreen = None
    
    @staticmethod
    def doInit():
        
        # Cargamos el cursor standard de Sugar
        if olpcgames.ACTIVITY:  # Running as Activity
            a, b, c, d = pygame.cursors.load_xbm(ResourceController.cursor_Sugar, ResourceController.cursor_SugarMask)
            pygame.mouse.set_cursor(a, b, c, d)

        # Este reloj se usa para correr el juego a un FPS determinados
        View.__clock = pygame.time.Clock()

        # Determinamos la resolucion de pantalla
        if olpcgames.ACTIVITY:  # Running as Activity
            resolution = (0, 0)
            flags = pygame.FULLSCREEN
            
        else:
            resolution = (GlobalsController.DISPLAY_WIDTH, GlobalsController.DISPLAY_HEIGHT)
            flags = 0
        
        # Creamos la superficie principal
        View.__displaySurface = pygame.display.set_mode(resolution, flags)
            
        # Titulo de la ventana del juego (Solo Standalone)
        pygame.display.set_caption("ParticipAccion - Colombia Games / OLPC Colombia / ANSPE")
        
        # Color inicial de fondo
        View.__displaySurface.fill((255, 255, 255))
    
    @staticmethod
    def showScreen(screenId):
        
        # Desactivamos la pantalla actual
        if View.__currentScreen is not None:
            View.__currentScreen.deactivate()
        
        # Creamos una nueva pantalla de acuerdo a la solicitud
        if screenId == eScreen.SPLASH_START:
            __currentScreen = ScreenStartSplash(View.__clock, View.__displaySurface)
            __currentScreen.activate()
               
        elif screenId == eScreen.LOGIN:
            __currentScreen = ScreenLogin(View.__clock, View.__displaySurface)
            __currentScreen.activate()

        elif screenId == eScreen.REGISTRATION:
            __currentScreen = ScreenRegistration(View.__clock, View.__displaySurface)
            __currentScreen.activate()
            
        elif screenId == eScreen.SELECT_LEVEL:
            __currentScreen = ScreenSelectLevel(View.__clock, View.__displaySurface)
            __currentScreen.activate()
            
        elif screenId == eScreen.BOARD:
            __currentScreen = ScreenBoard(View.__clock, View.__displaySurface)
            __currentScreen.activate()
            
        elif screenId == eScreen.SPLASH_CLOSE:
            __currentScreen = ScreenCloseSplash(View.__clock, View.__displaySurface)
            __currentScreen.activate()


class ScreenStartSplash:
    
    def __init__(self, clock, displaySurface):
        
        
        # Debug
        #if olpcgames.ACTIVITY:  # Running as Activity
        #    name = os.path.join(olpcgames.util.get_activity_root(), 'data', 'UserInfo.txt')
        #    newFile = open(name, 'w+')
        #else:
        #    newFile = open('UserInfo.txt', 'w+')
        #newFile.write('''rootUserId:''' + '''1''' + '''\n''')
        #newFile.write('''username:''' + '''betobeto123''' + '''\n''')
        #newFile.write('''password:''' + '''123''' + '''\n''')
        # Debug
        
        
        # Screen
        self.__clock = clock
        self.__displaySurface = displaySurface
        self.__isActive = False
        
        # Time
        self.__count = 1
        self.__to2SplashTime = 30
        self.__to3SplashTime = 60
        self.__to4SplashTime = 90
        self.__to5SplashTime = 120
        self.__endTime = 150
        
        # Image
        self.__image = None
        self.__imageId = 1
        self.__doUpdateImage()
        
        # Text
        self.__text = Label("Proyecto de Innovación Social", FontController.font60, (255, 255, 0), (0, 150))
        self.__text.setPosition((600 - (self.__text.getTextRenderLen() / 2), self.__text.getPosition()[1]))
        
        self.__shadow = Label("Proyecto de Innovación Social", FontController.font60, (0, 0, 0), (0, 150 + 4))
        self.__shadow.setPosition((600 + 4 - (self.__shadow.getTextRenderLen() / 2), self.__shadow.getPosition()[1]))

    def __doTask(self):
        
        # Operaciones de la Screen
        self.__count = self.__count + 1
        
        if self.__count == self.__to2SplashTime:
            self.__imageId = self.__imageId + 1
            self.__doUpdateImage()
            
        elif self.__count == self.__to3SplashTime:
            self.__imageId = self.__imageId + 1
            self.__doUpdateImage()
            
        elif self.__count == self.__to4SplashTime:
            self.__imageId = self.__imageId + 1
            self.__doUpdateImage()
            
        elif self.__count == self.__to5SplashTime:
            self.__imageId = self.__imageId + 1
            self.__doUpdateImage()
            
        elif self.__count == self.__endTime:
            
            # ------------------------------------------------------------------------------------------
            # No persistencia
            # ------------------------------------------------------------------------------------------
            View.showScreen(eScreen.SELECT_LEVEL)
            return
            # ------------------------------------------------------------------------------------------
            # Para activar la persistencia del juego solo es necesario remover el codigo anterior (Ver Tambien ScreenCloseSplash)
            # ------------------------------------------------------------------------------------------
            
            
            # Determinamos si el archivo existe y contiene los datos necesarios para el login
            persistedRootUserId = None
            persistedUsername = None
            persistedPassword = None
                
            try:
                openedFile = None
                
                # Abrimos el archivo en modo Solo Lectura
                if olpcgames.ACTIVITY:  # Running as Activity
                    name = os.path.join(olpcgames.util.get_activity_root(), 'data', 'UserInfo.txt')
                    openedFile = open(name, 'r')
                else:
                    openedFile = open('UserInfo.txt', 'r')
                    
                # Recorremos el archivo linea por linea
                for lineIndex in enumerate(openedFile):
                    
                    # Primera linea: Root User Id
                    if lineIndex[0] == 0:
                        
                        # Obtenemos el contenido de la linea correspondiente
                        lineContent = lineIndex[1]
                        
                        # Extraemos el nombre de usuario de la linea leida (removemos tambien el salto de linea al final)
                        persistedRootUserId = lineContent[11:len(lineContent) - 1]
                                            
                    # Segunda linea: Username
                    if lineIndex[0] == 1:
                        
                        # Obtenemos el contenido de la linea correspondiente
                        lineContent = lineIndex[1]
                        
                        # Extraemos el nombre de usuario de la linea leida (removemos tambien el salto de linea al final)
                        persistedUsername = lineContent[9:len(lineContent) - 1]
                        
                    # Tercera linea: Password
                    if lineIndex[0] == 2:
                        
                        # Obtenemos el contenido de la linea correspondiente
                        lineContent = lineIndex[1]
                        
                        # Extraemos el password de la linea leida
                        persistedPassword = lineContent[9:len(lineContent) - 1]
                        
                        # Finalizamos el recorrido del archivo
                        break
                    
            except:
                persistedRootUserId = None
                persistedUsername = None
                persistedPassword = None
                
            finally:
                # Se cierra el archivo, sin importar lo que haya pasado
                try:
                    openedFile.close
                except:
                    pass
                
            # Verificamos que los datos persistidos hayan sido leidos correctamente
            if (persistedRootUserId == None) or (persistedRootUserId == "") or (persistedUsername == None) or (persistedUsername == "") or (persistedPassword == None) or (persistedPassword == ""):
                
                # Pantalla para la creacion del archivo
                View.showScreen(eScreen.REGISTRATION)
                
            else:
                # Guardamos los datos obtenidos del archivo
                GlobalsController.INFO_ROOT_USER_ID = persistedRootUserId
                GlobalsController.INFO_USERNAME = persistedUsername
                GlobalsController.INFO_PASSWORD = persistedPassword
                
                # Mostramos la pantalla de Login
                View.showScreen(eScreen.LOGIN)
            
        # Detectamos todos los eventos y ejecutamos las acciones correspondientes
        if pygame.event:
            for event in pygame.event.get():
                 
                # Evento cerrar el juego
                if event.type == pygame.QUIT:
                    pass
                    
                # Eventos del sistema
                elif event.type == pygame.USEREVENT:
                    pass
                    
                # Deteccion de click de mouse
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    pass
                    
                # Deteccion de teclas presionadas
                elif event.type == pygame.KEYDOWN:
                    pass
                    
    def __doPaint(self):
        
        # Screen content
        self.__displaySurface.fill((255, 255, 255))
        self.__displaySurface.blit(self.__image, (0, 0))
        
        # Text
        if self.__imageId == 1:
            self.__shadow.doPaint(self.__displaySurface)
            self.__text.doPaint(self.__displaySurface)
        
        # Actualizamos la pantalla
        pygame.display.flip()
        
    def __doUpdateImage(self):
        if self.__imageId == 1:
            self.__image = ResourceController.background_Splash_1
        elif self.__imageId == 2:
            self.__image = ResourceController.background_Splash_2
        elif self.__imageId == 3:
            self.__image = ResourceController.background_Splash_3
        elif self.__imageId == 4:
            self.__image = ResourceController.background_Splash_4
        elif self.__imageId == 5:
            self.__image = ResourceController.background_Splash_5

    def activate(self):
        
        # Indicamos que esta pantalla pasa a estado Activo
        self.__isActive = True
        
        # Ocultamos el cursor
        pygame.mouse.set_visible(False)        
        
        # Ordanamos que comience el pintado de la pantalla
        self.__run()

    def deactivate(self):
        
        # Indicamos que esta pantalla pasa a estado Inactivo
        self.__isActive = False

    def __run(self):
        
        # Loop principal
        while self.__isActive is True:

            # Realizamos las operaciones propias del model
            self.__doTask()
            
            # Pintamos el resultado en pantalla
            self.__doPaint()
            
            # Running as Activity
            if olpcgames.ACTIVITY:
                pass
            else:
                # Saltamos a la siguiente iteracion
                self.__clock.tick(5)


class ScreenCloseSplash:
    
    def __init__(self, clock, displaySurface):
        
        # Detenemos la reproduccion de cualquier audio activo
        AudioController.stopMusic()
        AudioController.stopSounds()
        
        # Screen
        self.__clock = clock
        self.__displaySurface = displaySurface
        self.__isActive = False
        
        # Time
        self.__count = 1
        self.__endTime = 30
        
        # Control
        self.__dataProcessDefined = False
        self.__dataSentDefined = False
        
        self.__sendBatchThread = None
        self.__sendBatchInProgress = False
        
        # Text
        self.__text = Label("Impulsa el Cambio...", FontController.font60, (255, 255, 0), (0, 150))
        self.__text.setPosition((600 - (self.__text.getTextRenderLen() / 2), self.__text.getPosition()[1]))
        
        self.__shadow = Label("Impulsa el Cambio...", FontController.font60, (0, 0, 0), (0, 150 + 4))
        self.__shadow.setPosition((600 + 4 - (self.__shadow.getTextRenderLen() / 2), self.__shadow.getPosition()[1]))
        
    def __doTask(self):
        
        # ------------------------------------------------------------------------------------------
        # No persistencia
        # ------------------------------------------------------------------------------------------
        self.__dataSentDefined = True
        self.__dataProcessDefined = True
        # ------------------------------------------------------------------------------------------
        # Para activar la persistencia del juego solo es necesario remover el codigo anterior (Ver Tambien ScreenStartSplash)
        # ------------------------------------------------------------------------------------------
        
        
        if self.__dataProcessDefined == False:

            # Obtenemos la hora de finalizacion de la sesion de juego
            GlobalsController.INFO_FINISH_TIME = datetime.datetime.now().strftime("%d-%m-%Y %H:%M:%S")
            
            try:
                # Almacenamos la informacion de la sesion de juego recien finalizada
                openedFile = None
                
                # Creamos un archivo
                if olpcgames.ACTIVITY:  # Running as Activity
                    name = os.path.join(olpcgames.util.get_activity_root(), 'data', 'UserInfo.txt')
                    openedFile = open(name, 'a')
                else:
                    openedFile = open('UserInfo.txt', 'a')
                    
                # Escibimos el contenido apropiado
                openedFile.write('''---------------\n''')
                openedFile.write('''leafUserId:''' + str(GlobalsController.INFO_LEAF_USER_ID) + '''\n''')
                openedFile.write('''startDatetime:''' + str(GlobalsController.INFO_START_TIME) + '''\n''')
                openedFile.write('''finishDatetime:''' + str(GlobalsController.INFO_FINISH_TIME) + '''\n''')
                openedFile.write('''stars:''' + str(GlobalsController.INFO_STARS) + '''\n''')
                
            finally:
                # Se cierra el archivo, sin importar lo que haya pasado
                try:
                    openedFile.close
                except:
                    pass
            
            # Y se almaceno la informacion
            self.__dataProcessDefined = True
            
        elif self.__dataSentDefined == False:
            
            # Determinamos si hay un envio de batch en proceso
            if self.__sendBatchInProgress == False:
                
                # Armamos el JSON a enviar con los datos en batch
                fileLinesToProcess = None
                
                try:
                    openedFile = None
                    
                    # Abrimos el archivo en modo lectura
                    if olpcgames.ACTIVITY:  # Running as Activity
                        name = os.path.join(olpcgames.util.get_activity_root(), 'data', 'UserInfo.txt')
                        openedFile = open(name, 'r')
                    else:
                        openedFile = open('UserInfo.txt', 'r')
                        
                    # Escibimos el contenido apropiado
                    fileLinesToProcess = openedFile.readlines()
                    
                finally:
                    # Se cierra el archivo, sin importar lo que haya pasado
                    try:
                        openedFile.close
                    except:
                        pass
                    
                if (fileLinesToProcess == None) or (fileLinesToProcess == ""):
                    
                    # Falla en la creacion o envio del JSON
                    self.__dataSentDefined = True
                    return
                
                # Procesamos las lineas obtenidas:
                
                # Removemos los datos no relevantes en este momento: userId, username y password
                fileLinesToProcess = fileLinesToProcess[3:]
                
                # Variable para controlar la linea leida por bloque de informacion
                index = 0
                
                # Cadena con el batch de informacion a enviar
                batchDataToSend = ""
                
                for currentLine in fileLinesToProcess:
                    
                    if index == 0:  # Separador
                        
                        # La coma separadora solo se coloca despues de colocar el primer bloque
                        if batchDataToSend != "":
                            batchDataToSend = batchDataToSend + ''','''
                        index = index + 1

                    elif index == 1:  # Leaf User Id
                        batchDataToSend = batchDataToSend + '''
                            { "leafUserId": "''' + currentLine[11:len(currentLine) - 1] + '''", '''
                        index = index + 1

                    elif index == 2:  # Start Datetime
                        batchDataToSend = batchDataToSend + '''"startDatetime": "''' + currentLine[14:len(currentLine) - 4] + ''':00", '''
                        index = index + 1
                    
                    elif index == 3:  # Finish Datetime
                        batchDataToSend = batchDataToSend + '''"finishDatetime": "''' + currentLine[15:len(currentLine) - 4] + ''':00", '''
                        index = index + 1

                    elif index == 4:  # Stars
                        batchDataToSend = batchDataToSend + '''"stars": "''' + currentLine[6:len(currentLine) - 1] + '''"}'''
                        index = 0
                    
                # Iniciamos el proceso de envio de los datos en batch
                try:
                    # Parametros de conexion
                    url = 'http://www.transformando.gov.co/api/public/index/batch'
                    jsonParameters = '''
                    {
                        "gameId": "''' + str(GlobalsController.GAME_ID) + '''",
                        "rootUserId": "''' + str(GlobalsController.INFO_ROOT_USER_ID) + '''",
                        "data": [''' + batchDataToSend + '''
                        ]
                    }'''
                    
                    jsonParameters = jsonParameters.replace("\n", "")
                    jsonParameters = jsonParameters.replace("  ", "")
                    
                    parameters = urllib.urlencode({'data': jsonParameters})
                    
                    # Hacemos la solicitud por POST
                    self.__sendBatchThread = ConnectionController(eConnectionMethod.POST, url, parameters)
                    self.__sendBatchThread.start()
                    
                    # Levantamos la bandera correspondiente
                    self.__sendBatchInProgress = True
                    
                except:
                    # Falla en la creacion o envio del JSON
                    self.__dataSentDefined = True

            # Envio del batch en progreso            
            elif self.__sendBatchInProgress == True:
                
                # Si hay un hilo tratando de conectarse
                if self.__sendBatchThread != None:
                    
                    if self.__sendBatchThread.getState() == eConnectionState.CONNECTING:
                        # Esperamos hasta que se defina la situacion de la conexion
                        pass
                    
                    elif self.__sendBatchThread.getState() == eConnectionState.SUCCESS:
                        
                        # Datos en Batch enviados correctamente, ahora debemos eliminar del archivo el batch de datos enviados
                        newFile = None
                        
                        # Creamos un archivo
                        if olpcgames.ACTIVITY:  # Running as Activity
                            name = os.path.join(olpcgames.util.get_activity_root(), 'data', 'UserInfo.txt')
                            newFile = open(name, 'w+')
                        else:
                            newFile = open('UserInfo.txt', 'w+')
                            
                        # Escibimos el contenido apropiado
                        newFile.write('''rootUserId:''' + str(GlobalsController.INFO_ROOT_USER_ID) + '''\n''')
                        newFile.write('''username:''' + str(GlobalsController.INFO_USERNAME) + '''\n''')
                        newFile.write('''password:''' + str(GlobalsController.INFO_PASSWORD) + '''\n''')
                        
                        # Se cierra el archivo
                        try:
                            newFile.close
                        except:
                            pass
                        
                        # Levantamos la bandera para que comience el proceso de cerrado del juego                        
                        self.__dataSentDefined = True 
                        
                    elif self.__sendBatchThread.getState() == eConnectionState.FAILURE:
                        
                        # Falla de la conexion
                        self.__dataSentDefined = True

        # Ya se definio la situacion del batch de datos, ya puede comenzar el proceso de cerrado
        else:
            # Conteo para evitar Race Conditions y permitir el almacenamiento persistente
            self.__count = self.__count + 1
                
            if self.__count >= self.__endTime:
                from Game import App
                App.closeGame()
            
        # Detectamos todos los eventos y ejecutamos las acciones correspondientes
        if pygame.event:
            for event in pygame.event.get():
                 
                # Evento cerrar el juego
                if event.type == pygame.QUIT:
                    pass
                    
                # Eventos del sistema
                elif event.type == pygame.USEREVENT:
                    pass
                    
                # Deteccion de click de mouse
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    pass
                    
                # Deteccion de teclas presionadas
                elif event.type == pygame.KEYDOWN:
                    pass

    def __doPaint(self):
        
        # Screen content
        self.__displaySurface.blit(ResourceController.background_Splash_1, (0, 0))
        
        # Text
        self.__shadow.doPaint(self.__displaySurface)
        self.__text.doPaint(self.__displaySurface)
        
        # Actualizamos la pantalla
        pygame.display.flip()

    def activate(self):
        
        # Indicamos que esta pantalla pasa a estado Activo
        self.__isActive = True
        
        # Ocultamos el cursor
        pygame.mouse.set_visible(False)        
        
        # Ordanamos que comience el pintado de la pantalla
        self.__run()

    def deactivate(self):
        pass
        
    def __run(self):
        
        # Loop principal
        while self.__isActive is True:

            # Realizamos las operaciones propias del model
            self.__doTask()
            
            # Pintamos el resultado en pantalla
            self.__doPaint()
            
            # Running as Activity
            if olpcgames.ACTIVITY:
                pass
            else:
                # Saltamos a la siguiente iteracion
                self.__clock.tick(GlobalsController.GAME_FPS)

            
class ScreenLogin:

    def __init__(self, clock, displaySurface):
        
        # Screen
        self.__clock = clock
        self.__displaySurface = displaySurface
        self.__isActive = False
        
        # Input
        self.__loginInProgress = False
        self.__textboxUser = TextBox(385, 525, 440, 20, FontController.font30, False)
        self.__textboxPass = TextBox(385, 646, 440, 20, FontController.font30, True)
        
        # Login Control
        self.__loginStatus = Label("", FontController.font18, (255, 200, 200), (0, 796))
        self.__showLoginControls = False
        
        # User Checked
        self.__userCheck = False
        self.__userCheckTotalTime = 20
        self.__userCheckCurrentTime = 1
        
        # Hover
        self.__hoverCloseGame = False
        self.__hoverLoginButton = False
        self.__hoverLoginMainUser = False
        self.__hoverLoginParent = False
        self.__hoverLoginUncle = False
        self.__hoverLoginBrother = False
        self.__hoverLoginCousin = False
        self.__hoverLoginFriend = False
        
    def __doTask(self):
        
        # Mouse Hover Detection
        (xPos, yPos) = pygame.mouse.get_pos()
        
        # Outside
        self.__hoverCloseGame = False
        self.__hoverLoginButton = False
        self.__hoverLoginMainUser = False
        self.__hoverLoginParent = False
        self.__hoverLoginUncle = False
        self.__hoverLoginBrother = False
        self.__hoverLoginCousin = False
        self.__hoverLoginFriend = False
        
        # Close Game
        if (xPos >= 1200 - 87) and (xPos <= 1200) and (yPos >= 0) and (yPos <= 0 + 74): 
            self.__hoverCloseGame = True
        # Login Button
        elif (xPos >= 420) and (xPos <= 420 + 330) and (yPos >= 730) and (yPos <= 730 + 65) and (self.__showLoginControls == True):
            self.__hoverLoginButton = True
        # Main User
        elif (xPos >= 325) and (xPos <= 325 + 540) and (yPos >= 450) and (yPos <= 450 + 350) and (self.__showLoginControls == False):
            self.__hoverLoginMainUser = True
        # Parents
        elif (xPos >= 495) and (xPos <= 495 + 248) and (yPos >= 110) and (yPos <= 110 + 158):
            self.__hoverLoginParent = True
        # Uncle
        elif (xPos >= 750) and (xPos <= 750 + 246) and (yPos >= 190) and (yPos <= 190 + 156):
            self.__hoverLoginUncle = True
        # Brother
        elif (xPos >= 245) and (xPos <= 245 + 246) and (yPos >= 190) and (yPos <= 190 + 156):
            self.__hoverLoginBrother = True
        # Cousin
        elif (xPos >= 58) and (xPos <= 58 + 246) and (yPos >= 344) and (yPos <= 344 + 156):
            self.__hoverLoginCousin = True
        # Friend
        elif (xPos >= 922) and (xPos <= 922 + 246) and (yPos >= 345) and (yPos <= 345 + 156):
            self.__hoverLoginFriend = True
            
        # Si el usuario ya ha sido verificado
        if self.__userCheck == True:
            if self.__userCheckCurrentTime < self.__userCheckTotalTime:
                self.__userCheckCurrentTime = self.__userCheckCurrentTime + 1
            else:
                View.showScreen(eScreen.SELECT_LEVEL)
        
        # Detectamos todos los eventos y ejecutamos las acciones correspondientes
        if pygame.event:
            for event in pygame.event.get():
                 
                # Evento cerrar el juego
                if event.type == pygame.QUIT:
                    from Game import App
                    App.closeGame()
                    
                # Eventos del sistema
                elif event.type == pygame.USEREVENT:
                    pass
                    
                # Deteccion de click de mouse
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    self.__doMouseAction(event)
                    
                # Deteccion de teclas presionadas
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        from Game import App
                        App.closeGame()
                    elif event.key == pygame.K_RSHIFT:
                        self.__switchCase()
                    elif event.key == pygame.K_LSHIFT:
                        self.__switchCase()
                    else:
                        self.__doKeyAction(event)
                        
    def __doPaint(self):
        
        # Background
        self.__displaySurface.blit(ResourceController.background_Login, (0, 0))

        if self.__showLoginControls == True:
            
            # Background
            self.__displaySurface.blit(ResourceController.input_LoginInput, (163, 320))
            
            # TextBox
            self.__textboxUser.doPaint(self.__displaySurface)
            self.__textboxPass.doPaint(self.__displaySurface)
        
            # Buttons with Hover
            if self.__loginInProgress == False:
                if self.__hoverLoginButton == True:
                    self.__displaySurface.blit(ResourceController.input_Login_On, (420, 730))
                else:
                    self.__displaySurface.blit(ResourceController.input_Login_Off, (420, 730))
            else:
                self.__displaySurface.blit(ResourceController.input_Connecting, (420, 730))
        else:
            if self.__hoverLoginMainUser == True:
                self.__displaySurface.blit(ResourceController.input_LoginMainUser, (310, 345))
            
        if self.__hoverLoginParent == True:
            self.__displaySurface.blit(ResourceController.input_LoginParent, (485, 74))
            
        if self.__hoverLoginUncle == True:
            self.__displaySurface.blit(ResourceController.input_LoginUncle, (740, 150))
            
        if self.__hoverLoginBrother == True:
            self.__displaySurface.blit(ResourceController.input_LoginBrother, (230, 150))
            
        if self.__hoverLoginCousin == True:
            self.__displaySurface.blit(ResourceController.input_LoginCousin, (45, 305))
            
        if self.__hoverLoginFriend == True:
            self.__displaySurface.blit(ResourceController.input_LoginFriend, (910, 305))
            
        # Login Status
        self.__loginStatus.doPaint(self.__displaySurface)
        
        if self.__hoverCloseGame == True:
            self.__displaySurface.blit(ResourceController.input_CloseGame_On, (1200 - 87, 0))
        else:
            self.__displaySurface.blit(ResourceController.input_CloseGame_Off, (1200 - 87, 0))
        
        # Actualizamos la pantalla
        pygame.display.flip()

    def activate(self):
        
        # Indicamos que esta pantalla pasa a estado Activo
        self.__isActive = True
        
        # Mostramos el cursor
        pygame.mouse.set_visible(True)
        
        # Ordanamos que comience el pintado de la pantalla
        self.__run()

    def deactivate(self):
        
        # Indicamos que esta pantalla pasa a estado Inactivo
        self.__isActive = False

    def __run(self):
        
        # Loop principal
        while self.__isActive is True:

            # Realizamos las operaciones propias del model
            self.__doTask()
            
            # Pintamos el resultado en pantalla
            self.__doPaint()
            
            # Running as Activity
            if olpcgames.ACTIVITY:
                pass
            else:
                # Saltamos a la siguiente iteracion, respetando el FPS establecido
                self.__clock.tick(GlobalsController.GAME_FPS)
                
    def __doKeyAction(self, event):
        
        # Si no hay algun evento en progreso...
        if self.__userCheck == False:
            
            self.__textboxUser.doKeyAction(event)
            self.__textboxPass.doKeyAction(event)
        
    def __doMouseAction(self, event):
        
        if self.__userCheck == False:
        
            # Removemos el foco de todas la cajas de texto
            self.__textboxUser.quitFocus()
            self.__textboxPass.quitFocus()
            
            # Detectamos la posicion en X y Y del click
            xPos, yPos = event.pos
    
            # Close Game
            if (xPos >= 1200 - 87) and (xPos <= 1200) and (yPos >= 0) and (yPos <= 0 + 74):
                from Game import App
                App.closeGame()
            
            # Login Button
            elif (xPos >= 420) and (xPos <= 420 + 330) and (yPos >= 730) and (yPos <= 730 + 65) and (self.__showLoginControls == True):
                
                # Reiniciamos esta bandera dado que un nuevo proceso de verificacion de usuario va a comenzar
                self.__userCheck = False
        
                # Reiniciamos los mensajes de estado
                self.__loginStatus.setText("")
                
                # Obtenemos los datos ingresados
                username = self.__textboxUser.getText()
                password = self.__textboxPass.getText()
                
                # Verificamos si todos los datos fueron ingresados
                if (username == "") or (password == ""):
                    self.__loginStatus.setText("Se deben llenar todos los campos.")
                    self.__loginStatus.setPosition((585 - (self.__loginStatus.getTextRenderLen() / 2), self.__loginStatus.getPosition()[1]))
                    return
                
                # Verificamos que los datos ingresados correspondan con los persistidos
                if (GlobalsController.INFO_USERNAME == username) and (GlobalsController.INFO_PASSWORD == password):
                    self.__loginStatus.setText("Login exitoso. Ingresando al juego...")
                    self.__loginStatus.setPosition((585 - (self.__loginStatus.getTextRenderLen() / 2), self.__loginStatus.getPosition()[1]))
                    
                    # Indicamos el usuario que va a jugar
                    GlobalsController.INFO_LEAF_USER_ID = eLeafUserId.MAIN_USER
                    GlobalsController.INFO_START_TIME = datetime.datetime.now().strftime("%d-%m-%Y %H:%M:%S")  
                    
                    # Levantamos la bandera correspondiente
                    self.__userCheck = True
                    
                else:
                    self.__loginStatus.setText("Datos incorrectos.")
                    self.__loginStatus.setPosition((585 - (self.__loginStatus.getTextRenderLen() / 2), self.__loginStatus.getPosition()[1]))
            
            # Main User
            elif (xPos >= 325) and (xPos <= 325 + 540) and (yPos >= 450) and (yPos <= 450 + 350) and (self.__showLoginControls == False):
                self.__showLoginControls = True
                self.__textboxUser.takeFocus()
                
            # Parents
            elif (xPos >= 495) and (xPos <= 495 + 248) and (yPos >= 110) and (yPos <= 110 + 158):
                # Indicamos el usuario que va a jugar
                GlobalsController.INFO_LEAF_USER_ID = eLeafUserId.PARENTS
                GlobalsController.INFO_START_TIME = datetime.datetime.now().strftime("%d-%m-%Y %H:%M:%S")
                
                # Cambiamos a la pantalla correspondiente
                View.showScreen(eScreen.SELECT_LEVEL)
                
            # Uncle
            elif (xPos >= 750) and (xPos <= 750 + 246) and (yPos >= 190) and (yPos <= 190 + 156):
                # Indicamos el usuario que va a jugar
                GlobalsController.INFO_LEAF_USER_ID = eLeafUserId.UNCLE
                GlobalsController.INFO_START_TIME = datetime.datetime.now().strftime("%d-%m-%Y %H:%M:%S")
                                
                # Cambiamos a la pantalla correspondiente
                View.showScreen(eScreen.SELECT_LEVEL)
                
            # Brother
            elif (xPos >= 245) and (xPos <= 245 + 246) and (yPos >= 190) and (yPos <= 190 + 156):
                # Indicamos el usuario que va a jugar
                GlobalsController.INFO_LEAF_USER_ID = eLeafUserId.BROTHER
                GlobalsController.INFO_START_TIME = datetime.datetime.now().strftime("%d-%m-%Y %H:%M:%S")
                
                # Cambiamos a la pantalla correspondiente
                View.showScreen(eScreen.SELECT_LEVEL)
                
            # Cousin
            elif (xPos >= 58) and (xPos <= 58 + 246) and (yPos >= 344) and (yPos <= 344 + 156):
                # Indicamos el usuario que va a jugar
                GlobalsController.INFO_LEAF_USER_ID = eLeafUserId.COUSIN
                GlobalsController.INFO_START_TIME = datetime.datetime.now().strftime("%d-%m-%Y %H:%M:%S")
                
                # Cambiamos a la pantalla correspondiente
                View.showScreen(eScreen.SELECT_LEVEL)
                
            # Friend
            elif (xPos >= 922) and (xPos <= 922 + 246) and (yPos >= 345) and (yPos <= 345 + 156):
                # Indicamos el usuario que va a jugar
                GlobalsController.INFO_LEAF_USER_ID = eLeafUserId.FRIEND
                GlobalsController.INFO_START_TIME = datetime.datetime.now().strftime("%d-%m-%Y %H:%M:%S")
                
                # Cambiamos a la pantalla correspondiente
                View.showScreen(eScreen.SELECT_LEVEL)
                    
            # Textbox
            else:
                self.__textboxUser.doMouseAction(event)
                self.__textboxPass.doMouseAction(event)
        
    def __switchCase(self):
        if self.__userCheck == False:
            self.__textboxUser.switchCase()
            self.__textboxPass.switchCase()
        

class ScreenRegistration:

    def __init__(self, clock, displaySurface):
        
        # Screen
        self.__clock = clock
        self.__displaySurface = displaySurface
        self.__isActive = False
        
        # Registration Input
        self.__textboxNames = TextBox(110, 148, 440, 20, FontController.font30, False)
        self.__textboxAge = TextBox(110, 263, 150, 2, FontController.font30, False)
        self.__textboxSchool = TextBox(110, 375, 440, 20, FontController.font30, False)
        self.__textboxGrade = TextBox(110, 487, 440, 20, FontController.font30, False)
        
        self.__textboxUsername = TextBox(620, 148, 440, 20, FontController.font30, False)
        self.__textboxPassword1 = TextBox(620, 263, 440, 20, FontController.font30, True)
        self.__textboxPassword2 = TextBox(620, 375, 440, 20, FontController.font30, True)
        self.__textboxNames.takeFocus()
        
        # Registration Control
        self.__registrationThread = None
        self.__registrationInProgress = False
        self.__registrationStatus = Label("", FontController.font18, (255, 200, 200), (0, 445))
        
        # Login Input
        self.__textboxLoginUsername = TextBox(110, 682, 440, 20, FontController.font30, False)
        self.__textboxLoginPassword = TextBox(620, 682, 440, 20, FontController.font30, True)
        
        # Login Control
        self.__loginThread = None
        self.__loginInProgress = False
        self.__loginStatus = Label("", FontController.font18, (255, 200, 200), (770, 770))
        
        # User Checked
        self.__userCheck = False
        self.__userCheckTotalTime = 20
        self.__userCheckCurrentTime = 1
        
        # Hover
        self.__hoverCloseGame = False
        self.__hoverRegistration = False
        self.__hoverLoginButton = False
        
    def __doTask(self):
        
        # Mouse Hover Detection
        (xPos, yPos) = pygame.mouse.get_pos()
        
        # Outside
        self.__hoverCloseGame = False
        self.__hoverRegistration = False
        self.__hoverLoginButton = False
        
        # Close Game
        if (xPos >= 1200 - 87) and (xPos <= 1200) and (yPos >= 0) and (yPos <= 0 + 74): 
            self.__hoverCloseGame = True
        # Registration Button
        elif (xPos >= 670) and (xPos <= 670 + 330) and (yPos >= 475) and (yPos <= 475 + 65):
            self.__hoverRegistration = True
        # Login Button
        elif (xPos >= 435) and (xPos <= 435 + 330) and (yPos >= 750) and (yPos <= 750 + 65):
            self.__hoverLoginButton = True

        # Si el usuario ya ha sido verificado
        if self.__userCheck == True:
            if self.__userCheckCurrentTime < self.__userCheckTotalTime:
                self.__userCheckCurrentTime = self.__userCheckCurrentTime + 1
            else:
                View.showScreen(eScreen.SELECT_LEVEL)

        # Determinamos si hay un registro en proceso
        elif self.__registrationInProgress == True:
            
            # Si hay un hilo tratando de conectarse
            if self.__registrationThread != None:
                
                if self.__registrationThread.getState() == eConnectionState.CONNECTING:
                    
                    if self.__registrationStatus.text == "Conectando":
                        self.__registrationStatus.setText("Conectando.")
                    elif self.__registrationStatus.text == "Conectando.":
                        self.__registrationStatus.setText("Conectando..")
                    elif self.__registrationStatus.text == "Conectando..":
                        self.__registrationStatus.setText("Conectando...")
                    elif self.__registrationStatus.text == "Conectando...":
                        self.__registrationStatus.setText("Conectando")
                
                elif self.__registrationThread.getState() == eConnectionState.SUCCESS:
                    
                    # Obtenemos la respuesta dada por el servidor
                    result = self.__registrationThread.getResult()
                    
                    # Si el registro fue exitoso
                    if result[11:15] == 'true':
                        
                        # Leemos el id retornado
                        newUserId = result[23:43]
                        
                        # Si el nombre de usuario elegido ya existe
                        if newUserId == "":
                            self.__registrationStatus.setText("El Nombre de Usuario ya existe.")
                            self.__registrationStatus.setPosition((835 - (self.__registrationStatus.getTextRenderLen() / 2), self.__registrationStatus.getPosition()[1]))
                            
                            # Se alista todo para una nueva conexion
                            self.__registrationInProgress = False
                            self.__registrationThread = None
                            
                        else:
                            try:
                                newFile = None
                                
                                # Creamos un archivo
                                if olpcgames.ACTIVITY:  # Running as Activity
                                    name = os.path.join(olpcgames.util.get_activity_root(), 'data', 'UserInfo.txt')
                                    newFile = open(name, 'w+')
                                else:
                                    newFile = open('UserInfo.txt', 'w+')
                                    
                                # Volvemos a obtener los datos a persistir
                                username = self.__textboxUsername.getText()
                                password = self.__textboxPassword1.getText()
                            
                                # Escibimos el contenido apropiado
                                newFile.write('''rootUserId:''' + newUserId + '''\n''')
                                newFile.write('''username:''' + username + '''\n''')
                                newFile.write('''password:''' + password + '''\n''')
                                
                                # Se cierra el archivo
                                try:
                                    newFile.close
                                except:
                                    pass
                                
                                # El registro fue exitoso, levantamos la bandera correspondiente
                                self.__userCheck = True
                                
                                # Almacenamos la informacion en el juego
                                GlobalsController.INFO_ROOT_USER_ID = newUserId
                                GlobalsController.INFO_LEAF_USER_ID = eLeafUserId.MAIN_USER
                                GlobalsController.INFO_USERNAME = username
                                GlobalsController.INFO_PASSWORD = password
                                GlobalsController.INFO_START_TIME = datetime.datetime.now().strftime("%d-%m-%Y %H:%M:%S")
                                
                                # Informamos al usuario
                                self.__registrationStatus.setText("Registro exitoso. Ingresando al juego...")
                                self.__registrationStatus.setPosition((835 - (self.__registrationStatus.getTextRenderLen() / 2), self.__registrationStatus.getPosition()[1]))
                                
                                # Ya no se necesita la conexion abierta
                                self.__registrationInProgress = False
                                self.__registrationThread = None
                                
                            except:
                                # Fue lanzada una excepcion relacionada con la apertura del archivo
                                self.__registrationStatus.setText("Error en el Registro.")
                                self.__registrationStatus.setPosition((835 - (self.__registrationStatus.getTextRenderLen() / 2), self.__registrationStatus.getPosition()[1]))
                                
                                # Se alista todo para una nueva conexion
                                self.__registrationInProgress = False
                                self.__registrationThread = None
                                
                                # Se cierra el archivo, sin importar lo que haya pasado
                                try:
                                    newFile.close
                                except:
                                    pass
                                
                    else:
                        # Error en la respuesta del servidor
                        self.__registrationStatus.setText("Error en el Registro.")
                        self.__registrationStatus.setPosition((835 - (self.__registrationStatus.getTextRenderLen() / 2), self.__registrationStatus.getPosition()[1]))
                        
                        # Se alista todo para una nueva conexion
                        self.__registrationInProgress = False
                        self.__registrationThread = None
                        
                elif self.__registrationThread.getState() == eConnectionState.FAILURE:
                    
                    # Falla de la conexion
                    self.__registrationStatus.setText("Error de Conexión.")
                    self.__registrationStatus.setPosition((835 - (self.__registrationStatus.getTextRenderLen() / 2), self.__registrationStatus.getPosition()[1]))
                    
                    # Se alista todo para una nueva conexion
                    self.__registrationInProgress = False
                    self.__registrationThread = None
                    
        # Determinamos si hay un login en proceso
        elif self.__loginInProgress == True:
            
            # Si hay un hilo tratando de conectarse
            if self.__loginThread != None:
                
                if self.__loginThread.getState() == eConnectionState.CONNECTING:
                    
                    if self.__loginStatus.text == "Conectando":
                        self.__loginStatus.setText("Conectando.")
                    elif self.__loginStatus.text == "Conectando.":
                        self.__loginStatus.setText("Conectando..")
                    elif self.__loginStatus.text == "Conectando..":
                        self.__loginStatus.setText("Conectando...")
                    elif self.__loginStatus.text == "Conectando...":
                        self.__loginStatus.setText("Conectando")
                
                elif self.__loginThread.getState() == eConnectionState.SUCCESS:
               
                    # Obtenemos la respuesta dada por el servidor
                    result = self.__loginThread.getResult()
                    
                    # Si el login fue exitoso
                    if result[11:15] == 'true':
                        
                        # Leemos el id retornado
                        newUserId = result[23:len(result) - 2]
                        
                        # Si el nombre de usuario elegido no existe
                        if newUserId == "":
                            self.__loginStatus.setText("El Nombre de Usuario no existe.")
                            
                            # Se alista todo para una nueva conexion
                            self.__loginInProgress = False
                            self.__loginThread = None
                            
                        else:
                            try:
                                newFile = None
                                
                                # Creamos un archivo
                                if olpcgames.ACTIVITY:  # Running as Activity
                                    name = os.path.join(olpcgames.util.get_activity_root(), 'data', 'UserInfo.txt')
                                    newFile = open(name, 'w+')
                                else:
                                    newFile = open('UserInfo.txt', 'w+')
        
                                # Volvemos a obtener los datos a persistir
                                username = self.__textboxLoginUsername.getText()
                                password = self.__textboxLoginPassword.getText()
                            
                                # Escibimos el contenido apropiado
                                newFile.write('''rootUserId:''' + newUserId + '''\n''')
                                newFile.write('''username:''' + username + '''\n''')
                                newFile.write('''password:''' + password + '''\n''')
                                
                                # Se cierra el archivo
                                try:
                                    newFile.close
                                except:
                                    pass
                                
                                # El registro fue exitoso, levantamos la bandera correspondiente
                                self.__userCheck = True
                                
                                # Almacenamos la informacion en el juego
                                GlobalsController.INFO_ROOT_USER_ID = newUserId
                                GlobalsController.INFO_LEAF_USER_ID = eLeafUserId.MAIN_USER
                                GlobalsController.INFO_USERNAME = username
                                GlobalsController.INFO_PASSWORD = password
                                GlobalsController.INFO_START_TIME = datetime.datetime.now().strftime("%d-%m-%Y %H:%M:%S")
                                
                                # Informamos al usuario
                                self.__loginStatus.setText("Login exitoso. Ingresando al juego...")
                                
                                # Ya no se necesita la conexion abierta
                                self.__loginInProgress = False
                                self.__loginThread = None
                                
                            except:
                                # Fue lanzada una excepcion relacionada con la apertura del archivo
                                self.__loginStatus.setText("Error en el Login.")
                                
                                # Se alista todo para una nueva conexion
                                self.__loginInProgress = False
                                self.__loginThread = None
                                
                                # Se cierra el archivo, sin importar lo que haya pasado
                                try:
                                    newFile.close
                                except:
                                    pass
                                
                    else:
                        # Error en la respuesta del servidor
                        self.__loginStatus.setText("Error en el Login.")
                        
                        # Se alista todo para una nueva conexion
                        self.__loginInProgress = False
                        self.__loginThread = None
                      
                elif self.__loginThread.getState() == eConnectionState.FAILURE:
                    
                    self.__loginStatus.setText("Error de Conexión.")
                    
                    # Se alista todo para una nueva conexion
                    self.__loginInProgress = False
                    self.__loginThread = None
                
        # Detectamos todos los eventos y ejecutamos las acciones correspondientes
        if pygame.event:
            for event in pygame.event.get():
                 
                # Evento cerrar el juego
                if event.type == pygame.QUIT:
                    from Game import App
                    App.closeGame()
                    
                # Eventos del sistema
                elif event.type == pygame.USEREVENT:
                    pass
                    
                # Deteccion de click de mouse
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    self.__doMouseAction(event)
                    
                # Deteccion de teclas presionadas
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        from Game import App
                        App.closeGame()
                    elif event.key == pygame.K_RSHIFT:
                        self.__switchCase()
                    elif event.key == pygame.K_LSHIFT:
                        self.__switchCase()
                    else:
                        self.__doKeyAction(event)
                        
    def __doPaint(self):
        
        # Background
        self.__displaySurface.blit(ResourceController.background_Registration, (0, 0))

        # TextBox
        self.__textboxNames.doPaint(self.__displaySurface)
        self.__textboxAge.doPaint(self.__displaySurface)
        self.__textboxSchool.doPaint(self.__displaySurface)
        self.__textboxGrade.doPaint(self.__displaySurface)
        self.__textboxUsername.doPaint(self.__displaySurface)
        self.__textboxPassword1.doPaint(self.__displaySurface)
        self.__textboxPassword2.doPaint(self.__displaySurface)
        self.__textboxLoginUsername.doPaint(self.__displaySurface)
        self.__textboxLoginPassword.doPaint(self.__displaySurface)

        # Buttons with Hover
        if self.__registrationInProgress == False:
            if self.__hoverRegistration == True:
                self.__displaySurface.blit(ResourceController.input_Registration_On, (670, 475))
            else:
                self.__displaySurface.blit(ResourceController.input_Registration_Off, (670, 475))
        else:
            self.__displaySurface.blit(ResourceController.input_Connecting, (670, 475))
            
        if self.__loginInProgress == False:
            if self.__hoverLoginButton == True:
                self.__displaySurface.blit(ResourceController.input_Login_On, (435, 750))
            else:
                self.__displaySurface.blit(ResourceController.input_Login_Off, (435, 750))
        else:
            self.__displaySurface.blit(ResourceController.input_Connecting, (435, 750))

        # Connecton Status
        self.__registrationStatus.doPaint(self.__displaySurface)
        self.__loginStatus.doPaint(self.__displaySurface)
        
        if self.__hoverCloseGame == True:
            self.__displaySurface.blit(ResourceController.input_CloseGame_On, (1200 - 87, 0))
        else:
            self.__displaySurface.blit(ResourceController.input_CloseGame_Off, (1200 - 87, 0))
        
        # Actualizamos la pantalla
        pygame.display.flip()

    def activate(self):
        
        # Indicamos que esta pantalla pasa a estado Activo
        self.__isActive = True
        
        # Mostramos el cursor
        pygame.mouse.set_visible(True)
        
        # Ordanamos que comience el pintado de la pantalla
        self.__run()

    def deactivate(self):
        
        # Indicamos que esta pantalla pasa a estado Inactivo
        self.__isActive = False
        
    def __run(self):
        
        # Loop principal
        while self.__isActive is True:

            # Realizamos las operaciones propias del model
            self.__doTask()
            
            # Pintamos el resultado en pantalla
            self.__doPaint()
            
            # Running as Activity
            if olpcgames.ACTIVITY:
                pass
            else:
                # Saltamos a la siguiente iteracion, respetando el FPS establecido
                self.__clock.tick(GlobalsController.GAME_FPS)
                
    def __doKeyAction(self, event):
        
        # Si no hay algun evento en progreso...
        if (self.__registrationInProgress == False) and (self.__loginInProgress == False) and (self.__userCheck == False):
            
            self.__textboxNames.doKeyAction(event)
            self.__textboxAge.doKeyAction(event)
            self.__textboxSchool.doKeyAction(event)
            self.__textboxGrade.doKeyAction(event)
            self.__textboxUsername.doKeyAction(event)
            self.__textboxPassword1.doKeyAction(event)
            self.__textboxPassword2.doKeyAction(event)
            self.__textboxLoginUsername.doKeyAction(event)
            self.__textboxLoginPassword.doKeyAction(event)
        
    def __doMouseAction(self, event):
        
        if self.__userCheck == False:
        
            # Removemos el foco de todas la cajas de texto
            self.__textboxNames.quitFocus()
            self.__textboxAge.quitFocus()
            self.__textboxSchool.quitFocus()
            self.__textboxGrade.quitFocus()
            self.__textboxUsername.quitFocus()
            self.__textboxPassword1.quitFocus()
            self.__textboxPassword2.quitFocus()
            self.__textboxLoginUsername.quitFocus()
            self.__textboxLoginPassword.quitFocus()
            
            # Detectamos la posicion en X y Y del click
            xPos, yPos = event.pos
    
            # Close Game
            if (xPos >= 1200 - 87) and (xPos <= 1200) and (yPos >= 0) and (yPos <= 0 + 74):
                from Game import App
                App.closeGame()
            
            # Registration Button
            elif (xPos >= 670) and (xPos <= 670 + 330) and (yPos >= 475) and (yPos <= 475 + 65):
                
                if self.__registrationInProgress == False:
                
                    # Desabilitamos el registro
                    self.__registrationInProgress = True
                    
                    # Reiniciamos esta bandera dado que un nuevo proceso de verificacion de usuario va a comenzar
                    self.__userCheck = False
                    
                    # Reiniciamos los mensajes e estado
                    self.__loginStatus.setText("")
                    self.__registrationStatus.setText("")
                    
                    # Verificamos los datos a enviar
                    names = self.__textboxNames.getText()
                    age = self.__textboxAge.getText()
                    school = self.__textboxSchool.getText()
                    grade = self.__textboxGrade.getText()
                    username = self.__textboxUsername.getText()
                    password1 = self.__textboxPassword1.getText()
                    password2 = self.__textboxPassword2.getText()
                    
                    # Verificamos si todos los datos fueron ingresados
                    if (names == "") or (age == "") or (school == "") or (grade == "") or (username == "") or (password1 == "") or (password2 == ""):
    
                        self.__registrationStatus.setText("Se deben llenar todos los campos.")
                        self.__registrationStatus.setPosition((835 - (self.__registrationStatus.getTextRenderLen() / 2), self.__registrationStatus.getPosition()[1]))
                        
                        # Se alista todo para una nueva conexion
                        self.__registrationInProgress = False
                        self.__registrationThread = None
                        return
                                    
                    # Verificamos si las contraseñas coinciden
                    if password1 != password2:
                        
                        self.__registrationStatus.setText("Las contraseñas no coinciden.")
                        self.__registrationStatus.setPosition((835 - (self.__registrationStatus.getTextRenderLen() / 2), self.__registrationStatus.getPosition()[1]))
                        
                        # Se alista todo para una nueva conexion
                        self.__registrationInProgress = False
                        self.__registrationThread = None
                        return
                    
                    try:
                        self.__registrationStatus.setText("Conectando...")
                        self.__registrationStatus.setPosition((835 - (self.__registrationStatus.getTextRenderLen() / 2), self.__registrationStatus.getPosition()[1]))
                    
                        # Parametros de conexion
                        url = 'http://www.transformando.gov.co/api/public/index/register'
                        jsonParameters = '''
                        {
                            "gameId": "''' + str(GlobalsController.GAME_ID) + '''",
                            "newUser": {
                                "name": "''' + names + '''",
                                "nickname": "''' + username + '''",
                                "password": "''' + password1 + '''",
                                "age": "''' + age + '''",
                                "school": "''' + school + '''",
                                "degree": "''' + grade + '''"
                            }
                        }'''
                        parameters = urllib.urlencode({'data': jsonParameters})
                        
                        # Hacemos la solicitud por POST
                        self.__registrationThread = ConnectionController(eConnectionMethod.POST, url, parameters)
                        self.__registrationThread.start()
                        
                    except:
                        self.__registrationStatus.setText("Error de Conexión.")
                        self.__registrationStatus.setPosition((835 - (self.__registrationStatus.getTextRenderLen() / 2), self.__registrationStatus.getPosition()[1]))
                        
                        # Se alista todo para una nueva conexion
                        self.__registrationInProgress = False
                        self.__registrationThread = None
            
            # Login Button
            elif (xPos >= 435) and (xPos <= 435 + 330) and (yPos >= 750) and (yPos <= 750 + 65):
        
                if self.__loginInProgress == False:
                
                    # Desabilitamos el registro
                    self.__loginInProgress = True
                    
                    # Reiniciamos esta bandera dado que un nuevo proceso de verificacion de usuario va a comenzar
                    self.__userCheck = False
                    
                    # Reiniciamos los mensajes e estado
                    self.__loginStatus.setText("")
                    self.__registrationStatus.setText("")
                    
                    # Verificamos los datos a enviar
                    username = self.__textboxLoginUsername.getText()
                    password = self.__textboxLoginPassword.getText()
                    
                    # Verificamos si todos los datos fueron ingresados
                    if (username == "") or (password == ""):
    
                        self.__loginStatus.setText("Se deben llenar todos los campos.")
                        
                        # Se alista todo para una nueva conexion
                        self.__loginInProgress = False
                        self.__loginThread = None
                        return
                                    
                    try:
                        self.__loginStatus.setText("Conectando...")
                    
                        # Parametros de conexion
                        url = 'http://www.transformando.gov.co/api/public/index/checkuser'
                        parameters = urllib.urlencode({'user': username, 'pass': password})
                        
                        # Hacemos la solicitud por POST
                        self.__loginThread = ConnectionController(eConnectionMethod.POST, url, parameters)
                        self.__loginThread.start()
                        
                    except:
                        self.__loginStatus.setText("Error de Conexión.")
                        
                        # Se alista todo para una nueva conexion
                        self.__loginInProgress = False
                        self.__loginThread = None
            
            # Textbox
            else:
                self.__textboxNames.doMouseAction(event)
                self.__textboxAge.doMouseAction(event)
                self.__textboxSchool.doMouseAction(event)
                self.__textboxGrade.doMouseAction(event)
                self.__textboxUsername.doMouseAction(event)
                self.__textboxPassword1.doMouseAction(event)
                self.__textboxPassword2.doMouseAction(event)
                self.__textboxLoginUsername.doMouseAction(event)
                self.__textboxLoginPassword.doMouseAction(event)
        
    def __switchCase(self):
        if self.__userCheck == False:
            self.__textboxNames.switchCase()
            self.__textboxAge.switchCase()
            self.__textboxSchool.switchCase()
            self.__textboxGrade.switchCase()
            self.__textboxUsername.switchCase()
            self.__textboxPassword1.switchCase()
            self.__textboxPassword2.switchCase()
            self.__textboxLoginUsername.switchCase()
            self.__textboxLoginPassword.switchCase()
        

class ScreenSelectLevel:

    def __init__(self, clock, displaySurface):
        
        # Screen
        self.__clock = clock
        self.__displaySurface = displaySurface
        self.__isActive = False
        
        # Text
        self.__text = Label("Elige el nivel de dificultad:", FontController.font40, (255, 255, 255), (0, 45))
        self.__text.setPosition((600 - (self.__text.getTextRenderLen() / 2), self.__text.getPosition()[1]))
        
        # Hover
        self.__hoverCloseGame = False
        self.__hoverEasy = False
        self.__hoverNormal = False
        self.__hoverHard = False
        
    def __doTask(self):
        
        # Mouse Hover Detection
        (xPos, yPos) = pygame.mouse.get_pos()
        
        # Outside
        self.__hoverCloseGame = False
        self.__hoverEasy = False
        self.__hoverNormal = False
        self.__hoverHard = False        
        
        # Close Game
        if (xPos >= 1200 - 87) and (xPos <= 1200) and (yPos >= 0) and (yPos <= 0 + 74): 
            self.__hoverCloseGame = True
        
        # Easy
        elif (xPos >= 380) and (xPos <= 380 + 395) and (yPos >= 150) and (yPos <= 150 + 128):
            self.__hoverEasy = True
            
        # Normal
        elif (xPos >= 380) and (xPos <= 380 + 395) and (yPos >= 290) and (yPos <= 290 + 128):
            self.__hoverNormal = True
            
        # Hard
        elif (xPos >= 380) and (xPos <= 380 + 395) and (yPos >= 420) and (yPos <= 420 + 128):
            self.__hoverHard = True
            
        # Detectamos todos los eventos y ejecutamos las acciones correspondientes
        if pygame.event:
            for event in pygame.event.get():
                 
                # Evento cerrar el juego
                if event.type == pygame.QUIT:
                    View.showScreen(eScreen.SPLASH_CLOSE)
                    
                # Eventos del sistema
                elif event.type == pygame.USEREVENT:
                    pass
                    
                # Deteccion de click de mouse
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    self.__doMouseAction(event)
                    
                # Deteccion de teclas presionadas
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        View.showScreen(eScreen.SPLASH_CLOSE)

    def __doPaint(self):
        
        # Background
        self.__displaySurface.blit(ResourceController.background_SelectLevel, (0, 0))
        
        # Text
        self.__text.doPaint(self.__displaySurface)
        
        # Buttons with Hover
        if self.__hoverEasy == True:
            self.__displaySurface.blit(ResourceController.input_LevelEasy_On, (380, 150))
        else:
            self.__displaySurface.blit(ResourceController.input_LevelEasy_Off, (380, 150))
        
        if self.__hoverNormal == True:
            self.__displaySurface.blit(ResourceController.input_LevelNormal_On, (380, 290))
        else:
            self.__displaySurface.blit(ResourceController.input_LevelNormal_Off, (380, 290))
        
        if self.__hoverHard == True:
            self.__displaySurface.blit(ResourceController.input_LevelHard_On, (380, 420))
        else:
            self.__displaySurface.blit(ResourceController.input_LevelHard_Off, (380, 420))
        
        if self.__hoverCloseGame == True:
            self.__displaySurface.blit(ResourceController.input_CloseGame_On, (1200 - 87, 0))
        else:
            self.__displaySurface.blit(ResourceController.input_CloseGame_Off, (1200 - 87, 0))
        
        # Actualizamos la pantalla
        pygame.display.flip()

    def activate(self):
        
        # Indicamos que esta pantalla pasa a estado Activo    
        self.__isActive = True
        
        # Mostramos el cursor
        pygame.mouse.set_visible(True)
        
        # Ordanamos que comience el pintado de la pantalla
        self.__run()

    def deactivate(self):
        
        # Indicamos que esta pantalla pasa a estado Inactivo
        self.__isActive = False

    def __run(self):
        
        # Loop principal
        while self.__isActive is True:

            # Realizamos las operaciones propias del model
            self.__doTask()
            
            # Pintamos el resultado en pantalla
            self.__doPaint()
            
            # Running as Activity
            if olpcgames.ACTIVITY:
                pass
            else:
                # Saltamos a la siguiente iteracion, respetando el FPS establecido
                self.__clock.tick(GlobalsController.GAME_FPS)

    def __doMouseAction(self, event):
        
        # Detectamos la posicion en X y Y del click
        xPos, yPos = event.pos

        # Close Game
        if (xPos >= 1200 - 87) and (xPos <= 1200) and (yPos >= 0) and (yPos <= 0 + 74):
            View.showScreen(eScreen.SPLASH_CLOSE)

        # Button Easy
        elif (xPos >= 380) and (xPos <= 380 + 395) and (yPos >= 150) and (yPos <= 150 + 128):
            GlobalsController.GAME_DIFFICULTY = eGameDifficulty.EASY
            View.showScreen(eScreen.BOARD)
        # Button Normal
        elif (xPos >= 380) and (xPos <= 380 + 395) and (yPos >= 290) and (yPos <= 290 + 128):
            GlobalsController.GAME_DIFFICULTY = eGameDifficulty.NORMAL
            View.showScreen(eScreen.BOARD)
        # Button Hard
        elif (xPos >= 380) and (xPos <= 380 + 395) and (yPos >= 420) and (yPos <= 420 + 128):
            GlobalsController.GAME_DIFFICULTY = eGameDifficulty.HARD
            View.showScreen(eScreen.BOARD)
            

class ScreenBoard:

    def __init__(self, clock, displaySurface):
        
        # Screen
        self.__clock = clock
        self.__displaySurface = displaySurface
        self.__isActive = False
        
        # Stats
        self.__level = 1
        self.__stars = 0
        
        # Turn Control
        self.__state = eBoardState.CAN_PICK_FIRST_CARD
        self.__unlockTurnCurrentTime = 1
        self.__unlockTurnTotalTime = 3
        self.__firstCardShowed = None
        self.__secondCardShowed = None
        
        # Match
        self.__matchState = eMatchState.NO_LINE
        self.__matchActivity1Image = None
        self.__matchActivity2Image = None
        self.__matchActivity3Image = None
        self.__matchLine1 = None
        self.__matchLine2 = None
        self.__matchLine3 = None
        self.__textMatchIntructions = Label("Elije la actividad que realiza cada institucion", FontController.font20, (255, 255, 255), (340, 775))
        
        # Time
        self.__currentIteration = 0
        if GlobalsController.GAME_DIFFICULTY == eGameDifficulty.EASY:
            self.__seconds = 1
            self.__minutes = 5
        elif GlobalsController.GAME_DIFFICULTY == eGameDifficulty.NORMAL:
            self.__seconds = 1
            self.__minutes = 8
        elif GlobalsController.GAME_DIFFICULTY == eGameDifficulty.HARD:
            self.__seconds = 1
            self.__minutes = 12
        
        # Question
        self.__correctAnswer = None
        self.__selectedAnswer = None
        self.__isSelectedAnswerRight = False
        
        # Stars for Right Answer
        self.__secondsCountdownToAnswer = 10
        self.__currentCountdownToAnswer = 1
        self.__starsToWin = 5
        
        # Stats
        self.__titleLevel = Label("Nivel : ", FontController.font35, (255, 255, 0), (70, 5))
        self.__textLevel = Label(str(self.__level), FontController.font35, (255, 255, 255), (190, 5))
        self.__textStars = Label("x " + str(self.__stars), FontController.font35, (255, 255, 255), (530, 8))
        self.__textTime = Label("--- : ---", FontController.font35, (255, 255, 255), (880, 8))
        
        # Activity
        self.__activityImage = None
        self.__activityName1 = Label("", FontController.font30, (255, 255, 255), (30, 75))
        
        self.__activityDescription1 = Label("", FontController.font28, (255, 255, 255), (80, 380 + (30 * 0)))
        self.__activityDescription2 = Label("", FontController.font28, (255, 255, 255), (80, 380 + (30 * 1)))
        self.__activityDescription3 = Label("", FontController.font28, (255, 255, 255), (80, 380 + (30 * 2)))
        self.__activityDescription4 = Label("", FontController.font28, (255, 255, 255), (80, 380 + (30 * 3)))
        self.__activityDescription5 = Label("", FontController.font28, (255, 255, 255), (80, 380 + (30 * 4)))
        self.__activityDescription6 = Label("", FontController.font28, (255, 255, 255), (80, 380 + (30 * 5)))
        self.__activityDescription7 = Label("", FontController.font28, (255, 255, 255), (80, 380 + (30 * 6)))
        self.__activityDescription8 = Label("", FontController.font28, (255, 255, 255), (80, 380 + (30 * 7)))
        self.__activityDescription9 = Label("", FontController.font28, (255, 255, 255), (80, 380 + (30 * 8)))
        self.__activityDescription10 = Label("", FontController.font28, (255, 255, 255), (80, 380 + (30 * 9)))
        self.__activityDescription11 = Label("", FontController.font28, (255, 255, 255), (80, 380 + (30 * 10)))
        self.__activityDescription12 = Label("", FontController.font28, (255, 255, 255), (80, 380 + (30 * 11)))
        
        # Question
        self.__question1 = Label("", FontController.font25, (255, 255, 255), (650, 350 + (32 * 0)))
        self.__question2 = Label("", FontController.font25, (255, 255, 255), (650, 350 + (32 * 1)))
        self.__question3 = Label("", FontController.font25, (255, 255, 255), (650, 350 + (32 * 2)))
        self.__question4 = Label("", FontController.font25, (255, 255, 255), (650, 350 + (32 * 3)))
        
        self.__answerA_1 = Label("", FontController.font25, (255, 255, 255), (710, 550 - 40 + (32 * 0)))
        self.__answerA_2 = Label("", FontController.font25, (255, 255, 255), (710, 550 - 40 + (32 * 1)))
        
        self.__answerB_1 = Label("", FontController.font25, (255, 255, 255), (710, 650 - 40 + (32 * 0)))
        self.__answerB_2 = Label("", FontController.font25, (255, 255, 255), (710, 650 - 40 + (32 * 1)))
        
        self.__answerC_1 = Label("", FontController.font25, (255, 255, 255), (710, 750 - 40 + (32 * 0)))
        self.__answerC_2 = Label("", FontController.font25, (255, 255, 255), (710, 750 - 40 + (32 * 1)))
        
        # Background
        self.__backgroundIndex = random.randint(0, 5)
        if self.__backgroundIndex == 0:
            self.__background = ResourceController.background_BoardA
        if self.__backgroundIndex == 1:
            self.__background = ResourceController.background_BoardB
        if self.__backgroundIndex == 2:
            self.__background = ResourceController.background_BoardC
        if self.__backgroundIndex == 3:
            self.__background = ResourceController.background_BoardD
        if self.__backgroundIndex == 4:
            self.__background = ResourceController.background_BoardE
        if self.__backgroundIndex == 5:
            self.__background = ResourceController.background_BoardF
        
        # Creamos las matriz de cartas
        if GlobalsController.GAME_DIFFICULTY == eGameDifficulty.EASY:
            self.__columns = 5
            self.__rows = 4
        elif GlobalsController.GAME_DIFFICULTY == eGameDifficulty.NORMAL:
            self.__columns = 6
            self.__rows = 4
        elif GlobalsController.GAME_DIFFICULTY == eGameDifficulty.HARD:
            self.__columns = 8
            self.__rows = 4
        self.__cards = [list(range(self.__columns)) for i in list(range(self.__rows))]

        # Nos asegurarnos de no elegir actividades repetidas
        allActivities = list()
        for current in InformationActivities.allActivities:
            allActivities.append(current)
                
        # Elegimos las actividad al azar
        self.__chosenActivities = list()
        index = 0
        while index < ((self.__rows * self.__columns) / 2):
            
            if index == 0:
                # Elegimos la actividad Comodin
                randomActivity = allActivities[60]
            else:
                randomActivity = random.choice(allActivities)

            # La actividad elegida al azar es agregada a la lista de actividades a mostrar y
            #  removida de la lista de todas las actividades para evitar que en un tablero existan actividades repetidas            
            self.__chosenActivities.append(randomActivity)
            allActivities.remove(randomActivity)
            
            index = index + 1
            
        # Creamos una lista con todas las posibles combinaciones de indices para realizar la asignacion sin errores
        availableCardIndexes = list()
        indexRow = 0
        indexColumn = 0
        while indexRow < self.__rows:
            while indexColumn < self.__columns:
                availableCardIndexes.append((indexRow, indexColumn))
                indexColumn = indexColumn + 1
            indexRow = indexRow + 1
            indexColumn = 0
        
        # Le indicamos a cada carta la actividad que representa
        for currentActivity in self.__chosenActivities:
            
            # Elegimos una coordenada al azar y la revemos de la lista de opciones para no volver a seleccionarla
            chosenCardIndexes = random.choice(availableCardIndexes)
            availableCardIndexes.remove(chosenCardIndexes)
            
            # A la carta en dicha coordenada le asignamos la actividad actual
            self.__cards[chosenCardIndexes[0]][chosenCardIndexes[1]] = Card(currentActivity, chosenCardIndexes)
            
            # ---------------------------------------------
            # Repetimos el proceso para la carta compañera
            
            # Elegimos una coordenada al azar y la revemos de la lista de opciones para no volver a seleccionarla
            chosenCardIndexes = random.choice(availableCardIndexes)
            availableCardIndexes.remove(chosenCardIndexes)
            
            # A la carta en dicha coordenada le asignamos la actividad actual
            self.__cards[chosenCardIndexes[0]][chosenCardIndexes[1]] = Card(currentActivity, chosenCardIndexes)
            
        # Reproducimos la musica correspondiente
        AudioController.playMusic(eMusic.BOARD)
        
        # Hover
        self.__hoverCloseGame = False
        self.__hoverAnswerA = False
        self.__hoverAnswerB = False
        self.__hoverAnswerC = False
        self.__hoverCloseQuestion = False
        self.__hoverTryAgain = False

    def __doTask(self):
        
        # Mouse Hover Detection
        (xPos, yPos) = pygame.mouse.get_pos()
        
        # Outside
        self.__hoverCloseGame = False
        self.__hoverAnswerA = False
        self.__hoverAnswerB = False
        self.__hoverAnswerC = False
        self.__hoverCloseQuestion = False
        self.__hoverTryAgain = False
        
        # Close Game
        if (xPos >= 1200 - 87) and (xPos <= 1200) and (yPos >= 0) and (yPos <= 0 + 74):
            self.__hoverCloseGame = True
            
        elif self.__state == eBoardState.TIME_OUT:
            
            # Try Again
            if (xPos >= (600 - 165)) and (xPos <= (600 - 165 + 330)) and (yPos >= 500) and (yPos <= (500 + 65)):
                self.__hoverTryAgain = True
            
        elif self.__state == eBoardState.LEVEL_FINISHED:
            
            if self.__selectedAnswer != None:
            
                # Close Question
                if (xPos >= (600 - (380 / 2))) and (xPos <= (600 - (380 / 2)) + 380) and (yPos >= 520) and (yPos <= 520 + 108):
                    self.__hoverCloseQuestion = True
                    
            else:
                # Button Answer A
                if (xPos >= 620) and (xPos <= 620 + 72) and (yPos >= 500) and (yPos <= 500 + 72):
                    self.__hoverAnswerA = True
        
                # Button Answer B
                elif (xPos >= 620) and (xPos <= 620 + 72) and (yPos >= 600) and (yPos <= 600 + 72):
                    self.__hoverAnswerB = True
        
                # Button Answer C
                elif (xPos >= 620) and (xPos <= 620 + 72) and (yPos >= 700) and (yPos <= 700 + 72):
                    self.__hoverAnswerC = True
        
        elif self.__state == eBoardState.COMODIN:
            beto = 0
            # TODO
                
        # Actualizacion del timer
        self.__updateClock()
        
        # Si ya se cumplió el tiempo para que se permita nuevamente la seleccion de cartas...
        if self.__state == eBoardState.CAN_NOT_PICK:
            if self.__unlockTurnCurrentTime < self.__unlockTurnTotalTime:
                self.__unlockTurnCurrentTime = self.__unlockTurnCurrentTime + 1
            else:
                self.__unlockTurn()
                self.__unlockTurnCurrentTime = 1
                
        if self.__state == eBoardState.LEVEL_FINISHED:
            
            if self.__isSelectedAnswerRight == False:
                
                if self.__starsToWin > 1:
                    
                    if self.__currentCountdownToAnswer > 3:
                        
                        # Acaba de transcurrir un segundo
                        self.__currentCountdownToAnswer = 1
                        
                        # Disminuimos la cantidad de segundos del conteo
                        self.__secondsCountdownToAnswer = self.__secondsCountdownToAnswer - 1
                        
                        # Si el conteo par la estrella actual finalizo
                        if self.__secondsCountdownToAnswer < 1:
                            
                            # Disminuimos la cantidad de estrellas 
                            self.__starsToWin = self.__starsToWin - 1
                            
                            # Reiniciamos el conteo de estrellas
                            self.__secondsCountdownToAnswer = 10
                            
                            # Si las estrellas se acabaron
                            if self.__starsToWin == 1:
                                AudioController.stopSounds()
                                AudioController.stopMusic()
                    else:
                        # El conteo avanza
                        self.__currentCountdownToAnswer = self.__currentCountdownToAnswer + 1
        
        # Detectamos todos los eventos y ejecutamos las acciones correspondientes
        if pygame.event:
            for event in pygame.event.get():
                 
                # Evento cerrar el juego
                if event.type == pygame.QUIT:
                    GlobalsController.INFO_STARS = self.__stars
                    View.showScreen(eScreen.SPLASH_CLOSE)
                    
                # Eventos del sistema
                elif event.type == pygame.USEREVENT:
                    pass
                    
                # Deteccion de click de mouse
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    self.__doMouseAction(event)
                    
                # Deteccion de teclas presionadas
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        GlobalsController.INFO_STARS = self.__stars
                        View.showScreen(eScreen.SPLASH_CLOSE)
                    elif event.key == pygame.K_RSHIFT:
                        self.__switchCase()
                    elif event.key == pygame.K_LSHIFT:
                        self.__switchCase()
                    else:
                        self.__doKeyAction(event)
                        
    def __doPaint(self):
        
        # Background
        self.__displaySurface.blit(self.__background, (0, 0))
        
        # Activity Description
        self.__activityName1.doPaint(self.__displaySurface)
        
        # Cards
        for currentRow in self.__cards:
            for currentCard in currentRow:
                currentCard.doPaint(self.__displaySurface)
       
        if self.__state == eBoardState.TIME_OUT:
            
            # Background
            self.__displaySurface.blit(ResourceController.background_Transparent, (0, 0))
            self.__displaySurface.blit(ResourceController.game_MessageTryAgain, (600 - (742 / 2), (825 / 2) - (326 / 2) - 50))
            
            # Boton Try Again
            if self.__hoverTryAgain == True:
                self.__displaySurface.blit(ResourceController.input_Accept_On, (600 - (330 / 2), 500))
            else:
                self.__displaySurface.blit(ResourceController.input_Accept_Off, (600 - (330 / 2), 500))
            
        elif self.__state == eBoardState.LEVEL_FINISHED:
            
            # Answers Buttons
            if self.__selectedAnswer != None:
                
                # Background
                self.__displaySurface.blit(ResourceController.background_Transparent, (0, 0))                
                self.__displaySurface.blit(ResourceController.background_Answer, (600 - (960 / 2), 0))
                
                # Stats Bars
                self.__displaySurface.blit(ResourceController.game_StatsBackground, (20, 0))
                self.__titleLevel.doPaint(self.__displaySurface)
                self.__textLevel.doPaint(self.__displaySurface)
                
                self.__displaySurface.blit(ResourceController.game_StatsBackground, (380 + 20, 0))
                self.__displaySurface.blit(ResourceController.game_StarMini, (460, 4))
                self.__textStars.doPaint(self.__displaySurface)
                
                self.__displaySurface.blit(ResourceController.game_StatsBackground, (760 + 20, 0))
                self.__displaySurface.blit(ResourceController.game_ClockMini, (810, 4))
                self.__textTime.doPaint(self.__displaySurface)
                
                if self.__isSelectedAnswerRight == True:
                    
                    # Stars
                    if self.__starsToWin == 5:
                        self.__displaySurface.blit(ResourceController.game_StarBig_On, (250 + (130 * 0), 200))
                        self.__displaySurface.blit(ResourceController.game_StarBig_On, (250 + (130 * 1), 200))
                        self.__displaySurface.blit(ResourceController.game_StarBig_On, (250 + (130 * 2), 200))
                        self.__displaySurface.blit(ResourceController.game_StarBig_On, (250 + (130 * 3), 200))
                        self.__displaySurface.blit(ResourceController.game_StarBig_On, (250 + (130 * 4), 200))
                    elif self.__starsToWin == 4:
                        self.__displaySurface.blit(ResourceController.game_StarBig_On, (250 + (130 * 0), 200))
                        self.__displaySurface.blit(ResourceController.game_StarBig_On, (250 + (130 * 1), 200))
                        self.__displaySurface.blit(ResourceController.game_StarBig_On, (250 + (130 * 2), 200))
                        self.__displaySurface.blit(ResourceController.game_StarBig_On, (250 + (130 * 3), 200))
                        self.__displaySurface.blit(ResourceController.game_StarBig_Off, (250 + (130 * 4), 200))
                    elif self.__starsToWin == 3:
                        self.__displaySurface.blit(ResourceController.game_StarBig_On, (250 + (130 * 0), 200))
                        self.__displaySurface.blit(ResourceController.game_StarBig_On, (250 + (130 * 1), 200))
                        self.__displaySurface.blit(ResourceController.game_StarBig_On, (250 + (130 * 2), 200))
                        self.__displaySurface.blit(ResourceController.game_StarBig_Off, (250 + (130 * 3), 200))
                        self.__displaySurface.blit(ResourceController.game_StarBig_Off, (250 + (130 * 4), 200))
                    elif self.__starsToWin == 2:
                        self.__displaySurface.blit(ResourceController.game_StarBig_On, (250 + (130 * 0), 200))
                        self.__displaySurface.blit(ResourceController.game_StarBig_On, (250 + (130 * 1), 200))
                        self.__displaySurface.blit(ResourceController.game_StarBig_Off, (250 + (130 * 2), 200))
                        self.__displaySurface.blit(ResourceController.game_StarBig_Off, (250 + (130 * 3), 200))
                        self.__displaySurface.blit(ResourceController.game_StarBig_Off, (250 + (130 * 4), 200))
                    elif self.__starsToWin == 1:
                        self.__displaySurface.blit(ResourceController.game_StarBig_On, (250 + (130 * 0), 200))
                        self.__displaySurface.blit(ResourceController.game_StarBig_Off, (250 + (130 * 1), 200))
                        self.__displaySurface.blit(ResourceController.game_StarBig_Off, (250 + (130 * 2), 200))
                        self.__displaySurface.blit(ResourceController.game_StarBig_Off, (250 + (130 * 3), 200))
                        self.__displaySurface.blit(ResourceController.game_StarBig_Off, (250 + (130 * 4), 200))
                    else:
                        self.__displaySurface.blit(ResourceController.game_StarBig_Off, (250 + (130 * 0), 200))
                        self.__displaySurface.blit(ResourceController.game_StarBig_Off, (250 + (130 * 1), 200))
                        self.__displaySurface.blit(ResourceController.game_StarBig_Off, (250 + (130 * 2), 200))
                        self.__displaySurface.blit(ResourceController.game_StarBig_Off, (250 + (130 * 3), 200))
                        self.__displaySurface.blit(ResourceController.game_StarBig_Off, (250 + (130 * 4), 200))
                
                    # Messages
                    self.__displaySurface.blit(ResourceController.game_MessageYouGot, (600 - (612 / 2), 100))
                    self.__displaySurface.blit(ResourceController.game_MessageGoodWork, (400, 370))
                    
                    # Boy
                    self.__displaySurface.blit(ResourceController.game_Boy, (1040, 825 - 236))                    

                else:
                    # Wrong Answer
                    self.__displaySurface.blit(ResourceController.game_MessageWrongAnswer, (600 - (900 / 2), 90))
                
                # Close Question Button
                if self.__hoverCloseQuestion == True:
                    self.__displaySurface.blit(ResourceController.input_NextLevel_On, (600 - (380 / 2), 520))
                else:
                    self.__displaySurface.blit(ResourceController.input_NextLevel_Off, (600 - (380 / 2), 520))
                
            else:
                # Background
                self.__displaySurface.blit(ResourceController.background_Transparent, (0, 0))
                self.__displaySurface.blit(ResourceController.background_Question, (0, 0))
                
                # Stats Bars
                self.__displaySurface.blit(ResourceController.game_StatsBackground, (20, 0))
                self.__titleLevel.doPaint(self.__displaySurface)
                self.__textLevel.doPaint(self.__displaySurface)
                
                self.__displaySurface.blit(ResourceController.game_StatsBackground, (380 + 20, 0))
                self.__displaySurface.blit(ResourceController.game_StarMini, (460, 4))
                self.__textStars.doPaint(self.__displaySurface)
                
                self.__displaySurface.blit(ResourceController.game_StatsBackground, (760 + 20, 0))
                self.__displaySurface.blit(ResourceController.game_ClockMini, (810, 4))
                self.__textTime.doPaint(self.__displaySurface)
                
                # Clock
                if self.__starsToWin > 1:
                    self.__displaySurface.blit(ResourceController.game_ClockBig, (450, 300))  # (200, 130))
                    
                    if self.__secondsCountdownToAnswer == 10:
                        self.__displaySurface.blit(ResourceController.game_Number10, (480, 330))
                    elif self.__secondsCountdownToAnswer == 9:
                        self.__displaySurface.blit(ResourceController.game_Number9, (480, 330))
                    elif self.__secondsCountdownToAnswer == 8:
                        self.__displaySurface.blit(ResourceController.game_Number8, (480, 330))
                    elif self.__secondsCountdownToAnswer == 7:
                        self.__displaySurface.blit(ResourceController.game_Number7, (480, 330))
                    elif self.__secondsCountdownToAnswer == 6:
                        self.__displaySurface.blit(ResourceController.game_Number6, (480, 330))
                    elif self.__secondsCountdownToAnswer == 5:
                        self.__displaySurface.blit(ResourceController.game_Number5, (480, 330))
                    elif self.__secondsCountdownToAnswer == 4:
                        self.__displaySurface.blit(ResourceController.game_Number4, (480, 330))
                    elif self.__secondsCountdownToAnswer == 3:
                        self.__displaySurface.blit(ResourceController.game_Number3, (480, 330))
                    elif self.__secondsCountdownToAnswer == 2:
                        self.__displaySurface.blit(ResourceController.game_Number2, (480, 330))
                    elif self.__secondsCountdownToAnswer == 1:
                        self.__displaySurface.blit(ResourceController.game_Number1, (480, 330))
                
                # Stars
                if self.__starsToWin == 5:
                    self.__displaySurface.blit(ResourceController.game_StarBig_On, (250 + (130 * 0), 125))
                    self.__displaySurface.blit(ResourceController.game_StarBig_On, (250 + (130 * 1), 125))
                    self.__displaySurface.blit(ResourceController.game_StarBig_On, (250 + (130 * 2), 125))
                    self.__displaySurface.blit(ResourceController.game_StarBig_On, (250 + (130 * 3), 125))
                    self.__displaySurface.blit(ResourceController.game_StarBig_On, (250 + (130 * 4), 125))
                elif self.__starsToWin == 4:
                    self.__displaySurface.blit(ResourceController.game_StarBig_On, (250 + (130 * 0), 115))
                    self.__displaySurface.blit(ResourceController.game_StarBig_On, (250 + (130 * 1), 115))
                    self.__displaySurface.blit(ResourceController.game_StarBig_On, (250 + (130 * 2), 115))
                    self.__displaySurface.blit(ResourceController.game_StarBig_On, (250 + (130 * 3), 115))
                    self.__displaySurface.blit(ResourceController.game_StarBig_Off, (250 + (130 * 4), 115))
                elif self.__starsToWin == 3:
                    self.__displaySurface.blit(ResourceController.game_StarBig_On, (250 + (130 * 0), 115))
                    self.__displaySurface.blit(ResourceController.game_StarBig_On, (250 + (130 * 1), 115))
                    self.__displaySurface.blit(ResourceController.game_StarBig_On, (250 + (130 * 2), 115))
                    self.__displaySurface.blit(ResourceController.game_StarBig_Off, (250 + (130 * 3), 115))
                    self.__displaySurface.blit(ResourceController.game_StarBig_Off, (250 + (130 * 4), 115))
                elif self.__starsToWin == 2:
                    self.__displaySurface.blit(ResourceController.game_StarBig_On, (250 + (130 * 0), 115))
                    self.__displaySurface.blit(ResourceController.game_StarBig_On, (250 + (130 * 1), 115))
                    self.__displaySurface.blit(ResourceController.game_StarBig_Off, (250 + (130 * 2), 115))
                    self.__displaySurface.blit(ResourceController.game_StarBig_Off, (250 + (130 * 3), 115))
                    self.__displaySurface.blit(ResourceController.game_StarBig_Off, (250 + (130 * 4), 115))
                elif self.__starsToWin == 1:
                    self.__displaySurface.blit(ResourceController.game_StarBig_On, (250 + (130 * 0), 115))
                    self.__displaySurface.blit(ResourceController.game_StarBig_Off, (250 + (130 * 1), 115))
                    self.__displaySurface.blit(ResourceController.game_StarBig_Off, (250 + (130 * 2), 115))
                    self.__displaySurface.blit(ResourceController.game_StarBig_Off, (250 + (130 * 3), 115))
                    self.__displaySurface.blit(ResourceController.game_StarBig_Off, (250 + (130 * 4), 115))
                else:
                    self.__displaySurface.blit(ResourceController.game_StarBig_Off, (250 + (130 * 0), 105))
                    self.__displaySurface.blit(ResourceController.game_StarBig_Off, (250 + (130 * 1), 105))
                    self.__displaySurface.blit(ResourceController.game_StarBig_Off, (250 + (130 * 2), 105))
                    self.__displaySurface.blit(ResourceController.game_StarBig_Off, (250 + (130 * 3), 105))
                    self.__displaySurface.blit(ResourceController.game_StarBig_Off, (250 + (130 * 4), 105))

                # Activity description
                self.__activityName1.doPaint(self.__displaySurface)
                
                self.__activityDescription1.doPaint(self.__displaySurface)
                self.__activityDescription2.doPaint(self.__displaySurface)
                self.__activityDescription3.doPaint(self.__displaySurface)
                self.__activityDescription4.doPaint(self.__displaySurface)
                self.__activityDescription5.doPaint(self.__displaySurface)
                self.__activityDescription6.doPaint(self.__displaySurface)
                self.__activityDescription7.doPaint(self.__displaySurface)
                self.__activityDescription8.doPaint(self.__displaySurface)
                self.__activityDescription9.doPaint(self.__displaySurface)
                self.__activityDescription10.doPaint(self.__displaySurface)
                self.__activityDescription11.doPaint(self.__displaySurface)
                self.__activityDescription12.doPaint(self.__displaySurface)
                
                # Question Text
                self.__question1.doPaint(self.__displaySurface)
                self.__question2.doPaint(self.__displaySurface)
                self.__question3.doPaint(self.__displaySurface)
                self.__question4.doPaint(self.__displaySurface)
                
                # Answers Text
                self.__answerA_1.doPaint(self.__displaySurface)
                self.__answerA_2.doPaint(self.__displaySurface)
                
                self.__answerB_1.doPaint(self.__displaySurface)
                self.__answerB_2.doPaint(self.__displaySurface)
                
                self.__answerC_1.doPaint(self.__displaySurface)
                self.__answerC_2.doPaint(self.__displaySurface)
                
                if self.__hoverAnswerA == True:
                    self.__displaySurface.blit(ResourceController.input_AnswerA_On, (620, 500))
                else:
                    self.__displaySurface.blit(ResourceController.input_AnswerA_Off, (620, 500))
                        
                if self.__hoverAnswerB == True:
                    self.__displaySurface.blit(ResourceController.input_AnswerB_On, (620, 600))
                else:
                    self.__displaySurface.blit(ResourceController.input_AnswerB_Off, (620, 600))
                        
                if self.__hoverAnswerC == True:
                    self.__displaySurface.blit(ResourceController.input_AnswerC_On, (620, 700))
                else:
                    self.__displaySurface.blit(ResourceController.input_AnswerC_Off, (620, 700))
        
        elif self.__state == eBoardState.COMODIN: # Match
            
            # TODO
            
            # Fondo
            self.__displaySurface.blit(ResourceController.background_Match, (0, 0))

            # Instrucciones
            if self.__matchState != eMatchState.ANSWER:
                self.__textMatchIntructions.doPaint(self.__displaySurface)

            # Logos
            self.__displaySurface.blit(ResourceController.game_CultureLogo, (40, 80))
            self.__displaySurface.blit(ResourceController.game_RecreationLogo, (70, 330))
            self.__displaySurface.blit(ResourceController.game_SocialLogo, (40, 570))
            
            # Selectores
            if self.__matchState == eMatchState.NO_LINE:
                self.__displaySurface.blit(ResourceController.game_SelectorYellow, (40, 75))
            if self.__matchState == eMatchState.LINE_1:
                self.__displaySurface.blit(ResourceController.game_SelectorWhite, (40, 75))
                self.__displaySurface.blit(ResourceController.game_SelectorYellow, (40, 325))
            if self.__matchState == eMatchState.LINE_2:
                self.__displaySurface.blit(ResourceController.game_SelectorWhite, (40, 75))
                self.__displaySurface.blit(ResourceController.game_SelectorWhite, (40, 325))
                self.__displaySurface.blit(ResourceController.game_SelectorYellow, (40, 565))
            if self.__matchState == eMatchState.ANSWER:
                self.__displaySurface.blit(ResourceController.game_SelectorYellow, (40, 75))
                self.__displaySurface.blit(ResourceController.game_SelectorYellow, (40, 325))
                self.__displaySurface.blit(ResourceController.game_SelectorYellow, (40, 565))
            
            # Actividades
            self.__displaySurface.blit(self.__matchActivity1Image, (800, 60))
            self.__displaySurface.blit(self.__matchActivity2Image, (800, 320))
            self.__displaySurface.blit(self.__matchActivity3Image, (800, 570))
            
            # Lineas
            if self.__matchState == eMatchState.LINE_1:
                self.__displaySurface.blit(self.__matchLine1, (360, 85))
            if self.__matchState == eMatchState.LINE_2:
                self.__displaySurface.blit(self.__matchLine1, (360, 85))
                self.__displaySurface.blit(self.__matchLine2, (360, 85))
            if self.__matchState == eMatchState.ANSWER:
                self.__displaySurface.blit(self.__matchLine1, (360, 85))
                self.__displaySurface.blit(self.__matchLine2, (360, 85))
                self.__displaySurface.blit(self.__matchLine3, (360, 85))
                
            # Background Answer
            if self.__matchState == eMatchState.ANSWER: 
                self.__displaySurface.blit(ResourceController.background_Transparent, (0, 0))
                self.__displaySurface.blit(ResourceController.background_Answer, (600 - (960 / 2), 0))
                self.__displaySurface.blit(ResourceController.game_MessageGoodWork, (400, 300))
                self.__displaySurface.blit(ResourceController.input_Accept_On, (420, 520))
        
        # Stats Bars
        self.__displaySurface.blit(ResourceController.game_StatsBackground, (20, 0))
        self.__titleLevel.doPaint(self.__displaySurface)
        self.__textLevel.doPaint(self.__displaySurface)
        
        self.__displaySurface.blit(ResourceController.game_StatsBackground, (380 + 20, 0))
        self.__displaySurface.blit(ResourceController.game_StarMini, (460, 4))
        self.__textStars.doPaint(self.__displaySurface)
        
        self.__displaySurface.blit(ResourceController.game_StatsBackground, (760 + 20, 0))
        self.__displaySurface.blit(ResourceController.game_ClockMini, (810, 4))
        self.__textTime.doPaint(self.__displaySurface)
            
        # Buttons with Hover
        if self.__hoverCloseGame == True:
            self.__displaySurface.blit(ResourceController.input_CloseGame_On, (1200 - 87, 0))
        else:
            self.__displaySurface.blit(ResourceController.input_CloseGame_Off, (1200 - 87, 0))
        
        # Actualizamos la pantalla
        pygame.display.flip()

    def __resetBoard(self):
        
        # Turn Control
        self.__state = eBoardState.CAN_PICK_FIRST_CARD
        self.__unlockTurnCurrentTime = 1
        self.__firstCardShowed = None
        self.__secondCardShowed = None
        
        # Time
        self.__currentIteration = 0
        if GlobalsController.GAME_DIFFICULTY == eGameDifficulty.EASY:
            self.__seconds = 1
            self.__minutes = 3
        elif GlobalsController.GAME_DIFFICULTY == eGameDifficulty.NORMAL:
            self.__seconds = 1
            self.__minutes = 6
        elif GlobalsController.GAME_DIFFICULTY == eGameDifficulty.HARD:
            self.__seconds = 1
            self.__minutes = 8
        
        # Answer
        self.__correctAnswer = None
        self.__selectedAnswer = None
        self.__isSelectedAnswerRight = False
        
        # Stars for Right Answer
        self.__secondsCountdownToAnswer = 10
        self.__currentCountdownToAnswer = 1
        self.__starsToWin = 5
        
        # Stats
        self.__textLevel.setText(str(self.__level))
        self.__textStars.setText("x " + str(self.__stars))
        self.__textTime.setText("--- : ---")
        self.__textTime.setColor((255, 255, 255))
        
        # Activity
        self.__activityImage = None
        self.__activityName1.setText("")
        
        self.__activityDescription1.setText("")
        self.__activityDescription2.setText("")
        self.__activityDescription3.setText("")
        self.__activityDescription4.setText("")
        self.__activityDescription5.setText("")
        self.__activityDescription6.setText("")
        self.__activityDescription7.setText("")
        self.__activityDescription8.setText("")
        self.__activityDescription9.setText("")
        self.__activityDescription10.setText("")
        self.__activityDescription11.setText("")
        self.__activityDescription12.setText("")
        
        # Question
        self.__question1.setText("")
        self.__question2.setText("")
        self.__question3.setText("")
        self.__question4.setText("")
        
        self.__answerA_1.setText("")
        self.__answerA_2.setText("")
        
        self.__answerB_1.setText("")
        self.__answerB_2.setText("")
        
        self.__answerC_1.setText("")
        self.__answerC_2.setText("")
        
        self.__answerA_1.setColor((255, 255, 255))
        self.__answerA_2.setColor((255, 255, 255))
        
        self.__answerB_1.setColor((255, 255, 255))
        self.__answerB_2.setColor((255, 255, 255))
        
        self.__answerC_1.setColor((255, 255, 255))
        self.__answerC_2.setColor((255, 255, 255))
        
        # Creamos las matriz de cartas
        self.__cards = [list(range(self.__columns)) for i in list(range(self.__rows))]

        # Nos asegurarnos de no elegir actividades repetidas
        allActivities = list()
        for current in InformationActivities.allActivities:
            allActivities.append(current)
                
        # Elegimos las actividad al azar
        self.__chosenActivities = list()
        index = 0
        while index < ((self.__rows * self.__columns) / 2):
            
            if index == 0:
                # Elegimos la actividad Comodin
                randomActivity = allActivities[60]
            else:
                randomActivity = random.choice(allActivities)

            # La actividad elegida al azar es agregada a la lista de actividades a mostrar y
            # Removida de la lista de todas las actividades para evitar que en un tablero existan actividades repetidas            
            self.__chosenActivities.append(randomActivity)
            allActivities.remove(randomActivity)
            
            index = index + 1
            
        # Creamos una lista con todas las posibles combinaciones de indices para realizar la asignacion sin errores
        availableCardIndexes = list()
        indexRow = 0
        indexColumn = 0
        while indexRow < self.__rows:
            while indexColumn < self.__columns:
                availableCardIndexes.append((indexRow, indexColumn))
                indexColumn = indexColumn + 1
            indexRow = indexRow + 1
            indexColumn = 0
        
        # Le indicamos a cada carta la actividad que representa
        for currentActivity in self.__chosenActivities:
            
            # Elegimos una coordenada al azar y la revemos de la lista de opciones para no volver a seleccionarla
            chosenCardIndexes = random.choice(availableCardIndexes)
            availableCardIndexes.remove(chosenCardIndexes)
            
            # A la carta en dicha coordenada le asignamos la actividad actual
            self.__cards[chosenCardIndexes[0]][chosenCardIndexes[1]] = Card(currentActivity, chosenCardIndexes)
            
            # ---------------------------------------------
            # Repetimos el proceso para la carta compañera
            
            # Elegimos una coordenada al azar y la revemos de la lista de opciones para no volver a seleccionarla
            chosenCardIndexes = random.choice(availableCardIndexes)
            availableCardIndexes.remove(chosenCardIndexes)
            
            # A la carta en dicha coordenada le asignamos la actividad actual
            self.__cards[chosenCardIndexes[0]][chosenCardIndexes[1]] = Card(currentActivity, chosenCardIndexes)
            
        # Reproducimos la musica correspondiente
        AudioController.playMusic(eMusic.BOARD)

    def activate(self):
        
        # Indicamos que esta pantalla pasa a estado Activo
        self.__isActive = True
        
        # Mostramos el cursor
        pygame.mouse.set_visible(True)
        
        # Ordanamos que comience el pintado de la pantalla
        self.__run()

    def deactivate(self):
        
        # Indicamos que esta pantalla pasa a estado Inactivo
        self.__isActive = False

    def __run(self):
        
        # Loop principal
        while self.__isActive is True:

            # Realizamos las operaciones propias del model
            self.__doTask()
            
            # Pintamos el resultado en pantalla
            self.__doPaint()
            
            # Running as Activity
            if olpcgames.ACTIVITY:
                pass
            else:
                # Saltamos a la siguiente iteracion, respetando el FPS establecido
                self.__clock.tick(GlobalsController.GAME_FPS)
                
    def __doKeyAction(self, event):
        pass
        
    def __processMatchInput(self, value):
        
        # Determinamos si el grupo seleccionado coincide con el grupo actual
        if value == 1:
            selectedGroup = self.__matchActivity1Group
        if value == 2:
            selectedGroup = self.__matchActivity2Group
        if value == 3:
            selectedGroup = self.__matchActivity3Group
        
        AudioController.stopSounds()
        goodChoice = False
        
        if self.__matchState == eMatchState.NO_LINE: # Culture
            if selectedGroup ==  eMatchActivityGroup.CULTURE:
                # Avanzamos al siguiente paso
                self.__matchState = self.__matchState + 1
                goodChoice = True
            else:
                goodChoice = False
            pass

        elif self.__matchState == eMatchState.LINE_1: # Recreation
            if selectedGroup == eMatchActivityGroup.RECREATION:
                # Avanzamos al siguiente paso
                self.__matchState = self.__matchState + 1
                goodChoice = True
            else:
                goodChoice = False
            pass
                            
        elif self.__matchState == eMatchState.LINE_2: # Social
            if selectedGroup ==  eMatchActivityGroup.SOCIAL:
                # Avanzamos al siguiente paso
                self.__matchState = self.__matchState + 1
                goodChoice = True
            else:
                goodChoice = False
            pass
        
        if goodChoice == True:
            if self.__matchState == eMatchState.ANSWER:
                AudioController.playSound(eSound.YUJU_BOY, 1)
                AudioController.playSound(eSound.LEVEL_WIN, 1)
            else:
                AudioController.playSound(eSound.YUJU_BOY, 1)
        else:
            AudioController.playSound(eSound.PAIR_INCORRECT, 1)
        
    def __doMouseAction(self, event):
        
        # Detectamos la posicion en X y Y del click
        xPos, yPos = event.pos

        # Close Game
        if (xPos >= 1200 - 87) and (xPos <= 1200) and (yPos >= 0) and (yPos <= 0 + 74):
            GlobalsController.INFO_STARS = self.__stars
            View.showScreen(eScreen.SPLASH_CLOSE)
            
        elif self.__state == eBoardState.TIME_OUT:
            
            # Boton Try Again
            if (xPos >= (600 - 165)) and (xPos <= (600 - 165 + 330)) and (yPos >= 500) and (yPos <= (500 + 65)):
                self.__resetBoard()
        
        elif self.__state == eBoardState.COMODIN:
            
            if self.__matchState == eMatchState.ANSWER:
                
                # Boton Aceptar
                if (xPos >= 420) and (xPos <= 420 + 335) and (yPos >= 520) and (yPos <= 520 + 72):
                    
                    # Volvemos a activar el juego
                    self.__state = eBoardState.CAN_PICK_FIRST_CARD
                    
                    # Detenemos todos los sonidos
                    AudioController.stopSounds()
                    
                    # Reanudamos la musica
                    AudioController.playMusic(eMusic.BOARD)
                    
            else:
                # Actividades
                if (xPos >= 810) and (xPos <= 810 + 375) and (yPos >= 80) and (yPos <= 80 + 230):
                    self.__processMatchInput(1)
                elif (xPos >= 810) and (xPos <= 810 + 375) and (yPos >= 310) and (yPos <= 310 + 230):
                    self.__processMatchInput(2)
                elif (xPos >= 810) and (xPos <= 810 + 375) and (yPos >= 560) and (yPos <= 560 + 230):
                    self.__processMatchInput(3)
                
        elif self.__state == eBoardState.LEVEL_FINISHED:
            
            if self.__selectedAnswer == None:
                
                # Answers Buttons
                if (xPos >= 620) and (xPos <= 620 + 72) and (yPos >= 500) and (yPos <= 500 + 72):
                    self.__checkAnswer(eQuestionAnswer.ANSWER_A)
                elif (xPos >= 620) and (xPos <= 620 + 72) and (yPos >= 600) and (yPos <= 600 + 72):
                    self.__checkAnswer(eQuestionAnswer.ANSWER_B)
                elif (xPos >= 620) and (xPos <= 620 + 72) and (yPos >= 700) and (yPos <= 700 + 72):
                    self.__checkAnswer(eQuestionAnswer.ANSWER_C)
                    
            else:
                # Next Level Button
                if (xPos >= (600 - (380 / 2))) and (xPos <= (600 - (380 / 2)) + 380) and (yPos >= 520) and (yPos <= 520 + 108):
                    
                    # Avanzamos al siguiente nivel
                    self.__level = self.__level + 1
                    
                    # Elegimos un nuevo fondo al azar
                    self.__backgroundIndex = random.randint(0, 5)
                    if self.__backgroundIndex == 0:
                        self.__background = ResourceController.background_BoardA
                    if self.__backgroundIndex == 1:
                        self.__background = ResourceController.background_BoardB
                    if self.__backgroundIndex == 2:
                        self.__background = ResourceController.background_BoardC
                    if self.__backgroundIndex == 3:
                        self.__background = ResourceController.background_BoardD
                    if self.__backgroundIndex == 4:
                        self.__background = ResourceController.background_BoardE
                    if self.__backgroundIndex == 5:
                        self.__background = ResourceController.background_BoardF
                    
                    AudioController.playSound(eSound.OPEN_CARD, 1)
                    
                    # Reiniciamos el tablero
                    self.__resetBoard()
                    
        elif (self.__state == eBoardState.CAN_PICK_FIRST_CARD) or (self.__state == eBoardState.CAN_PICK_SECOND_CARD):
        
            # Cards
            if GlobalsController.GAME_DIFFICULTY == eGameDifficulty.EASY:
                
                cardToflip = None
                
                # Row 1
                if (xPos >= 190 + (170 * 0)) and (xPos <= 190 + (170 * 0) + 142) and (yPos >= 120 + (175 * 0)) and (yPos <= 120 + (175 * 0) + 168):
                    cardToflip = self.__cards[0][0]
                elif (xPos >= 190 + (170 * 1)) and (xPos <= 190 + (170 * 1) + 142) and (yPos >= 120 + (175 * 0)) and (yPos <= 120 + (175 * 0) + 168):
                    cardToflip = self.__cards[0][1]
                elif (xPos >= 190 + (170 * 2)) and (xPos <= 190 + (170 * 2) + 142) and (yPos >= 120 + (175 * 0)) and (yPos <= 120 + (175 * 0) + 168):
                    cardToflip = self.__cards[0][2]
                elif (xPos >= 190 + (170 * 3)) and (xPos <= 190 + (170 * 3) + 142) and (yPos >= 120 + (175 * 0)) and (yPos <= 120 + (175 * 0) + 168):
                    cardToflip = self.__cards[0][3]
                elif (xPos >= 190 + (170 * 4)) and (xPos <= 190 + (170 * 4) + 142) and (yPos >= 120 + (175 * 0)) and (yPos <= 120 + (175 * 0) + 168):
                    cardToflip = self.__cards[0][4]
                
                # Row 2
                elif (xPos >= 190 + (170 * 0)) and (xPos <= 190 + (170 * 0) + 142) and (yPos >= 120 + (175 * 1)) and (yPos <= 120 + (175 * 1) + 168):
                    cardToflip = self.__cards[1][0]
                elif (xPos >= 190 + (170 * 1)) and (xPos <= 190 + (170 * 1) + 142) and (yPos >= 120 + (175 * 1)) and (yPos <= 120 + (175 * 1) + 168):
                    cardToflip = self.__cards[1][1]
                elif (xPos >= 190 + (170 * 2)) and (xPos <= 190 + (170 * 2) + 142) and (yPos >= 120 + (175 * 1)) and (yPos <= 120 + (175 * 1) + 168):
                    cardToflip = self.__cards[1][2]
                elif (xPos >= 190 + (170 * 3)) and (xPos <= 190 + (170 * 3) + 142) and (yPos >= 120 + (175 * 1)) and (yPos <= 120 + (175 * 1) + 168):
                    cardToflip = self.__cards[1][3]
                elif (xPos >= 190 + (170 * 4)) and (xPos <= 190 + (170 * 4) + 142) and (yPos >= 120 + (175 * 1)) and (yPos <= 120 + (175 * 1) + 168):
                    cardToflip = self.__cards[1][4]
                    
                # Row 3
                elif (xPos >= 190 + (170 * 0)) and (xPos <= 190 + (170 * 0) + 142) and (yPos >= 120 + (175 * 2)) and (yPos <= 120 + (175 * 2) + 168):
                    cardToflip = self.__cards[2][0]
                elif (xPos >= 190 + (170 * 1)) and (xPos <= 190 + (170 * 1) + 142) and (yPos >= 120 + (175 * 2)) and (yPos <= 120 + (175 * 2) + 168):
                    cardToflip = self.__cards[2][1]
                elif (xPos >= 190 + (170 * 2)) and (xPos <= 190 + (170 * 2) + 142) and (yPos >= 120 + (175 * 2)) and (yPos <= 120 + (175 * 2) + 168):
                    cardToflip = self.__cards[2][2]
                elif (xPos >= 190 + (170 * 3)) and (xPos <= 190 + (170 * 3) + 142) and (yPos >= 120 + (175 * 2)) and (yPos <= 120 + (175 * 2) + 168):
                    cardToflip = self.__cards[2][3]
                elif (xPos >= 190 + (170 * 4)) and (xPos <= 190 + (170 * 4) + 142) and (yPos >= 120 + (175 * 2)) and (yPos <= 120 + (175 * 2) + 168):
                    cardToflip = self.__cards[2][4]
                    
                # Row 4
                elif (xPos >= 190 + (170 * 0)) and (xPos <= 190 + (170 * 0) + 142) and (yPos >= 120 + (175 * 3)) and (yPos <= 120 + (175 * 3) + 168):
                    cardToflip = self.__cards[3][0]
                elif (xPos >= 190 + (170 * 1)) and (xPos <= 190 + (170 * 1) + 142) and (yPos >= 120 + (175 * 3)) and (yPos <= 120 + (175 * 3) + 168):
                    cardToflip = self.__cards[3][1]
                elif (xPos >= 190 + (170 * 2)) and (xPos <= 190 + (170 * 2) + 142) and (yPos >= 120 + (175 * 3)) and (yPos <= 120 + (175 * 3) + 168):
                    cardToflip = self.__cards[3][2]
                elif (xPos >= 190 + (170 * 3)) and (xPos <= 190 + (170 * 3) + 142) and (yPos >= 120 + (175 * 3)) and (yPos <= 120 + (175 * 3) + 168):
                    cardToflip = self.__cards[3][3]
                elif (xPos >= 190 + (170 * 4)) and (xPos <= 190 + (170 * 4) + 142) and (yPos >= 120 + (175 * 3)) and (yPos <= 120 + (175 * 3) + 168):
                    cardToflip = self.__cards[3][4]
                    
                if cardToflip != None:
                    if cardToflip.isOpen() == False:
                        cardToflip.flipToShow()
                        self.__turnChange(cardToflip)
                        
            elif GlobalsController.GAME_DIFFICULTY == eGameDifficulty.NORMAL:
                
                cardToflip = None
                
                # Row 1
                if (xPos >= 110 + (170 * 0)) and (xPos <= 110 + (170 * 0) + 142) and (yPos >= 120 + (175 * 0)) and (yPos <= 120 + (175 * 0) + 168):
                    cardToflip = self.__cards[0][0]
                elif (xPos >= 110 + (170 * 1)) and (xPos <= 110 + (170 * 1) + 142) and (yPos >= 120 + (175 * 0)) and (yPos <= 120 + (175 * 0) + 168):
                    cardToflip = self.__cards[0][1]
                elif (xPos >= 110 + (170 * 2)) and (xPos <= 110 + (170 * 2) + 142) and (yPos >= 120 + (175 * 0)) and (yPos <= 120 + (175 * 0) + 168):
                    cardToflip = self.__cards[0][2]
                elif (xPos >= 110 + (170 * 3)) and (xPos <= 110 + (170 * 3) + 142) and (yPos >= 120 + (175 * 0)) and (yPos <= 120 + (175 * 0) + 168):
                    cardToflip = self.__cards[0][3]
                elif (xPos >= 110 + (170 * 4)) and (xPos <= 110 + (170 * 4) + 142) and (yPos >= 120 + (175 * 0)) and (yPos <= 120 + (175 * 0) + 168):
                    cardToflip = self.__cards[0][4]
                elif (xPos >= 110 + (170 * 5)) and (xPos <= 110 + (170 * 5) + 142) and (yPos >= 120 + (175 * 0)) and (yPos <= 120 + (175 * 0) + 168):
                    cardToflip = self.__cards[0][5]
                
                # Row 2
                elif (xPos >= 110 + (170 * 0)) and (xPos <= 110 + (170 * 0) + 142) and (yPos >= 120 + (175 * 1)) and (yPos <= 120 + (175 * 1) + 168):
                    cardToflip = self.__cards[1][0]
                elif (xPos >= 110 + (170 * 1)) and (xPos <= 110 + (170 * 1) + 142) and (yPos >= 120 + (175 * 1)) and (yPos <= 120 + (175 * 1) + 168):
                    cardToflip = self.__cards[1][1]
                elif (xPos >= 110 + (170 * 2)) and (xPos <= 110 + (170 * 2) + 142) and (yPos >= 120 + (175 * 1)) and (yPos <= 120 + (175 * 1) + 168):
                    cardToflip = self.__cards[1][2]
                elif (xPos >= 110 + (170 * 3)) and (xPos <= 110 + (170 * 3) + 142) and (yPos >= 120 + (175 * 1)) and (yPos <= 120 + (175 * 1) + 168):
                    cardToflip = self.__cards[1][3]
                elif (xPos >= 110 + (170 * 4)) and (xPos <= 110 + (170 * 4) + 142) and (yPos >= 120 + (175 * 1)) and (yPos <= 120 + (175 * 1) + 168):
                    cardToflip = self.__cards[1][4]
                elif (xPos >= 110 + (170 * 5)) and (xPos <= 110 + (170 * 5) + 142) and (yPos >= 120 + (175 * 1)) and (yPos <= 120 + (175 * 1) + 168):
                    cardToflip = self.__cards[1][5]
                    
                # Row 3
                elif (xPos >= 110 + (170 * 0)) and (xPos <= 110 + (170 * 0) + 142) and (yPos >= 120 + (175 * 2)) and (yPos <= 120 + (175 * 2) + 168):
                    cardToflip = self.__cards[2][0]
                elif (xPos >= 110 + (170 * 1)) and (xPos <= 110 + (170 * 1) + 142) and (yPos >= 120 + (175 * 2)) and (yPos <= 120 + (175 * 2) + 168):
                    cardToflip = self.__cards[2][1]
                elif (xPos >= 110 + (170 * 2)) and (xPos <= 110 + (170 * 2) + 142) and (yPos >= 120 + (175 * 2)) and (yPos <= 120 + (175 * 2) + 168):
                    cardToflip = self.__cards[2][2]
                elif (xPos >= 110 + (170 * 3)) and (xPos <= 110 + (170 * 3) + 142) and (yPos >= 120 + (175 * 2)) and (yPos <= 120 + (175 * 2) + 168):
                    cardToflip = self.__cards[2][3]
                elif (xPos >= 110 + (170 * 4)) and (xPos <= 110 + (170 * 4) + 142) and (yPos >= 120 + (175 * 2)) and (yPos <= 120 + (175 * 2) + 168):
                    cardToflip = self.__cards[2][4]
                elif (xPos >= 110 + (170 * 5)) and (xPos <= 110 + (170 * 5) + 142) and (yPos >= 120 + (175 * 2)) and (yPos <= 120 + (175 * 2) + 168):
                    cardToflip = self.__cards[2][5]
                    
                # Row 4
                elif (xPos >= 110 + (170 * 0)) and (xPos <= 110 + (170 * 0) + 142) and (yPos >= 120 + (175 * 3)) and (yPos <= 120 + (175 * 3) + 168):
                    cardToflip = self.__cards[3][0]
                elif (xPos >= 110 + (170 * 1)) and (xPos <= 110 + (170 * 1) + 142) and (yPos >= 120 + (175 * 3)) and (yPos <= 120 + (175 * 3) + 168):
                    cardToflip = self.__cards[3][1]
                elif (xPos >= 110 + (170 * 2)) and (xPos <= 110 + (170 * 2) + 142) and (yPos >= 120 + (175 * 3)) and (yPos <= 120 + (175 * 3) + 168):
                    cardToflip = self.__cards[3][2]
                elif (xPos >= 110 + (170 * 3)) and (xPos <= 110 + (170 * 3) + 142) and (yPos >= 120 + (175 * 3)) and (yPos <= 120 + (175 * 3) + 168):
                    cardToflip = self.__cards[3][3]
                elif (xPos >= 110 + (170 * 4)) and (xPos <= 110 + (170 * 4) + 142) and (yPos >= 120 + (175 * 3)) and (yPos <= 120 + (175 * 3) + 168):
                    cardToflip = self.__cards[3][4]
                elif (xPos >= 110 + (170 * 5)) and (xPos <= 110 + (170 * 5) + 142) and (yPos >= 120 + (175 * 3)) and (yPos <= 120 + (175 * 3) + 168):
                    cardToflip = self.__cards[3][5]
                    
                if cardToflip != None:
                    if cardToflip.isOpen() == False:
                        cardToflip.flipToShow()
                        self.__turnChange(cardToflip)

            elif GlobalsController.GAME_DIFFICULTY == eGameDifficulty.HARD:
                
                cardToflip = None
                
                # Row 1
                if (xPos >= 10 + (148 * 0)) and (xPos <= 10 + (148 * 0) + 142) and (yPos >= 120 + (175 * 0)) and (yPos <= 120 + (175 * 0) + 168):
                    cardToflip = self.__cards[0][0]
                elif (xPos >= 10 + (148 * 1)) and (xPos <= 10 + (148 * 1) + 142) and (yPos >= 120 + (175 * 0)) and (yPos <= 120 + (175 * 0) + 168):
                    cardToflip = self.__cards[0][1]
                elif (xPos >= 10 + (148 * 2)) and (xPos <= 10 + (148 * 2) + 142) and (yPos >= 120 + (175 * 0)) and (yPos <= 120 + (175 * 0) + 168):
                    cardToflip = self.__cards[0][2]
                elif (xPos >= 10 + (148 * 3)) and (xPos <= 10 + (148 * 3) + 142) and (yPos >= 120 + (175 * 0)) and (yPos <= 120 + (175 * 0) + 168):
                    cardToflip = self.__cards[0][3]
                elif (xPos >= 10 + (148 * 4)) and (xPos <= 10 + (148 * 4) + 142) and (yPos >= 120 + (175 * 0)) and (yPos <= 120 + (175 * 0) + 168):
                    cardToflip = self.__cards[0][4]
                elif (xPos >= 10 + (148 * 5)) and (xPos <= 10 + (148 * 5) + 142) and (yPos >= 120 + (175 * 0)) and (yPos <= 120 + (175 * 0) + 168):
                    cardToflip = self.__cards[0][5]
                elif (xPos >= 10 + (148 * 6)) and (xPos <= 10 + (148 * 6) + 142) and (yPos >= 120 + (175 * 0)) and (yPos <= 120 + (175 * 0) + 168):
                    cardToflip = self.__cards[0][6]
                elif (xPos >= 10 + (148 * 7)) and (xPos <= 10 + (148 * 7) + 142) and (yPos >= 120 + (175 * 0)) and (yPos <= 120 + (175 * 0) + 168):
                    cardToflip = self.__cards[0][7]
                
                # Row 2
                elif (xPos >= 10 + (148 * 0)) and (xPos <= 10 + (148 * 0) + 142) and (yPos >= 120 + (175 * 1)) and (yPos <= 120 + (175 * 1) + 168):
                    cardToflip = self.__cards[1][0]
                elif (xPos >= 10 + (148 * 1)) and (xPos <= 10 + (148 * 1) + 142) and (yPos >= 120 + (175 * 1)) and (yPos <= 120 + (175 * 1) + 168):
                    cardToflip = self.__cards[1][1]
                elif (xPos >= 10 + (148 * 2)) and (xPos <= 10 + (148 * 2) + 142) and (yPos >= 120 + (175 * 1)) and (yPos <= 120 + (175 * 1) + 168):
                    cardToflip = self.__cards[1][2]
                elif (xPos >= 10 + (148 * 3)) and (xPos <= 10 + (148 * 3) + 142) and (yPos >= 120 + (175 * 1)) and (yPos <= 120 + (175 * 1) + 168):
                    cardToflip = self.__cards[1][3]
                elif (xPos >= 10 + (148 * 4)) and (xPos <= 10 + (148 * 4) + 142) and (yPos >= 120 + (175 * 1)) and (yPos <= 120 + (175 * 1) + 168):
                    cardToflip = self.__cards[1][4]
                elif (xPos >= 10 + (148 * 5)) and (xPos <= 10 + (148 * 5) + 142) and (yPos >= 120 + (175 * 1)) and (yPos <= 120 + (175 * 1) + 168):
                    cardToflip = self.__cards[1][5]
                elif (xPos >= 10 + (148 * 6)) and (xPos <= 10 + (148 * 6) + 142) and (yPos >= 120 + (175 * 1)) and (yPos <= 120 + (175 * 1) + 168):
                    cardToflip = self.__cards[1][6]
                elif (xPos >= 10 + (148 * 7)) and (xPos <= 10 + (148 * 7) + 142) and (yPos >= 120 + (175 * 1)) and (yPos <= 120 + (175 * 1) + 168):
                    cardToflip = self.__cards[1][7]
                    
                # Row 3
                elif (xPos >= 10 + (148 * 0)) and (xPos <= 10 + (148 * 0) + 142) and (yPos >= 120 + (175 * 2)) and (yPos <= 120 + (175 * 2) + 168):
                    cardToflip = self.__cards[2][0]
                elif (xPos >= 10 + (148 * 1)) and (xPos <= 10 + (148 * 1) + 142) and (yPos >= 120 + (175 * 2)) and (yPos <= 120 + (175 * 2) + 168):
                    cardToflip = self.__cards[2][1]
                elif (xPos >= 10 + (148 * 2)) and (xPos <= 10 + (148 * 2) + 142) and (yPos >= 120 + (175 * 2)) and (yPos <= 120 + (175 * 2) + 168):
                    cardToflip = self.__cards[2][2]
                elif (xPos >= 10 + (148 * 3)) and (xPos <= 10 + (148 * 3) + 142) and (yPos >= 120 + (175 * 2)) and (yPos <= 120 + (175 * 2) + 168):
                    cardToflip = self.__cards[2][3]
                elif (xPos >= 10 + (148 * 4)) and (xPos <= 10 + (148 * 4) + 142) and (yPos >= 120 + (175 * 2)) and (yPos <= 120 + (175 * 2) + 168):
                    cardToflip = self.__cards[2][4]
                elif (xPos >= 10 + (148 * 5)) and (xPos <= 10 + (148 * 5) + 142) and (yPos >= 120 + (175 * 2)) and (yPos <= 120 + (175 * 2) + 168):
                    cardToflip = self.__cards[2][5]
                elif (xPos >= 10 + (148 * 6)) and (xPos <= 10 + (148 * 6) + 142) and (yPos >= 120 + (175 * 2)) and (yPos <= 120 + (175 * 2) + 168):
                    cardToflip = self.__cards[2][6]
                elif (xPos >= 10 + (148 * 7)) and (xPos <= 10 + (148 * 7) + 142) and (yPos >= 120 + (175 * 2)) and (yPos <= 120 + (175 * 2) + 168):
                    cardToflip = self.__cards[2][7]
                    
                # Row 4
                elif (xPos >= 10 + (148 * 0)) and (xPos <= 10 + (148 * 0) + 142) and (yPos >= 120 + (175 * 3)) and (yPos <= 120 + (175 * 3) + 168):
                    cardToflip = self.__cards[3][0]
                elif (xPos >= 10 + (148 * 1)) and (xPos <= 10 + (148 * 1) + 142) and (yPos >= 120 + (175 * 3)) and (yPos <= 120 + (175 * 3) + 168):
                    cardToflip = self.__cards[3][1]
                elif (xPos >= 10 + (148 * 2)) and (xPos <= 10 + (148 * 2) + 142) and (yPos >= 120 + (175 * 3)) and (yPos <= 120 + (175 * 3) + 168):
                    cardToflip = self.__cards[3][2]
                elif (xPos >= 10 + (148 * 3)) and (xPos <= 10 + (148 * 3) + 142) and (yPos >= 120 + (175 * 3)) and (yPos <= 120 + (175 * 3) + 168):
                    cardToflip = self.__cards[3][3]
                elif (xPos >= 10 + (148 * 4)) and (xPos <= 10 + (148 * 4) + 142) and (yPos >= 120 + (175 * 3)) and (yPos <= 120 + (175 * 3) + 168):
                    cardToflip = self.__cards[3][4]
                elif (xPos >= 10 + (148 * 5)) and (xPos <= 10 + (148 * 5) + 142) and (yPos >= 120 + (175 * 3)) and (yPos <= 120 + (175 * 3) + 168):
                    cardToflip = self.__cards[3][5]
                elif (xPos >= 10 + (148 * 6)) and (xPos <= 10 + (148 * 6) + 142) and (yPos >= 120 + (175 * 3)) and (yPos <= 120 + (175 * 3) + 168):
                    cardToflip = self.__cards[3][6]
                elif (xPos >= 10 + (148 * 7)) and (xPos <= 10 + (148 * 7) + 142) and (yPos >= 120 + (175 * 3)) and (yPos <= 120 + (175 * 3) + 168):
                    cardToflip = self.__cards[3][7]

                if cardToflip != None:
                    if cardToflip.isOpen() == False:
                        cardToflip.flipToShow()
                        self.__turnChange(cardToflip)

    def __turnChange(self, cardToflip):
        
        if self.__state == eBoardState.CAN_PICK_FIRST_CARD:
            self.__firstCardShowed = cardToflip
            self.__state = eBoardState.CAN_PICK_SECOND_CARD
            AudioController.playSound(eSound.OPEN_CARD, 1)
            
        elif self.__state == eBoardState.CAN_PICK_SECOND_CARD:
            self.__secondCardShowed = cardToflip
            
            # Determinamos si las cartas corresponden a la misma actividad
            if self.__firstCardShowed.activityId == self.__secondCardShowed.activityId:
                self.__state = eBoardState.CAN_PICK_FIRST_CARD
                
                # Cargamos la descripcion de la actividad correspondiente
                self.__activityImage = InformationActivities.allActivities[self.__firstCardShowed.activityId].image
                self.__activityName1.setText(InformationActivities.allActivities[self.__firstCardShowed.activityId].name)
                self.__activityName1.setPosition((600 - (self.__activityName1.getTextRenderLen() / 2), self.__activityName1.getPosition()[1]))

                # Determinamos si todas las cartas estan abiertas
                currentRow = 0
                currentColumn = 0
                allCardsAreOpen = True
                
                while (currentRow < self.__rows) and (allCardsAreOpen == True):
                    while (currentColumn < self.__columns) and (allCardsAreOpen == True):
                        
                        # Si la carta actual no esta abierta
                        if self.__cards[currentRow][currentColumn].isOpen() == False:
                            
                            # Levantamos la bandera correspondiente
                            allCardsAreOpen = False
                        
                        currentColumn = currentColumn + 1
                        
                    currentRow = currentRow + 1
                    currentColumn = 0
                    
                # Si todas las cartas estan abiertas
                if allCardsAreOpen == True:
                    
                    # Nivel finalizado
                    self.__state = eBoardState.LEVEL_FINISHED
                    
                    # Elegimos una de las actividades representadas al azar
                    questionActivityId = random.choice(self.__chosenActivities)
                    
                    # Si se elige comodin
                    if questionActivityId == 61:
                        questionActivityId = 60
                    
                    # Cargamos la descripcion de la actividad correspondiente
                    questionActivity = InformationActivities.allActivities[questionActivityId]
                    self.__activityName1.setText(questionActivity.name)
                    self.__activityName1.setPosition((600 - (self.__activityName1.getTextRenderLen() / 2), self.__activityName1.getPosition()[1]))
                    
                    self.__activityImage = questionActivity.image
                    
                    self.__activityDescription1.setText(questionActivity.description[0])
                    self.__activityDescription2.setText(questionActivity.description[1])
                    self.__activityDescription3.setText(questionActivity.description[2])
                    self.__activityDescription4.setText(questionActivity.description[3])
                    self.__activityDescription5.setText(questionActivity.description[4])
                    self.__activityDescription6.setText(questionActivity.description[5])
                    self.__activityDescription7.setText(questionActivity.description[6])
                    self.__activityDescription8.setText(questionActivity.description[7])
                    self.__activityDescription9.setText(questionActivity.description[8])
                    self.__activityDescription10.setText(questionActivity.description[9])
                    self.__activityDescription11.setText(questionActivity.description[10])
                    self.__activityDescription12.setText(questionActivity.description[11])
                    
                    self.__question1.setText(questionActivity.question[0])
                    self.__question2.setText(questionActivity.question[1])
                    self.__question3.setText(questionActivity.question[2])
                    self.__question4.setText(questionActivity.question[3])
        
                    self.__answerA_1.setText(questionActivity.optionA[0])
                    self.__answerA_2.setText(questionActivity.optionA[1])
                    
                    self.__answerB_1.setText(questionActivity.optionB[0])
                    self.__answerB_2.setText(questionActivity.optionB[1])
                    
                    self.__answerC_1.setText(questionActivity.optionC[0])
                    self.__answerC_2.setText(questionActivity.optionC[1])
                    
                    self.__correctAnswer = questionActivity.answer
                    
                    # Detenemos la musica
                    AudioController.stopMusic()
                    
                    # Reproducimos los sonidos correspondientes
                    AudioController.playSound(eSound.PAIR_CORRECT, 1)
                    AudioController.playSound(eSound.TIME_RUNNING, 0)
                    
                else:
                    # Determinamos si destapo el comodin
                    if self.__firstCardShowed.activityId == eActivityId._61_COMODIN:

                        # Detenemos la musica
                        AudioController.stopMusic()
                        AudioController.stopSounds()
                        
                        # Reproducimos los sonidos correspondientes
                        AudioController.playSound(eSound.LEVEL_WIN, 1)
                        
                        # Activamos el modo Match
                        self.__state = eBoardState.COMODIN
                        
                        # Reiniciamos la data del match
                        self.__matchState = eMatchState.NO_LINE
                        self.__matchLine1 = ResourceController.game_Line1_1;
                        self.__matchLine2 = ResourceController.game_Line2_2;
                        self.__matchLine3 = ResourceController.game_Line3_3;
                        
                        # Culture
                        # Recreation
                        # Social

                        # Elejimos de manera aleatoria los grupos de actividades
                        randomGroup = randrange(3)
                        if randomGroup == 0:
                            self.__matchActivity1Group = eMatchActivityGroup.CULTURE # **********
                            self.__matchActivity2Group = eMatchActivityGroup.RECREATION
                            self.__matchActivity3Group = eMatchActivityGroup.SOCIAL
                            
                            self.__matchLine1 = ResourceController.game_Line1_1
                            self.__matchLine2 = ResourceController.game_Line2_2
                            self.__matchLine3 = ResourceController.game_Line3_3
                            
                        if randomGroup == 1:
                            self.__matchActivity1Group = eMatchActivityGroup.SOCIAL
                            self.__matchActivity2Group = eMatchActivityGroup.CULTURE # **********
                            self.__matchActivity3Group = eMatchActivityGroup.RECREATION

                            self.__matchLine1 = ResourceController.game_Line1_2
                            self.__matchLine2 = ResourceController.game_Line2_3
                            self.__matchLine3 = ResourceController.game_Line3_1
                            
                        if randomGroup == 2:
                            self.__matchActivity1Group = eMatchActivityGroup.RECREATION
                            self.__matchActivity2Group = eMatchActivityGroup.SOCIAL
                            self.__matchActivity3Group = eMatchActivityGroup.CULTURE # **********
                        
                            self.__matchLine1 = ResourceController.game_Line1_3
                            self.__matchLine2 = ResourceController.game_Line2_1
                            self.__matchLine3 = ResourceController.game_Line3_2
                        
                        # Por cada actividad elejimos una actividad aleatoria
                        randomImageContent = None
                        
                        # - Culture
                        randomImageId = randrange(3)
                        if randomImageId == 0:
                            randomImageContent = ResourceController.game_Culture_Bailar
                        if randomImageId == 1:
                            randomImageContent = ResourceController.game_Culture_Guitarra
                        if randomImageId == 2:
                            randomImageContent = ResourceController.game_Culture_Teatro
                            
                        if randomGroup == 0:
                            self.__matchActivity1Image = randomImageContent
                        if randomGroup == 1:
                            self.__matchActivity2Image = randomImageContent
                        if randomGroup == 2:
                            self.__matchActivity3Image = randomImageContent
                        
                        # - Recreation
                        randomImageId = randrange(3)
                        if randomImageId == 0:
                            randomImageContent = ResourceController.game_Recreation_Atletismo
                        if randomImageId == 1:
                            randomImageContent = ResourceController.game_Recreation_Basketball
                        if randomImageId == 2:
                            randomImageContent = ResourceController.game_Recreation_Deportes

                        if randomGroup == 0:
                            self.__matchActivity2Image = randomImageContent
                        if randomGroup == 1:
                            self.__matchActivity3Image = randomImageContent
                        if randomGroup == 2:
                            self.__matchActivity1Image = randomImageContent
                            
                        # - Social
                        randomImageId = randrange(4)
                        if randomImageId == 0:
                            randomImageContent = ResourceController.game_Social_Anciano
                        if randomImageId == 1:
                            randomImageContent = ResourceController.game_Social_Arena
                        if randomImageId == 2:
                            randomImageContent = ResourceController.game_Social_Floristeria
                        if randomImageId == 3:
                            randomImageContent = ResourceController.game_Social_Jovenes
                            
                        if randomGroup == 0:
                            self.__matchActivity3Image = randomImageContent
                        if randomGroup == 1:
                            self.__matchActivity1Image = randomImageContent
                        if randomGroup == 2:
                            self.__matchActivity2Image = randomImageContent
                             
                        # TODO
                    
                    else:
                        # Se destapo un par de cartas normal
                        AudioController.playSound(eSound.PAIR_CORRECT, 1)
                
                # Reset
                self.__firstCardShowed = None
                self.__secondCardShowed = None
                    
            # Las cartas NO corresponden a la misma actividad        
            else:  
                self.__state = eBoardState.CAN_NOT_PICK
                AudioController.playSound(eSound.OPEN_CARD, 1)
            
    def __unlockTurn(self):
        
        if self.__state == eBoardState.CAN_NOT_PICK:
            
            # Dado que las cartas no corresponden a la misma actividad, las volvemos a ocultar
            self.__firstCardShowed.flipToHide()
            self.__secondCardShowed.flipToHide()            
            
            # Reset
            self.__firstCardShowed = None
            self.__secondCardShowed = None
            
            self.__state = eBoardState.CAN_PICK_FIRST_CARD            

    def __updateClock(self):
        
        # Si aun es valido contar el tiempo
        if (self.__state != eBoardState.LEVEL_FINISHED) and (self.__state != eBoardState.TIME_OUT) and (self.__state != eBoardState.COMODIN):
        
            # Determinamos si ya paso un segundo
            if self.__currentIteration < 3:
                self.__currentIteration = self.__currentIteration + 1
            else:
                self.__currentIteration = 0
                
                if (self.__seconds == 0) and (self.__minutes == 0):
                    self.__textTime.setText("--- : ---")
                    self.__textTime.setColor((255, 0, 0))
                    self.__state = eBoardState.TIME_OUT
                    
                    # Reproducimos el audio correspondiente
                    AudioController.stopMusic()
                    AudioController.playSound(eSound.TIME_OUT, 1)
                    
                else:
                    # Disminuimos el tiempo en un segundo
                    self.__seconds = self.__seconds - 1
                    
                    # Si dicha disminucion implica un cambio de los minutos
                    if self.__seconds < 0:
                        self.__minutes = self.__minutes - 1
                        self.__seconds = 59
                        
                    # Le ponemos el cero a los numeros entre 0 y 9
                    if self.__seconds > 9:
                        strSeconds = str(self.__seconds)
                    else:
                        strSeconds = "0" + str(self.__seconds)
                        
                    if self.__minutes > 9:
                        strMinutes = str(self.__minutes)
                    else:
                        strMinutes = "0" + str(self.__minutes)
                        
                    # Actualizamos el texto a mostrar
                    self.__textTime.setText(strMinutes + " : " + strSeconds)
        
    def __checkAnswer(self, selectedAnswer):
                    
        # Ocultamos los botones para elegir respuesta
        self.__answerButtonA = False
        self.__answerButtonB = False
        self.__answerButtonC = False
        
        # Guardamos la informacion sobre la respuesta seleccionada
        self.__selectedAnswer = selectedAnswer
        
        # Determinamos si se eligio la respuesta correcta
        if self.__selectedAnswer == self.__correctAnswer:

            # Sumamos 3 estrellas por haber elegido la respuesta correcta
            self.__stars = self.__stars + self.__starsToWin
            self.__textStars.setText("x " + str(self.__stars))
            
            self.__isSelectedAnswerRight = True
            
            # Reproducimos el sonido correspondiente
            AudioController.stopSounds()
            AudioController.playSound(eSound.BOARD_COMPLETE, 1)
            
        else:
            self.__isSelectedAnswerRight = False
            
            # Reproducimos el sonido correspondiente
            AudioController.stopSounds()
            AudioController.playSound(eSound.PAIR_INCORRECT, 1)


class Label:
 
    def __init__(self, text, fontAndSize, color, positionXY):
        self.text = text
        self.__font = fontAndSize
        self.__color = color
        self.__positionXY = positionXY
 
    def doPaint(self, displaySurface):
        if self.text != "":
            renderedText = self.__font.render(self.text, 1, self.__color)
            displaySurface.blit(renderedText, (self.__positionXY[0], self.__positionXY[1]))

    def setText(self, newText):
        self.text = newText
        
    def setColor(self, newColor):
        self.__color = newColor
        
    def setPosition(self, positionXY):
        self.__positionXY = positionXY
        
    def getPosition(self):
        return self.__positionXY
        
    def addChar(self, charToAdd):
        self.text = self.text + charToAdd
        
    def delLastChar(self):
        if len(self.text) > 0:
            self.text = self.text[:len(self.text) - 1]        
        
    def getTextLen(self):
        return len(self.text)
    
    def getTextRenderLen(self):
        return self.__font.size(self.text)[0]

        
class TextBox:

    def __init__(self, posX, posY, width, maxChars, font, isPassword):
        
        self.__posX = posX
        self.__posY = posY
        
        self.__focusBorderColor = (255, 255, 0)
        self.__normalBorderColor = (48, 116, 135)
        self.__contentColor = (147, 212, 192)
        self.__textColor = (38, 95, 110)
        
        self.__textReal = Label("", font, self.__textColor, (posX, posY))
        self.__textPassword = Label("", font, self.__textColor, (posX, posY))
        
        self.__maxChars = maxChars
        self.__focus = False
        self.__uppercase = False
        self.__isPassword = isPassword
        
        if font == FontController.font10:
            fontValue = 10
        elif font == FontController.font15:
            fontValue = 15
        elif font == FontController.font20:
            fontValue = 20
        elif font == FontController.font25:
            fontValue = 25
        elif font == FontController.font27:
            fontValue = 27
        elif font == FontController.font30:
            fontValue = 30
        elif font == FontController.font35:
            fontValue = 35
        elif font == FontController.font40:
            fontValue = 40
            
        self.__height = fontValue * 1.5
        self.__width = width
        
        self.__normalBorderWidth = 4
        self.__focusBorderWidth = self.__normalBorderWidth * 2
        
    def getText(self):
        return self.__textReal.text
        
    def doTask(self):
        pass
    
    def doPaint(self, displaySurface):
        
        # Borde de Foco
        if self.__focus == True:
            pygame.draw.rect(displaySurface, self.__focusBorderColor, pygame.Rect(self.__posX - self.__focusBorderWidth, self.__posY - self.__focusBorderWidth, self.__width + (self.__focusBorderWidth * 2), self.__height + (self.__focusBorderWidth * 2)))
        
        # Borde
        pygame.draw.rect(displaySurface, self.__normalBorderColor, pygame.Rect(self.__posX - self.__normalBorderWidth, self.__posY - self.__normalBorderWidth, self.__width + (self.__normalBorderWidth * 2), self.__height + (self.__normalBorderWidth * 2)))
        
        # Contenido
        pygame.draw.rect(displaySurface, self.__contentColor, pygame.Rect(self.__posX, self.__posY, self.__width, self.__height))
        
        # Texto ingresado
        if self.__isPassword == False:
            self.__textReal.doPaint(displaySurface)
        else:
            self.__textPassword.doPaint(displaySurface)
            
    def takeFocus(self):
        self.__focus = True
    
    def quitFocus(self):
        self.__focus = False

    def doMouseAction(self, event):
        
        # Detectamos la posicion en X y Y del click
        xPos, yPos = event.pos
        
        if (xPos >= self.__posX) and (xPos <= self.__posX + self.__width) and (yPos >= self.__posY) and (yPos <= self.__posY + self.__height):
            self.__focus = True
        else:
            self.__focus = False

    def doKeyAction(self, event):
        if self.__focus == True:

            # Teclas no permitidas                
            if event.key == pygame.K_TAB:
                pass
            elif event.key == pygame.K_CAPSLOCK:
                pass
            elif event.key == pygame.K_RETURN:
                pass
            
            # Eliminacion de un caracter
            elif event.key == pygame.K_BACKSPACE:
                self.__textReal.delLastChar()
                self.__textPassword.delLastChar()
                
            # Letra valida presionada
            elif event.key <= 255 and (self.__textReal.getTextLen() < self.__maxChars):
                
                # Obtenemos la letra
                charToAdd = chr(event.key)
                
                # Mayusculas
                if self.__uppercase == True:
                    charToAdd = charToAdd.upper()
                    # self.__uppercase = False
                
                # Añadimos la letra a la cadena
                self.__textReal.addChar(charToAdd)
                self.__textPassword.addChar("*")
                
    def switchCase(self):
        if self.__uppercase == True:
            self.__uppercase = False
        else:
            self.__uppercase = True
