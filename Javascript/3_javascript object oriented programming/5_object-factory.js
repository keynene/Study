// constructor 생성 전
// 객체 속성이 변하면 객체마다 일일이 수정해줘야 함 (1억개면 1억개 다)

var noi = {
    name:'noi',
    first:10,
    second:20,
    third:30,
    sum:function(){
        return this.first + this.second + this.third;
    }
}
var kim = {
    name:'kim',
    first:10,
    second:10,
    third:10,
    sum:function(){
        return this.first + this.second + this.third;
    }
}
console.log("noi.sum()", noi.sum());
console.log("kim.sum()", kim.sum());



// constructor 생성 후
// Person이라는 껍데기 함수를 만들고 이후 객체들을 'new'생성자를 이용하여 객체화 시켜주었다
// 매개변수값만 조정하면 반복 선언할 필요 없이 고유의 속성을 가진 객체로 선언할 수 있다
// 객체 속성에 변화가 생기면 껍데기 함수만 수정하거나 각 객체에 매개변수만 조정해주면 된다.
function Person(name, first, second, third){
    this.name = 'kim';
    this.first = first;
    this.second = second,
    this.third = third,
    this.sum = function(){
        return this.first + this.second + this.third;
    }
}

var noi = new Person('noi', 10, 20, 30);
var kim = new Person('kim', 10, 10, 10);
console.log("noi.sum()", noi.sum());
console.log("kim.sum()", kim.sum());





// constructor 예시
var d1 = new Date('2022-09-15');
console.log('d1.getFullYear()', d1.getFullYear());
console.log('d1.getMonth()', d1.getMonth());

console.log('Date', Date);


//constructor
console.log('new Person()', new Person());

