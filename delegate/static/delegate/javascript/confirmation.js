$(document).ready(function(){

  // Show email modal on page load
  $('#email-confirmation-modal').modal('show');

  // Send email confirmation
  $('body').on('click', '#send-email', function(){
    // Verify stuff here
    var regDetailId = $('#reg-id').val();
    var emailMessage = $('#email_message').val();
    var emailSubject = $('#email_subject').val();
    var toList = [];
    var ccList = [];
    var bccList = [];
    $('input[name="to_field"]').each(function(){
      if (!$(this).prop('disabled')){
        toList.push($(this).val());
      };
    });
    $('input[name="cc_field"]').each(function(){
      if (!$(this).prop('disabled')){
        ccList.push($(this).val());
      };
    });
    $('input[name="bcc_field"]').each(function(){
      if (!$(this).prop('disabled')){
        bccList.push($(this).val());
      };
    });
    console.log(toList);
    // Add other variables
    $.ajax({
      url: '/delegate/send_conf_email/',
      type: 'POST',
      data: {
        'reg_id': regDetailId,
        'email_message': emailMessage,
        'email_subject': emailSubject,
        'to_list': toList,
        'cc_list': ccList,
        'bcc_list': bccList,
      },
      success: function(){
        $('#email-confirmation-modal').modal('hide');
      }
    });
  });


  // Disable email address
  $('body').on('click', '.deactivate-email', function(){
    console.log('deactivating email');
    $(this).children('span').removeClass('glyphicon-remove');
    $(this).children('span').addClass('glyphicon-plus');
    $(this).removeClass('deactivate-email');
    $(this).addClass('activate-email');
    $(this).parent().next('input').prop('disabled', true);
    if ($(this).parent().next('input').val() != ''){
      var oldEmail = $(this).parent().next('input').val();
    } else {
      var oldEmail = 'Add'
    };
    $(this).parent().next('input').prop('placeholder', oldEmail);
    $(this).parent().next('input').val('');
  });


  // Enable email address and add new blank field if needed
  $('body').on('click', '.activate-email', function(){
    console.log('activating-email');
    $(this).children('span').removeClass('glyphicon-plus');
    $(this).children('span').addClass('glyphicon-remove');
    $(this).removeClass('activate-email');
    $(this).addClass('deactivate-email');
    $(this).parent().next('input').removeAttr('disabled');
    if ($(this).parent().next('input').prop('placeholder') != 'Add'){
      var newEmail = $(this).parent().next('input').prop('placeholder');
    } else {
      var newEmail = '';
    };
    $(this).parent().next('input').val(newEmail);
    if ($(this).parent().parent().is(':last-child')){
      console.log('last child');
      // $('#id-tag').append(html-content);
    };
  });
});