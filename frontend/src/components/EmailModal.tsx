'use client';

import { useState } from 'react';
import { isValidEmail } from '@/lib/validators';

type props = {
    handleSetEmail: (email: string) => void;
};

const EmailPopup = ({ handleSetEmail }: props) => {
    const [email, setEmail] = useState<string>('');
    const [errorMessage, setErrorMessage] = useState<string | null>(null);

    const onChange = (e: React.ChangeEvent<HTMLInputElement>) => {
        const emailValue: string = e.target.value;
        setEmail(emailValue);

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
                    <h3 className="text-xl font-bold mb-4">
                        Enter the email on which you want to receive
                        notifications.
                    </h3>
                    <input
                        type="email"
                        name="email"
                        placeholder="Enter email"
                        required={true}
                        value={email}
                        onChange={onChange}
                        className="w-full border p-2 outline-none"
                    />
                    <span className="h-5 text-left font-medium text-sm text-red-500">
                        {errorMessage}
                    </span>
                    <button
                        disabled={!isValidEmail(email)}
                        onClick={() => handleSetEmail(email)}
                        className="rounded bg-blue-500 w-full p-3 text-sm text-white transition-all duration-300 hover:bg-blue-400 focus:outline-none focus:ring-2 focus:ring-gray-400 disabled:cursor-not-allowed hover:disabled:blur-[1px] sm:py-3 sm:text-xl"
                    >
                        Save
                    </button>
                </div>
            </div>
        </div>
    );
};

export default EmailPopup;
