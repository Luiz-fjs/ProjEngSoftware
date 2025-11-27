'use client'

import { useContext } from "react"
import { SurveyQuestionContext } from "../../../context/survey_context";

export default function SurveyResponseCounter() {
    const questionsResponse = useContext(SurveyQuestionContext);

    const answeredQuestionsCount = questionsResponse.filter((q) => q.response !== undefined).length;
    
    return (
        <div className="h-10 mx-10 my-2 content-center">
            <p className="font-mono font-semi-bold text-center dark:text-white text-ellipsis">Você possui {answeredQuestionsCount} questões de {questionsResponse.length} respondidas</p>
        </div>
    )
}