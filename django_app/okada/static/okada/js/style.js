var elem = document.getElementById('elem');
elem.addEventListener('click',function(){
  anime({
    targets: elem,
    translateX:[
      150,150,0,0
    ],
    translateY:[
      0,150,150,0
    ]
  })
})