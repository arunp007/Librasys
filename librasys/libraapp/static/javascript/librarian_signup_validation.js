function validation(){
    var status = 1
    var fname = document.getElementById('firstname')
    var lname = document.getElementById('lastname')
    var library_name = document.getElementById('library_name')
    var library_location = document.getElementById('library_location')
    var email = document.getElementById('email')
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
        document.getElementById('firstname').style.borderColor="black"
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
        document.getElementById('lastname').style.borderColor="black"
        document.getElementById('lastname_error').style.display="none"
        var status = 1
    }

    if(library_name.value == ""){
        document.getElementById('library_name').style.borderColor="red"
        document.getElementById('libraryname_error').innerHTML="** Enter Your Library Name **"
        document.getElementById('libraryname_error').style.color="red"
        document.getElementById('libraryname_error').style.display="block"
        var status = 0
    }

    else{
        document.getElementById('library_name').style.borderColor="black"
        document.getElementById('libraryname_error').style.display="none"
        var status = 1
    }

    if(library_location.value == ""){
        document.getElementById('library_location').style.borderColor="red"
        document.getElementById('librarylocation_error').innerHTML="** Enter Your Library Location **"
        document.getElementById('librarylocation_error').style.color="red"
        document.getElementById('librarylocation_error').style.display="block"
        var status = 0
    }

    else{
        document.getElementById('library_location').style.borderColor="black"
        document.getElementById('librarylocation_error').style.display="none"
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
        document.getElementById('email').style.borderColor="black"
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
        document.getElementById('phone').style.borderColor="black"
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
        document.getElementById('password').style.borderColor="black"
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
        document.getElementById('cpassword').style.borderColor="black"
        document.getElementById('cpassword_error').style.display="none"
        var status = 1
    }



    if(status == 0){
        return false
    }

    if(status == 1){
        return true
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