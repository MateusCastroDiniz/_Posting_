$(document).ready(function(){
    let currentStep = 1;

    $('#nextStep').on('click', function () {
        $('#step' + currentStep).css('display', 'none');
        currentStep++;
        $('#step' + currentStep).css('display', 'block');
        $('#prevStep').css('display', 'block');
        if (currentStep === 3) {
            $('#nextStep').css('display', 'none');
            $('#submitBtn').css('display', 'block');
        }
    });

    $('#prevStep').on('click', function () {
        $('#step' + currentStep).css('display', 'none');
        currentStep--;
        $('#step' + currentStep).css('display', 'block');
        $('#submitBtn').css('display', 'none');
        if (currentStep === 1) {
            $('#prevStep').css('display', 'none');
        }
        if (currentStep < 3) {
            $('#nextStep').css('display', 'block');
        }
    });

    $('input').on('focusout', function(){

    })

})

