function convert1() {
  var inputValue = parseFloat(document.getElementById('inputValue').value);
  var inputCurrency = document.getElementById('inputCurrency').value;
  var outputCurrency = document.getElementById('outputCurrency').value;

  // Отправляем AJAX-запрос на сервер Flask
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
      // Обработка успешного ответа от сервера
      var result = response.result;
      document.getElementById('outputValue').value = result;
    }
  });
}

function convert2() {
  var inputValue = parseFloat(document.getElementById('outputValue').value);
  var inputCurrency = document.getElementById('inputCurrency').value;
  var outputCurrency = document.getElementById('outputCurrency').value;

  // Отправляем AJAX-запрос на сервер Flask
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
      // Обработка успешного ответа от сервера
      var result = response.result;
      document.getElementById('inputValue').value = result;
    }
  });
}
