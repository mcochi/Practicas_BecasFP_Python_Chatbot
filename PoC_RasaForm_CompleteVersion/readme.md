### REQUERIMIENTOS TECNICOS:
version python
version rasa 
version mongo 
entorno virtual



DESARROLADOR......



hipervinculos...










Descripcion Funcional.
Este ChatbBot de lo que trata es de lo siguiente: Le saludas, te saluda y te pregunta tu nombre, le dices tu nombre, y el ChatBot automáticamente se guardara tu nombre, y te preguntara oye Pepito, tienes tal síntoma, y le contestaras yes or no, si l contestas otra cosa diferente, el ChatBot auténticamente te repetirá la pregunta, y te aclarara yes or no, y después de que te pregunte tu nombre y todos los síntomas, lo que hará este ChatBot es guardaren la base de datos MongoDB.

Descripción Técnica:
``` version: "2.0"

stories:
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

Cuando le saludas, te devuelve el saludo, y te pregunta por tu nombre, imaginate que te llamas pepe, luego la siguiente acción es un formulario, que empieza preguntando si tienes tos, y guarda el nombre y te pregunta pepe, tienes fiebre?, lo que contestaras con un yes o un no, si contestas otra cosa se ejecuta otra accion que te repite la pregunta y recalca que contestes con yes or no:
def validate_tos(
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






Luego despues de la tos te pregunta mas sintomas, que tienen la misma estructura preguntan el sintoma empezando por tu nombre:

utter_ask_tos:
  - text: "Hello, {name}, do you cough?"
  utter_ask_feel_tired:
  - text: "{name}, Do you feel tired?"
  utter_ask_aches_pains:
  - text: "{name}, Do you have aches and pains?"
  utter_ask_sore_throat:
  - text: "{name}, Do you have sore throat?"

 Name es lo que has guardado anteriormente cuando le preguntas el nombre al usuario. 

Una vez pregunta todos los sintomas y le dices si o no, lo guardara en una base de datos MongoDB 
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

Se guardara el nombre, y si has dicho yes un valor true y si has dicho no un valor false

Luego para las custom actions, tendremos que ejecutar otro terminal con el siguiente comando:
“rasa run actions” y dejarlo correr mientras en otro terminal.ejecutas el rasa shell.

FUTURAS MEJORAS:
Incorporar una api, que lleve todos los registros de corona virus por comunidades, y a partir de eso, preguntar el usuario por ejemplo cuantos casos hay en la rioja y que el chatbot le proporcione la información de la api

he estado pensandoo....

TELEGRAM/ngrok

poner de donde es el fichero