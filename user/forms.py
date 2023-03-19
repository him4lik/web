from django import forms

class LoginForm(forms.Form):
	phone=forms.CharField(widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'Phone...'}))

	def clean(self):
		cleaned_data = super().clean()
		phone = cleaned_data.get("phone")
		try:
			value=int(phone)
		except:
			raise forms.ValidationError('Invalid phone')
		if len(phone)!=10:
			raise forms.ValidationError('Invalid phone')

		# user=authenticate(email_or_phone=e_or_p, password=password)

		# if user==None:
		# 	raise forms.ValidationError("User doesn't exist")
		# if user.is_staff:
		# 	raise  forms.ValidationError("Staff users don't have access")

class OTPForm(forms.Form):
	otp = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'OTP...'}))
	request_id = forms.CharField(widget=forms.HiddenInput(attrs={'class':'form-control'}))

	def clean(self):
		cleaned_data = super().clean()
		otp = cleaned_data.get("otp")
		try:
			value=int(otp)
		except:
			raise forms.ValidationError('Invalid otp')
		if len(otp)!=6:
			raise forms.ValidationError('Invalid otp')

		# user=authenticate(email_or_phone=e_or_p, password=password)

		# if user==None:
		# 	raise forms.ValidationError("User doesn't exist")
		# if user.is_staff:
		# 	raise  forms.ValidationError("Staff users don't have access")