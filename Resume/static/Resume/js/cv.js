document.addEventListener("DOMContentLoaded", function () {
    let mybutton = document.getElementById("myBtn");

    window.addEventListener("scroll", function () {
        mybutton.style.display = (window.scrollY > 20) ? "block" : "none";
    });

    mybutton.addEventListener("click", function () {
        window.scrollTo({ top: 0, behavior: "smooth" });
    });
});
