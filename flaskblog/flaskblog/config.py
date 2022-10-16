import os

class Config:
	SECRET_KEY= '3eb3e7a12bd9eab74cd31ec4b9e8f5b4'
	SQLALCHEMY_DATABASE_URI = 'sqlite:///site.db'
	MAIL_SERVER= 'smtp.googlemail.com'
	MAIL_PORT=587
	MAIL_USE_TLS = True
	MAIL_USERNAME = os.environ.get('EMAIL_USER')
	MAIL_PASSWORD = os.environ.get('EMAIL_PASS')
