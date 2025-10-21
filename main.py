from src.make_sign import AutomaticSignature

# PFX file's name and password (without extension)
PFX_NAME = "MyPFX"
PFX_PASSWORD = "testpfx"

# Edit your signature image's name (without extension)
SIGN_NAME = "sign"

# Page and position
PAGE = 1
X_POS = 280.0
Y_POS = 375.0

esign = AutomaticSignature(PFX_NAME,PFX_PASSWORD,SIGN_NAME)
esign.set_position(PAGE, X_POS, Y_POS)
esign.set_scale(0.85) # for signature scale (optional)
esign.generate()