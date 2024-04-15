'use client';

import { useCallback, useRef, useState } from 'react';
import Image from 'next/image';
import Webcam from 'react-webcam';

import useSettings from '@/store/surveillance-settings';
import { detectIntrusion, detectThreat } from '@/lib/api';

export default function WebcamVideo() {
    const webcamRef = useRef<Webcam>(null);
    const mediaRecorderRef = useRef<MediaRecorder | null>(null);
    const captureIntervalRef = useRef<NodeJS.Timeout | null>(null);
    const [capturing, setCapturing] = useState<boolean>(false);
    const { email, surveillanceType } = useSettings();

    const handleStartCaptureClick = useCallback(() => {
        setCapturing(true);

        captureIntervalRef.current = setInterval(() => {
            if (mediaRecorderRef.current) {
                mediaRecorderRef.current.stop();
                mediaRecorderRef.current.start();
            }
        }, 10000);

        mediaRecorderRef.current = new MediaRecorder(
            webcamRef.current!.stream as MediaStream,
            {
                mimeType: 'video/webm',
            },
        );

        mediaRecorderRef.current.addEventListener('dataavailable', (event) => {
            if (event.data.size > 0) {
                switch (surveillanceType) {
                    case 'intrusion':
                        detectIntrusion({
                            data: event.data,
                            email: email as string,
                        });
                        break;
                    case 'threat':
                        detectThreat({
                            data: event.data,
                            email: email as string,
                        });
                        break;
                    default:
                        break;
                }
            }
        });
        mediaRecorderRef.current.start();
    }, [webcamRef, setCapturing, mediaRecorderRef, email, surveillanceType]);

    const handleStopCaptureClick = useCallback(() => {
        mediaRecorderRef.current!.stop();
        mediaRecorderRef.current = null;
        setCapturing(false);

        if (captureIntervalRef.current) {
            clearInterval(captureIntervalRef!.current);
        }
    }, [mediaRecorderRef, setCapturing]);

    const videoConstraints = {
        width: 640,
        height: 640,
        facingMode: 'user',
    };

    return (
        <div className="relative flex flex-col items-center justify-center gap-4 p-10">
            <Image
                src="/assets/recording.png"
                alt="recording"
                width={100}
                height={100}
                className={`${
                    capturing ? 'block' : 'hidden'
                } absolute top-8 left-10 w-32 h-24`}
            />
            <Webcam
                height={640}
                width={640}
                audio={false}
                mirrored={false}
                ref={webcamRef}
                imageSmoothing={true}
                videoConstraints={videoConstraints}
            />
            {capturing ? (
                <button
                    onClick={handleStopCaptureClick}
                    className="bg-red-500 text-white rounded px-8 py-2 transition-all duration-150 hover:bg-red-400"
                >
                    Stop Capture
                </button>
            ) : (
                <button
                    onClick={handleStartCaptureClick}
                    className="bg-green-500 text-white rounded px-8 py-2 transition-all duration-150 hover:bg-green-400"
                >
                    Start Capture
                </button>
            )}
        </div>
    );
}
