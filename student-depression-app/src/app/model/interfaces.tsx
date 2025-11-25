export interface onResponseCallbackInterface {
    onChange: (value: string) => void;
}

export interface QuestionBaseInterface {
    id: string;
    title: string;
    description: string;
    response?: string;
}