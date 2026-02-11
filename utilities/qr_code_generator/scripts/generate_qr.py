import qrcode

def generate_qr(url, file_path="qr_code.png"):
    """Generate a QR code from a URL and save it to a file"""
    qr = qrcode.QRCode(
        version=1,
        box_size=10,
        border=5,
    )
    qr.add_data(url)
    qr.make(fit=True)
    img = qr.make_image(fill_color="black", back_color="white")
    img.save(file_path)
    print(f"QR Code was generated and saved to: {file_path}")

