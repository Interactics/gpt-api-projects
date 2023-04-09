const fileInput = document.getElementById('pdf');
const fileName = document.getElementById('file-name');
const uploadForm = document.getElementById('upload-form');
const summaryText = document.getElementById('summary-text');
const loading = document.getElementById('loading');
const languageSelect = document.getElementById('language'); // Add this line to get the language select element

fileInput.addEventListener('change', () => {
  if (fileInput.files.length) {
    fileName.textContent = fileInput.files[0].name;
  } else {
    fileName.textContent = '';
  }
});
uploadForm.addEventListener('submit', async (e) => {
  e.preventDefault();

  if (!fileInput.files.length) {
    alert('Please select a PDF file to upload.');
    return;
  }

  loading.style.display = 'inline-block';
  summaryText.textContent = '';
  const languageSelect = document.getElementById('language');

  const formData = new FormData();
  formData.append('pdf', fileInput.files[0]);
  formData.append('language', languageSelect.value);

  try {
    const response = await fetch('/upload', { // Remove the query parameter from here
      method: 'POST',
      body: formData,
    });

    const data = await response.json();
    loading.style.display = 'none';

    if (data.error) {
      summaryText.textContent = 'An error occurred while processing the PDF.';
      console.error(data.error);
    } else {
      summaryText.textContent = data.summary;
    }
  } catch (error) {
    loading.style.display = 'none';
    summaryText.textContent = 'An error occurred while processing the PDF.';
  }
});
