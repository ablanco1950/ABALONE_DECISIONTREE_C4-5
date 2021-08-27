
import numpy as np
import math


""" CLASIFIER FUNCTION ==========================================================="""

def Abalone_C4_5(Y_train, X_Train, Y_test, X_test, W):
    
               
        Max=[float(2.0)]
        Max.append(float(0.815))
        Max.append(float(0.65))
        Max.append(float(1.13))
        Max.append(float(2.8255))
        Max.append(float(1.488))
        Max.append(float(0.76))
        Max.append(float(1.005))
        Min=[float(0.0)]
        Min.append(float(0.075))
        Min.append(float(0.055))
        Min.append(float(0.0))
        Min.append(float(0.002))
        Min.append(float(0.001))
        Min.append(float(0.0005))
        Min.append(float(0.0015))
        NumClases=3
        NumCampos =8
        TopeMemoria = 154
        
        # Got frm https://stackoverflow.com/questions/15448594/how-to-add-elements-to-3-dimensional-array-in-python
        TabVotos = np.zeros((NumCampos,TopeMemoria,NumClases))
        
        Maximo=0.0
        Conta=0.0
        Cont=-1
        
        ContClase=[float(0.0)]
        for j in range(NumClases):
             ContClase.append(float(0.0))
       
        Start=0
        End = 3133
       
    
       
        f=open("C:\\abalone-1.data ","r")
        
        
        for linea in f:
            
            lineadelTrain =linea.split(",")
            Conta = Conta + 1
            if Conta < Start:
                continue
            if Conta > End:
                break
         
            Cont = Cont +1
            if len(W) == 1:
              FactorPri=1.0
            else:
                FactorPri=W[Cont]
                
            ClaseLeida=float(lineadelTrain[8])
            
            Clase=0    
        	
            if (ClaseLeida > 10.0): 
                Clase=2
            else:
                if (ClaseLeida > 8.0): 
                		Clase=1
          
            ContClase[Clase]=ContClase[Clase] + 1
                       
            
           
            z=-1
            for x  in lineadelTrain:
                
                z=z+1
                if z==NumCampos:
                    break
              
                if z==0:
                    if lineadelTrain[0] == "M":
                      ValorTrain=0.0
                    else:
                        if lineadelTrain[0] == "F":
                           ValorTrain=1.0
                        else:
                                if lineadelTrain[0] == "I":
                                    ValorTrain=2.0
                else:
                    ValorTrain =float(lineadelTrain[z])
                ValorTrain =ValorTrain - Min[z]
                Maximo = Max[z]
                Maximo = Maximo - Min[z]
                indice =(int) (((TopeMemoria - 2.0) * ValorTrain)/ Maximo)
                if ( (indice > (TopeMemoria-2)) or  (indice < 0)):	
                    print("index overflowed=" + str( indice) + " in  the field ="+ str(z-1) )
                    indice=TopeMemoria
                Wvalor=0.0
             
                Wvalor= TabVotos[z,TopeMemoria-1,Clase]
                Wvalor= Wvalor + 1
                TabVotos[z,TopeMemoria-1,Clase]=Wvalor 
               
                Wvalor= TabVotos[z,indice,Clase]
                Wvalor=Wvalor+FactorPri
                TabVotos[z,indice,Clase]=Wvalor 
                # print("Acumula en el indice = " + str(indice) + " Clase =" + str(Clase) + " Wvalor =" + str(Wvalor))
       
        f.close()
        
       # for Campo in range(NumCampos):
        Campo=3
        
        HClase_PreguntaMin=999999999.0
        indiceMin=999999
        for i in range (TopeMemoria-2):
            
            ClasesMenos = np.zeros(NumClases)
            ClasesMas = np.zeros(NumClases)
            TotClaseMenos=0
            TotClaseMas=0
            EntroCampoMenos=0
            EntroCampoMas=0
            for y in range(i):
               
                for w in range (NumClases):
                    # print("Recupera indice = "+str(i) + "Clase= " + str(w) + "Valor = " +str(TabVotos[Campo,i,w]))
                    TotClaseMenos= TotClaseMenos + TabVotos[Campo,y,w]
                    ClasesMenos[w]=ClasesMenos[w]+ TabVotos[Campo,y,w]
            
            for j in range (NumClases):
                    if (ClasesMenos[j] != 0.0) :
                        P=ClasesMenos[j]/TotClaseMenos
                        # print("Indice =" + str(i) + " Clase= " + str(j) +  " Probabilidad Campo  "+  str(P) + "Total Clases = "+ str(TotClases))
                        EntroCampoMenos= EntroCampoMenos +  P*math.log(1.0/P,2)
            print("Entropy < indiex =" +str(i) + " field "+  str(Campo)+ " = " + str(EntroCampoMenos) )
            for y in range(i,TopeMemoria-2):
               
                for w in range (NumClases):
                    # print("Recupera indice = "+str(i) + "Clase= " + str(w) + "Valor = " +str(TabVotos[Campo,i,w]))
                    TotClaseMas= TotClaseMas + TabVotos[Campo,y,w]
                    ClasesMas[w]=ClasesMas[w]+ TabVotos[Campo,y,w]
            
            for j in range (NumClases):
                    if (ClasesMas[j] != 0.0) :
                        P=ClasesMas[j]/TotClaseMas
                        # print("Indice =" + str(i) + " Clase= " + str(j) +  " Probabilidad Campo  "+  str(P) + "Total Clases = "+ str(TotClases))
                        EntroCampoMas= EntroCampoMas +  P*math.log(1.0/P,2)
            print("Entropy > index=" +str(i) + " field "+  str(Campo)+ " = " + str(EntroCampoMas) )
            HClase_Pregunta =(TotClaseMenos/(TotClaseMenos+TotClaseMas) )*EntroCampoMenos +  (TotClaseMas/(TotClaseMenos+TotClaseMas) )*EntroCampoMas
            print("HClass_Question index =" +str(i) + " field "+  str(Campo)+ " = " + str(HClase_Pregunta) )
            if (HClase_Pregunta < HClase_PreguntaMin):
                indiceMin=i
                HClase_PreguntaMin=HClase_Pregunta
        print("Index minimum =" +str(indiceMin) + " field "+  str(Campo)+ " Class Question " + str(HClase_PreguntaMin) )
        ClasesMenos = np.zeros(NumClases)
        ClasesMas = np.zeros(NumClases)
        TotClaseMenos=0
        TotClaseMas=0
        for y in range(indiceMin+1,TopeMemoria-2):
               
                for w in range (NumClases):
                   
                    TotClaseMas= TotClaseMas + TabVotos[Campo,y,w]
                    ClasesMas[w]=ClasesMas[w]+ TabVotos[Campo,y,w]
        for y in range(indiceMin):
                
                for w in range (NumClases):
                   
                    TotClaseMenos = TotClaseMenos + TabVotos[Campo,y,w]
                    ClasesMenos[w]=ClasesMenos[w]+ TabVotos[Campo,y,w] 
        print(" " )
        print("Index Classes Values = " + str(indiceMin))
        for w in range (NumClases):
                    print("Class = " + str(w) + " in branch > "+ str( ClasesMas[w]) + " in branch < "+ str( ClasesMenos[w]))
                                                                                            
############################################################################33
# MAIN
###########################################################################333

Y_train=[float(1.0)]
X_train=[float(1.0)]
Y_test=[float(1.0)]
X_test=[float(1.0)]
W=[float(1.0)]
er_train=[float(1.0)]
er_test=[float(1.0)]
clf_tree=""
TotHits=0.0
Abalone_C4_5(Y_train, X_train, Y_test, X_test, W)

    