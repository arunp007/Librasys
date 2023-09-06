function validation(){
    var status = 1
    var name = document.getElementById('fullname')
    var location = document.getElementById('location')
    var address = document.getElementById('address')
    var email = document.getElementById('email')
    var phone = document.getElementById('phone')
    var book = document.getElementById('book')
    var author = document.getElementById('author')
    var pdate = document.getElementById('purchase_date')
    var rdate = document.getElementById('return_date')

    if(name.value == ""){
        document.getElementById('fullname').style.borderColor="red"
        document.getElementById('fullname_error').innerHTML="** Enter Your Fullname **"
        document.getElementById('fullname_error').style.color="red"
        document.getElementById('fullname_error').style.display="block"
        var status = 0
    }

    else{
        document.getElementById('fullname').style.borderColor="black"
        document.getElementById('fullname_error').style.display="none"
        var status = 1
    }

    if(location.value == ""){
        document.getElementById('location').style.borderColor="red"
        document.getElementById('location_error').innerHTML="** Enter Your Location **"
        document.getElementById('location_error').style.color="red"
        document.getElementById('location_error').style.display="block"
        var status = 0
    }

    else{
        document.getElementById('location').style.borderColor="black"
        document.getElementById('location_error').style.display="none"
        var status = 1
    }

    if(address.value == ""){
        document.getElementById('address').style.borderColor="red"
        document.getElementById('address_error').innerHTML="** Enter Your Permanent Address **"
        document.getElementById('address_error').style.color="red"
        document.getElementById('address_error').style.display="block"
        var status = 0
    }

    else{
        document.getElementById('address').style.borderColor="black"
        document.getElementById('address_error').style.display="none"
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

    if(book.value == ""){
        document.getElementById('book').style.borderColor="red"
        document.getElementById('book_error').innerHTML="** Enter Your Book Name **"
        document.getElementById('book_error').style.color="red"
        document.getElementById('book_error').style.display="block"
        var status = 0
    }

    else{
        document.getElementById('book').style.borderColor="black"
        document.getElementById('book_error').style.display="none"
        var status = 1
    }

    if(author.value == ""){
        document.getElementById('author').style.borderColor="red"
        document.getElementById('author_error').innerHTML="** Enter Your Author Name **"
        document.getElementById('author_error').style.color="red"
        document.getElementById('author_error').style.display="block"
        var status = 0
    }

    else{
        document.getElementById('author').style.borderColor="black"
        document.getElementById('author_error').style.display="none"
        var status = 1
    }

    if(pdate.value == ""){
        document.getElementById('purchase_date').style.borderColor="red"
        document.getElementById('purchase_date_error').innerHTML="** Enter Your Book Purchasing Date **"
        document.getElementById('purchase_date_error').style.color="red"
        document.getElementById('purchase_date_error').style.display="block"
        var status = 0
    }

    else{
        document.getElementById('purchase_date').style.borderColor="black"
        document.getElementById('purchase_date_error').style.display="none"
        var status = 1
    }

    if(rdate.value == ""){
        document.getElementById('return_date').style.borderColor="red"
        document.getElementById('return_date_error').innerHTML="** Enter Your Book Returning Date **"
        document.getElementById('return_date_error').style.color="red"
        document.getElementById('return_date_error').style.display="block"
        var status = 0
    }

    else{
        document.getElementById('return_date').style.borderColor="black"
        document.getElementById('return_date_error').style.display="none"
        var status = 1
    }

    if(status == 1){
        return true
    }

    if(status == 0){
        return false
    }
}