import Robot from '../../public/svgs/robot';
import Link from 'next/link';

export default function Home() {
  return (
    <div className="min-h-screen bg-gradient-to-br from-blue-50 via-indigo-50 to-purple-50 dark:from-gray-900 dark:via-indigo-900 dark:to-purple-900 flex flex-col">
      <div className="flex-1 flex flex-col items-center justify-center px-6 py-12">
        {/* Header Section */}
        <div className="text-center mb-8">
          <Robot className='h-32 w-32 fill-indigo-600 stroke-indigo-800 dark:fill-indigo-400 dark:stroke-indigo-200 transition-colors duration-300' />
        </div>
        
        {/* Title Section */}
        <div className="text-center mb-12 max-w-4xl">
          <h1 className="text-4xl md:text-5xl font-bold bg-gradient-to-r from-indigo-600 via-purple-600 to-pink-600 dark:from-indigo-400 dark:via-purple-400 dark:to-pink-400 bg-clip-text text-transparent mb-6 leading-tight">
            Avaliação de Risco de Depressão Estudantil
          </h1>
        </div>

        {/* Content Cards */}
        <div className="max-w-4xl w-full space-y-6 mb-8">
          <div className="bg-white/80 dark:bg-gray-800/80 backdrop-blur-sm rounded-2xl p-8 shadow-xl border border-white/20 dark:border-gray-700/20 transform hover:scale-105 transition-all duration-300">
            <div className="flex items-start space-x-4">
              <div className="flex-shrink-0">
                <div className="w-12 h-12 bg-gradient-to-r from-indigo-500 to-purple-500 rounded-full flex items-center justify-center">
                  <span className="text-white text-xl">🤖</span>
                </div>
              </div>
              <div>
                <h3 className="text-lg font-semibold text-gray-800 dark:text-gray-100 mb-2">
                  Tecnologia Avançada de IA
                </h3>
                <p className="text-gray-600 dark:text-gray-300 leading-relaxed">
                  Bem-vindo(a) à nossa ferramenta de avaliação de saúde mental estudantil, desenvolvida com tecnologia de inteligência artificial.
                </p>
              </div>
            </div>
          </div>

          <div className="bg-white/80 dark:bg-gray-800/80 backdrop-blur-sm rounded-2xl p-8 shadow-xl border border-white/20 dark:border-gray-700/20 transform hover:scale-105 transition-all duration-300">
            <div className="flex items-start space-x-4">
              <div className="flex-shrink-0">
                <div className="w-12 h-12 bg-gradient-to-r from-green-500 to-blue-500 rounded-full flex items-center justify-center">
                  <span className="text-white text-xl">📊</span>
                </div>
              </div>
              <div>
                <h3 className="text-lg font-semibold text-gray-800 dark:text-gray-100 mb-2">
                  Análise Personalizada
                </h3>
                <p className="text-gray-600 dark:text-gray-300 leading-relaxed">
                  Este sistema analisa suas respostas para fornecer uma estimativa personalizada do risco de transtornos depressivos, ajudando a identificar quando pode ser recomendável buscar apoio profissional.
                </p>
              </div>
            </div>
          </div>

          <div className="bg-white/80 mb-25 dark:bg-gray-800/80 backdrop-blur-sm rounded-2xl p-8 shadow-xl border border-white/20 dark:border-gray-700/20 transform hover:scale-105 transition-all duration-300">
            <div className="flex items-start space-x-4">
              <div className="flex-shrink-0">
                <div className="w-12 h-12 bg-gradient-to-r from-red-500 to-orange-500 rounded-full flex items-center justify-center">
                  <span className="text-white text-xl">⚕️</span>
                </div>
              </div>
              <div>
                <h3 className="text-lg font-semibold text-gray-800 dark:text-gray-100 mb-2">
                  Aviso Importante
                </h3>
                <p className="text-gray-600 dark:text-gray-300 leading-relaxed">
                  <strong className="text-orange-600 dark:text-orange-400">Importante:</strong> Esta ferramenta é apenas educativa e não substitui avaliação médica profissional. Em caso de necessidade, procure sempre um psicólogo ou psiquiatra qualificado.
                </p>
              </div>
            </div>
          </div>
        </div>
      </div>

      {/* Action Button */}
      <div className="fixed bottom-0 left-0 right-0 p-4 bg-gradient-to-t from-white/90 to-transparent dark:from-gray-900/90 backdrop-blur-sm">
        <Link href={"/survey"}>
          <button className="w-full group relative overflow-hidden bg-gradient-to-r from-indigo-600 via-purple-600 to-pink-600 hover:from-indigo-700 hover:via-purple-700 hover:to-pink-700 text-white font-bold py-4 px-8 rounded-2xl shadow-lg transform hover:scale-105 active:scale-95 transition-all duration-300 cursor-pointer">
            <span className="relative z-10 text-2xl">
              🚀 Começar Avaliação
            </span>
            <div className="absolute inset-0 bg-gradient-to-r from-white/20 to-transparent opacity-0 group-hover:opacity-100 transition-opacity duration-300"></div>
          </button>
        </Link>
      </div>
    </div>
  );
}