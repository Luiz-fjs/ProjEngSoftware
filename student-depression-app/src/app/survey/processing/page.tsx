'use client';

import { SurveyQuestionContext } from "@/app/context/survey_context";
import { useContext, useEffect, useState } from "react";
import { SurveyProcessing } from "../../../../public/svgs/survey-processing";
import { Loading } from "../../../../public/animated/loading";
import SurveyFeedback from "../../../../public/svgs/survey-feedback";
import Link from "next/dist/client/link";
import { SurveyPredictDepressionResponse } from "@/app/model/survey_predict_depression_response";
import DetailedFeedback from "../component/detailed_feedback";

// Adicionar estilos CSS customizados
const customStyles = `
  @keyframes fade-in {
    from {
      opacity: 0;
      transform: translateY(20px);
    }
    to {
      opacity: 1;
      transform: translateY(0);
    }
  }
  
  .animate-fade-in {
    animation: fade-in 0.6s ease-out;
  }
`;

// Adicionar estilos ao head
if (typeof document !== 'undefined') {
  const styleSheet = document.createElement("style");
  styleSheet.innerText = customStyles;
  document.head.appendChild(styleSheet);
}

export default function Processing() {
    const [loading] = useState<boolean>(true);
    const [predictResponse] = useState<SurveyPredictDepressionResponse | null>(null);
    const questions = useContext(SurveyQuestionContext);
    const answeredQuestions: Record<string, string | number> = questions
        .filter(q => q.response !== undefined && q.response !== null)
        .sort((a, b) => Number.parseInt(a.id) - Number.parseInt(b.id))
        .reduce((json, question) => {
            if (question.id == 'age') {
                const birthDate = new Date(question.response!);
                const today = new Date();
                let age = today.getFullYear() - birthDate.getFullYear();
                const monthDiff = today.getMonth() - birthDate.getMonth();
                if (monthDiff < 0 || (monthDiff === 0 && today.getDate() < birthDate.getDate())) {
                    age = (age - 1);
                }

                json[question.id] = age.toString();
                return json;
            }

            json[question.id] = question.response as string | number;
            return json;
        }, {} as Record<string, string | number>);

    // Usado para depuração/evitar warning de variável não utilizada enquanto
    // a integração com o serviço permanece comentada.
    console.debug('answeredQuestions:', answeredQuestions);

    useEffect(() => {
        const fetchData = async () => {

            /*
            try {
                const response: SurveyPredictDepressionResponse = await SurveyService.requestFeedback(answeredQuestions)
                setPredictResponse(response);
                setLoading(false);

            } catch (error) {
                console.error('Error fetching depression prediction:', error);

            }*/
        }

        fetchData();
    }, []);

    if (loading) {
        return (
            <div className="min-h-screen bg-gradient-to-br from-blue-50 via-indigo-50 to-purple-50 dark:from-gray-900 dark:via-indigo-900 dark:to-purple-900 flex flex-col items-center justify-center p-6">
                <div className="text-center space-y-6 max-w-md mx-auto">
                    <div className="animate-pulse">
                        <SurveyProcessing className="w-32 h-32 mx-auto" />
                    </div>
                    <div className="space-y-3">
                        <h1 className="text-3xl font-bold bg-gradient-to-r from-indigo-600 to-purple-600 dark:from-indigo-400 dark:to-purple-400 bg-clip-text text-transparent">
                            Submetendo respostas...
                        </h1>
                        <p className="text-gray-600 dark:text-gray-300 text-lg leading-relaxed">
                            Estamos analisando e processando sua resposta. Obrigado por participar.
                        </p>
                    </div>
                    <div className="pt-4">
                        <Loading />
                    </div>
                </div>
            </div>
        );
    }

    return (
        <div className="min-h-screen bg-gradient-to-br from-blue-50 via-indigo-50 to-purple-50 dark:from-gray-900 dark:via-indigo-900 dark:to-purple-900">
            <div className="container mx-auto px-4 py-8 flex flex-col min-h-screen">
                {/* Header Section */}
                <div className="text-center mb-8 animate-fade-in">
                    <div className="inline-block mb-6">
                        <SurveyFeedback className="w-24 h-24 mx-auto" />
                    </div>
                    
                    <div className="bg-white/80 dark:bg-gray-800/80 backdrop-blur-sm rounded-2xl p-8 shadow-xl border border-white/20 dark:border-gray-700/20">
                        <h1 className="text-2xl font-semibold text-gray-700 dark:text-gray-200 mb-4">
                            Resultado da Análise
                        </h1>
                        
                        <p className="text-lg text-gray-600 dark:text-gray-300 mb-2">
                            Suas chances de ter depressão são
                        </p>
                        
                        <div className="relative">
                            <p className="text-7xl font-bold bg-gradient-to-r from-indigo-600 via-purple-600 to-pink-600 dark:from-indigo-400 dark:via-purple-400 dark:to-pink-400 bg-clip-text text-transparent animate-pulse">
                                {((predictResponse?.probability[1] ?? 0)*100)?.toFixed(1)}%
                            </p>
                            
                            {/* Risk Level Indicator */}
                            <div className="mt-4">
                                {(() => {
                                    const risk = ((predictResponse?.probability[1] ?? 0) * 100);
                                    if (risk < 30) {
                                        return (
                                            <span className="inline-flex items-center px-4 py-2 rounded-full text-sm font-medium bg-green-100 text-green-800 dark:bg-green-900/20 dark:text-green-400">
                                                🟢 Baixo Risco
                                            </span>
                                        );
                                    } else if (risk < 70) {
                                        return (
                                            <span className="inline-flex items-center px-4 py-2 rounded-full text-sm font-medium bg-yellow-100 text-yellow-800 dark:bg-yellow-900/20 dark:text-yellow-400">
                                                🟡 Risco Moderado
                                            </span>
                                        );
                                    } else {
                                        return (
                                            <span className="inline-flex items-center px-4 py-2 rounded-full text-sm font-medium bg-red-100 text-red-800 dark:bg-red-900/20 dark:text-red-400">
                                                🔴 Alto Risco
                                            </span>
                                        );
                                    }
                                })()}
                            </div>
                        </div>
                    </div>
                </div>

                {/* Detailed Feedback Section */}
                <div className="flex-1 mb-8">
                    <div className="bg-white/60 dark:bg-gray-800/60 backdrop-blur-sm rounded-2xl p-6 shadow-xl border border-white/20 dark:border-gray-700/20 max-h-[60vh] overflow-y-auto">
                        <h2 className="text-xl font-semibold text-gray-800 dark:text-gray-100 mb-4 text-center">
                            Análise Detalhada dos Fatores
                        </h2>
                        <DetailedFeedback featureFeedback={predictResponse?.feature_feedback ?? []}/>
                    </div>
                </div>

                {/* Action Section */}
                <div className="text-center">
                    <Link href="/" className="group relative inline-flex items-center justify-center px-10 py-4 overflow-hidden font-medium text-white transition-all duration-300 ease-out border-2 border-indigo-500 rounded-full shadow-lg hover:shadow-xl transform hover:scale-105 active:scale-95">
                        <span className="absolute inset-0 flex items-center justify-center w-full h-full text-white duration-300 -translate-x-full bg-gradient-to-r from-indigo-500 via-purple-500 to-pink-500 group-hover:translate-x-0 ease">
                            <svg className="w-6 h-6 mr-2" fill="none" stroke="currentColor" viewBox="0 0 24 24" xmlns="http://www.w3.org/2000/svg">
                                <path strokeLinecap="round" strokeLinejoin="round" strokeWidth="2" d="M7 16l-4-4m0 0l4-4m-4 4h18"></path>
                            </svg>
                            Voltar para início
                        </span>
                        <span className="absolute flex items-center justify-center w-full h-full text-indigo-600 dark:text-indigo-400 transition-all duration-300 transform group-hover:translate-x-full ease font-semibold text-lg">
                            Voltar para início
                        </span>
                        <span className="relative invisible text-lg">Voltar para início</span>
                    </Link>
                </div>
            </div>
        </div>
    )


}