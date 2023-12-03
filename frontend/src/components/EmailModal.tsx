"use client";

import { useState } from "react";

type props = {
    handleSetEmail: (email: string) => void;
};

const EmailPopup = ({ handleSetEmail }: props) => {
    const [email, setEmail] = useState("");

    return (
        <div className="flex items-center justify-center h-screen">
            <div className="fixed top-0 left-0 w-full h-full bg-opacity-50 flex items-center justify-center">
                <div className="flex flex-col items-center justify-center bg-white rounded shadow-lg w-[500px] gap-2 h-auto px-3 py-4 z-[9999]">
                    <h2 className="text-xl font-bold mb-4">
                        Enter the email on which you want to receive
                        notifications.
                    </h2>
                    <input
                        type="email"
                        id="userEmail"
                        placeholder="Enter email"
                        className="w-full border p-2 mb-4 outline-none"
                        value={email}
                        onChange={(e) => setEmail(e.target.value)}
                    />
                    <button
                        onClick={() => handleSetEmail(email)}
                        className="bg-blue-500 text-white p-3 rounded w-full"
                    >
                        Save
                    </button>
                </div>
            </div>
        </div>
    );
};

export default EmailPopup;
