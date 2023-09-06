function validation(){
    var status = 1
    var fname = document.getElementById('firstname')
    var lname = document.getElementById('lastname')
    var email = document.getElementById('email')
    var phone  = document.getElementById('phone')
    var password = document.getElementById('password')
    var cpassword = document.getElementById('cpassword')

    if(fname.value == ""){
        document.getElementById('firstname').style.borderColor="red"
        document.getElementById('firstname_error').innerHTML="** Enter Your First Name **"
        document.getElementById('firstname_error').style.color="red"
        document.getElementById('firstname_error').style.display="block"
        var status = 0
    }

    else{
        document.getElementById('firstname').style.borderColor="red"
        document.getElementById('firstname_error').style.display="none"
        var status = 1
    }

    if(lname.value == ""){
        document.getElementById('lastname').style.borderColor="red"
        document.getElementById('lastname_error').innerHTML="** Enter Your Last Name **"
        document.getElementById('lastname_error').style.color="red"
        document.getElementById('lastname_error').style.display="block"
        var status = 0
    }

    else{
        document.getElementById('lastname').style.borderColor="red"
        document.getElementById('lastname_error').style.display="none"
        var status = 1
    }

    if(email.value == ""){
        document.getElementById('email').style.borderColor="red"
        document.getElementById('email_error').innerHTML="** Enter Your Email Address **"
        document.getElementById('email_error').style.color="red"
        document.getElementById('email_error').style.display="block"
        var status = 0
    }

    else{
        document.getElementById('email').style.borderColor="red"
        document.getElementById('email_error').style.display="none"
        var status = 1
    }

    if(phone.value == ""){
        document.getElementById('phone').style.borderColor="red"
        document.getElementById('phone_error').innerHTML="** Enter Your Phone Number **"
        document.getElementById('phone_error').style.color="red"
        document.getElementById('phone_error').style.display="block"
        var status = 0
    }

    else{
        document.getElementById('phone').style.borderColor="red"
        document.getElementById('phone_error').style.display="none"
        var status = 1
    }

    if(password.value == ""){
        document.getElementById('password').style.borderColor="red"
        document.getElementById('password_error').innerHTML="** Enter Your Password **"
        document.getElementById('password_error').style.color="red"
        document.getElementById('password_error').style.display="block"
        var status = 0
    }

    else{
        document.getElementById('password').style.borderColor="red"
        document.getElementById('password_error').style.display="none"
        var status = 1
    }

    if(cpassword.value == ""){
        document.getElementById('cpassword').style.borderColor="red"
        document.getElementById('cpassword_error').innerHTML="** Enter Your Confirm Password **"
        document.getElementById('cpassword_error').style.color="red"
        document.getElementById('cpassword_error').style.display="block"
        var status = 0
    }

    else{
        document.getElementById('cpassword').style.borderColor="red"
        document.getElementById('cpassword_error').style.display="none"
        var status = 1
    }

    if(status == 1){
        return true
    }

    if(status == 0){
        return false
    }
}

function pass(){
    var password = document.getElementById('password').value

    if(password.length < 2){
        document.getElementById('password').style.borderColor="red"
        document.getElementById('password_error').innerHTML="** Password Must Have 8 digits **"
        document.getElementById('password_error').style.color="red"
        document.getElementById('password_error').style.display="block"
    }

    if(password.length == 8){
        document.getElementById('password').style.borderColor="green"
        document.getElementById('password_error').innerHTML="** You Entered A Pefect Password **"
        document.getElementById('password_error').style.color="green"
        document.getElementById('password_error').style.display="block"
    }

    if(password.length > 8){
        document.getElementById('password').style.borderColor="red"
        document.getElementById('password_error').innerHTML="** Please Enter A Valid Password **"
        document.getElementById('password_error').style.color="red"
        document.getElementById('password_error').style.display="block"
    }

}

function cpass(){
    var password = document.getElementById('password').value
    var cpassword = document.getElementById('cpassword').value


    if(cpassword.length < 2){
        document.getElementById('cpassword').style.borderColor="red"
        document.getElementById('cpassword_error').innerHTML="** Password Must Have 8 digits **"
        document.getElementById('cpassword_error').style.color="red"
        document.getElementById('cpassword_error').style.display="block"
    }

    if(cpassword.length == 8){
        document.getElementById('cpassword').style.borderColor="green"
        document.getElementById('cpassword_error').innerHTML="** You Entered A Pefect Password **"
        document.getElementById('cpassword_error').style.color="green"
        document.getElementById('cpassword_error').style.display="block"
    }

    if(cpassword.length > 8){
        document.getElementById('cpassword').style.borderColor="red"
        document.getElementById('cpassword_error').innerHTML="** Please Enter A Valid Password **"
        document.getElementById('cpassword_error').style.color="red"
        document.getElementById('cpassword_error').style.display="block"
    }

    if(password != cpassword){
        document.getElementById('cpassword').style.borderColor="red"
        document.getElementById('cpassword_error').innerHTML="** Password And Confirm Password Must Be Equal **"
        document.getElementById('cpassword_error').style.color="red"
        document.getElementById('cpassword_error').style.display="block"
    }
}