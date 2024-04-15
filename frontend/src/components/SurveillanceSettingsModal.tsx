'use client';

import { useState } from 'react';

import useSettings from '@/store/surveillance-settings';
import { isValidEmail } from '@/lib/validators';
import { TSurveillance } from '@/types/settings';

const SurveillanceSettingsModal = () => {
    const { setEmail, setSurveillanceType } = useSettings();

    const [_email, _setEmail] = useState<string>('');
    const [_surveillanceType, _setSurveillanceType] =
        useState<TSurveillance>('intrusion');
    const [errorMessage, setErrorMessage] = useState<string | null>(null);

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
        <div className="flex items-center justify-center h-screen">
            <div className="fixed top-0 left-0 w-full h-full bg-opacity-50 flex items-center justify-center">
                <div className="flex flex-col items-start justify-center bg-white rounded shadow-lg w-[500px] gap-2 h-auto px-3 py-4 z-[9999]">
                    <h2 className="text-2xl font-bold mb-4">
                        Surveillance Settings
                    </h2>

                    <div className="relative h-full w-full">
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
                    <select
                        value={_surveillanceType}
                        onChange={(e) =>
                            _setSurveillanceType(
                                e.target.value as TSurveillance,
                            )
                        }
                        className="w-full border p-2 outline-none"
                    >
                        <option value="intrusion">Intrusion</option>
                        <option value="threat">Threat</option>
                    </select>
                    <span className="h-5 text-left font-medium text-sm text-red-500">
                        {errorMessage}
                    </span>
                    <button
                        disabled={!isValidEmail(_email)}
                        onClick={() => {
                            setEmail(_email);
                            setSurveillanceType(_surveillanceType);
                        }}
                        className="rounded bg-blue-500 w-full p-3 text-sm text-white transition-all duration-300 hover:bg-blue-400 focus:outline-none focus:ring-2 focus:ring-gray-400 disabled:cursor-not-allowed hover:disabled:blur-[1px] sm:py-3 sm:text-xl"
                    >
                        Next
                    </button>
                </div>
            </div>
        </div>
    );
};

export default SurveillanceSettingsModal;
