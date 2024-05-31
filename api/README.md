##start
uvicorn api.main:app --reload

##example call

POST http://127.0.0.1:8000/predict

{
"Gender": "Female",
"Age": 21,
"Height": 1.62,
"Weight": 64,
"family_history_with_overweight": "yes",
"FAVC": "no",
"FCVC": 2,
"NCP": 3,
"CAEC": "Sometimes",
"SMOKE": "no",
"CH2O": 2,
"SCC": "no",
"FAF": 0,
"TUE": 1,
"CALC": "no",
"MTRANS": "Public_Transportation"
}


