# dsensegif
Mini auxiliary project that helps to generate QR codes that direct the user to images that are already hosted in a website/repository. This project uses the `qrcode`[https://pypi.org/project/qrcode/#description] library.

# Usage instructions

1. Clone the repository:

    ```console
    $ git clone git@github.com:Marcony1/dsensegif.git
    ```

2. Create and activate the `conda` environment after `changing directory` to the root of the repo:
    ```console
    $ conda env create --file environment.yml
    ```

    ```console
    $ conda activate dsensegif
    ```

3. Open `generate_qr.py` and replace the url string assigned to `gif_url` with the url of the image for which you want to generate the QR code. Save this file. 

4. From the root of the directory run: 

    ```console
    $ python generate_qr.py
    ```

5. You will find your generated QR code under the folder `results` and with the name `qrcode.png`.