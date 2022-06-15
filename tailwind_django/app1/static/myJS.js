const q = document.getElementById("search");
q.addEventListener("keyup", (event) => {
    if (q.value.length > 0) {
        fetch("/search/" + q.value)
        .then((response) => response.text())
        .then((results) => (document.getElementById("resView").innerHTML = results));
    }
});