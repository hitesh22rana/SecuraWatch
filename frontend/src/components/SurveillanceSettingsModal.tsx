'use client';

import { useState, Fragment, useEffect } from 'react';
import { Button } from '@/components/ui/button';

import useSurveillanceSettings from '@/store/surveillance-settings';
import { isValidEmail } from '@/lib/validators';
import { TSurveillance } from '@/types/settings';

const IntrusionSurveillanceSettingsForm = ({
    onSubmit,
}: {
    onSubmit: () => void;
}) => {
    const [_email, _setEmail] = useState<string>('');
    const [errorMessage, setErrorMessage] = useState<string | null>(null);
    const { setEmail } = useSurveillanceSettings();

    const onChange = (e: React.ChangeEvent<HTMLInputElement>) => {
        const emailValue: string = e.target.value;
        _setEmail(emailValue);

        if (!isValidEmail(emailValue)) {
            setErrorMessage('Invalid email format.');
        } else {
            setErrorMessage(null);
        }
    };

    return (
        <Fragment>
            <div className="relative h-full w-full mt-5">
                <input
                    type="email"
                    name="email"
                    placeholder="Enter email"
                    required={true}
                    value={_email}
                    onChange={onChange}
                    className="peer/input-field h-full w-full rounded border-[1px] p-2 text-gray-500 outline-none placeholder:text-sm focus:outline-none focus:ring-1 focus:ring-gray-400 focus:placeholder:text-transparent"
                />
                <span className="absolute -top-[10px] left-[10px] hidden bg-white text-sm text-gray-400 peer-focus/input-field:block">
                    Enter email
                </span>
            </div>

            <span className="h-5 text-left font-medium text-sm text-red-500">
                {errorMessage}
            </span>

            <Button
                variant="default"
                disabled={!isValidEmail(_email)}
                onClick={() => {
                    setEmail(_email);
                    onSubmit();
                }}
                className="w-full p-5 font-medium text-base disabled:opacity-90 disabled:pointer-events-auto disabled:cursor-not-allowed"
            >
                Next
            </Button>
        </Fragment>
    );
};

const ThreatSurveillanceSettingsForm = ({
    onSubmit,
}: {
    onSubmit: () => void;
}) => {
    const [_email, _setEmail] = useState<string>('');
    const [errorMessage, setErrorMessage] = useState<string | null>(null);
    const { setEmail } = useSurveillanceSettings();

    const onChange = (e: React.ChangeEvent<HTMLInputElement>) => {
        const emailValue: string = e.target.value;
        _setEmail(emailValue);

        if (!isValidEmail(emailValue)) {
            setErrorMessage('Invalid email format.');
        } else {
            setErrorMessage(null);
        }
    };

    return (
        <Fragment>
            <div className="relative h-full w-full mt-5">
                <input
                    type="email"
                    name="email"
                    placeholder="Enter email"
                    required={true}
                    value={_email}
                    onChange={onChange}
                    className="peer/input-field h-full w-full rounded border-[1px] p-2 text-gray-500 outline-none placeholder:text-sm focus:outline-none focus:ring-1 focus:ring-gray-400 focus:placeholder:text-transparent"
                />
                <span className="absolute -top-[10px] left-[10px] hidden bg-white text-sm text-gray-400 peer-focus/input-field:block">
                    Enter email
                </span>
            </div>

            <span className="h-5 text-left font-medium text-sm text-red-500">
                {errorMessage}
            </span>

            <Button
                variant="default"
                disabled={!isValidEmail(_email)}
                onClick={() => {
                    setEmail(_email);
                    onSubmit();
                }}
                className="w-full p-5 font-medium text-base disabled:opacity-90 disabled:pointer-events-auto disabled:cursor-not-allowed"
            >
                Next
            </Button>
        </Fragment>
    );
};

const surveillance = {
    intrusion: IntrusionSurveillanceSettingsForm,
    threat: ThreatSurveillanceSettingsForm,
};

const SurveillanceSettingsModal = () => {
    const { resetSurveillanceSettings, setSurveillanceType } =
        useSurveillanceSettings();

    const [_surveillanceType, _setSurveillanceType] =
        useState<TSurveillance>('intrusion');

    const Surveillance = surveillance[_surveillanceType];

    useEffect(() => {
        resetSurveillanceSettings();
    }, [_surveillanceType, resetSurveillanceSettings]);

    const onSubmit = () => {
        setSurveillanceType(_surveillanceType);
    };

    return (
        <div className="flex items-center justify-center h-screen">
            <div className="fixed top-0 left-0 w-full h-full bg-opacity-50 flex items-center justify-center p-1">
                <div className="flex flex-col items-start justify-center bg-white rounded shadow-lg w-[500px] h-auto px-3 pt-4 pb-2 z-[9999]">
                    <h2 className="text-2xl font-bold mb-4">
                        Surveillance Settings
                    </h2>

                    <div className="flex flex-row items-center justify-center bg-gray-50 shadow mx-auto w-full rounded-lg">
                        <Button
                            variant={
                                _surveillanceType === 'intrusion'
                                    ? 'default'
                                    : 'ghost'
                            }
                            className="h-8 w-full font-medium rounded-none rounded-l-md"
                            onClick={() => _setSurveillanceType('intrusion')}
                        >
                            Intrusion
                        </Button>
                        <Button
                            variant={
                                _surveillanceType === 'threat'
                                    ? 'default'
                                    : 'ghost'
                            }
                            className="h-8 w-full font-medium rounded-none rounded-r-md"
                            onClick={() => _setSurveillanceType('threat')}
                        >
                            Threat
                        </Button>
                    </div>
                    <Surveillance onSubmit={onSubmit} />
                </div>
            </div>
        </div>
    );
};

export default SurveillanceSettingsModal;
