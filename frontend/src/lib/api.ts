export const handleVideoUpload = async ({ data }: { data: Blob }) => {
    if (data) {
        try {
            const formData = new FormData();
            const fileName = Date.now().toString() + ".webm";
            formData.append("file", data, fileName);

            await fetch("http://127.0.0.1:8000/api/v1/files/upload", {
                method: "POST",
                body: formData,
            });
        } catch (error) {
            console.log(error);
        }
    }
};
