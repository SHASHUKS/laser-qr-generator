async function generateQR(){

    const data = {
        item_id: document.getElementById('item_id').value,
        item_type: document.getElementById('item_type').value,
        supplier: document.getElementById('supplier').value,
        manufacture_date: document.getElementById('manufacture_date').value,
        expiry_date: document.getElementById('expiry_date').value,
        notes: document.getElementById('notes').value
    };

    const response = await fetch('/generate_qr', {
        method:'POST',
        headers:{
            'Content-Type':'application/json'
        },
        body:JSON.stringify(data)
    });

    const result = await response.json();

    document.getElementById('qr-result').innerHTML =
        `<img src="data:image/png;base64,${result.qr_code}" />`;
}