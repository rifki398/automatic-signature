from spire.pdf.common import *
from spire.pdf import *
from pathlib import Path

class AutomaticSignature():
    def __init__(self,pdf,pfx,pfx_password,sign):
        self.pdf = Path(pdf)
        self.pfx = pfx
        self.pfx_password = pfx_password
        self.sign = sign

        self._dx = 0.0
        self._dy = 0.0

    def set_position(self,page : int, dx : float,dy : float):
        self._dx = dx
        self._dy = dy
        self._page = page

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
            image = PdfImage.FromFile(self.sign)

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
                                        (float)(image.Width), 
                                        (float)(image.Height), 
                                        appearance)

            # Save the signed document
            output_path = ".\\results\\" + file_name
            doc.SaveToFile(output_path)

            # Dispose resources
            doc.Dispose()