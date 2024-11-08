const tabs = document.querySelectorAll(".tab");
const tabContent = document.querySelectorAll(".tab-content .tab-item");

tabs.forEach((tab, index) => {
    tab.addEventListener("click", () => {
        tabs.forEach((tab) => {
            tab.classList.remove("active");
        });
        tab.classList.add("active");

        tabContent.forEach((tabContent) => {
            tabContent.classList.remove("active");
        });
        tabContent[index].classList.add("active");
    });
})

const dropArea = document.getElementById('drop-area');

dropArea.addEventListener('dragover', (event) => {
    event.preventDefault(); // Prevent default behavior (Prevent file from being opened)
    dropArea.classList.add('active'); // Optional: Add a class for styling
});

dropArea.addEventListener('dragleave', () => {
    dropArea.classList.remove('active'); // Remove the class when leaving
});

dropArea.addEventListener('drop', (event) => {
    event.preventDefault(); // Prevent default behavior
    dropArea.classList.remove('active'); // Remove the class
    const files = event.dataTransfer.files; // Get the dropped files
    console.log(files); // Handle the files as needed
});


document.querySelector("input[name='design']").addEventListener("change", (e) => {
    const reader = new FileReader();
    reader.onload = (e) => {
        document.querySelector(".preview").innerHTML = `<img src="${e.target.result}" />`;
    }
    reader.readAsDataURL(e.target.files[0]);

    document.querySelector("#drop-area").style.display = 'none';
    document.querySelector(".buttons").style.display = 'block';
})

document.querySelector("form").addEventListener("reset", () => {
    document.querySelector(".preview").innerHTML = "";
    document.querySelector(".buttons").style.display = 'none';
    document.querySelector("#drop-area").style.display = 'block';
})
