import joblib
from pathlib import Path
from fastapi import APIRouter
from src.model.prediction_request import PredictionRequest
from src.model.prediction_response import PredictionResponse
from typing import List, Dict, Any
router = APIRouter()

RESOURCES_PATH = Path(__file__).parent / "resources"
MODEL_PATH = RESOURCES_PATH / "student-depression-svm.joblib"

# Importância das features baseada na análise real do modelo SVM não linear (Obtidas por script executado no notebook)
FEATURE_IMPORTANCE = {
    'Have you ever had suicidal thoughts ?': 48.5,
    'Academic Pressure': 26.1,
    'Financial Stress': 11.4,
    'Age': 5.9,
    'Work/Study Hours': 2.4,
    'Dietary Habits': 2.4,
    'Study Satisfaction': 2.3,
    'Sleep Duration': 0.6,
    'Gender': 0.4,
    'Family History of Mental Illness': 0.1,
    'CGPA': -0.1,
}

# Mapeamento para português
FEATURE_MAPPING = {
    'Gender': 'Gênero',
    'Age': 'Idade',
    'CGPA': 'Coeficiente de Rendimento (CR)',
    'Sleep Duration': 'Duração do Sono',
    'Dietary Habits': 'Hábitos Alimentares',
    'Have you ever had suicidal thoughts ?': 'Pensamentos Suicidas',
    'Work/Study Hours': 'Horas de Estudo/Trabalho',
    'Financial Stress': 'Estresse Financeiro',
    'Family History of Mental Illness': 'Histórico Familiar',
    'Study Satisfaction': 'Satisfação Academica',
    'Academic Pressure': 'Academic Total'
}

def generate_feature_feedback(user_data: dict) -> List[Dict[str, Any]]:
    """
    Gera feedback detalhado para cada feature baseado na resposta do usuário
    """
    feedback_list = []
    
    # 1. Gênero
    feedback_list.append({
        'feature': 'Gênero',
        'user_value': user_data['gender'],
        'importance': FEATURE_IMPORTANCE['Gender'],
        'impact_level': 'BAIXO',
        'message': f"Com base em sua resposta, o gênero '{user_data['gender']}' tem impacto mínimo na predição de depressão. Estudos mostram pequenas diferenças entre gêneros, mas fatores individuais são mais determinantes.",
        'context': f"O gênero representa apenas {FEATURE_IMPORTANCE['Gender']}% da importância no modelo, indicando que não é um fator determinante."
    })
    
    # 2. Idade - MODERADO (5.9%)
    age_feedback = f"Com base na sua idade de {user_data['age']} anos, "
    if user_data['age'] <= 20:
        age_feedback += "você está em uma faixa etária onde episódios depressivos podem estar relacionados à adaptação universitária e independência. A idade tem um impacto moderado no modelo."
    elif user_data['age'] <= 25:
        age_feedback += "você está em uma idade de transições importantes (formatura, primeiro emprego), que podem ser fatores de estresse significativos."
    else:
        age_feedback += "você está em uma faixa etária com maior estabilidade emocional, o que pode ser um fator protetor importante."
    
    feedback_list.append({
        'feature': 'Idade',
        'user_value': f"{user_data['age']} anos",
        'importance': FEATURE_IMPORTANCE['Age'],
        'impact_level': 'MODERADO',
        'message': age_feedback,
        'context': f"A idade tem importância moderada ({FEATURE_IMPORTANCE['Age']}%) no modelo, sendo o quarto fator mais relevante."
    })
    
    # 4. Coeficiente de Rendimento (CR)
    cgpa_feedback = f"Seu CR de {user_data['cgpa']:.1f} "
    if user_data['cgpa'] >= 8.0:
        cgpa_feedback += "indica excelente desempenho acadêmico, o que geralmente está associado a maior autoestima e senso de competência."
    elif user_data['cgpa'] >= 7.0:
        cgpa_feedback += "mostra bom desempenho acadêmico, equilibrando expectativas e resultados adequadamente."
    elif user_data['cgpa'] >= 6.0:
        cgpa_feedback += "sugere desempenho mediano, que pode gerar algumas preocupações mas não é necessariamente problemático."
    else:
        cgpa_feedback += "pode estar gerando estresse acadêmico e impactando sua autoestima. Considere buscar apoio pedagógico."
    
    feedback_list.append({
        'feature': 'Coeficiente de Rendimento (CR)',
        'user_value': f"{user_data['cgpa']:.1f}",
        'importance': FEATURE_IMPORTANCE['CGPA'],
        'impact_level': 'BAIXO',
        'message': cgpa_feedback,
        'context': f"O CR tem baixa importância ({FEATURE_IMPORTANCE['CGPA']}%) no modelo, mas pode afetar autoestima e perspectivas futuras."
    })
    
    # 5. Duração do Sono - BAIXO (0.6%)
    sleep_feedback = f"Sua duração de sono '{user_data['sleep_duration']}' "
    if user_data['sleep_duration'] == 'Menos de 5 horas':
        sleep_feedback += "é insuficiente e pode estar impactando seu humor, concentração e bem-estar geral. Embora tenha baixo peso no modelo, é fundamental para saúde mental."
    elif user_data['sleep_duration'] == '5-6 horas':
        sleep_feedback += "está abaixo do recomendado para a maioria dos adultos. Pode estar afetando sua capacidade de lidar com estresse."
    elif user_data['sleep_duration'] == '7-8 horas':
        sleep_feedback += "está dentro da faixa ideal para a maioria dos adultos, contribuindo positivamente para sua saúde mental."
    elif user_data['sleep_duration'] == 'Mais de 8 horas':
        sleep_feedback += "pode indicar boa recuperação, mas se for excessivo (>9h) pode sinalizar possível escape ou alterações do humor."
    else:
        sleep_feedback += "com padrões irregulares pode estar impactando sua regulação emocional e energia."
    
    feedback_list.append({
        'feature': 'Duração do Sono',
        'user_value': user_data['sleep_duration'],
        'importance': FEATURE_IMPORTANCE['Sleep Duration'],
        'impact_level': 'BAIXO',
        'message': sleep_feedback,
        'context': f"A duração do sono tem baixa importância ({FEATURE_IMPORTANCE['Sleep Duration']}%) no modelo, mas permanece crucial para bem-estar geral."
    })
    
    # 6. Hábitos Alimentares - BAIXO (2.3%)
    diet_feedback = f"Seus hábitos alimentares '{user_data['dietary_habits']}' "
    if user_data['dietary_habits'] == 'Muito saudáveis':
        diet_feedback += "são excelentes e contribuem positivamente para sua energia, humor e bem-estar geral. Embora tenham baixo peso no modelo, são importantes para qualidade de vida."
    elif user_data['dietary_habits'] == 'Moderadamente saudáveis':
        diet_feedback += "mostram boa consciência nutricional, com espaço para pequenos ajustes que podem melhorar seu bem-estar."
    elif user_data['dietary_habits'] == 'Pouco saudáveis':
        diet_feedback += "podem estar impactando sua energia e humor. Mudanças na alimentação podem ter benefícios para bem-estar geral."
    else:
        diet_feedback += "podem estar afetando negativamente sua energia, concentração e estabilidade emocional."
    
    feedback_list.append({
        'feature': 'Hábitos Alimentares',
        'user_value': user_data['dietary_habits'],
        'importance': FEATURE_IMPORTANCE['Dietary Habits'],
        'impact_level': 'BAIXO',
        'message': diet_feedback,
        'context': f"Os hábitos alimentares têm baixa importância ({FEATURE_IMPORTANCE['Dietary Habits']}%) no modelo, mas contribuem para o bem-estar geral."
    })
    
    # 7. Pensamentos Suicidas (CRÍTICO - 48.5%)
    suicidal_feedback = f"Sua resposta '{user_data['suicidal_thoughts']}' sobre pensamentos suicidas "
    if user_data['suicidal_thoughts'] == 'Sim':
        suicidal_feedback += "é o fator de MAIOR RISCO identificado pelo modelo, representando quase metade da importância total. É FUNDAMENTAL buscar ajuda profissional imediatamente. Existem tratamentos eficazes e você não está sozinho(a)."
    else:
        suicidal_feedback += "é extremamente protetiva e representa o fator mais importante para reduzir o risco de depressão no modelo, com quase metade do peso total da predição."
    
    feedback_list.append({
        'feature': 'Pensamentos Suicidas',
        'user_value': user_data['suicidal_thoughts'],
        'importance': FEATURE_IMPORTANCE['Have you ever had suicidal thoughts ?'],
        'impact_level': 'CRÍTICO',
        'message': suicidal_feedback,
        'context': f"Esta é a feature MAIS IMPORTANTE ({FEATURE_IMPORTANCE['Have you ever had suicidal thoughts ?']}%) no modelo, representando quase metade de toda a predição. É o fator mais determinante."
    })
    
    # 8. Horas de Estudo/Trabalho - BAIXO (2.4%)
    hours_feedback = f"Suas {user_data['work_study_hours']} horas de estudo/trabalho por dia "
    if user_data['work_study_hours'] <= 4:
        hours_feedback += "indicam carga leve, o que pode ser protetor contra sobrecarga. Embora tenha baixo peso no modelo, ainda influencia o bem-estar."
    elif user_data['work_study_hours'] <= 8:
        hours_feedback += "representam uma carga equilibrada, adequada para a maioria das pessoas."
    elif user_data['work_study_hours'] <= 12:
        hours_feedback += "indicam carga intensa que pode gerar estresse, mas ainda manejável com boa organização."
    else:
        hours_feedback += "representam sobrecarga significativa que pode estar impactando seu bem-estar e eficiência."
    
    feedback_list.append({
        'feature': 'Horas de Estudo/Trabalho',
        'user_value': f"{user_data['work_study_hours']} horas/dia",
        'importance': FEATURE_IMPORTANCE['Work/Study Hours'],
        'impact_level': 'BAIXO',
        'message': hours_feedback,
        'context': f"As horas de estudo/trabalho têm baixa importância ({FEATURE_IMPORTANCE['Work/Study Hours']}%) no modelo, mas ainda podem afetar o bem-estar."
    })
    
    # 9. Estresse Financeiro - ALTO (12.8%)
    financial_feedback = f"Seu nível de estresse financeiro {user_data['financial_stress']}/5 "
    if user_data['financial_stress'] <= 2:
        financial_feedback += "é baixo, o que contribui positivamente para sua estabilidade emocional e foco nos estudos."
    elif user_data['financial_stress'] == 3:
        financial_feedback += "é moderado, mas ainda manejável. Considere estratégias de planejamento financeiro."
    else:
        financial_feedback += "é alto e pode estar impactando significativamente seu bem-estar e capacidade de concentração."
    
    feedback_list.append({
        'feature': 'Estresse Financeiro',
        'user_value': f"{user_data['financial_stress']}/5",
        'importance': FEATURE_IMPORTANCE['Financial Stress'],
        'impact_level': 'ALTO',
        'message': financial_feedback,
        'context': f"O estresse financeiro é o terceiro fator mais importante ({FEATURE_IMPORTANCE['Financial Stress']}%) no modelo - mudanças aqui têm impacto significativo."
    })
    
    # 10. Histórico Familiar
    family_feedback = f"Seu histórico familiar '{user_data['family_history']}' "
    if user_data['family_history'] == 'Sim':
        family_feedback += "indica predisposição genética, mas não determina seu destino. Estar ciente pode ajudar na prevenção e cuidado preventivo."
    else:
        family_feedback += "não indica predisposição familiar conhecida, o que pode ser um fator protetor."
    
    feedback_list.append({
        'feature': 'Histórico Familiar',
        'user_value': user_data['family_history'],
        'importance': FEATURE_IMPORTANCE['Family History of Mental Illness'],
        'impact_level': 'BAIXO',
        'message': family_feedback,
        'context': f"O histórico familiar tem baixa importância ({FEATURE_IMPORTANCE['Family History of Mental Illness']}%) no modelo."
    })
    
    # 11. Satisfação Com estudos - BAIXO (2.3%)
    study_satisfaction = user_data['study_satisfaction']
    satisfaction_feedback = f"Sua satisfação com os estudos de {study_satisfaction}/5 "
    if study_satisfaction >= 4:
        satisfaction_feedback += "é alta, indicando boa realização pessoal com suas atividades atuais. Embora tenha baixo peso no modelo, é um fator protetor importante para qualidade de vida."
    elif study_satisfaction >= 3:
        satisfaction_feedback += "é moderada, mostrando alguma satisfação mas com espaço para melhorias na qualidade de vida."
    elif study_satisfaction >= 2:
        satisfaction_feedback += "é baixa e pode estar contribuindo para sentimentos de desmotivação e insatisfação geral."
    else:
        satisfaction_feedback += "é muito baixa, indicando possível necessidade de mudanças significativas em suas atividades ou perspectivas."
    
    feedback_list.append({
        'feature': 'Satisfação com Estudos',
        'user_value': f"{study_satisfaction}/5",
        'importance': FEATURE_IMPORTANCE['Study Satisfaction'],
        'impact_level': 'BAIXO',
        'message': satisfaction_feedback,
        'context': f"A satisfação com os estudos tem baixa importância ({FEATURE_IMPORTANCE['Study Satisfaction']}%) no modelo, mas é relevante para qualidade de vida geral."
    })
    
    # 12. Pressão Acadêmica (MUITO ALTO - 26.1%)
    academic_pressure = user_data['academic_pressure']
    pressure_feedback = f"Sua pressão acadêmica de {academic_pressure}/5 "
    if academic_pressure <= 1:
        pressure_feedback += "é muito baixa, o que é extremamente protetor contra desenvolvimento de sintomas depressivos."
    elif academic_pressure <= 2:
        pressure_feedback += "é baixa, o que é altamente protetor contra desenvolvimento de sintomas depressivos."
    elif academic_pressure == 3:
        pressure_feedback += "é moderada e ainda manejável, mas requer atenção para não aumentar, dado seu alto peso no modelo."
    elif academic_pressure == 4:
        pressure_feedback += "é alta e representa um fator de risco MUITO SIGNIFICATIVO. É importante desenvolver estratégias de manejo de estresse urgentemente."
    else:
        pressure_feedback += "é extremamente alta e representa o SEGUNDO MAIOR FATOR DE RISCO no modelo. É CRUCIAL buscar formas de reduzir essa pressão imediatamente."
    
    feedback_list.append({
        'feature': 'Pressão Acadêmica',
        'user_value': f"{academic_pressure}/5",
        'importance': FEATURE_IMPORTANCE['Academic Pressure'],
        'impact_level': 'MUITO ALTO',
        'message': pressure_feedback,
        'context': f"A pressão acadêmica é o SEGUNDO FATOR MAIS IMPORTANTE ({FEATURE_IMPORTANCE['Academic Pressure']}%) no modelo de predição, com peso muito significativo."
    })
    
    return feedback_list

# Carregar os modelos
try:
    model = joblib.load(MODEL_PATH)
    print("Modelo carregados com sucesso!")
except Exception as e:
    print(f"Erro ao carregar modelo: {e}")
    model = None



@router.get("/example")
async def example_route():
    return {"message": "This is an example route from model.py"}