from kivy.uix.boxlayout import BoxLayout
from popups import ModbusPopup, ScanPopup, MotorPopup, CoPopup, DataGraphPopup, HistGraphPopup
from pyModbusTCP.client import ModbusClient
from kivy.core.window import Window
from threading import Thread, Lock
from time import sleep
from datetime import datetime
import random
from pymodbus.payload import BinaryPayloadBuilder, BinaryPayloadDecoder
from pymodbus.constants import Endian
from timeseriesgraph import TimeSeriesGraph
from bdhandler import BDHandler
from kivy_garden.graph import LinePlot
from kivy.clock import Clock

class MainWidget(BoxLayout):
    
    _updateThread = None
    _updateWidgets = True
    _tags = {}
    _max_points = 20 #maximo de pontos visiveis no eixo x do grafico

    def __init__(self, **kwargs):

        super().__init__()

        self._scan_time = kwargs.get('scan_time')
        #configurando o servidor Modbus
        self._serverIP = kwargs.get('server_ip')
        self._serverPort = kwargs.get('server_port')
        
        self._modbusPopup = ModbusPopup(self._serverIP, self._serverPort) #tem que relacionar com o botão no arquivo kivy para abrir o Popup
        self._scanPopup = ScanPopup(self._scan_time) #também tem
        self._motorPopup = MotorPopup(sendData = self.sendData, readData = self.readDataPopup)
        self._coPopup = CoPopup(sendData = self.sendData, readData = self.readDataPopup)

        #criando o cliente Modbus
        self._modbusClient = ModbusClient(host=self._serverIP, port=self._serverPort)
        
        #atributo para a leitura de dados
        self._meas = {}
        self._meas['timestamp'] = None
        self._meas['values'] = {}

        for key,value in kwargs.get('modbus_info').items():
            plot_color = (random.random(), random.random(), random.random(), 1)
            self._tags[key] = {'addr': value['addr'], 'color': plot_color, 'type': value['type'], 'div': value['div'], 'unit': value['unit']}

        self._graph = DataGraphPopup(self._max_points, self._tags['encoder']['color'])
        self._hgraph = HistGraphPopup(tags = self._tags)
        self._db = BDHandler(kwargs.get('db_path'), self._tags)
        
        self._lock = Lock()

    def startDataRead(self, ip, port): #tenho que ir no kivy do popups e relacionar um botão com esse método para conectar

        """
        configuração do ip e porta do servidor modbus e inicializa uma thread para a leitura dos dados
        e atualização da interface gráfica
        """
        self._serverIP = ip
        self._serverPort = port
        self._modbusClient.host = self._serverIP
        self._modbusClient.port = self._serverPort

        try:
            Window.set_system_cursor("wait") #tento abrir o cliente, altero o mouse na tela
            self._modbusClient.open()
            Window.set_system_cursor("arrow")

            if self._modbusClient.is_open: #se o cliente abrir, crio uma thread
                
                self._updatePopup()
                #self.chama_update_image()
                
                self._updateThread = Thread(target=self.updater) #crio uma thread secundaria para melhorar a responsividade do programa
                self._updateThread.start()
                self.ids.img_con.source = 'imgs/conectado.png' #a imagem de conexão será alterada
                self._modbusPopup.dismiss() #fecho o Popup
            else:
                self._modbusPopup.setInfo("Falha na conexão com o servidor")
        
        except Exception as e:
            print("Erro: ",e.args)
        
    def updater(self):
        """
        leitura de dados, atualização de interface, inserção de dados no Banco de dados
        """
        try:
            while self._updateWidgets:
                #ler dos dados MODBUS
                with self._lock:
                    self.readData()
                #atualizar a interface
                self.updateGUI()
                #inserir os dados no BD
                self._db.insertData(self._meas)
                
                sleep(self._scan_time/1000)
        except Exception as e:
            self._modbusClient.close()
            print("Erro: ", e)
    
    def readData(self):
        """
        Leitura dos 12 dados por meio do MODBUS
        """
        self._meas['timestamp'] = datetime.now()
        for key, value in self._tags.items():
            if (value['type']) == '4X':
                self._meas['values'][key] = self._modbusClient.read_holding_registers(value['addr'],1)[0]/value['div']
            elif (value['type']) == 'FP':
                leitura = self._modbusClient.read_holding_registers(value['addr'], 2)
                decoder = BinaryPayloadDecoder.fromRegisters(leitura, byteorder=Endian.Big, wordorder=Endian.Little)
                self._meas['values'][key] = decoder.decode_32bit_float()/value['div']
            self._meas['values'][key] = float(f"{self._meas['values'][key]:.1f}")
            
    def updateGUI(self):
        """
        atualização da interface grafica a partir dos dados lidos
        """
        for key, value in self._tags.items(): #atualização dos valores lidos
            self.ids[key].text = str(self._meas['values'][key])

        self.chama_update_image()

        self._graph.ids.graph.updateGraph((self._meas['timestamp'], self._meas['values']['temperatura']),0)
        
    def sendData(self, addr, value):
        with self._lock:
            self._modbusClient.write_single_register(addr, int(value))
        
    def readDataPopup(self, addr):
        with self._lock:
            return self._modbusClient.read_holding_registers(addr, 1)
    
    def _updatePopup(self):
        # atualiza valores da interface do motor
        try:
            self_driver = self.readDataPopup(1324)[0]
            if (self_driver == 1):
                self._motorPopup.ids.txt_motor.text = 'ATS48'
                self._motorPopup.ids.txt_acc.text = str(int(self.readDataPopup(1317)[0]))
                self._motorPopup.ids.txt_dcc.text = str(int(self.readDataPopup(1318)[0]))
            elif (self_driver == 2):
                self._motorPopup.ids.txt_motor.text = 'ATV31'
                self._motorPopup.ids.txt_acc.text = str(int(self.readDataPopup(1314)[0]/10))
                self._motorPopup.ids.txt_dcc.text = str(int(self.readDataPopup(1315)[0]/10))
            elif (self_driver == 3):
                self._motorPopup.ids.txt_motor.text = 'Tesys'
            
            self._motorPopup.ids.txt_freq.text = str(self.readDataPopup(1313)[0]/10)
            
            tag_1328 = self.readDataPopup(1328)[0]
            tag_1328 = [int(i) for i in list('{0:08b}'.format(tag_1328))]
            
            self._motorPopup.ids.sel_axial.active = tag_1328[7-2]
            self._motorPopup.ids.sel_radial.active = not tag_1328[7-2]
            self._motorPopup.ids.sel_convencional.active = tag_1328[7-5]
            self._motorPopup.ids.sel_rendimento.active = not tag_1328[7-5]            
            
            comutacao = self.readDataPopup(1420)[0]
            if (comutacao == 0):
                self._motorPopup.ids.sel_opcao.text = 'Encoder'
            if (comutacao == 2):
                self._motorPopup.ids.sel_opcao.text = 'Torque Axial'
            if (comutacao == 1):
                self._motorPopup.ids.sel_opcao.text = 'Torque Radial'
            
            # atualiza valores da interface do compressor
            self._coPopup.ids.sel_scroll.active = not tag_1328[7-1]
            self._coPopup.ids.sel_hermetico.active = tag_1328[7-1]
            
            self._coPopup.ids.txt_termostato.text = str(self.readDataPopup(1338)[0])
            
            #self._coPopup.ids.lb_freq.text = str(self._modbusClient.read_holding_registers(1236,1)[0])
            self._coPopup.ids.slider_freq.value = str(self.readDataPopup(1236)[0])
            
            if (tag_1328[7-3] == 0):
                self._coPopup.ids.lb_man_sel.text = 'MAN\nSEL.'
            elif (tag_1328[7-3] == 1):
                self._coPopup.ids.lb_man_sel.text = 'AUTO\nSEL.'
            
        except Exception as e:
            print("Erro: ", e)
            #self._updatePopup()

    def stopRefresh(self):
        self._updateWidgets = False
        
    def getDataDB(self):
        try:
            init_t = self.parseDTString(self._hgraph.ids.txt_init_time.text)
            final_t = self.parseDTString(self._hgraph.ids.txt_final_time.text)
            cols = []
            for var in self._hgraph.ids.variaveis.children:
                if var.ids.checkbox.active:
                    cols.append(var.id)
                    
            if init_t is None or final_t is None or len(cols)==0:
                return
            
            cols.append('timestamp')
            
            dados = self._db.selectData(cols, init_t, final_t)
            
            if dados is None or len(dados['timestamp']) == 0:
                return
            
            self._hgraph.ids.graph.clearPlots()
            
            for key, value in dados.items():
                if key == 'timestamp':
                    continue
                p = LinePlot(line_width=1.5, color = self._tags[key]['color'])
                p.points = [(x, value[x]) for x in range(0, len(value))]
                self._hgraph.ids.graph.add_plot(p)
            self._hgraph.ids.graph.xmax = len(dados[cols[0]])
            self._hgraph.ids.graph.update_x_labels([datetime.strptime(x, "%Y-%m-%d %H:%M:%S.%f") for x in dados['timestamp']])
            
        except Exception as e:
            print("Erro!!!: ", e.args)
            
    def parseDTString(self, datetime_str):
        try:
            d = datetime.strptime(datetime_str, '%d/%m/%Y %H:%M:%S')
            return d.strftime("%Y-%m-%d %H:%M:%S")
        except Exception as e:
            print("Erro: ", e.args)

    def chama_update_image(self):
        try:
            sleep(0.1)

            valor= 0
            
            condicao = float(f"{self._meas['values']['encoder']:.1f}")

            if condicao == 0:
                cond_motor = 0
            elif condicao != 0:
                cond_motor = 1
            
            tipo_motor = (self._modbusClient.read_holding_registers(708,1))[0]

            if tipo_motor == 1 and cond_motor == 0:
                valor = 0
            if tipo_motor == 2 and cond_motor == 0:
                valor = 1
            if tipo_motor == 1 and cond_motor == 1:
                valor = 2
            elif tipo_motor == 2 and cond_motor == 1:
                valor = 3

            self.tipo_imagem_fundo = valor
            Clock.schedule_once(self.update_menu_image)
        except Exception as e:
            print("Erro (mainwidget.py, chama_update() ),", e.args)

    def update_menu_image(self,dt):
        if self.tipo_imagem_fundo== 0:
            self.ids.img_inicial.source = "imgs/rendimento_selecionado.png"
        if self.tipo_imagem_fundo== 1:
            self.ids.img_inicial.source = "imgs/convencional_selecionado.png"
        if self.tipo_imagem_fundo== 2:
            self.ids.img_inicial.source = "imgs/rendimento_ativo.png"
        if self.tipo_imagem_fundo== 3:
            self.ids.img_inicial.source = "imgs/convencional_ativo.png"