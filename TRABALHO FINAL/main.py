from kivy.app import App
from mainwidget import MainWidget
from kivy.lang.builder import Builder

class MainApp(App):

    def build(self):

        #self._widget = MainWidget(scan_time = 1000, server_ip = '192.168.0.12', server_port = 502, #defino o ip do servidor e a porta aqui
        self._widget = MainWidget(scan_time = 1000, server_ip = '10.15.20.17', server_port = 10012, #defino o ip do servidor e a porta aqui
        modbus_info = {
            'encoder': {'addr': 884, 'type': 'FP', 'div': 1, 'unit': 'RPM'},
            'tit02': {'addr': 1218, 'type': 'FP', 'div': 10, 'unit': 'ºC'},
            'tit01': {'addr': 1220, 'type': 'FP', 'div': 10, 'unit': 'ºC'},
            'pit02': {'addr': 1222, 'type': 'FP', 'div': 10, 'unit': 'PSI'},
            'pit01': {'addr': 1224, 'type': 'FP', 'div': 10, 'unit': 'PSI'},
            'pit03': {'addr': 1226, 'type': 'FP', 'div': 10, 'unit': 'PSI'},
            'temperatura': {'addr': 710, 'type': 'FP', 'div': 1, 'unit': 'ºC'},
            'velocidade': {'addr': 712, 'type': 'FP', 'div': 1, 'unit': 'm/s'},
            'vazao': {'addr': 714, 'type': 'FP', 'div': 1, 'unit': 'm³/h'},
            'ativa_total': {'addr': 855, 'type': '4X', 'div': 1, 'unit': 'W'},
            'reativa_total': {'addr': 859, 'type': '4X', 'div': 1, 'unit': 'VAr'},
            'aparente_total': {'addr': 863, 'type': '4X', 'div': 1, 'unit': 'VA'},
        }, db_path = 'C:\\Users\\Luís Eduardo\\Documents\\trabalho final de inf ind\\TRABALHO FINAL\\db\\scada.db'
        )
        
        return self._widget
    
    def on_stop(self):
        self._widget.stopRefresh() 
    
if __name__=='__main__':
    Builder.load_string(open("mainwidget.kv", encoding="utf-8").read(), rulesonly=True)
    Builder.load_string(open("popups.kv", encoding="utf-8").read(), rulesonly=True)
    MainApp().run()
