const images = document.querySelectorAll('.slide img');
        const prevBtn = document.getElementById('prevBtn');
        const nextBtn = document.getElementById('nextBtn');
        let currentImageIndex = 0;

        function showImage(index) {
            images.forEach((img, idx) => {
                img.style.transform = `translateX(-${index * 100}%)`; // Move images horizontally
            });
        }

        function showNextImage() {
            currentImageIndex = (currentImageIndex + 1) % images.length;
            showImage(currentImageIndex);
        }

        function showPrevImage() {
            currentImageIndex = (currentImageIndex - 1 + images.length) % images.length;
            showImage(currentImageIndex);
        }

        // Button click event listeners
        prevBtn.addEventListener('click', showPrevImage);
        nextBtn.addEventListener('click', showNextImage);

        // Automatic slideshow
        setInterval(showNextImage, 5000);