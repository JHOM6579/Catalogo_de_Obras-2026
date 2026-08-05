document.addEventListener('DOMContentLoaded', () => {
    const galleries = document.querySelectorAll('[data-gallery]');

    galleries.forEach((gallery) => {
        const images = Array.from(
            gallery.querySelectorAll('[data-gallery-image]')
        );

        const thumbnails = Array.from(
            gallery.querySelectorAll('[data-gallery-thumbnail]')
        );

        const previousButton = gallery.querySelector('[data-gallery-prev]');
        const nextButton = gallery.querySelector('[data-gallery-next]');
        const currentCounter = gallery.querySelector('[data-gallery-current]');

        if (images.length === 0) {
            return;
        }

        let currentIndex = 0;

        const showImage = (index) => {
            currentIndex = (index + images.length) % images.length;

            images.forEach((image, imageIndex) => {
                image.classList.toggle(
                    'is-active',
                    imageIndex === currentIndex
                );
            });

            thumbnails.forEach((thumbnail, thumbnailIndex) => {
                thumbnail.classList.toggle(
                    'is-active',
                    thumbnailIndex === currentIndex
                );
            });

            if (currentCounter) {
                currentCounter.textContent = String(currentIndex + 1);
            }
        };

        previousButton?.addEventListener('click', () => {
            showImage(currentIndex - 1);
        });

        nextButton?.addEventListener('click', () => {
            showImage(currentIndex + 1);
        });

        thumbnails.forEach((thumbnail) => {
            thumbnail.addEventListener('click', () => {
                const index = Number(thumbnail.dataset.index);

                if (Number.isInteger(index)) {
                    showImage(index);
                }
            });
        });

        gallery.setAttribute('tabindex', '0');

        gallery.addEventListener('keydown', (event) => {
            if (event.key === 'ArrowLeft') {
                showImage(currentIndex - 1);
            }

            if (event.key === 'ArrowRight') {
                showImage(currentIndex + 1);
            }
        });

        showImage(0);
    });
});