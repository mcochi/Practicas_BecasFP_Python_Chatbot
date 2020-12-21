Trabajo y documentación realizado por Adrián Moral 


## REQUERIMIENTOS TECNICOS:
Versión Rasa(ejecutando: “rasa --version”)
Rasa Versión     : 2.0.2
Rasa SDK Versión : 2.1.2
Rasa X Versión   : None
Python Versión   : 3.7.9
Operating System : Windows-10-10.0.18362-SP0
Python Path      : c:\users\thinktic\desktop\chatbot_covid\venv\scripts\python.exe

MongoDB 
``` C:\Users\Your Name\AppData\Local\Programs\Python\Python36-32\Scripts>python -m pip install pymongo ```

Para instalar el servidor de mongo, deberemos alojar el servidor en un contenedor de docker, mediante los siguientes 4 comandos:

``` docker pull mongo:4.0.4
docker run -d -p 27017-27019:27017-27019 --name mongodb mongo:4.0.4
docker exec -it mongodb bash
Para activarlo en docker: docker start mongodb 
```

# Entorno virtual:
#### 1- Instalar Virtualenv

``` “pip install virtualenv” ```

#### 2- Preparación del entorno virtual 

En Windows nos vamos al directorio donde tengamos los ficheros destacados

``` “venv\Scripts\activate”``` 
Siempre que ejecutemos algo en rasa tenemos que tener el entorno activo -> Recuerda que para desactivarlo es simplemente el comando desactivate. 

Para saber que estamos dentro del entorno virtual, al principio de toda la ruta en la que estes, en el cmd antes pone (VENV)

#### 3-Una vez dentro del entorno virtual, instalaremos RASA

``` “pip install rasa ==2.0.2”``` 

``` “pip install –use-feature=2020-resolver rasa==2.0.2” ```

#### 4- Puesta a punto del entorno
“rasa train”
Después del rasa train, ejecutaremos rasa shell para empezar a hablar con el bot.

#### 5- Si tienes custom actions:
abrir otro terminal y ejecutaremos “rasa run actions”


PODREMOS CONSULTAR LA SIGUIENTE PAGINA PARA CUALQUIER DUDA

https://rasa.com/docs/rasa/

# Descripción Funcional.

Este ChatBot, de lo que trata es de saludarle, el te devolverá el saludo y te preguntara tu nombre, tu le dirás tu nombre, en mi caso Adrián, acto inmediato le hayas dicho tu nombre, el chatbot te preguntara oye Adrián tienes Tos Seca, y tu le dirás si o no, depende de lo que le digas se guardara un valor true o false, para luego insertarlo en la base de datos de mongo, (yes:true/no:false), si le contestas otra cosa que no sea no o si, te dirá lo siento no he podido entender, puedes repetir la respuesta, si o no?. A parte de tos seca te pregunta mas síntomas a los que se le aplica el mismo método decir si o no y depende de lo que le digas pone le valor true o false.
Por ultimo los valores nombre True o False, se guardaran en una base de datos MongoDB.

## Descripción Técnica:
(STORIES)
version: "2.0"

``` stories:
- story: happy path
  steps:
  - intent: greet
  - action: utter_greet
  - action: nombre_form
  - active_loop: nombre_form
  - active_loop: null
  - slot_was_set:
    - requested_slot: null
  - action: action_insert_mongo
  - action: utter_resume
  - intent: goodbye
  - action: utter_goodbye
  - action: action_restart 
``` 
Cuando le saludas, te devuelve el saludo, y te pregunta el nombre, cuando le das el nombre el se lo gurda en una variable, y empieza el formulario preguntándote síntomas, empezando pot tu nombre. EJ:(Adrián tienes tos seca?). Después de el formulario, vemos la action insert Mongo, que es para que los datos almacenados del formulario queden guardados en la base de datos de mongo. 
El utter resume es por decirlo así una vista previa a lo que va a insertar en la base de datos de mongo, y después de haber guardado los datos en la base de datos, se despide con un simple bye


# INSERTAR EN MONGO DB
(ACTIONS)

``` class ActionInsertMongo(Action):
    def name(self) -> Text:
        return "action_insert_mongo"
    
    def run(
        self,
        dispatcher: CollectingDispatcher,
        tracker: Tracker,
        domain: Dict[Text,Any]) -> List[Dict[Text,Any]]:
        
        dispatcher.utter_message(text='Storing Data')
        name = tracker.get_slot('name')
        tos = tracker.get_slot('tos')
        feel_tired = tracker.get_slot('feel_tired')
        aches_pains = tracker.get_slot('aches_pains')
        sore_throat = tracker.get_slot('sore_throat')

        myclient = pymongo.MongoClient("mongodb://localhost:27017/")
        mydb = myclient["mydatabase"]
        mycol = mydb["customers"]
        mydict = { "tos": tos, "feel_tired": feel_tired, "sore_throat": sore_throat, "name": name}
        x = mycol.insert_one(mydict) 
```

Este acción tendremos que mencionarla en el domain, para que se pueda ejecutar, y gracias a esta acción, las respuestas del usuario sera almacenada en la base de datos de mongo.

Lo que guarda es lo que hemos dicho anteriormente, el nombre y la respuesta a los síntomas si es true o false. Y hemos añadido un texto también, que cuando se ejecuta la acción de guardar los datos en mongo, el chatbot pondrá : “Storing data”

(ACTIONS),  formulario de los síntomas 

``` def validate_tos(
        self,
        slot_value: Any,
        dispatcher: CollectingDispatcher,
        tracker: Tracker,
        domain: DomainDict,
    ) -> Dict[Text, Any]:
        if(slot_value.lower() == 'yes'):
            return {"tos": True}
        else: 
            if(slot_value.lower()=='no'):
                return {"tos": False}
            else:
                dispatcher.utter_message(text="Sorry, but I didn't understand, can you please repeat the anwser (yes or no)?")
                return {"tos": None}
```
Esta es la estructura que tiene las preguntas de los síntomas, he puesto el primer ejemplo el de la tos, pero luego los demás son completamente iguales pero cambiando la variable de los síntomas, esta es tos, la siguiente si estas cansado, la siguiente dolor de cabeza... etc

## TELEGRAM 

Para que tu chatbot este activo en telegram, tendrás que ir a telegram al bot father, y poner:

``` /newbot ```
 
Una vez creado el bot, telegram te dará un acces token, y el nombre de tu bot definitivo.
 Una vez tengas tu acces token y el nombre de tu bot lo que haremos es ejecutar negrox.exe en el directorio donde tengamos creado el chatbot. Nos aparecerá una terminal, en la cual ejecutaremos el siguiente comando: 

``` Ngrok.exe http 5005 ``` 

(CREDENTIALS)
Te aparecerá una dirección HTTPS, que tendrás que poner antes de esto:

webhooks/telegram/webhook

``` telegram:
  access_token: "token de tu bot"
  verify: "nombre de tu bot"
  webhook_url: "dirección https de ngrok/webhooks/telegram/webhook"
```




Para que funcione tambien el chatbot hay que hacer lo siguiente: En config.yml, tendremos que activar la siguiente politica

(CONFIG)
``` policies:
   - name: MemoizationPolicy
   - name: TEDPolicy
     max_history: 5
     epochs: 100
   - name: RulePolicy
```

# FUTURAS MEJORAS

1. (MAPS)
Podremos crear y personalizar una API nosotros mismos en la cual, con un servicio de google maps localicemos todos los
centros de salud, y depende donde este el ususuario que esta hablando con el chatbot, lo llevariamos al centro de salud
mas cercano a su ubicacion.

2. (DEPENDE DE LOS SINTOMAS QUE TENGAS, QUE TE DIGA UNA COSA U OTRA)
Tu le preguntaras los sintomas, los cuales si son true, llegaran a un motor de inteligencia artificial, y para acceder a 
dicho motor, accederemos desde una api, una vez hecho esto, luego haremos un POST y te dira si te tienes que quedar en 
casa, ir a hacerte una pcr...

3. (PREGUNTAR LOS CASOS DE COVID EN LA ZONA QUE PREGUNTES)
Por ejemplo, que el usuario pregunte cuantos casos hay en la rioja, o como va el corona virus en la rioja, y que el chatbot
te de las cifras. Esto se hara practicamente igual que las anteriores mejoras, con una API, y luego hacerle un post y que te 
de los datos de La Rioja o de donde te haya preguntado dicho usuario.