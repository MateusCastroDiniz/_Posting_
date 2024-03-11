$(document).ready(function () {

//  const btnToastFreq = $('#btn-toast-freq')
//  const toastFreq = $('#toast-freq')
//
//  if (btnToastFreq) {
//    const toastBootstrap = bootstrap.Toast.getOrCreateInstance(toastFreq)
//    btnToastFreq.on('click', () => {
//      toastBootstrap.show()
//      toastFreq.addClass("d-flex")
//    })
//  }

  function validarCampo(campo) {
    const regexNome = /\d|,/g;
    let camposValidos = true;
    let textoAlerta = campo.parent().find('.text-muted');

    if (campo.val() == "") {
        campo.addClass('invalido')
        textoAlerta.fadeIn()
        camposValidos = false
        return camposValidos
    } else {

        if (campo.attr('name') == 'nome') {
            if (campo.val().length < 2 || campo.val().match(regexNome)) {
                campo.addClass('invalido')
                textoAlerta.show()
                camposValidos = false
                return camposValidos
            } else {
                campo.removeClass('invalido')
                textoAlerta.hide()
                camposValidos = true
                return camposValidos
            }
        }
        if (campo.attr('name') == 'email') {
            if (!campo.val().match(/^[a-z0-9.]+@[a-z0-9]+\.[a-z]+(\.[a-z]+)?/i)) {
                campo.addClass('invalido')
                textoAlerta.show()
                camposValidos = false
                return camposValidos
            } else {
                campo.removeClass('invalido')
                textoAlerta.hide()
                camposValidos = true
                return camposValidos
            }
        }

        if (campo.attr('name') == 'cep') {
            if (!campo.val().match(/\d{5}-\d{3}/)) {
                campo.addClass('invalido')
                textoAlerta.show()
                camposValidos = false
                return camposValidos

            } else {
                campo.removeClass('invalido')
                textoAlerta.hide()
                camposValidos = true
                return camposValidos
            }
        }
        if (campo.attr('name') == 'cpf') {
            if (!campo.val().match(/([0-9]{2}[\.]?[0-9]{3}[\.]?[0-9]{3}[\/]?[0-9]{4}[-]?[0-9]{2})|([0-9]{3}[\.]?[0-9]{3}[\.]?[0-9]{3}[-]?[0-9]{2})/)) {
                campo.addClass('invalido')
                textoAlerta.show()
                camposValidos = false
                return camposValidos
            } else {
                campo.removeClass('invalido')
                textoAlerta.hide()
                camposValidos = true
                return camposValidos
            }
        }

        campo.removeClass('invalido')
        textoAlerta.hide()
        camposValidos = true
        return camposValidos
    }
}


$('.obrigatorio').on('blur', function (e) {
  e.preventDefault();
  validarCampo($(this));
});

$('#fone-input').on('keyup', function () {
  $(this).mask('(00)00000-0000');
});

$('#cep-input').on('keyup', function () {
  $(this).mask('00000-000');
});

$('#cpf-input').on('keyup', function () {
  $(this).mask('000.000.000-00');
});

  $('#link-avatar').hover(function () {
    $('#span-avatar').toggleClass('visible')
  })

  function exibirErro(campo) {
    let textoAlerta = campo.parent().find('.text-muted');
    campo.addClass('invalido');
    textoAlerta.fadeIn();
}

$('#btn-salvar-dados').on('click', function (event) {
    event.preventDefault();
    event.stopPropagation();

    let camposValidos = true;

    $('.obrigatorio').each(function () {
        if (!validarCampo($(this))) {
            camposValidos = false;
            exibirErro($(this));
        }
    });

    if (camposValidos) {
        const btnSalvardados = $('#btn-salvar-dados');
        const toastSalvarDados = $('#toast-salvar-dados');

        if (btnSalvardados) {
            const toastBootstrap = bootstrap.Toast.getOrCreateInstance(toastSalvarDados);
            btnSalvardados.on('click', () => {
                toastBootstrap.show();
                toastSalvarDados.addClass("d-flex");
            });
        }

        // Envie o formulário
        $('#form-cadastro').submit()
        console.log('Formulário enviado');
    }else{
      return false
    }
});



})