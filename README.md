# Questionaries App
This is a simple Questionnaries app developed in Django (for the backend REST API) and with Vue.js for the frontend.


# Usage
Developed using Django 2 and Python 3.7 
## Backend (Django REST API)
1. ```pip install -r requirements.txt```
2. ```python manage.py migrate```
3. ```python manage.py runserver 0.0.0.0:8001```

This app also has a `load_questionnarie` command that is used to load a Questionnaire from a json file.
It takes `-p` (path to json file) and `-n` (name of the questionnaire) as arguments.
The following JSON file can be located from `questionnaires/management/commands/questionnaires_examples/questionnaire_example.json`
JSON file must be like:

```json
{
  "question": "Are you hungry?",
  "answer_variants": {
    "Yes": {
      "question": "What would you like to eat?",
      "answer_variants": {
        "Hamburger": {
          "question": "Nice, I will order a hamburger for you!",
          "answer_variants": null
        },
        "Pizza": {
          "question": "Would you like pizza with mushrooms?",
          "answer_variants": {
            "Yes": {
              "question": "Ok, I will order the best pizza in town for you",
              "answer_variants": null
            },
            "No": {
              "question": "No? Well... stay hungry then",
              "answer_variants": null
            }
          }
        }
      }
    },
    "No": {
      "question": "Ok. Call me when you're hungry.",
      "answer_variants": null
    }
  }
}
```


## Frontend (Vue App)
1. cd into frontend directory and run ```npm install```
2. ```npm run serve```