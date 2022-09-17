// Person은 생성자 new를 통해 Person이 정의될 때마다 실행됨
function Person(name, first, second){
    this.name = name;
    this.first = first;
    this.second = second;
}
// prototype으로 선언한 Person의 sum의 함수는 최초 1번만 실행됨
Person.prototype.sum = function(){
    return 'prototype : '+ (this.first + this.second);
}

var noi = new Person('noi', 10, 20);
console.log("noi.sum()", noi.sum());
// noi.sum = function(){
//     return 'this : '+ this.first + this.second; 
// }
var kim = new Person('kim', 10, 10);
console.log("kim.sum()", kim.sum());

/* 
실행 시 우선 객체에 sum이라는 속성이 있는지 먼지 확인 후 실행함
noi와 kim에 sum이라는 속성이 있는지 검사 후 있으면 그것을 우선적으로 실행하고 
prototype을 최후로 실행함
*/
