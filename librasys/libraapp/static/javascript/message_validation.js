function validation(){
    var status = 1
    var message = document.getElementById('message')

    if(message.value == ""){
        document.getElementById('message').style.borderColor="red"
        document.getElementById('message_error').innerHTML="** Enter Your Message **"
        document.getElementById('message_error').style.color="red"
        document.getElementById('message_error').style.display="block"
        var status = 0
    }

    else{
        document.getElementById('message').style.borderColor="black"
        document.getElementById('message_error').style.display="none"
        var status = 1
    }

    if(status == 1){
        return true
    }

    if(status == 0){
        return false
    }
}