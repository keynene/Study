// 함수형 객체 생성자로는 선언 시 초기값이 세팅이 되는데 class는 초기값 세팅이 안됨
// constructor : 객체를 생성되는 과정에서 실행됨
class Person{
    constructor(name, first, second){
        this.name = name;
        this.first = first;
        this.second = second;
    }
    // constructor에서의 메소드 실행방법
    sum(){
        return 'prototype : '+ (this.first + this.second);
    }
}
/*
// 정석 prototype 메소드 실행 방법
Person.prototype.sum = function(){
    return 'prototype : '+ (this.first + this.second);
}
*/

var noi = new Person('noi', 10, 20);
console.log('noi', noi);
console.log('noi.sum()', noi.sum());


// var noi = new Person('noi', 10, 20);
// noi.sum = function(){
//     return 'this : '+ this.first + this.second; 
// }
// var kim = new Person('kim', 10, 10);
// console.log("noi.sum()", noi.sum());
// console.log("kim.sum()", kim.sum());