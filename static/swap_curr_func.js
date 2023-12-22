function swapCurrencies() {
  var inputCurrency = document.getElementById("inputCurrency");
  var outputCurrency = document.getElementById("outputCurrency");

  var tempCurrency = inputCurrency.value;

  inputCurrency.value = outputCurrency.value;
  outputCurrency.value = tempCurrency;

  convert1();
}