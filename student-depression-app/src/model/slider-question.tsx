import React from 'react';
import { QuestionBase } from './question-base';
import { QuestionBaseInterface, onResponseCallbackInterface } from './interfaces';

export interface SliderQuestionInterface extends QuestionBaseInterface {
    min?: number;
    max?: number;
    step?: number;
    defaultValue?: number;
    labels?: string[];
}

export class SliderQuestion extends QuestionBase implements SliderQuestionInterface {
    constructor(props: SliderQuestionInterface) {
        super({ id: props.id, title: props.title, description: props.description });
        this.min = props.min ?? 0;
        this.max = props.max ?? 5;
        this.step = props.step ?? 1;
        this.labels = props.labels ?? ['0', '1', '2', '3', '4', '5'];
        this.defaultValue = props.defaultValue ?? 0;
    }

    min: number;
    max: number;
    step: number;
    defaultValue: number;
    labels: string[];

    buildWidget(onResponseCallback: onResponseCallbackInterface): React.ReactElement {
        return (
            <div>
                <input
                    type="range"
                    className="w-full h-2 bg-gray-200 rounded-lg appearance-none cursor-pointer dark:bg-gray-700"
                    min={this.min}
                    max={this.max}
                    step={this.step}
                    defaultValue={this.defaultValue}
                    onChange={(e) => onResponseCallback.onChange(e.target.value)}
                />
                <div className="flex flex-row justify-between mt-2">
                    {
                        this.labels.map((label, index) => (
                            <span key={index} className="text-sm text-gray-500 dark:text-gray-400 text-ellipsis" >
                                {label}
                            </span>
                        ))
                    }
                </div>
            </div>
        );
    }
}