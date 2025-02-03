document.addEventListener("DOMContentLoaded", function () {
    const hamburger = document.querySelector(".hamburger");
    const navLinks = document.querySelector(".nav-links");

    hamburger.addEventListener("click", () => {
        navLinks.classList.toggle("active");
        hamburger.querySelectorAll("span").forEach((span, index) => {
            if (navLinks.classList.contains("active")) {
                span.style.transform = index === 1 ? "rotate(45deg)" : "rotate(-45deg)";
            } else {
                span.style.transform = "rotate(0deg)";
            }
        });
    });
});