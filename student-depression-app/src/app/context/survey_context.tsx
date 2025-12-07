'use client'

import { createContext, Dispatch, useEffect, useReducer, useState } from "react";
import { StudentDepressionRepositoryImp } from "../repository/student-depression-repository";
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
  const repo = StudentDepressionRepositoryImp.instance;
  const [initQuestions, surveyDispatch] = useReducer(surveyReducer, [] as QuestionBase[]);
  const [loading, setLoading] = useState(true);

  useEffect(() => {
    let active = true;
    const load = async () => {
      try {
        const qs = await repo.getQuestions();
        if (!active) return;
        surveyDispatch({ type: 'save_fetch', questions: qs });
      } finally {
        if (active) setLoading(false);
      }
    };
    load();
    return () => { active = false; };
  }, [repo]);

  if (loading) return <p>Loading...</p>;

  return (
    <SurveyQuestionContext.Provider value={initQuestions}>
      <SurveyDispatchContext.Provider value={surveyDispatch}>
        {children}
      </SurveyDispatchContext.Provider>
    </SurveyQuestionContext.Provider>
  );
}