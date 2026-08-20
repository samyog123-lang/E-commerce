document.addEventListener("DOMContentLoaded", function() {
    const inputs = document.querySelectorAll('.input-group input');

    inputs.forEach(input => {
        input.addEventListener('focus', () => {
            input.nextElementSibling.classList.add('focused');
        });

        input.addEventListener('blur', () => {
            if(input.value === "") {
                input.nextElementSibling.classList.remove('focused');
            }
        });
    });

    // Example: shake animation on submit if empty
    const forms = document.querySelectorAll('.auth-form');
    forms.forEach(form => {
        form.addEventListener('submit', (e) => {
            let empty = false;
            inputs.forEach(input => {
                if(input.value.trim() === "") empty = true;
            });
            if(empty) {
                e.preventDefault();
                form.querySelectorAll('input').forEach(inp => {
                    inp.classList.add('input-error');
                    setTimeout(() => inp.classList.remove('input-error'), 400);
                });
            }
        });
    });
});
