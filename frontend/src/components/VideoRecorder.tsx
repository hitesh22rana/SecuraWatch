"use client";
import { useCallback, useRef, useState } from "react";
import Webcam from "react-webcam";

import { handleVideoUpload } from "@/lib/api";

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
            handleVideoUpload
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
        <div>
            <Webcam
                height={400}
                width={400}
                audio={false}
                mirrored={false}
                ref={webcamRef}
                videoConstraints={videoConstraints}
            />
            {capturing ? (
                <button onClick={handleStopCaptureClick}>Stop Capture</button>
            ) : (
                <button onClick={handleStartCaptureClick}>Start Capture</button>
            )}
        </div>
    );
}
