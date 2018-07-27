function register() {
  let ccnum  = document.getElementById('ccnum')
  console.log(payform.validateCardNumber(ccnum.value))
  if (!payform.validateCardNumber(ccnum.value)) {
    $("#errorAlert").text("Credit Card invalid!")
    $('#errorAlert').show()
    return
  }
  let firstName = $('#firstName').val()
  if (!firstName) {
    $("#errorAlert").text("First Name is required!")
    $('#errorAlert').show()
    return
  }
  let lastName = $('#lastName').val()
  if (!lastName) {
    $("#errorAlert").text("Last Name is required!")
    $('#errorAlert').show()
    return
  }
  let email = $('#email').val()
  if (!email) {
    $("#errorAlert").text("Email is required!")
    $('#errorAlert').show()
    return
  }
  let password = $('#password').val()
  if (!password) {
    $("#errorAlert").text("Password is required!")
    $('#errorAlert').show()
    return
  }
  let expiry = $('#expiry').val()
  if (!expiry) {
    $("#errorAlert").text("Credit card expiry is required!")
    $('#errorAlert').show()
    return
  }
  let cvc = $('#cvc').val()
  if (!cvc) {
    $("#errorAlert").text("CVC is required!")
    $('#errorAlert').show()
    return
  }
  
  $('#errorAlert').hide()
  
  data = {
    "first_name": firstName,
    "last_name": lastName,
    "email": email,
    "password": password,
    "ccnum": ccnum.value,
    "expiry": expiry,
    "cvc": cvc
  }

  $.ajax({
    url: 'http://coreydxc.pythonanywhere.com/user',
    dataType: 'json',
    type: 'post',
    contentType: 'application/json',
    data: JSON.stringify(data),
    success: function(data) { $('#successAlert').show() },
    error: function() {
      $("#errorAlert").text("Failed to register. Server error!")
      $('#errorAlert').show()
   }
  })
}