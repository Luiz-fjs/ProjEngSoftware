'use client';

import { useParams } from 'next/navigation';
import SurveyInit from "../../../../public/svgs/survey-init";
import { useContext, useEffect, useState } from 'react';
import { SurveyQuestionContext, SurveyDispatchContext } from '../../context/survey_context';
import { useRouter } from "next/navigation";

export default function SurveyQuestionPage() {
    const params = useParams();
    const surveyId = params.surveyId as string;
    const router = useRouter();
    const questions = useContext(SurveyQuestionContext);
    const dispatch = useContext(SurveyDispatchContext);

    const [selectedOption, setSelectedOption] = useState<string | null>(null);

    // Busca a pergunta específica pelo surveyId da URL
    const question = questions.find(q => q.id === surveyId);
    const currentIndex = questions.findIndex(q => q.id === surveyId);
    const progress = ((currentIndex + 1) / questions.length) * 100;

    useEffect(() => {
        setSelectedOption(question?.response || null);
    }, [question]);

    const handleNext = async () => {
        if (!selectedOption || !question) return;

        dispatch?.({
            type: 'update_response',
            questionId: question.id,
            response: selectedOption
        });

        const currentIndex = questions.findIndex(q => q.id === question.id);
        const nextQuestion = questions[currentIndex + 1];

        if (nextQuestion) {
            setSelectedOption(null); // Reseta a seleção
            router.push(`/survey/${nextQuestion.id}`);
        } else {
            router.push('/survey/processing');
        }
    };

    if (!question) {
        return (
            <div className="min-h-screen bg-gradient-to-br from-blue-50 via-indigo-50 to-purple-50 dark:from-gray-900 dark:via-indigo-900 dark:to-purple-900 flex items-center justify-center">
                <div className="text-center p-8 bg-white/80 dark:bg-gray-800/80 rounded-2xl shadow-xl">
                    <span className="text-4xl mb-4 block">❓</span>
                    <p className="text-xl text-gray-800 dark:text-gray-200">Pergunta não encontrada</p>
                </div>
            </div>
        );
    }

    return (
        <div className="min-h-screen bg-gradient-to-br from-blue-50 via-indigo-50 to-purple-50 dark:from-gray-900 dark:via-indigo-900 dark:to-purple-900 flex flex-col">
            {/* Progress Bar */}
            <div className="w-full bg-gray-200 dark:bg-gray-700 h-2">
                <div 
                    className="h-2 bg-gradient-to-r from-indigo-500 to-purple-500 transition-all duration-500 ease-out"
                    style={{ width: `${progress}%` }}
                />
            </div>
            
            {/* Progress Info */}
            <div className="bg-white/80 dark:bg-gray-800/80 backdrop-blur-sm border-b border-white/20 dark:border-gray-700/20 p-4">
                <div className="text-center">
                    <p className="text-sm text-gray-600 dark:text-gray-300">
                        Pergunta <span className="font-bold text-indigo-600 dark:text-indigo-400">{currentIndex + 1}</span> de <span className="font-bold">{questions.length}</span>
                    </p>
                    <p className="text-xs text-gray-500 dark:text-gray-400 mt-1">
                        {progress.toFixed(0)}% concluído
                    </p>
                </div>
            </div>

            <div className="flex-1 flex flex-col p-6">
                {/* Header Icon */}
                <div className="text-center mb-8">
                    <div className="inline-block">
                        <SurveyInit className="w-20 h-20 mx-auto opacity-60" />
                    </div>
                </div>

                {/* Question Content */}
                <div className="flex-1 max-w-4xl mx-auto w-full">
                    <div className="bg-white/80 dark:bg-gray-800/80 backdrop-blur-sm rounded-2xl p-8 shadow-xl border border-white/20 dark:border-gray-700/20">
                        {question.buildWidget({
                            onChange: (value: string) => {
                                setSelectedOption(value);
                            }
                        })}
                    </div>
                </div>
            </div>

            {/* Action Button */}
            <div className="p-4 bg-gradient-to-t from-white/90 to-transparent dark:from-gray-900/90 backdrop-blur-sm">
                <button
                    onClick={handleNext}
                    disabled={!selectedOption}
                    className={`w-full py-4 px-8 rounded-2xl font-bold text-xl transition-all duration-300 transform ${
                        selectedOption
                            ? 'bg-gradient-to-r from-indigo-600 via-purple-600 to-pink-600 hover:from-indigo-700 hover:via-purple-700 hover:to-pink-700 text-white shadow-lg hover:scale-105 active:scale-95 cursor-pointer'
                            : 'bg-gray-300 dark:bg-gray-600 text-gray-500 dark:text-gray-400 cursor-not-allowed opacity-50'
                    }`}
                >
                    {selectedOption ? (
                        <span className="flex items-center justify-center space-x-2">
                            <span>Próximo</span>
                            <span>→</span>
                        </span>
                    ) : (
                        'Selecione uma opção'
                    )}
                </button>
            </div>
        </div>
    );
}