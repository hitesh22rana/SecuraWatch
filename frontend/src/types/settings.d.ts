export type TSurveillance = 'intrusion' | 'threat';

export type TSettings = {
    email: string | null;
    surveillanceType: TSurveillance | null;
};
