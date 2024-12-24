async function uploadFile() {
    const formData = new FormData(document.getElementById('uploadForm'));
    const statusElement = document.getElementById('status');
    const spinner = document.getElementById('spinner');

    statusElement.textContent = "";
    spinner.style.display = "block";

    try {
        const response = await fetch('/convert', {
            method: 'POST',
            body: formData,
        });
        const data = await response.json();

        if (response.ok) {
            statusElement.style.color = "#2ecc71";
            statusElement.textContent = data.message;
        } else {
            statusElement.style.color = "#e74c3c";
            statusElement.textContent = data.message || "An error occurred.";
        }
    } catch (error) {
        statusElement.style.color = "#e74c3c";
        statusElement.textContent = "Failed to connect to the server.";
    } finally {
        spinner.style.display = "none";
    }
}
