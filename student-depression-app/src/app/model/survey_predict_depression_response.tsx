import { FeatureFeedback } from "../survey/component/detailed_feedback";

export interface SurveyPredictDepressionResponse {
    prediction: number;
    probability: number[];
    depressionRisk: string;
    feature_feedback: FeatureFeedback[];
}