import React from 'react';
import { QuestionBase } from './question-base';
import { QuestionBaseInterface, onResponseCallbackInterface } from './interfaces';

interface AlternativeQuestionInterface extends QuestionBaseInterface {
    alternatives: string[];
    labels: string[];
}

export class AlternativeQuestion extends QuestionBase implements AlternativeQuestionInterface {
    constructor(props: AlternativeQuestionInterface) {
        super({ id: props.id, title: props.title, description: props.description});
        this.alternatives = props.alternatives;
        this.labels = props.labels;
    }

    alternatives: string[];
    labels: string[];

    buildWidget(onResponseCallback: onResponseCallbackInterface): React.ReactElement {
        return (
            <div>
                <fieldset>
                    {
                        this.alternatives.map((alternative, index) => (
                            <label key={index} className="flex items-center space-x-3 font-mono dark:text-white border-3 my-2 p-3 rounded-md border-indigo-300 hover:border-indigo-500 dark:hover:border-indigo-400 cursor-pointer">
                                <input
                                    type="radio"
                                    name={`q-${this.id}`}
                                    value={alternative}
                                    onChange={(e) => {
                                        onResponseCallback.onChange(e.target.value);
                                    }}
                                />
                                <span className='font-mono dark:text-white'>{this.labels[index]}</span>
                            </label>
                        ),)
                    }
                </fieldset>
            </div>
        )
    }
}