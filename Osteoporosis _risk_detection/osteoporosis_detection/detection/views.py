import numpy as np
import joblib
from django.shortcuts import render
from django.http import JsonResponse
import warnings
warnings.filterwarnings('ignore')


model = joblib.load(r'C:\Users\HP\Osteoporosis\osteoporosis_model.pkl')

def predict_osteoporosis(request):
    if request.method == 'POST':
        try:
            age = int(request.POST.get('age'))
            
            alcohol = 1 if request.POST.get('alcohol') == 'yes' else 0
            family_history = 1 if request.POST.get('family_history') == 'yes' else 0
            smoking = 1 if request.POST.get('smoking') == 'yes' else 0
            prior_fractures = 1 if request.POST.get('prior_fractures') == 'yes' else 0
            
            medical_conditions = request.POST.get('medical_conditions')
            medications = request.POST.get('medications')
            gender = request.POST.get('gender')
            hormonal_changes = request.POST.get('hormonal_changes')
            race = request.POST.get('race')
            weight = request.POST.get('weight')
            calcium_intake = request.POST.get('calcium_intake')
            vitamin_d_intake = request.POST.get('vitamin_d_intake')
            physical_activity = request.POST.get('physical_activity')

            mappings = {
                "race": {"Asian": 1, "Caucasian": 2, "African American": 3},
                "weight": {"Underweight": 1, "Normal": 2, "Overweight": 3},
                "calcium_intake": {"Low": 0, "Adequate": 1},
                "vitamin_d_intake": {"Insufficient": 0, "Sufficient": 1},
                "physical_activity": {"Sedentary": 0, "Active": 1},
                "medical_conditions": {"None": 0, "Hyperthyroidism": 1, "Rheumatoid Arthritis": 2},
                "medications": {"None": 0, "Corticosteroids": 1},
                "hormonal_changes": {"Normal": 0, "Postmenopausal": 1},
                "gender": {"Male": 0, "Female": 1}
            }

            user_data = np.array([
                age,
                alcohol,
                mappings['medical_conditions'][medical_conditions],
                mappings['medications'][medications],
                mappings['gender'][gender],
                mappings['hormonal_changes'][hormonal_changes],
                family_history,
                mappings['race'][race],
                mappings['weight'][weight],
                mappings['calcium_intake'][calcium_intake],
                mappings['vitamin_d_intake'][vitamin_d_intake],
                mappings['physical_activity'][physical_activity],
                smoking,
                prior_fractures
            ]).reshape(1, -1)
            prediction = model.predict(user_data)[0]  
            probability = model.predict_proba(user_data)[0][1]  
            result = "Osteoporosis is likely present." if prediction == 1 else "Osteoporosis is unlikely."
            probability_percentage = round(probability * 100, 2)

            return JsonResponse({
                "result": result,
                "probability": f"{probability_percentage}%"
            })
        except Exception as e:
            return JsonResponse({
                "error": str(e)
            })

    return render(request, 'index.html')
def bmi_calculator(request):
    return render(request, 'bmi_calculator.html')