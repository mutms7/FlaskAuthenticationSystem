from passlib.context import CryptContext


cryptcontext=CryptContext(schemes=['des_crypt'],deprecated="auto")


def get_password_hash(password):
	return cryptcontext.hash(password)

def verify_password(plain_password,hashed_password):
	return cryptcontext.verify(plain_password,hashed_password)
