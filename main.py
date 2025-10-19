from src.make_sign import AutomaticSignature

# Edit the PFX file's name and password
PFX_NAME = "MyPFX"
PFX_PASSWORD = "testpfx"

# Edit your signature file's name
SIGN_NAME = "sign"

# Edit the page and position
PAGE = 1
X_POS = 320.0
Y_POS = 380.0

# Keep these variable
PDF_PATH = ".\\pdf"
PFX_PATH = ".\\pfx\\" + PFX_NAME + ".pfx"
SIGN_PATH = ".\\sign\\" + SIGN_NAME + ".png"

auto = AutomaticSignature(PDF_PATH,PFX_PATH,PFX_PASSWORD,SIGN_PATH)
auto.set_position(PAGE, X_POS, Y_POS)
auto.generate()