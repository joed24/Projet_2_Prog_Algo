# Tp_Algo_Programmation

with open('cdr.txt', 'r') as cdr_file:
    cdr_content = cdr_file.read()

with open('both.txt', 'w') as both_file:
    both_file.write(cdr_content)

with open('tp_algo.txt', 'r') as tp_algo_file:
    tp_algo_content = tp_algo_file.read()

with open('both.txt', 'a') as both_file:
    both_file.write(tp_algo_content)


class Client:
    def __init__(self, nom, date_de_naissance, numero, facture):
        self.nom = nom
        self.date_de_naissance = date_de_naissance
        self.numero = numero
        self.facture = facture

    def gerer_client(self):
        if len(self.numero) != 12 or self.numero[0:3] != "243" or self.numero[3:5] != "80" or self.numero[3:5] != "89" or self.numero[3:5] != "81" or self.numero[3:5] != "83" or self.numero[3:5] != "82" or self.numero[3:5] != "85" or self.numero[3:5] != "84" or self.numero[3:5] != "90" or self.numero[3:5] != "91" or self.numero[3:5] != "99" or self.numero[3:5] != "97" or self.numero[3:5] != "98":
            return "votre numero n'est pas correct"
        else:
            dictionnaire_client = {"nom": self.nom,
                                   "date_de_naissance": self.date_de_naissance,
                                   "numero": self.numero,
                                   "facture": self.facture
                                   }
            return dictionnaire_client


class ImporterCDR(Client):
    def __init__(self, nom_ficher):
        self.nom_ficher = open(nom_ficher).readlines()
        # print(self.nom_ficher)

    def importer(self):
        self.importe = []
        for line in self.nom_ficher:
            lin = line.rstrip('\n').split('|')
            self.importe.append(lin)
        return self.importe

    def pile_de_dictionnaire(self):
        self.pile_dictionnaire = []
        for x in self.importer():
            self.dictio = { "identifiant de l\'appel" : x[0],
                           "type call" : x[1],
                           "date et heure" : x[2],
                           "appelant" : x[3],
                           "appele" : x[4],
                           "duree" : x[5],
                           "taxe" : x[6],
                           "totalVolume" : x[7]}
            self.pile_dictionnaire.append(self.dictio)
        return self.pile_dictionnaire

class Facture(ImporterCDR):
    def __init__(self, nom_ficher):
        ImporterCDR.__init__(self, nom_ficher)
        
        self.sms = []
        for x in self.importer():
            if x[1] == '1':
                self.sms.append(x)
        
        self.appel = []
        for x in self.importer():
            if x[1] == '0':
                self.appel.append(x)
        
        self.internet = []
        for x in self.importer():
            if x[1] == '2':
                self.internet.append(x)
        
        self.cout_appel = []
        for x in self.appel:
            y = x[4]
            if y[3:5] == '81' or y[3:5] == '82':
                if x[6] == '0':
                    z = 1
                    w = int(x[5])/60*0.025*z
                    self.cout_appel.append(w)
                if x[6] == '1':
                    z = 1 + 10/100
                    w = int(x[5])/60*0.025*z
                    self.cout_appel.append(w)
                if x[6] == '2':
                    z = 1 + 16/100
                    w = int(x[5])/60*0.025*z
                    self.cout_appel.append(w)
            if y[3:5] != '81' or y[3:5] != '82':
                if x[6] == '0':
                    z = 1
                    w = int(x[5])/60*0.05*z
                    self.cout_appel.append(w)
                if x[6] == '1':
                    z = 1 + 10/100
                    w = int(x[5])/60*0.05*z
                    self.cout_appel.append(w)
                if x[6] == '2':
                    z = 1 + 16/100
                    w = int(x[5])/60*0.05*z
                    self.cout_appel.append(w)

        self.cout_internet = []
        for x in self.internet:
            if x[6] == '0':
                w = int(x[7])*0.03
                self.cout_internet.append(w)
            if x[6] == '1':
                z = 1 + 10/100
                w = int(x[7])*0.03*z
                self.cout_internet.append(w)
            if x[6] == '2':
                z = 1 + 16/100
                w = int(x[7])*0.03*z
                self.cout_internet.append(w)
    
        self.cout_sms = []
        for x in self.sms:
            y = x[4]
            if y[3:5] == '81' or y[3:5] == '82':
                if x[6] == '0':
                    z = 1
                    w = 0.001*z
                    self.cout_sms.append(w)
                if x[6] == '1':
                    z = 1 + 10/100
                    w = 0.001*z
                    self.cout_sms.append(w)
                if x[6] == '2':
                    z = 1 + 16/100
                    w = 0.001*z
                    self.cout_sms.append(w)
            if y[3:5] != '81' or y[3:5] != '82':
                if x[6] == '0':
                    z = 1
                    w = 0.002*z
                    self.cout_sms.append(w)
                if x[6] == '1':
                    z = 1 + 10/100
                    w = 0.002*z
                    self.cout_sms.append(w)
                if x[6] == '2':
                    z = 1 + 16/100
                    w = 0.002*z
                    self.cout_sms.append(w)
                    
        self.facture_appel = sum(self.cout_appel)
        
        self.facture_sms = sum(self.cout_sms)
        
        self.facture_internet = sum(self.cout_internet)
        
    def facture_totals(self):
        return self.facture_appel + self.facture_sms + self.facture_internet


class Statistique(Facture):
    def __init__(self, nom_ficher):
        Facture.__init__(self, nom_ficher)
        
        self.num_1 = '243818140560'
        self.num_2 = '243818140120'
        self.cdr = self.importer()
        
        self.numero_1 = []
        for x in self.cdr:
            if x[3] == self.num_1:
                self.numero_1.append(x)
        
        self.numero_2 = []
        for x in self.cdr:
            if x[3] == self.num_2:
                self.numero_2.append(x)
        
        self.sms_1 = []
        for x in self.numero_1:
            if x[1] == '1':
                self.sms_1.append(x)
        
        self.sms_2 = []
        for x in self.numero_2:
            if x[1] == '1':
                self.sms_2.append(x)
        
        self.appel_1 = []
        for x in self.numero_1:
            if x[1] == '0':
                self.appel_1.append(x)
        
        self.appel_2 = []
        for x in self.numero_2:
            if x[1] == '0':
                self.appel_2.append(x)
        
        self.internet_1 = []
        for x in self.numero_1:
            if x[1] == '2':
                self.internet_1.append(x)
        
        self.internet_2 = []
        for x in self.numero_2:
            if x[1] == '2':
                self.internet_2.append(x)
        
        self.nomnbre_appel_1 = len(self.appel_1)
        
        self.nomnbre_appel_2 = len(self.appel_2)
        
        self.dur_1 = []
        for x in self.appel_1:
            self.dur_1.append(int(x[5]))
        self.duree_1 = sum(self.dur_1)/60
        
        self.dur_2 = []
        for x in self.appel_2:
            self.dur_2.append(int(x[5]))
        self.duree_2 = sum(self.dur_2)/60
        
        self.nombre_sms_1 = len(self.sms_1)
        
        self.nombre_sms_2 = len(self.sms_2)
        
        self.cons_1 = []
        for x in self.internet_1:
            self.cons_1.append(int(x[7]))
        self.consommation_1 = sum(self.cons_1)/1024
        
        self.cons_2 = []
        for x in self.internet_2:
            self.cons_2.append(int(x[7]))
        self.consommation_2 = sum(self.cons_2)/1024
        
    def pile_numero_1(self):
        self.stat_1 = []
        dico = { "nombre d'appel": self.nomnbre_appel_1,
                "duree d'appel en minutes" : self.duree_1,
                "nombre des sms" : self.nombre_sms_1,
                "consommation internet en Gigabyte": self.consommation_1}
        self.stat_1.append(dico)
        print('statistique pour numero: ',self.num_1)
        return self.stat_1
    
    def pile_numero_2(self):
        self.stat_2 = []
        dico = { "nombre d'appel": self.nomnbre_appel_2,
                "duree d'appel en minutes" : self.duree_2,
                "nombre des sms" : self.nombre_sms_2,
                "consommation internet en Gigabyte": self.consommation_2}
        self.stat_2.append(dico)
        print('statistique pour numero: ',self.num_2)
        return self.stat_2
    
    def mois_info(self,date):
        self.date = date
        self.info_date = []
        for x in self.cdr:
            if x[2][0:6] == self.date:
                self.info_date.append(x)
        
        self.sms = []
        for x in self.info_date:
            if x[1] == '1':
                self.sms.append(x)
        
        self.appel = []
        for x in self.info_date:
            if x[1] == '0':
                self.appel.append(x)
        
        self.internet = []
        for x in self.info_date:
            if x[1] == '2':
                self.internet.append(x)
        
        self.nomnbre_appel = len(self.appel)
        
        self.dur = []
        for x in self.appel:
            self.dur.append(int(x[5]))
        self.duree_date = sum(self.dur)/60
        
        self.nombre_sms = len(self.sms)
        
        self.cons = []
        for x in self.internet:
            self.cons.append(int(x[7]))
        self.consommation = sum(self.cons)/1024
        
        self.dates = []
        dico = { "nombre d'appel": self.nomnbre_appel,
                "duree d'appel en minutes" : self.duree_date,
                "nombre des sms" : self.nombre_sms,
                "consommation internet en Gigabyte": self.consommation}
        self.dates.append(dico)
        print('statistique pour la date : ',self.date)
        return self.dates
        
            
    
    


    



      

cdr = ImporterCDR("both.txt")
print(cdr.pile_de_dictionnaire())
print('\n')

cdr = Facture("both.txt")
print('la facture est de:',cdr.facture_totals(),'USD')
print('\n')

cdr = Statistique("both.txt")
print(cdr.pile_numero_1())
print('\n')
print(cdr.pile_numero_2())
print('\n')
print(cdr.mois_info('202301'))
print('\n')















