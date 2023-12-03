"use client";
import { useCallback, useRef, useState } from "react";
import Webcam from "react-webcam";

import { detectIntrusion } from "@/lib/api";

export default function WebcamVideo() {
    const webcamRef = useRef<Webcam>(null);
    const mediaRecorderRef = useRef<MediaRecorder | null>(null);
    const captureIntervalRef = useRef<NodeJS.Timer | null>(null);
    const [capturing, setCapturing] = useState<boolean>(false);

    const handleStartCaptureClick = useCallback(() => {
        setCapturing(true);

        captureIntervalRef.current = setInterval(() => {
            if (mediaRecorderRef.current) {
                mediaRecorderRef.current.stop();
                mediaRecorderRef.current.start();
            }
        }, 10000);

        // Set up media recorder
        mediaRecorderRef.current = new MediaRecorder(
            webcamRef.current!.stream as MediaStream,
            {
                mimeType: "video/webm",
            }
        );
        mediaRecorderRef.current.addEventListener(
            "dataavailable",
            detectIntrusion
        );
        mediaRecorderRef.current.start();
    }, [webcamRef, setCapturing, mediaRecorderRef]);

    const handleStopCaptureClick = useCallback(() => {
        mediaRecorderRef.current!.stop();
        mediaRecorderRef.current = null;
        setCapturing(false);

        if (captureIntervalRef.current) {
            clearInterval(captureIntervalRef!.current);
        }
    }, [mediaRecorderRef, setCapturing]);

    const videoConstraints = {
        width: 420,
        height: 420,
        facingMode: "user",
    };

    return (
        <div className="flex flex-col items-center justify-center gap-4 h-full w-full p-10">
            <Webcam
                className="rounded outline-dotted"
                height={640}
                width={640}
                audio={false}
                mirrored={false}
                ref={webcamRef}
                videoConstraints={videoConstraints}
            />
            {capturing ? (
                <button
                    onClick={handleStopCaptureClick}
                    className="bg-red-500 text-white font-semibold transition-all duration-150 hover:bg-red-400 px-8 py-4 rounded"
                >
                    Stop Capture
                </button>
            ) : (
                <button
                    onClick={handleStartCaptureClick}
                    className="bg-green-500 text-white font-semibold transition-all duration-150 hover:bg-green-400 px-8 py-4 rounded"
                >
                    Start Capture
                </button>
            )}
        </div>
    );
}
