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
                       



# Results
Winter --> Summer generation using V1
![sample-004000-X-Y](https://user-images.githubusercontent.com/48278123/134184459-cdfb41a2-ad9e-4ded-b112-abc7da5a74b6.png)

Summer --> Winter generation using V1
![sample-004000-Y-X](https://user-images.githubusercontent.com/48278123/134184485-c1714831-6a4e-4e05-846f-c9a23608aa66.png)

Winter --> Summer generation using V2
![Fake_summer01](https://user-images.githubusercontent.com/48278123/134184669-01198b48-be4c-4817-992a-2e5877daf927.PNG)
![Fake_summer03](https://user-images.githubusercontent.com/48278123/134184683-5e265d8c-22a8-4c37-89b2-33d850b79dda.PNG)
![Fake_summer07](https://user-images.githubusercontent.com/48278123/134184705-1745374f-0b9b-487c-9296-125ff71b210a.png)
![Fake_summer22](https://user-images.githubusercontent.com/48278123/134184742-928da12a-0ea1-4f61-b12a-96fad8c71456.png)
![Fake_summer26](https://user-images.githubusercontent.com/48278123/134184781-dbd4c1da-3070-4858-9edd-a505516bc26b.png)

Summer --> Winter generation using V2
![Fake_winter01](https://user-images.githubusercontent.com/48278123/134184922-e3653515-a12d-4dc5-8916-a609beaaade6.PNG)
![Fake_winter02](https://user-images.githubusercontent.com/48278123/134184932-73febed9-520e-4516-baa9-073eb3335ee0.PNG)
![Fake_winter03](https://user-images.githubusercontent.com/48278123/134184947-bc22f60a-a1dd-4afa-9c07-65e7c516e601.PNG)
![Fake_winter16](https://user-images.githubusercontent.com/48278123/134184967-681002c0-abc0-4ec9-acf7-b7e378141dd9.png)
![Fake_winter24](https://user-images.githubusercontent.com/48278123/134185022-546516c2-c367-4c33-96ba-1078e048a419.png)








                  
