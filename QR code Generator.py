import qrcode
import qrcode.constants


def generate_qr_code(text, file_name):
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=10,
        border=3
    )

    qr.add_data(text)
    qr.make(fit=True)
    img = qr.make_image(fill_color='#4B8BBE', back_color="white")
    img.save(file_name)


if __name__ == "__main__":
    text = "https://github.com/PhulusoN"  # enter your link
    file_name = "qr_code.png"
    generate_qr_code(text, file_name)
    print(f"QR code saved as {file_name}")
