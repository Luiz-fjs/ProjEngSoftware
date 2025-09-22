export default function Home() {
  return (
    <div className="flex flex-col items-center justify-center min-h-screen px-6 bg-gradient-to-b from-blue-50 to-blue-100 text-gray-800">
      
      {/* Logo / Nome */}
      <h1 className="text-4xl sm:text-5xl font-bold mb-6 text-blue-700">
        Terapp.ia
      </h1>

      {/* Subtítulo */}
      <h2 className="text-2xl sm:text-3xl font-semibold mb-4 text-center">
        Cuidar da mente começa pelo autoconhecimento
      </h2>

      {/* Texto explicativo */}
      <p className="max-w-2xl text-center text-lg leading-relaxed mb-8">
        Estamos desenvolvendo uma ferramenta online para auxiliar estudantes 
        universitários a refletirem sobre sua saúde mental. 
        Com o <strong>Terapp.ia</strong>, você poderá responder a um questionário 
        e nossa inteligência artificial fará uma análise baseada em dados de pesquisas 
        internacionais, indicando a chance de estar passando por sintomas relacionados 
        à depressão. <br/><br/>
        ⚠️ <em>Importante: o Terapp.ia não substitui acompanhamento médico ou psicológico. 
        Ele é apenas uma ferramenta de apoio e conscientização.</em>
      </p>

      {/* "Em breve" */}
      <span className="text-xl font-semibold text-blue-600 animate-pulse">
        🚀 Em breve!
      </span>

    </div>
  );
}