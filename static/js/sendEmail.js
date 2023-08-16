function sendMail(contactForm){
    emailjs.send("service_jfcl0wd","template_nwzgivn", {
        "from_name": contactForm.name.value,
        "from_email": contactForm.email.value,
        "from_number": contactForm.phone.value,
        "message": contactForm.message.value
    })
    .then(
        function(response) {
            console.log("SUCCESS", response);
        },
        function(error) {
            console.log("FAILED", error)
        }
    )
    return false;
}

function submitDisappear(){
    let submitDiv = document.getElementById("submitDiv");
    submitDiv.style.display = "none";
}


function thanksAppear() {
    let thanksDiv = document.getElementById("thanksDiv");
    thanksDiv.style.display = 'block';
}


function resetPage() {
    window.location.reload();
}