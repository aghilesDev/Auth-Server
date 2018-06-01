from AuthenticationHandler import AuthenticationHandler as AuthHandler,generator
from Validator import SignatureProvider as Provider

authHandler=AuthHandler()
token=authHandler.generateChallenge('Aghiles')

private=b'\xd7a^\xcb\xae}\x96R\x95H\x19\x1fu[\xb24E\x91\x86Zm\xdd\x8e~\t>P\x0bf\t\xfdw'

signature=Provider(private).sign(message=token)


authHandler.AuthentificateToken(token=token,signature=signature)

print('token:'.format(token))
data=generator.decryptToken(token)
if(generator.verifyChallengeToken(token)):
    print('identifiant'.format(data.id))
