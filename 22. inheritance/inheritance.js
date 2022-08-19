function Person(name){
    this.name = name;
    this.introduce = function (){
        return 'My name is '+this.name;
    }
}
var p1 = new Person('keynene');
console.log(p1.introduce()+'\n');




/* inheritance 사용 */
function Person(name){
    this.name = name;
}
Person.prototype.name = null;
Person.prototype.introduce = function(){
    return 'My name is '+this.name;
}
function Programmer(name){
    this.name = name;
}
Programmer.prototype = new Person();
var p1 = new Person('keynene');
console.log(p1.introduce()+'\n');




/* inheritance를 통한 original객체 응용 */
function Person(name){
    this.name = name;
}
Person.prototype.name = null;
Person.prototype.introduce = function(){
    return 'My nickname is '+this.name;
}
function Programmer(name){
    this.name = name;
}
Programmer.prototype = new Person();
Programmer.prototype.coding = function(){
    return "hello world";
}
function Desinger(name){
    this.name = name;
}
Desinger.prototype = new Person();
Desinger.prototype.design = function(){
    return "beautiful";
}
////
var p1 = new Programmer('keynene');
console.log(p1.introduce()+'\n');
console.log(p1.coding()+'\n');
////
var p2 = new Desinger('Noi');
console.log(p2.introduce()+'\n');
console.log(p2.design()+'\n');





/* Prototype chain 예제 */
function Ultra(){}
Ultra.prototype.ultraProp = true;  //key : UltraProp, value : true인 객체를 선언한 것이라고 할 수 있음 (자식에게 상속하기 위해 prototype 이용)
////
function Super(){}
Super.prototype = new Ultra();
////
function Sub(){}
Sub.prototype = new Super();
////
var o = new Sub();    //o에 Sub 객체 생성
console.log(o.ultraProp);
