import axios from 'axios';

type props = {
    data: Blob;
    email: string;
};

const BACKEND_API_URL = process.env.NEXT_PUBLIC_BACKEND_API_URL;

export const detectIntrusion = async ({ data, email }: props) => {
    try {
        const formData = new FormData();
        const fileName = Date.now().toString() + '.webm';
        formData.append('file', data, fileName);

        const uploadResponse = await axios.post(
            BACKEND_API_URL + '/files/upload',
            formData,
        );

        const file_id = uploadResponse.data?.file_id;

        await axios.post(BACKEND_API_URL + '/detect/intrusion', {
            file_id: file_id,
            file_format: 'webm',
            intrusion_type: 'person',
            recipient: email,
        });
    } catch (error) {
        console.log(error);
    }
};

export const detectThreat = async ({ data, email }: props) => {
    try {
        const formData = new FormData();
        const fileName = Date.now().toString() + '.webm';
        formData.append('file', data, fileName);

        const uploadResponse = await axios.post(
            BACKEND_API_URL + '/files/upload',
            formData,
        );

        const file_id = uploadResponse.data?.file_id;

        await axios.post(BACKEND_API_URL + '/detect/threat', {
            file_id: file_id,
            file_format: 'webm',
            intrusion_type: 'person',
            recipient: email,
        });
    } catch (error) {
        console.log(error);
    }
};
