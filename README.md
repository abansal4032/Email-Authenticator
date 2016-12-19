# Email-Authenticator

This app provides 2 APIs:

1. http://{server_ip}:{port}/get_otp?email=sample_email&name=sample_name
It generates an OTP for the email given and sends the corresponding mail to the email.

2. http://{server_ip}:{port}/authenticate?email=sample_email&otp=mailed_otp
It checks the email against the OTP mailed to the user and returns 'Success', 'Failure' or 'Not registered' correspondingly.
