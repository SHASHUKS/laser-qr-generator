from flask import Flask, render_template, request, jsonify
import segno
import base64
from io import BytesIO

app = Flask(
    __name__,
    template_folder="../templates",
    static_folder="../static"
)

@app.route('/')
def home():
    return render_template("index.html")

@app.route('/generate_qr', methods=['POST'])
def generate_qr():

    data = request.json

    qr_text = (
        f"Item ID: {data['item_id']}\n"
        f"Item Type: {data['item_type']}\n"
        f"Supplier: {data['supplier']}\n"
        f"Manufactured On: {data['manufacture_date']}\n"
        f"Warranty Expiry: {data['expiry_date']}\n"
        f"Notes: {data['notes']}"
    )

    qr = segno.make(qr_text, micro=False)

    buffer = BytesIO()
    qr.save(buffer, kind="png", scale=7)

    qr_base64 = base64.b64encode(
        buffer.getvalue()
    ).decode("utf-8")

    return jsonify({
        "qr_code": qr_base64
    })

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5600, debug=True)