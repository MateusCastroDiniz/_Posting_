// $(document).ready(function(){
//     let currentStep = 1;

//     $('#nextStep').on('click', function () {
//         $('#step' + currentStep).css('display', 'none');
//         currentStep++;
//         $('#step' + currentStep).css('display', 'block');
//         $('#prevStep').css('display', 'block');
//         if (currentStep === 3) {
//             $('#nextStep').css('display', 'none');
//             $('#submitBtn').css('display', 'block');
//         }
//     });

//     $('#prevStep').on('click', function () {
//         $('#step' + currentStep).css('display', 'none');
//         currentStep--;
//         $('#step' + currentStep).css('display', 'block');
//         $('#submitBtn').css('display', 'none');
//         if (currentStep === 1) {
//             $('#prevStep').css('display', 'none');
//         }
//         if (currentStep < 3) {
//             $('#nextStep').css('display', 'block');
//         }
//     });

//     $('input').on('focusout', function(){

//     })

// })

$(document).ready(function () {
    let currentStep = 1;
    let progress = 33;

    $('#nextStep').on('click', function () {
        $('cadastro_progressbar').css('width', progress + '%')
        progress += 33;

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
    
})