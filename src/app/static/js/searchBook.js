document.getElementById("input").addEventListener("keypress", function (event) {
    if (event.key === "Enter") {
        event.preventDefault();

        let valor = this.value;

        fetch(homeIndex, {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify({ message: valor })
        })
            .then(response => {
                if (response.redirected) {
                    window.location.href = response.url;
                } else {
                    return response.text();
                }
            })
            .then(html => {
                document.open();
                document.write(html);
                document.close();
            })
            .catch(error => console.error('Erro:', error));

        this.value = "";
    }
});
