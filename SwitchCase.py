class SentenciaSwitch:
    
    def switch(self,mes):
        default = "Mes incorrecto"
        return getattr(self,'case_' + str(mes),lambda:default)()
    
    def case_1(self):
        return "Enero"
    
    def case_2(self):
        return "Febrero"
    
    def case_3(self):
        return "Marzo"
    
    def case_4(self):
        return "Abril"
    
    def case_5(self):
        return "Mayo"
    
    def case_6(self):
        return "Junio"