import mapQuestions, { RawQuestion } from "@/domain/mappers/question-maper"
import { QuestionBase } from "../model/question-base"

interface StudentDepressionRepository {
    getQuestions(): Promise<QuestionBase[]>
}

const BASE_URL = "https://studant-depression-api.com"

class StudentDepressionRepositoryImp implements StudentDepressionRepository {
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