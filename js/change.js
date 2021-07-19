var btn = document.getElementById('click');
var trocar = document.getElementById('trocaimg');

btn.onclick = function() {
  if (btn.value=== 'trocar'){
    trocar.src= './img/humor/barneys.png';
    btn.value="dary";
    btn.innerHTML='dary';
  } 
  else if (btn.value==='dary'){
    trocar.src='./img/humor/barneys2.png';
    btn.value="trocar";
    btn.innerHTML='Legen...';  
  }
}
