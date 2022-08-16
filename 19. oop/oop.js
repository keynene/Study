/* 객체정의 방법1 */
var person = {};
person.name = 'keynene';
person.introduce = function(){
    return 'My name is '+this.name;
}
console.log(person.introduce());


/* 객체정의 방법2 */
var person = {
    'name' : 'keynene',
    'introduce' : function(){
        return 'My name is '+this.name;
    }
}
console.log(person.introduce());


/* 중복되는 객체가 있는 경우 */
var person1 = {
    'name' : 'keynene',
    'introduce' : function(){
        return 'My name is '+this.name;
    }
}

var person2 = {
    'name' : 'Noi',
    'introduce' : function(){
        return 'My name is '+this.name;
    }
}


/* 생성자 new사용 */
function Person(){
    var p1 = new Person();   //new : Person()함수를 함수라고 하지않고 '생성자'라고 칭함
    p1.name = 'keynene';
    p1.introduce = function(){
        return 'My name is '+this.name;
    }
}
console.log(p.introduce());


/* 중복 해결 */
function Person(name){
    this.name = name;
    this.introduce = function(){
        return 'My name is '+this.name;
    }
}
var p1 = new Person('keynene');
console.log(p1.introduce()+'\n');
var p2 = new Person('Noi');
console.log(p2.introduce()+'\n');