import { AlternativeQuestion, AlternativeQuestionInterface } from '../model/alternative-question';
import { DateQuestion, DateQuestionInterface } from '../model/date-question';
import { NumberQuestion, NumberQuestionInterface } from '../model/number-question';
import { SliderQuestion, SliderQuestionInterface } from '../model/slider-question';
import { QuestionWithLayoutDecorator } from '../model/question-with-layout-decorator';
import { QuestionBase } from '../model/question-base';

export type RawQuestion = {
    type: string;
    data: { [key: string]: string | string[] | number};
}

export function mapQuestions(raw: RawQuestion[]): QuestionBase[] {
    return raw.map((item) => mapQuestion(item)).filter(Boolean) as QuestionBase[];
}

export function mapQuestion(item: RawQuestion): QuestionBase | null {
    const { type, data } = item;

    try {
        switch (type) {
            case 'alternative': {
                const props: AlternativeQuestionInterface = {
                    id: data.id as string,
                    title: data.title as string,
                    description: (data.description ?? '') as string,
                    alternatives: (data.alternatives ?? []) as string[],
                    labels: (data.labels ?? (data.alternatives ?? [])) as string[],
                };

                const q = new AlternativeQuestion(props);
                return new QuestionWithLayoutDecorator(q);
            }

            case 'date': {
                const props: DateQuestionInterface = {
                    id: data.id as string,
                    title: data.title as string,
                    description: (data.description ?? '') as string,
                    min: data.min as string,
                    max: data.max as string,
                };

                const q = new DateQuestion(props);
                return new QuestionWithLayoutDecorator(q);
            }

            case 'number': {
                const props: NumberQuestionInterface = {
                    id: data.id as string,
                    title: data.title as string,
                    description: (data.description ?? '') as string,
                    placeholder: (data.placeholder ?? '') as string,
                    min: (data.min ?? 0) as number,
                    max: (data.max ?? 0) as number,
                };

                const q = new NumberQuestion(props);
                return new QuestionWithLayoutDecorator(q);
            }

            case 'slider': {
                const props: SliderQuestionInterface = {
                    id: data.id as string,
                    title: data.title as string,
                    description: (data.description ?? '') as string,
                    min: data.min as number,
                    max: data.max as number,
                    step: data.step as number,
                    defaultValue: data.defaultValue as number,
                    labels: data.labels as string[],
                };

                const q = new SliderQuestion(props);
                return new QuestionWithLayoutDecorator(q);
            }

            default:
                return null;
        }
    } catch (e) {
        // Em caso de dados inesperados, ignoramos a questão e retornamos null
        return null;
    }
}

export default mapQuestions;
