import { create } from 'zustand';
import { createTrackedSelector } from 'react-tracked';

import { TSurveillance } from '@/types/settings';

interface Settings {
    email: string | null;
    surveillanceType: TSurveillance | null;

    setEmail: (email: string) => void;
    setSurveillanceType: (surveillanceType: TSurveillance) => void;
}

const _useSettings = create<Settings>((set, get) => ({
    email: null,
    surveillanceType: null,

    setEmail: (email: string) => set({ email }),
    setSurveillanceType: (surveillanceType: TSurveillance) =>
        set({ surveillanceType }),
}));

const useSettings = createTrackedSelector(_useSettings);
export default useSettings;
