import React from 'react';
import { QuestionBaseInterface, onResponseCallbackInterface } from './interfaces';

export abstract class QuestionBase implements QuestionBaseInterface {
    constructor(props: QuestionBaseInterface) {
        this.id = props.id;
        this.title = props.title;
        this.description = props.description;
    }

    id: string;
    title: string;
    description: string;
    response: string | undefined;

    abstract buildWidget(onResponseCallback: onResponseCallbackInterface): React.ReactElement;
}