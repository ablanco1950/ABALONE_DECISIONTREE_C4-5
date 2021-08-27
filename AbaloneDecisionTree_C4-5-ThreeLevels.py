"""
Created on  Aug 8 2021

@author: Alfonso Blanco García
"""
import numpy as np


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
        
               
        Maximo=0.0
        Conta=0
        Cont=-1
        
        ContClase=[float(0.0)]
        for j in range(NumClases):
             ContClase.append(float(0.0))
             
         
        C0MasC7MasC4Mas =np.zeros(NumClases)
        C0MasC7MasC4Menos =np.zeros(NumClases)
        C0MasC7MenosC4Mas =np.zeros(NumClases)
        C0MasC7MenosC4Menos =np.zeros(NumClases)
        C0MenosC7MasC4Mas =np.zeros(NumClases)
        C0MenosC7MasC4Menos =np.zeros(NumClases)
        C0MenosC7MenosC4Mas =np.zeros(NumClases)
        C0MenosC7MenosC4Menos =np.zeros(NumClases)
        
        SinAsignar=np.zeros(NumClases)
        
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
            
            # W in case of receiving weights from an external adaboost
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
                       
            TabIndices = np.zeros(NumCampos)
           
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
                TabIndices[z]=indice
            if (TabIndices[0] > 1.0 ) and (TabIndices[7] > 29.0 ) and (TabIndices[4] > 33.0 ):
               C0MasC7MasC4Mas[Clase] = C0MasC7MasC4Mas[Clase] + 1.0
            if (TabIndices[0] > 1.0 ) and (TabIndices[7] > 29.0 ) and (TabIndices[4] <= 33.0 ):
                C0MasC7MasC4Menos[Clase]=  C0MasC7MasC4Menos[Clase] +1.0
            if (TabIndices[0] > 1.0 ) and (TabIndices[7] <= 29.0 ) and (TabIndices[4] > 33.0 ):
                C0MasC7MenosC4Mas[Clase] =C0MasC7MenosC4Mas[Clase] +1.0
            if (TabIndices[0] > 1.0 ) and (TabIndices[7] <= 29.0 ) and (TabIndices[4] <= 33.0 ):
                C0MasC7MenosC4Menos[Clase] =C0MasC7MenosC4Menos[Clase] +1.0
            if (TabIndices[0] <= 1.0 ) and (TabIndices[7] > 29.0 ) and (TabIndices[4] > 33.0 ):
               C0MenosC7MasC4Mas[Clase] = C0MenosC7MasC4Mas[Clase] + 1.0
            if (TabIndices[0] <= 1.0 ) and (TabIndices[7] > 29.0 ) and (TabIndices[4] <= 33.0 ):
                C0MenosC7MasC4Menos[Clase]=  C0MenosC7MasC4Menos[Clase] +1.0
            if (TabIndices[0] <= 1.0 ) and (TabIndices[7] <= 29.0 ) and (TabIndices[4] > 33.0 ):
                C0MenosC7MenosC4Mas[Clase] =C0MenosC7MenosC4Mas[Clase] +1.0
            if (TabIndices[0] <= 1.0 ) and (TabIndices[7] <= 29.0 ) and (TabIndices[4] <= 33.0 ):
                C0MenosC7MenosC4Menos[Clase] =C0MenosC7MenosC4Menos[Clase] +1.0
        
        SinAsignar=np.zeros(NumClases)    
        f.close()
        
        # TEST
        
        Start=3133
        End = 4177
        
        
        
        TotAciertos =0.0
        TotFallos =0.0
        TotSinAsignar=0.0
    
       
        Conta=0
        Cont=-1
        
        SwInicial=0
       
        t=open("C:\\abalone-1.data","r")
        with open("C:\AbaloneCorrected.txt","w") as  w:
        
            for linea1 in t:
                
                lineadelTest =linea1.split(",")
               
                Conta = Conta + 1
                if (Conta > Start):
                    
                 
                   
                    if Conta > End:
                        break
                 
                    Cont = Cont +1
                    
                    # W in case of receiving weights from an external adaboost
                    if len(W) == 1:
                      FactorPri=1.0
                    else:
                        FactorPri=W[Cont]
                        
                    ClaseLeida=float(lineadelTest[8])
                    
                    Clase=0    
                	
                    if (ClaseLeida > 10.0): 
                        Clase=2
                    else:
                        if (ClaseLeida > 8.0): 
                        		Clase=1
                  
                    ContClase[Clase]=ContClase[Clase] + 1
                               
                    TabIndices = np.zeros(NumCampos)
                   
                    z=-1
                    for x  in lineadelTest:
                        
                        z=z+1
                        if z==NumCampos:
                            break
                      
                        if z==0:
                            if lineadelTest[0] == "M":
                              ValorTrain=0.0
                            else:
                                if lineadelTest[0] == "F":
                                   ValorTrain=1.0
                                else:
                                        if lineadelTest[0] == "I":
                                            ValorTrain=2.0
                        else:
                            ValorTrain =float(lineadelTest[z])
                        ValorTrain =ValorTrain - Min[z]
                        Maximo = Max[z]
                        Maximo = Maximo - Min[z]
                        indice =(int) (((TopeMemoria - 2.0) * ValorTrain)/ Maximo)
                        if ( (indice > (TopeMemoria-2)) or  (indice < 0)):	
                            print("index overflowed=" + str( indice) + " in  the field ="+ str(z-1) )
                            indice=TopeMemoria
                        TabIndices[z]=indice
                    TabClases=np.zeros(NumClases)
                    if (TabIndices[0] > 1.0 ) and (TabIndices[7] > 29.0 ) and (TabIndices[4] > 33.0 ):
                       TabClases = C0MasC7MasC4Mas
                    if (TabIndices[0] > 1.0 ) and (TabIndices[7] > 29.0 ) and (TabIndices[4] <= 33.0 ):
                        TabClases=  C0MasC7MasC4Menos
                    if (TabIndices[0] > 1.0 ) and (TabIndices[7] <= 29.0 ) and (TabIndices[4] > 33.0 ):
                        TabClases =C0MasC7MenosC4Mas
                    if (TabIndices[0] > 1.0 ) and (TabIndices[7] <= 29.0 ) and (TabIndices[4] <= 33.0 ):
                        TabClases =C0MasC7MenosC4Menos
                    if (TabIndices[0] <= 1.0 ) and (TabIndices[7] > 29.0 ) and (TabIndices[4] > 33.0 ):
                       TabClases = C0MenosC7MasC4Mas
                    if (TabIndices[0] <= 1.0 ) and (TabIndices[7] > 29.0 ) and (TabIndices[4] <= 33.0 ):
                        TabClases=  C0MenosC7MasC4Menos
                    if (TabIndices[0] <= 1.0 ) and (TabIndices[7] <= 29.0 ) and (TabIndices[4] > 33.0 ):
                        TabClases =C0MenosC7MenosC4Mas
                    if (TabIndices[0] <= 1.0 ) and (TabIndices[7] <= 29.0 ) and (TabIndices[4] <= 33.0 ):
                        TabClases =C0MenosC7MenosC4Menos
                    longitud=len(linea1)
                    longitud=longitud-1
                    strlinea1 = str(linea1)
                    strlinea1=strlinea1[0:longitud]
                    ClasePredecida=-1 
                    TotClases=0
                    for i in range(NumClases):
                        if (TabClases[i] > TotClases):
                            TotClases=TabClases[i]
                            ClasePredecida=i
                    if (SwInicial==0):
                         SwInicial=1
                         Y=[float(Clase)]
                         X=[float(ClasePredecida)]
                    
                    else:
                         Y.append(float(Clase))
                         X.append(float(ClasePredecida))
                         
                    if (Clase==ClasePredecida):
                        TotAciertos=TotAciertos+1
                        strlinea1=strlinea1+",Correct,"+ str(ClasePredecida) + "," + str(Conta) + "\n"
                        w.write(strlinea1)
                        
                    else:
                        TotFallos=TotFallos+1
                        strlinea1=strlinea1+",ERROR," + str(ClasePredecida) + "," + str(Conta) + "\n"
                        w.write(strlinea1)
                    if (ClasePredecida==-1):
                        TotSinAsignar= TotSinAsignar+1
               
        t.close() 
        w.close()
        print("Total Hits Test =" + str(TotAciertos))  
        print("Total Failures Test =" + str(TotFallos)) 
                                                                                       
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

    