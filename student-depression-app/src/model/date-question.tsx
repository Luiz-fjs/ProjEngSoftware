import React from 'react';
import { QuestionBase } from './question-base';
import { QuestionBaseInterface, onResponseCallbackInterface } from './interfaces';

export interface DateQuestionInterface extends QuestionBaseInterface {
    min?: string;
    max?: string;
}

export class DateQuestion extends QuestionBase implements DateQuestionInterface {
    constructor(props: DateQuestionInterface) {
        super({ id: props.id, title: props.title, description: props.description });
        this.min = props.min ?? '1940-01-01';
        this.max = props.max ?? '2025-12-31';
    }

    min: string;
    max: string;

    buildWidget(onResponseCallback: onResponseCallbackInterface): React.ReactElement {
        return (
            <input
                type="date"
                className="w-full p-2 border border-gray-300 rounded-md dark:bg-gray-800 dark:text-white"
                onChange={(e) => {
                    const maxDate = new Date(this.max);
                    const selectedDate = new Date(e.target.value);

                    if (selectedDate < maxDate) {
                        onResponseCallback.onChange(e.target.value)
                    } else {
                        onResponseCallback.onChange('')
                    }
                }}
                min={this.min}
                max={this.max}
            />
        )
    }
}