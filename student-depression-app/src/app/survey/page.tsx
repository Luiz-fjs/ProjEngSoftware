'use client'
import SurveyInit from "../../../public/svgs/survey-init";
import Link from "next/link";

export default function Home() {

  return (
    <div className="min-h-screen bg-gradient-to-br from-blue-50 via-indigo-50 to-purple-50 dark:from-gray-900 dark:via-indigo-900 dark:to-purple-900 flex flex-col">
      <div className="flex-1 px-6 py-12">
        {/* Header */}
        <div className="text-center mb-8">
          <div className="inline-block">
            <SurveyInit className="w-32 h-32 mx-auto" />
          </div>
          <h1 className="text-3xl font-bold bg-gradient-to-r from-indigo-600 to-purple-600 dark:from-indigo-400 dark:to-purple-400 bg-clip-text text-transparent mt-4">
            Vamos Começar!
          </h1>
        </div>

        {/* Content Cards */}
        <div className="max-w-4xl mx-auto space-y-6">
          <div className="bg-white/80 dark:bg-gray-800/80 backdrop-blur-sm rounded-2xl p-6 shadow-xl border border-white/20 dark:border-gray-700/20">
            <div className="flex items-start space-x-4">
              <span className="text-2xl">👋</span>
              <div>
                <h3 className="text-lg font-semibold text-gray-800 dark:text-gray-100 mb-2">
                  Olá! Que bom ter você aqui
                </h3>
                <p className="text-gray-600 dark:text-gray-300 leading-relaxed">
                  Vamos começar com algumas perguntas sobre você e sua rotina.
                  São questões simples do dia a dia - nada muito complicado, prometo!
                </p>
              </div>
            </div>
          </div>

          <div className="bg-white/80 dark:bg-gray-800/80 backdrop-blur-sm rounded-2xl p-6 shadow-xl border border-white/20 dark:border-gray-700/20">
            <div className="flex items-start space-x-4">
              <span className="text-2xl">🎯</span>
              <div>
                <h3 className="text-lg font-semibold text-gray-800 dark:text-gray-100 mb-2">
                  Nosso Objetivo
                </h3>
                <p className="text-gray-600 dark:text-gray-300 leading-relaxed">
                  O objetivo é entender melhor como você tem se sentido ultimamente.
                  Pode ser sobre estudos, trabalho, sono, ou qualquer coisa que faça parte da sua vida.
                </p>
              </div>
            </div>
          </div>

          <div className="bg-white/80 dark:bg-gray-800/80 backdrop-blur-sm rounded-2xl p-6 shadow-xl border border-white/20 dark:border-gray-700/20">
            <div className="flex items-start space-x-4">
              <span className="text-2xl">🔒</span>
              <div>
                <h3 className="text-lg font-semibold text-gray-800 dark:text-gray-100 mb-2">
                  Privacidade Garantida
                </h3>
                <p className="text-gray-600 dark:text-gray-300 leading-relaxed font-semibold">
                  Seus dados são tratadors de forma anonima e segura.
                  Ninguém vai saber suas respostas, e elas não vão ser usadas para nada além de melhorar nossa análise.
                </p>
              </div>
            </div>
          </div>

          <div className="bg-gradient-to-r from-orange-50 to-red-50 dark:from-orange-900/20 dark:to-red-900/20 border border-orange-200 dark:border-orange-700/50 rounded-2xl p-6 shadow-xl">
            <div className="flex items-start space-x-4">
              <span className="text-2xl">⚠️</span>
              <div>
                <h3 className="text-lg font-semibold text-orange-800 dark:text-orange-300 mb-2">
                  Lembrete Importante
                </h3>
                <p className="text-orange-700 dark:text-orange-200 leading-relaxed">
                  <span className="font-bold">Só um lembrete importante:</span> Esse teste usa IA para detectar alguns padrões,
                  mas <span className="font-bold">não é um diagnóstico médico de verdade.</span>
                  Se você está passando por algo pesado, vale a pena conversar com um psicólogo ou psiquiatra.
                </p>
              </div>
            </div>
          </div>

          <div className="bg-gradient-to-r mb-25 from-green-50 to-blue-50 dark:from-green-900/20 dark:to-blue-900/20 border border-green-200 dark:border-green-700/50 rounded-2xl p-6 shadow-xl">
            <div className="flex items-start space-x-4">
              <span className="text-2xl">💚</span>
              <div>
                <h3 className="text-lg font-semibold text-green-800 dark:text-green-300 mb-2">
                  Cuidar de Si É Importante
                </h3>
                <p className="text-green-700 dark:text-green-200 leading-relaxed">
                  E lembra: não tem problema nenhum em pedir ajuda quando a gente precisa.
                  Na verdade, isso mostra que você está cuidando de si mesmo.
                </p>
              </div>
            </div>
          </div>
        </div>
      </div>

      {/* Action Button */}
      <div className="fixed bottom-0 left-0 right-0 p-4 bg-gradient-to-t from-white/90 to-transparent dark:from-gray-900/90 backdrop-blur-sm">
        <Link href={"/survey/gender"}>
          <button className="w-full group relative overflow-hidden bg-gradient-to-r from-indigo-600 via-purple-600 to-pink-600 hover:from-indigo-700 hover:via-purple-700 hover:to-pink-700 text-white font-bold py-4 px-8 rounded-2xl shadow-lg transform hover:scale-105 active:scale-95 transition-all duration-300 cursor-pointer">
            <span className="relative z-10 text-2xl flex items-center justify-center space-x-2">
              <span>🚀</span>
              <span>Iniciar Questionário</span>
            </span>
            <div className="absolute inset-0 bg-gradient-to-r from-white/20 to-transparent opacity-0 group-hover:opacity-100 transition-opacity duration-300"></div>
          </button>
        </Link>
      </div>
    </div>
  );
}