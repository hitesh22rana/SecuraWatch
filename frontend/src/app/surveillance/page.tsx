'use client';

import Image from 'next/image';

import SurveillanceSettingsModal from '@/components/SurveillanceSettingsModal';
import VideoRecorder from '@/components/VideoRecorder';

import useSettings from '@/store/surveillance-settings';

export default function Home() {
    const { email, surveillanceType } = useSettings();

    return (
        <main className="flex flex-col items-center justify-center w-screen h-screen">
            <Image
                src="/assets/background-surveillance.jpg"
                alt="background-surveillance"
                width={1920}
                height={1080}
                className="w-full h-full bg-contain absolute -z-50 brightness-50"
            />

            {email && surveillanceType ? (
                <VideoRecorder />
            ) : (
                <SurveillanceSettingsModal />
            )}
        </main>
    );
}
