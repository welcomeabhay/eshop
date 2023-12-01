function Validation(){
Psd = document.r_form.psd.value();
Cpsd = document.r_form.psd.value();
if (Psd==Cpsd){
return true
}
else {
alert("Password and confirm password must be same.")
return false
}
}