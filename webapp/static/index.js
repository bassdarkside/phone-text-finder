function deleteNumber(numberId) {
    fetch('/delete-number', {
        method: 'POST',
        body: JSON.stringify({ numberId: numberId })
    }).then((_res) => {
        window.location.href = "/";
    });
}