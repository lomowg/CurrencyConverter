function convert_to_second_form() {
  var inputValue = parseFloat(document.getElementById('inputValue').value);
  var inputCurrency = document.getElementById('inputCurrency').value;
  var outputCurrency = document.getElementById('outputCurrency').value;

  $.ajax({
    url: '/convert_to_second_form',
    type: 'POST',
    contentType: 'application/json;charset=UTF-8',
    data: JSON.stringify({
      inputCurrency: inputCurrency,
      outputCurrency: outputCurrency,
      inputValue: inputValue
    }),
    success: function(response) {
      var result = response.result;
      document.getElementById('outputValue').value = result;
    }
  });
}

function convert_to_first_form() {
  var inputValue = parseFloat(document.getElementById('outputValue').value);
  var inputCurrency = document.getElementById('inputCurrency').value;
  var outputCurrency = document.getElementById('outputCurrency').value;

  $.ajax({
    url: '/convert_to_first_form',
    type: 'POST',
    contentType: 'application/json;charset=UTF-8',
    data: JSON.stringify({
      inputCurrency: inputCurrency,
      outputCurrency: outputCurrency,
      inputValue: inputValue
    }),
    success: function(response) {
      var result = response.result;
      document.getElementById('inputValue').value = result;
    }
  });
}
