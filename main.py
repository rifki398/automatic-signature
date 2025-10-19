from src.make_sign import AutomaticSignature

# PFX file's name and password
PFX_NAME = "MyPFX"
PFX_PASSWORD = "testpfx"

# Edit your signature image's name
SIGN_NAME = "sign"

# Page and position
PAGE = 1
X_POS = 280.0
Y_POS = 375.0

# Keep these variables
PDF_PATH = ".\\pdf"
PFX_PATH = ".\\pfx\\" + PFX_NAME + ".pfx"
SIGN_PATH = ".\\sign\\" + SIGN_NAME + ".png"

esign = AutomaticSignature(PDF_PATH,PFX_PATH,PFX_PASSWORD,SIGN_PATH)
esign.set_position(PAGE, X_POS, Y_POS)
esign.set_scale(0.85) # for signature scale (optional)
esign.generate()