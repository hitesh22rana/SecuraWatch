import Image from 'next/image';
import Link from 'next/link';

export default function Home() {
    return (
        <main className="flex flex-col items-center justify-center w-screen h-screen">
            <Image
                src="/assets/background.jpg"
                alt="background"
                width={1920}
                height={1080}
                className="w-full h-full bg-contain absolute -z-50 brightness-50"
            />

            <Image
                src="/assets/logo.png"
                alt="logo"
                width={400}
                height={400}
                className="w-auto h-auto"
            />

            <Link
                href="/surveillance"
                className="text-white text-xl rounded border-2 px-4 py-2 my-10 hover:brightness-75 transition-all duration-150"
            >
                Get Started
            </Link>
        </main>
    );
}
