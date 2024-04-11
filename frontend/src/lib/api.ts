import axios from 'axios';

type props = {
    data: Blob;
    email: string;
};

export const detectIntrusion = async ({ data, email }: props) => {
    try {
        const formData = new FormData();
        const fileName = Date.now().toString() + '.webm';
        formData.append('file', data, fileName);

        const uploadResponse = await axios.post(
            'http://127.0.0.1:8000/api/v1/files/upload',
            formData,
        );

        const file_id = uploadResponse.data?.file_id;

        const detectResponse = await axios.post(
            'http://127.0.0.1:8000/api/v1/detect/intrusion',
            {
                file_id: file_id,
                file_format: 'webm',
                intrusion_type: 'person',
                recipient: email,
            },
            {
                headers: {
                    Accept: 'application/json',
                    'Content-Type': 'application/json',
                },
            },
        );

        console.log(detectResponse);
    } catch (error) {
        console.log(error);
    }
};
