import { AlternativeQuestion, AlternativeQuestionInterface } from '../model/alternative-question';
import { DateQuestion, DateQuestionInterface } from '../model/date-question';
import { NumberQuestion, NumberQuestionInterface } from '../model/number-question';
import { SliderQuestion, SliderQuestionInterface } from '../model/slider-question';
import { QuestionWithLayoutDecorator } from '../model/question-with-layout-decorator';
import { QuestionBase } from '../model/question-base';

export type RawQuestion = {
    type: string;
    data: any;
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
                    id: data.id,
                    title: data.title,
                    description: data.description ?? '',
                    alternatives: data.alternatives ?? [],
                    labels: data.labels ?? (data.alternatives ?? [])
                } as any;

                const q = new AlternativeQuestion(props);
                return new QuestionWithLayoutDecorator(q);
            }

            case 'date': {
                const props: DateQuestionInterface = {
                    id: data.id,
                    title: data.title,
                    description: data.description ?? '',
                    min: data.min,
                    max: data.max,
                } as any;

                const q = new DateQuestion(props);
                return new QuestionWithLayoutDecorator(q);
            }

            case 'number': {
                const props: NumberQuestionInterface = {
                    id: data.id,
                    title: data.title,
                    description: data.description ?? '',
                    placeholder: data.placeholder ?? '',
                    min: data.min ?? 0,
                    max: data.max ?? 0,
                } as any;

                const q = new NumberQuestion(props);
                return new QuestionWithLayoutDecorator(q);
            }

            case 'slider': {
                const props: SliderQuestionInterface = {
                    id: data.id,
                    title: data.title,
                    description: data.description ?? '',
                    min: data.min,
                    max: data.max,
                    step: data.step,
                    defaultValue: data.defaultValue,
                    labels: data.labels,
                } as any;

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
