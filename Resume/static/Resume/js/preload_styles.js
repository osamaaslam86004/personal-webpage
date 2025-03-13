document.addEventListener("DOMContentLoaded", function () {
    function loadCSS(id) {
        var link = document.getElementById(id);
        if (link) {
            link.rel = "stylesheet"; // Apply CSS after page is loaded
        }
    }

    loadCSS("bootstrap-css");
    loadCSS("cv-css");
});