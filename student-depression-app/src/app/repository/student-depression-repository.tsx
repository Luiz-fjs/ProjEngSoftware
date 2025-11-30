import mapQuestions, { RawQuestion } from "@/app/mappers/question-maper"
import { QuestionBase } from "../model/question-base"
import { SurveyPredictDepressionResponse } from '../model/survey_predict_depression_response';

interface StudentDepressionRepository {
    getQuestions(): Promise<QuestionBase[]>
}

const BASE_URL = "https://projengsoftware-o465.onrender.com"

export class StudentDepressionRepositoryImp implements StudentDepressionRepository {
    private constructor() { }
    static instance = new StudentDepressionRepositoryImp();

    async getQuestions(): Promise<QuestionBase[]> {
        const questionResponse = await fetch(`${BASE_URL}/questions`)
        if (questionResponse.ok) {
            const questionJson : RawQuestion[] = await questionResponse.json()
            const questions = mapQuestions(questionJson)
            return questions
        }

        return []
    }

    static async requestFeedback(responses: Record<string, string | number>): Promise<SurveyPredictDepressionResponse> {
        try {
            const response = await fetch(`${BASE_URL}/predict`, {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json',
                },
                body: JSON.stringify(responses),
            });

            if (response.ok) {
                const data: SurveyPredictDepressionResponse = await response.json();
                return data
            }

            throw new Error(`Error: ${response.status} ${response.statusText}`);
        } catch (error) {
            throw error;
        }
    }
}