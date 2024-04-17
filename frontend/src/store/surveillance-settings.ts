import { create } from 'zustand';
import { createTrackedSelector } from 'react-tracked';

import { TSurveillance } from '@/types/settings';

interface Settings {
    email: string | null;
    surveillanceType: TSurveillance | null;

    setEmail: (email: string) => void;
    setSurveillanceType: (surveillanceType: TSurveillance) => void;
    resetSurveillanceSettings: () => void;
}

const _useSurveillanceSettings = create<Settings>((set, get) => ({
    email: null,
    surveillanceType: null,

    setEmail: (email: string) => set({ email }),
    setSurveillanceType: (surveillanceType: TSurveillance) =>
        set({ surveillanceType }),
    resetSurveillanceSettings: () =>
        set({ email: null, surveillanceType: null }),
}));

const useSurveillanceSettings = createTrackedSelector(_useSurveillanceSettings);
export default useSurveillanceSettings;
