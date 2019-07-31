let log = document.querySelector('p');



function validateNum(val) {
    console.log(val.value);


 if (val.value.length > 5) {
        log.textContent = "The number is" +  ${val.value.length} + "characters(s)"

    }


    if (val.value.length > 10)
        document.getElementById("Submit").classList.remove("hidden");
}



   /* function whitespacing(v) {
    let enteredValue = document.querySelector('#inputmask');

    if (v.match(/^\d{4}$/) !== null) {
        enteredValue.value = v + ' ';
    } else if (v.match(/^\d{4}\ \d{4}$/) !== null) {
        enteredValue.value = v + ' ';
    }

    $(":input").();

}
    */
