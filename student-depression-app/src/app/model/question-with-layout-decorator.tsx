import React from 'react';
import { QuestionDecorator } from './question-decorator';
import { QuestionBase } from './question-base';
import { onResponseCallbackInterface } from './interfaces';

export class QuestionWithLayoutDecorator extends QuestionDecorator {
    constructor(question: QuestionBase) {
        super(question);
    }

    buildWidget(onResponseCallback: onResponseCallbackInterface): React.ReactElement {
        return (
            <div className="flex-1 p-6 mt-4">
                <h2 className="text-[2rem] font-bold text-center dark:text-white">
                    {this.title}
                </h2>
                <p className="text-[1.3rem] text-indigo-500 mb-4 text-center">
                    {this.description}
                </p>
                {super.buildWidget(onResponseCallback)}
            </div>
        )
    }
}