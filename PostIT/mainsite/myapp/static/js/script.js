const navBar = document.getElementById("navBar");

document.addEventListener("mousemove", (event)=> {
    const mouseY = event.clientY;
    const windowHeight = window.innerHeight;

    if (mouseY >= windowHeight * 0.8) {
        navBar.classList.remove("hidden");
        navBar.classList.add("visible");
    } else {
        navBar.classList.remove("visible");
        navBar.classList.add("hidden");
    }
});