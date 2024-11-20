const button = document.getElementById('button');
const productName = document.getElementById('productName');
const productName5 = document.getElementById('name');
 function productdis(inputproductName){
    inputproductName.innerText =  inputproductName;
 }
 button.addEventListener('click', () => {
    productdis(productName.value)
 }
 )