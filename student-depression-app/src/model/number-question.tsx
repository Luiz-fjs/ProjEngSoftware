import React from 'react';
import { QuestionBase } from './question-base';
import { QuestionBaseInterface, onResponseCallbackInterface } from './interfaces';

interface NumberQuestionInterface extends QuestionBaseInterface {
    placeholder: string;
    min: number;
    max: number;
}

export class NumberQuestion extends QuestionBase implements NumberQuestionInterface {
    constructor(props: NumberQuestionInterface) {
        super({ id: props.id, title: props.title, description: props.description });
        this.placeholder = props.placeholder;
        this.min = props.min;
        this.max = props.max;
    }

    placeholder: string;
    min: number;
    max: number;

    buildWidget(onResponseCallback: onResponseCallbackInterface): React.ReactElement {
        return (
            <input
                type="number"
                className="w-full p-2 border border-gray-300 rounded-md dark:bg-gray-800 dark:text-white"
                placeholder={this.placeholder}
                onChange={(e) => {
                    const value = parseInt(e.target.value);

                    if (isNaN(value)) {
                        onResponseCallback.onChange('');
                        return;
                    }

                    if (value >= this.min && value <= this.max) {
                        onResponseCallback.onChange(e.target.value);
                        return;
                    } else {
                        onResponseCallback.onChange('');
                        return;
                    }
                }}
            />
        )
    }
}