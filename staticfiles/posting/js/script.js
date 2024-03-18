$(document).ready(function () {


    $('#editPostForm').on('submit', function (e) {
        e.preventDefault();
        var post_id = $('#post_id').val();
        var text_content = $('#text_content').val();
        var image_content = $('#image_content').attr('src');

        // Envie os dados do formulário via AJAX para a viewset de Post
        $.ajax({
            type: 'POST',
            url: '{% url "edit_post" %}',
            data: {
                'post_id': post_id,
                'text_content': text_content,
                'image_content': image_content,
                'csrfmiddlewaretoken': '{{ csrf_token }}'
            },
            success: function (data) {
                // Se a atualização for bem-sucedida, feche o modal
                $('#editPostModal').modal('hide');
                // Atualize a página ou faça qualquer outra ação necessária
            },
            error: function (xhr, textStatus, errorThrown) {
                // Em caso de erro, manipule conforme necessário
            }
        });
    });

    // $('#editPostForm').on('submit', function (e) {
    //     e.preventDefault();
    //     var post_id = $('#post_id').val();
    //     var text_content = $('#text_content').val();
    //     var image_content = $('#image_content').attr('src');

    //     // Envie os dados do formulário via AJAX para a viewset de Post
    //     $.ajax({
    //         type: 'POST',
    //         url: '{% url "edit_post" %}',
    //         data: {
    //             'post_id': post_id,
    //             'text_content': text_content,
    //             'image_content': image_content,
    //             'csrfmiddlewaretoken': '{{ csrf_token }}'
    //         },
    //         success: function (data) {
    //             // Se a atualização for bem-sucedida, feche o modal
    //             $('#editPostModal').modal('hide');
    //             // Atualize a página ou faça qualquer outra ação necessária
    //         },
    //         error: function (xhr, textStatus, errorThrown) {
    //             // Em caso de erro, manipule conforme necessário
    //         }
    //     });
    // });

//    $('.remove_img_btn').on('click', function(e){
//        $('#image_content').attr('src', '');
//        $('.image_container_edit').css('display', 'none');
//
////        $.ajax({
////            type:'POST',
////            url: '{% url "edit_post"%}',
////            data:{
////                'post_id': post_id,
////                'image_content': image_content,
////                'csrfmiddlewaretoken': '{{ csrf_token }}',
////                'delete_image': 'true',
////            }
////        })
////
   });
