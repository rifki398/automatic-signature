from src.make_sign import AutomaticSignature

PDF_PATH = ".\\pdf"
PFX_PATH = ".\\pfx\\MyPFX.pfx"
PFX_PASSWORD = "testpfx"
SIGN_PATH = ".\\sign\\sign.png"

auto = AutomaticSignature(PDF_PATH,PFX_PATH,PFX_PASSWORD,SIGN_PATH)

PAGE = 1
X_POS = 320.0
Y_POS = 380.0

auto.set_position(PAGE, X_POS, Y_POS)
auto.generate()