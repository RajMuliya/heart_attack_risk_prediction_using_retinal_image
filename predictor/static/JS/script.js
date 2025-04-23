document.addEventListener('DOMContentLoaded', function() {
    // Elements
    const heroSection = document.getElementById('hero-section');
    const uploadSection = document.getElementById('upload-section');
    const uploadContent = document.getElementById('upload-content');
    const uploadArea = document.getElementById('upload-area');
    const uploadPlaceholder = document.getElementById('upload-placeholder');
    const imagePreview = document.getElementById('image-preview');
    const previewImg = document.getElementById('preview-img');
    const fileInput = document.getElementById('file-input');
    const removeImageBtn = document.getElementById('remove-image-btn');
    const analyzeBtn = document.getElementById('analyze-btn');
    const tryNowBtn = document.getElementById('try-now-btn');
    const resetBtn = document.getElementById('reset-btn');
    const resultsImg = document.getElementById('results-img');

    const toast = document.getElementById('toast');
    const toastMessage = document.getElementById('toast-message');
    const currentYearElement = document.getElementById('current-year');
    
    // Set current year in footer
    currentYearElement.textContent = new Date().getFullYear();
    
    // Variables
    let currentImage = null;
    
    // Event Listeners
    tryNowBtn.addEventListener('click', scrollToUpload);
    uploadPlaceholder.addEventListener('click', triggerFileInput);
    fileInput.addEventListener('change', handleFileSelect);
    removeImageBtn.addEventListener('click', removeImage);
    analyzeBtn.addEventListener('click', analyzeImage);
    resetBtn.addEventListener('click', resetAnalysis);
    
    // Drag and drop functionality
    uploadArea.addEventListener('dragover', function(e) {
      e.preventDefault();
      uploadArea.style.borderColor = 'var(--primary)';
    });
    
    uploadArea.addEventListener('dragleave', function(e) {
      e.preventDefault();
      uploadArea.style.borderColor = 'var(--gray-300)';
    });
    
    uploadArea.addEventListener('drop', function(e) {
      e.preventDefault();
      uploadArea.style.borderColor = 'var(--gray-300)';
      
      if (e.dataTransfer.files && e.dataTransfer.files[0]) {
        handleFile(e.dataTransfer.files[0]);
      }
    });
    
    // Functions
    function scrollToUpload() {
      uploadSection.scrollIntoView({ behavior: 'smooth' });
    }
    
    function triggerFileInput() {
      fileInput.click();
    }
    
    function handleFileSelect(e) {
      if (e.target.files && e.target.files[0]) {
        handleFile(e.target.files[0]);
      }
    }
    
    // Check if file is an image
    function handleFile(file) {
      if (!file.type.match('image.*')) {
        showToast('Please select an image file');
        return;
      }
      
      const reader = new FileReader();
      
      reader.onload = function(e) {
        previewImg.src = e.target.result;
        resultsImg.src = e.target.result;
        uploadPlaceholder.style.display = 'none';
        imagePreview.style.display = 'block';
        analyzeBtn.disabled = false;
        currentImage = file;
      };
      
      reader.readAsDataURL(file);
    }
    
    function removeImage() {
      uploadPlaceholder.style.display = 'flex';
      imagePreview.style.display = 'none';
      fileInput.value = '';
      previewImg.src = '';
      analyzeBtn.disabled = true;
      currentImage = null;
    }
    
    function showToast(message) {
      toastMessage.textContent = message;
      toast.classList.remove('hidden');
      
      setTimeout(() => {
        toast.classList.add('hidden');
      }, 3000);
    }
  

});