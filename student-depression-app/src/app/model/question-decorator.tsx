import React from 'react';
import { QuestionBase } from './question-base';
import { onResponseCallbackInterface } from './interfaces';

export abstract class QuestionDecorator extends QuestionBase {
    protected question: QuestionBase;

    constructor(question: QuestionBase) {
        super({ id: question.id, title: question.title, description: question.description});
        this.question = question;
    }

    buildWidget(onResponseCallback: onResponseCallbackInterface): React.ReactElement {
        return this.question.buildWidget(onResponseCallback);
    }
}