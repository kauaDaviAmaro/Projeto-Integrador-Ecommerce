// Navbar

window.addEventListener("scroll", () => {
    const navbar = document.querySelector(".navbar");

    const isScrolled = window.scrollY > 0;

    if (isScrolled) {
        navbar.classList.add("scrolled");
    } else {
        navbar.classList.remove("scrolled");
    }
});

function toggleMenu() {
    const hamburguerMenu = document.querySelector(".hamburguer-menu");
    const links = document.querySelector(".hamburguer-links");
    
    const menuIcon = hamburguerMenu.querySelector(".bx");
    menuIcon.classList.toggle("bx-menu");
    menuIcon.classList.toggle("bx-x");
    links.classList.toggle("hidden");
}

document.addEventListener('DOMContentLoaded', () => {
    const form = document.querySelector('form');

    form.addEventListener('submit', function (event) {
        event.preventDefault();
        const isValid = validateField(this);

        if (isValid) {
            this.submit();
        }
    });

    const requiredFields = form.querySelectorAll('[required]');

    requiredFields.forEach(field => {
        const label = field.previousElementSibling;
        if (label) {
            label.insertAdjacentHTML('beforeend', ' <span style="color:red;">*</span>');
        }
    });
});

function createTooltip(field) {
    const tooltip = document.createElement('span');
    tooltip.classList.add('tooltip');
    tooltip.textContent = field.title;
    field.after(tooltip);
}

function removeTooltip(field) {
    const tooltip = field.nextElementSibling;
    if (tooltip) {
        tooltip.remove();
    }
}

function validateField(form) {
    let isValid = true;
    const fields = form.querySelectorAll('.validable');

    fields.forEach(field => {
        if (!field.checkValidity()) {
            field.classList.add('input-invalid');

            if (field.title && !field.nextElementSibling) {
                createTooltip(field);
            }

            isValid = false;
        } else {
            field.classList.remove('input-invalid');
            field.classList.add('input-valid');
            removeTooltip(field);
        }
    });

    return isValid;
}

function closeToast() {
    const toast = document.querySelector('.toast');
    if (toast) {
        toast.style.opacity = 1;
        (function fade() {
            if ((toast.style.opacity -= 0.1) < 0) {
                toast.remove();
            } else {
                requestAnimationFrame(fade);
            }
        })();
    }
}
