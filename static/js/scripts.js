/*!
* Start Bootstrap - Shop Homepage v5.0.6 (https://startbootstrap.com/template/shop-homepage)
* Copyright 2013-2023 Start Bootstrap
* Licensed under MIT (https://github.com/StartBootstrap/startbootstrap-shop-homepage/blob/master/LICENSE)
*/
// This file is intentionally blank
// Use this file to add JavaScript to your project

document.addEventListener("DOMContentLoaded", () => {

    const stars = document.querySelectorAll(".rating-stars .star");
    const ratingInput = document.querySelector("#id_rating");

    if (!stars.length || !ratingInput) return;

    function paintStars(rating) {

        stars.forEach((star, index) => {

            if (index < rating) {
                star.classList.remove("bi-star");
                star.classList.add("bi-star-fill");
                star.classList.add("active");
            } else {
                star.classList.remove("bi-star-fill");
                star.classList.add("bi-star");
                star.classList.remove("active");
            }

        });

    }

    stars.forEach(star => {

        star.addEventListener("mouseenter", () => {
            paintStars(Number(star.dataset.value));
        });

        star.addEventListener("click", () => {

            const rating = Number(star.dataset.value);

            ratingInput.value = rating;

            paintStars(rating);

        });

    });

    document.querySelector(".rating-stars").addEventListener("mouseleave", () => {

        paintStars(Number(ratingInput.value || 0));

    });


});

