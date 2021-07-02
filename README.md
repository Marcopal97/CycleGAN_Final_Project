# CycleGAN_Final_Project
Passi da seguire per caricare il progetto e poterlo eseguire:

  1. Importare su Google Colab i notebook rinominati "CycleGAN_V1" e "CycleGAN_V2".
  2. Importare sul proprio Google Drive gli script python di supporto rinominati "helpers.py", "config.py" e "utils.py". Tali file dovranno essere caricati nella directory principale del proprio Drive. Lo script "helpers.py" contiene delle funzioni per il salvataggio dei parametri del modello V1 e per il salvataggio dei campioni delle immagini generate. I file "config.py" e "utils.py" vengono utilizzati dal modello V2 e contengono, rispettivamente:
    
   - I parametri di configurazione del modello + la funzione di trasformazione delle immagini per il pre-processing.
   - Le funzioni per il salvataggio e il caricamento dei parametri del modello.
    
  3. Scaricare i dataset dai seguenti link:
  
    - https://drive.google.com/drive/folders/1FpL0IRgObg82uTVX7-Qh847LI9qc23xh?usp=sharing --> utilizzato dal modello V1
    - https://drive.google.com/drive/folders/1R7kaKV3pfYMTT0bQgn8Ox23b45YtJ3GC?usp=sharing --> utilizzato dal modello V2
  
   E' possibile anche scaricare solamente uno dei due dataset, a patto che si replichi la seguente struttura di directory per ciascuna delle due implementazioni:
   
   - Per il modello V1:
   
    summer2winter -----
                       |
                       |-------- /summer_train -----
                       |                            |
                       |                            |----- /trainA
                       |
                       |-------- /summer_test -----
                       |                           |
                       |                           |----- /testA
                       |            
                       |-------- /winter_train -----
                       |                            |
                       |                            |-----/trainB
                       |
                       |-------- /winter_test -----
                                                  |
                                                  |-----/testB
                                                  
  - Per il modello V2:
   
        data ----------
                       |
                       |-------- /train -----
                       |                     |
                       |                     |----- /summer
                       |                     |
                       |                     |----- /winter
                       |-------- /val -------
                       |                     |
                       |                     |----- /summer
                       |                     |
                       |                     |----- /winter
                       
 Entrambe le directory ("summer2winter" e "data") devono essere caricate nella cartella principale del proprio Drive (allo stesso modo di quanto fatto con gli script .py).
 
 
La directory "Results" contiene i risultati ottenuti mediante i modelli V1 e V2. In particolare, i risultati del modello V2 sono stati ottenuti utilizzando i campioni del training set. 
                       
                       
                  
