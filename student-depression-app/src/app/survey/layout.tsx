import { SurveyProvider } from "../context/survey_context";

export default function RootLayout({
  children,
}: Readonly<{
  children: React.ReactNode;
}>) {

  return (
    <div>
      <SurveyProvider >
        {children}
      </SurveyProvider>
    </div>
  );
}