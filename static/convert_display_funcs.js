function convert1() {
  var inputValue = parseFloat(document.getElementById('inputValue').value);
  var inputCurrency = document.getElementById('inputCurrency').value;
  var outputCurrency = document.getElementById('outputCurrency').value;

  $.ajax({
    url: '/convert1',
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

function convert2() {
  var inputValue = parseFloat(document.getElementById('outputValue').value);
  var inputCurrency = document.getElementById('inputCurrency').value;
  var outputCurrency = document.getElementById('outputCurrency').value;

  $.ajax({
    url: '/convert2',
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
