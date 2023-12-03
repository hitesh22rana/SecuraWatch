"use client";

import EmailPopup from "@/components/EmailModal";
import VideoRecorder from "@/components/VideoRecorder";
import Image from "next/image";

import { useEffect, useState } from "react";

export default function Home() {
    const [email, setEmail] = useState<string | null>();

    useEffect(() => {
        setEmail(localStorage.getItem("securawatch_notification_email"));
    }, []);

    const handleSetEmail = (email: string) => {
        setEmail(email);
    };

    return (
        <main className="flex flex-col items-center justify-center w-screen h-screen">
            <Image
                src="/assets/background-surveillance.jpg"
                alt="background-surveillance"
                width={1920}
                height={1080}
                className="w-full h-full bg-contain absolute -z-50 brightness-50"
            />

            {email ? (
                <VideoRecorder email={email} />
            ) : (
                <EmailPopup handleSetEmail={handleSetEmail} />
            )}
        </main>
    );
}
