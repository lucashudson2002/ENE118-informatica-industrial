from kivy.uix.popup import Popup
from kivy.uix.label import Label
from kivy_garden.graph import LinePlot
from kivy.uix.boxlayout import BoxLayout

class ModbusPopup(Popup):

    _info_lb = None
    
    def __init__(self, server_ip, server_port, **kwargs): #**kwrags = key word arguments /// #scantime -> popups.kv

        super().__init__(**kwargs)
        self.ids.txt_ip.text = str(server_ip) #isso inicializa usando um texto do modbuspopup -> popups.kv
        self.ids.txt_porta.text = str(server_port) #isso inicializa usando um texto do modbuspopup -> popups.kv

    def setInfo(self, message): #crio uma mensagem no modbuspopup e uso para informar problemas de conexão
                                #mainmidget #48
        self._info_lb = Label(text=message)
        self.ids.layout.add_widget(self._info_lb)

    def clearInfo(self):

        if self._info_lb is not None:   
            self.ids.layout.remove_widget(self._info_lb)

class ScanPopup(Popup):
    
    def __init__(self, scantime, **kwargs): #**kwrags = key word arguments /// #scantime -> popups.kv

        super().__init__(**kwargs)
        self.ids.txt_st.text = str(scantime) #isso inicializa usando um texto do scanpopup -> popups.kv
        
class MotorPopup(Popup):
    def __init__(self, sendData, readData, **kwargs):
        super().__init__(**kwargs)
        self.sendData = sendData
        self.readData = readData
        
    def on_slider_freq(self, instance, value):
        if(self.ids.txt_motor.text == 'ATV31'):
            self.ids.txt_freq.text = str(int(value))
        else:
            self.ids.slider_freq.value = '60'
    
    def on_input_freq(self, instance, value):
        if(self.ids.txt_motor.text == 'ATV31'):
            if (value == ''):
                value = 0
            value = float(value)
            if (value < 0):
                value = 0
            elif (value > 60):
                value = 60
            self.ids.txt_freq.text = str(int(value))
            self.ids.slider_freq.value = str(value)
            self.sendData(1313, value*10)
        else:
            self.ids.txt_freq.text = '60'
            
    def on_list_change(self, instance, value):
        if (value == 'Encoder'):
            self.sendData(1420, 0)
        elif (value == 'Torque Axial'):
            self.sendData(1420, 2)
        elif (value == 'Torque Radial'):
            self.sendData(1420, 1)
            
    def sel_ventilador_btn(self, instance, action):
        if (action == 'Liga'):
            if (self.ids.txt_motor.text == 'Tesys'):
                self.sendData(1319, 1)
            elif (self.ids.txt_motor.text == 'ATV31'):
                self.sendData(1312, 1)
            elif (self.ids.txt_motor.text == 'ATS48'):
                self.sendData(1316, 1)
        elif (action == 'Desliga'):
            if (self.ids.txt_motor.text == 'Tesys'):
                self.sendData(1319, 0)
            elif (self.ids.txt_motor.text == 'ATV31'):
                self.sendData(1312, 0)
            elif (self.ids.txt_motor.text == 'ATS48'):
                self.sendData(1316, 0)
        elif (action == 'Reset'):
            if (self.ids.txt_motor.text == 'Tesys'):
                self.sendData(1319, 2)
            elif (self.ids.txt_motor.text == 'ATV31'):
                self.sendData(1312, 2)
            elif (self.ids.txt_motor.text == 'ATS48'):
                self.sendData(1316, 2)
    
    def sel_partida(self, instance, partida):
        if (partida == 'Tesys'):
            self.sendData(1324, 3)
            self.ids.txt_motor.text = 'Tesys'
            freq = 60
        elif (partida == 'ATV31'):
            self.sendData(1324, 2)
            self.ids.txt_motor.text = 'ATV31'
            try:
                freq = int(self.readData(1313)[0]/10)
            except Exception as e:
                print("Erro1: ",e.args)
                return
        elif (partida == 'ATS48'):
            self.sendData(1324, 1)
            self.ids.txt_motor.text = 'ATS48'
            freq = 60
        self.ids.slider_freq.value = str(freq)
        self.ids.txt_freq.text = str(freq)
        
    def set_accel(self, instance, value):
        try:
            if ('\n' in value):
                value = int(value)
                if (value < 10):
                    value = 10
                elif (value > 60):
                    value = 60

                if (self.ids.txt_motor.text == 'Tesys'):
                    value = 0
                elif (self.ids.txt_motor.text == 'ATV31'):
                    self.sendData(1314, value*10)
                elif (self.ids.txt_motor.text == 'ATS48'):
                    self.sendData(1317, value)
                    
                self.ids.txt_acc.text = str(int(value))
        except Exception as e:
            print("Erro2: ",e.args)
            return
            
    def set_desaccel(self, instance, value):
        try:
            if ('\n' in value):
                value = int(value)
                if (value < 10):
                    value = 10
                elif (value > 60):
                    value = 60
            
                if (self.ids.txt_motor.text == 'Tesys'):
                    value = 0
                elif (self.ids.txt_motor.text == 'ATV31'):
                    self.sendData(1315, value*10)
                elif (self.ids.txt_motor.text == 'ATS48'):
                    self.sendData(1318, value)
                    
                self.ids.txt_dcc.text = str(int(value))
        except Exception as e:
            print("Erro3: ",e.args)
            return
        
    def sel_ventilador_checkbox(self, instance, sel):
        if (sel == 'axial' and not self.ids.sel_axial.active):
            return
        if (sel == 'radial' and not self.ids.sel_radial.active):
            return
        try:
            tag_1328 = self.readData(1328)[0]
        except Exception as e:
            print("Erro4: ",e.args)
            return
        tag_1328 = [str(i) for i in list('{0:08b}'.format(tag_1328))]
        if (sel == 'axial'):
            tag_1328[7-2] = '1'
        elif (sel == 'radial'):
            tag_1328[7-2] = '0'
        tag_1328 = ''.join(tag_1328)
        tag_1328 = int(tag_1328, 2)
        self.sendData(1328, tag_1328)
    
    def sel_motor_checkbox(self, instance, sel):
        if (sel == 'rendimento' and not self.ids.sel_rendimento.active):
            return
        if (sel == 'convencional' and not self.ids.sel_convencional.active):
            return
        try:
            tag_1328 = self.readData(1328)[0]
        except Exception as e:
            print("Erro5: ",e.args)
            return
        tag_1328 = [str(i) for i in list('{0:08b}'.format(tag_1328))]
        if (sel == 'rendimento' and self.ids.sel_rendimento.active):
            tag_1328[7-5] = '0'
        elif (sel == 'convencional' and self.ids.sel_convencional.active):
            tag_1328[7-5] = '1'
        tag_1328 = ''.join(tag_1328)
        tag_1328 = int(tag_1328, 2)
        self.sendData(1328, tag_1328)
    
class CoPopup(Popup):
    def __init__(self, sendData, readData, **kwargs):
        super().__init__(**kwargs)
        self.sendData = sendData
        self.readData = readData
    
    def sel_compressor_checkbox(self, instance, sel):
        if (sel == 'scroll' and not self.ids.sel_scroll.active):
            return
        if (sel == 'hermetico' and not self.ids.sel_hermetico.active):
            return
        try:
            tag_1328 = self.readData(1328)[0]
        except Exception as e:
            print("Erro6: ",e.args)
            return
        tag_1328 = [str(i) for i in list('{0:08b}'.format(tag_1328))]
        if (sel == 'scroll'):
            tag_1328[7-1] = '0'
        elif (sel == 'hermetico'):
            tag_1328[7-1] = '1'
            self.ids.slider_freq.value = '60'
            self.ids.lb_freq.text = '60'
        tag_1328 = ''.join(tag_1328)
        tag_1328 = int(tag_1328, 2)
        self.sendData(1328, tag_1328)
    
    def btn_compressor(self, instance, action):
        if (action == 'Liga'):
            try:
                tag_1328 = self.readData(1328)[0]
            except Exception as e:
                print("Erro7: ",e.args)
                return
            tag_1328 = [str(i) for i in list('{0:08b}'.format(tag_1328))]
            if (self.ids.sel_scroll.active):
                tag_1328[7-4] = '1'
            elif (self.ids.sel_hermetico.active):
                tag_1328[7-4] = '1'
            tag_1328 = ''.join(tag_1328)
            tag_1328 = int(tag_1328, 2)
            self.sendData(1328, tag_1328)
        elif (action == 'Desliga'):
            try:
                tag_1329 = self.readData(1329)[0]
            except Exception as e:
                print("Erro8: ",e.args)
                return
            tag_1329 = [str(i) for i in list('{0:08b}'.format(tag_1329))]
            if (self.ids.sel_scroll.active):
                tag_1329[7-0] = '0'
            elif (self.ids.sel_hermetico.active):
                tag_1329[7-0] = '0'
            tag_1329 = ''.join(tag_1329)
            tag_1329 = int(tag_1329, 2)
            self.sendData(1329, tag_1329)
    
    def btn_umidificador(self, instance, action):
        try:
            tag_1329 = self.readData(1329)[0]
        except Exception as e:
            print("Erro9: ",e.args)
            return
        tag_1329 = [str(i) for i in list('{0:08b}'.format(tag_1329))]
        if (action == 'Liga'):
            tag_1329[7-2] = '1'
            tag_1329[7-3] = '0'
        elif (action == 'Desliga'):
            tag_1329[7-2] = '0'
            tag_1329[7-3] = '1'
        tag_1329 = ''.join(tag_1329)
        tag_1329 = int(tag_1329, 2)
        self.sendData(1329, tag_1329)
    
    def btn_aquecedor1(self, instance, action):
        try:
            tag_1329 = self.readData(1329)[0]
        except Exception as e:
            print("Erro10: ",e.args)
            return
        tag_1329 = [str(i) for i in list('{0:08b}'.format(tag_1329))]
        if (action == 'Liga'):
            tag_1329[7-4] = '1'
            tag_1329[7-5] = '0'
        elif (action == 'Desliga'):
            tag_1329[7-4] = '0'
            tag_1329[7-5] = '1'
        tag_1329 = ''.join(tag_1329)
        tag_1329 = int(tag_1329, 2)
        self.sendData(1329, tag_1329)
    
    def btn_aquecedor2(self, instance, action):
        try:
            tag_1329 = self.readData(1329)[0]
        except Exception as e:
            print("Erro11: ",e.args)
            return
        tag_1329 = [str(i) for i in list('{0:08b}'.format(tag_1329))]
        if (action == 'Liga'):
            tag_1329[7-6] = '1'
            tag_1329[7-7] = '0'
        elif (action == 'Desliga'):
            tag_1329[7-6] = '0'
            tag_1329[7-7] = '1'
        tag_1329 = ''.join(tag_1329)
        tag_1329 = int(tag_1329, 2)
        self.sendData(1329, tag_1329)
    
    def set_termostato(self, instance, value):
        try:
            if ('\n' in value):
                value = float(value)
                if (value < 18):
                    value = 18.0
                elif (value > 30):
                    value = 30.0

                self.sendData(1338, value)
                self.ids.txt_termostato.text = str(value)
        except Exception as e:
            print("Erro12: ",e.args)
            return
    
    def on_slider_freq(self, instance, value):
        if(self.ids.sel_scroll.active):
            self.ids.lb_freq.text = str(int(value))
            self.sendData(1236, value)
        else:
            self.ids.slider_freq.value = '60'
            self.ids.lb_freq.text = '60'
            
    def btn_auto_man(self, instance, action):
        try:
            tag_1328 = self.readData(1328)[0]
        except Exception as e:
            print("Erro13: ",e.args)
            return
        tag_1328 = [str(i) for i in list('{0:08b}'.format(tag_1328))]
        if (action == 'Man'):
            tag_1328[7-3] = '0'
            self.ids.lb_man_sel.text = 'MAN\nSEL.'
        elif (action == 'Auto'):
            tag_1328[7-3] = '1'
            self.ids.lb_man_sel.text = 'AUTO\nSEL.'
        tag_1328 = ''.join(tag_1328)
        tag_1328 = int(tag_1328, 2)
        self.sendData(1328, tag_1328)

class DataGraphPopup(Popup): #popup do gráfico
    def __init__(self, xmax, plot_color, **kwargs):
        super().__init__(**kwargs)
        self.plot = LinePlot(line_width =1.5, color= plot_color)
        self.ids.graph.add_plot(self.plot)
        self.ids.graph.xmax = xmax

class LabelCheckBoxDataGraph(BoxLayout):
    pass

class HistGraphPopup(Popup):
    def __init__(self, **kwargs):
        super().__init__()
        for key,value in kwargs.get('tags').items():
            cb = LabelCheckBoxHistGraph()
            cb.ids.label.text = key
            cb.ids.label.color = value['color']
            cb.id = key
            self.ids.variaveis.add_widget(cb)
            
class LabelCheckBoxHistGraph(BoxLayout):
    pass