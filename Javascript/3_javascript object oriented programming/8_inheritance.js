
class Person{
    constructor(name, first, second){
        this.name = name;
        this.first = first;
        this.second = second;
    }
    sum(){
        return 'prototype : '+ (this.first + this.second);
    }
}
/* Person이라는 클래스를 상속하는 PersonPlus */
class PersonPlus extends Person{
    avg(){
        return (this.first + this.second)/2;
    }
}

var noi = new PersonPlus('noi', 10, 20);
console.log('noi.sum()', noi.sum());
console.log('noi.avg()', noi.avg());