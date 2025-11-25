'use client'

import { createContext, Dispatch, Suspense, use, useReducer } from "react";
import { QuestionRepository } from "../repository/question_respository";
import { QuestionBase } from "../model";

type SurveyAction =
  | { type: 'save_fetch', questions: QuestionBase[] }
  | { type: 'update_response', questionId: string, response: string };
export const SurveyQuestionContext = createContext<QuestionBase[]>([]);
export const SurveyDispatchContext = createContext<Dispatch<SurveyAction> | null>(null);

export function surveyReducer(questions: QuestionBase[], action: SurveyAction): QuestionBase[] {
  switch (action.type) {
    case 'save_fetch':
      return [...action.questions];
    case 'update_response':
      {
        const questionIndex = questions.findIndex(q => q.id === action.questionId);
        if (questionIndex === -1) return questions;
        questions[questionIndex].response = action.response;

        return [...questions];
      }
    default:
      return questions;
  }
}

export function SurveyProvider({ children }: { children: React.ReactNode }) {
  const repo = QuestionRepository.instance;
  const questions = repo.fetch();

  return (
    <Suspense fallback={<p>Loading...</p>}>
      <SurveyConsumer questions={questions}>
        {children}
      </SurveyConsumer>
    </Suspense>
  )
}

export function SurveyConsumer({ children, questions }: { children: React.ReactNode, questions: Promise<QuestionBase[]> }) {
  const allQuestions = use(questions);
  const [initQuestions, surveyDispatch] = useReducer(surveyReducer, allQuestions);

  return (
    <SurveyQuestionContext.Provider value={initQuestions}>
      <SurveyDispatchContext.Provider value={surveyDispatch}>
        {children}
      </SurveyDispatchContext.Provider>
    </SurveyQuestionContext.Provider>

  )
} 