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

    let scrollInit = 40;
    $(window).on('scroll', function (e) {

        let scrollTop = window.scrollY

        if (scrollTop > scrollInit) {
            $('header').addClass('position-fixed')
            // console.log('eita')
        } else {
            $('header').removeClass('position-fixed')
        }

    })


    $('.edit-post-btn').click(function () {
        var postSlug = $(this).data('post-slug');
        var textContent = $(this).data('text-content');
        var imageContent = $(this).data('image-content');

        $('#edit-post-slug').val(postSlug);
        $('#text_content').val(textContent);
        $('#file_content').attr('src', imageContent);
    });

    $('#uploadFileInputCreatePost').change(function () {
        var files = this.files;

        for (var i = 0; i < files.length; i++) {
            var reader = new FileReader();
            reader.onload = function (e) {
                var imageUrl = e.target.result;
                var carouselItem = '<div class="carousel-item active"><img src="' +
                    imageUrl +
                    '" class="d-block w-100" alt="Imagem"></div>';
                $('#preview-post-image-create').append(carouselItem);
            };
            reader.readAsDataURL(files[i]);
        }
    });

    $('.edit-post-btn').click(function () {
        $('#preview-post-file-edit').empty();
        var postSlug = $(this).data('post-slug');
        var textContent = $(this).data('text-content');
        var fileContent = $(this).data('file-content').split(' ');

        $('#edit-post-slug').val(postSlug);
        $('#text_content').val(textContent);

        fileContent.forEach(function (fileUrl) {
            if (fileUrl.toLowerCase().endsWith('.jpg') || fileUrl.toLowerCase().endsWith('.jpeg') || fileUrl.toLowerCase().endsWith('.png')) {
                var carouselItem = '<div class="carousel-item active"><img src="' + fileUrl +
                    '" class="d-block w-100" alt="Imagem"></div>';
                $('#preview-post-file-edit').append(carouselItem);
            }
        });
    });

    $('#uploadFileInput').change(function () {
        var reader = new FileReader();
        reader.onload = function (e) {
            var fileUrl = e.target.result;
            var carouselItem = '<div class="carousel-item active"><img src="' + fileUrl +
                '" class="d-block w-100" alt="Imagem"></div>';
            $('#preview-post-file-edit').append(carouselItem);

            $('#uploadFileInput').attr('src', fileUrl);
        };
        reader.readAsDataURL(this.files[0]);
    });

    $('#editPostForm').submit(function (e) {
        e.preventDefault();
        var formData = new FormData(this);
        var postSlug = $('#edit-post-slug').val();
        $.ajax({
            url: '/posting/feed/' + postSlug + '/update/',
            type: 'POST',
            data: formData,
            processData: false,
            contentType: false,
            success: function (data) {
                window.location.reload();
            },
            error: function (xhr, textStatus, errorThrown) {}
        });
    });

    $('#deletePost').on('click', function (e) {
        e.preventDefault();

        var PostSlugdelete = $(this).data('post-delete-slug')

        $.ajax({
            url: '/posting/feed/' + PostSlugdelete + '/delete/',
            type: 'POST',
            data: {
                csrfmiddlewaretoken: '{{ csrf_token }}'
            },
            success: function (data) {
                window.location.reload();
            },
            error: function (xhr, textStatus, errorThrown) {}
        })


    })

})