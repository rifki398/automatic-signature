from spire.pdf.common import *
from spire.pdf import *
from pathlib import Path
from PIL import Image
import tempfile

class AutomaticSignature():
    def __init__(self,PFX_NAME,PFX_PASSWORD,SIGN_NAME):
        PDF_PATH = ".\\pdf"
        PFX_PATH = ".\\pfx\\" + PFX_NAME + ".pfx"
        SIGN_PATH = ".\\sign\\" + SIGN_NAME + ".png"

        self.pdf = Path(PDF_PATH)
        self.pfx = PFX_PATH
        self.pfx_password = PFX_PASSWORD
        self.sign = SIGN_PATH

        self._dx = 0.0
        self._dy = 0.0

        self._scale = 1.0

        # Clean the result's folder
        result_folder = Path(".\\results")
        for file in result_folder.glob("*"):
            if file.is_file():
                os.remove(file)

    def set_position(self,page : int, dx : float,dy : float):
        self._dx = dx
        self._dy = dy
        self._page = page

    def set_scale(self,scale : float):
        self._scale = scale

    def generate(self):
        for pdf_file in self.pdf.glob("*.pdf"):
            file_name = pdf_file.name

            # Create a PdfDocument object
            doc = PdfDocument()

            # Load a PDF file
            doc.LoadFromFile(str(pdf_file))

            # Specify the path of the pfx certificate
            pfxCertificatePath = self.pfx

            # Specify the password of the pdf certificate

            # Create a signature maker
            signatureMaker = PdfOrdinarySignatureMaker(doc, 
                                                    pfxCertificatePath,
                                                    self.pfx_password)

            # Get the signature
            signature = signatureMaker.Signature

            # Create a signature appearance
            appearance = PdfSignatureAppearance(signature)

            # Load an image
            image = self._resize_image()

            # Set the image as the signature image
            appearance.SignatureImage = image

            # Set the graphic mode as SignImageOnly
            appearance.GraphicMode = GraphicMode.SignImageOnly

            # Get the last page
            page = doc.Pages[doc.Pages.Count - (doc.Pages.Count - self._page + 1)]

            # Add the signature to a specified location of the page
            signatureMaker.MakeSignature("Signature by Unknown", 
                                        page,
                                        page.Size.Width - self._dx, 
                                        page.Size.Height - self._dy, 
                                        float(image.Width), 
                                        float(image.Height), 
                                        appearance)

            # Save the signed document
            output_path = ".\\results\\" + file_name
            doc.SaveToFile(output_path)

            # Dispose resources
            doc.Dispose()

    def _resize_image(self):
        # Resize image before using
        with Image.open(self.sign) as img:
            new_size = (int(img.width * self._scale), int(img.height * self._scale))
            resized_img = img.resize(new_size, Image.Resampling.LANCZOS)

            # Make temp file and save
            with tempfile.NamedTemporaryFile(delete=False, suffix=".png") as temp_file:
                temp_path = temp_file.name
                resized_img.save(temp_path, format="PNG")

        # Close file before using by Spire
        image = PdfImage.FromFile(temp_path)
        return image