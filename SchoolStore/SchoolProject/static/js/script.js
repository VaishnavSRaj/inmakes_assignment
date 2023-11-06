//$(document).ready(function() {
//  var message = $('#message');
//
//  setTimeout(function() {
//    message.fadeOut('slow');
//  }, 2000);
//});


 $(document).ready(function() {
            console.log('triggered');

            $('#department').change(function() {
                var department = $(this).val();
                var courses = $('#courses');
                courses.empty();

                if (department === 'Commerce') {
                    courses.append('<option value="BBA">BBA</option>');
                    courses.append('<option value="BCom">BCom</option>');
                } else if (department === 'Science') {
                    courses.append('<option value="BSc">BSc</option>');
                    courses.append('<option value="MSc">MSc</option>');
                } else if (department === 'Arts') {
                    courses.append('<option value="BA">BA</option>');
                    courses.append('<option value="MA">MA</option>');
                }
            });
        });



//  $(document).ready(function () {
//  $('#submit-button').click(function (event) {
//
//      $('#name').val('');
//      $('#dob').val('');
//      $('#age').val('');
//      $('#phoneNumber').val('');
//      $('#mailId').val('');
//      $('#address').val('');
//      $('#department').val('');
//      $('#courses').val('');
//      $('#purpose').val('');
//
//
//
//    $('#alerts-container').show();
//  });
//});
