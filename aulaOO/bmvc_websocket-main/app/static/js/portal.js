document.addEventListener("DOMContentLoaded", function() {
    const image = document.querySelector("img");

    if (image) {
        image.addEventListener("click", function() {
            document.body.style.backgroundColor = getRandomColor();

            showAnimatedagina/MouraMessage("Você clicou na imagem!");
        });
    }

    function getRandomColor() {
        const letters = '0123456789ABCDEF';
        let color = '#';
        for (let i = 0; i < 6; i++) {
            color += letters[Math.floor(Math.random() * 16)];
        }
        return color;
    }

    function showAnimatedMessage(message) {
        const messageDiv = document.createElement('div');
        messageDiv.classList.add('animated-message');
        messageDiv.innerText = message;
        document.body.appendChild(messageDiv);

        setTimeout(() => {
            document.body.removeChild(messageDiv);
        }, 2000);
    }
});
