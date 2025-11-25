import mapQuestions, { RawQuestion } from "@/app/mappers/question-maper"
import { QuestionBase } from "../model/question-base"

interface StudentDepressionRepository {
    getQuestions(): Promise<QuestionBase[]>
}

const BASE_URL = "http://0.0.0.0:3001"

export class StudentDepressionRepositoryImp implements StudentDepressionRepository {
    private constructor() { }
    static instance = new StudentDepressionRepositoryImp();

    async getQuestions(): Promise<QuestionBase[]> {
        let questionResponse = await fetch(`${BASE_URL}/questions`)
        if (questionResponse.ok) {
            let questionJson : RawQuestion[] = await questionResponse.json()
            let questions = mapQuestions(questionJson)
            return questions
        }

        return []
    }
}