function validation(){
    var status = 1
    var email = document.getElementById('email')
    var password = document.getElementById('password')

    if(email.value == ""){
        document.getElementById('email').style.borderColor="red"
        document.getElementById('email_error').innerHTML="** Enter Your Email Address **"
        document.getElementById('email_error').style.color="red"
        document.getElementById('email_error').style.display="block"
        var status = 0
    }

    else{
        document.getElementById('email').style.borderColor="black"
        document.getElementById('email_error').style.display="none"
        var status =1
    }

    if(password.value == ""){
        document.getElementById('password').style.borderColor="red"
        document.getElementById('password_error').innerHTML="** Enter Your Password **"
        document.getElementById('password_error').style.color="red"
        document.getElementById('password_error').style.display="block"
        var status = 0
    }

    else{
        document.getElementById('password').style.borderColor="black"
        document.getElementById('password_error').style.display="none"
        var status =1
    }

    if(status == 0){
        return false
    }

    if(status == 1){
        return true
    }
}