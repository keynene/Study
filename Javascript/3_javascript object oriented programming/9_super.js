
class Person{
    constructor(name, first, second){
        this.name = name;
        this.first = first;
        this.second = second;
    }
    sum(){
        return this.first + this.second;
    }
}
class PersonPlus extends Person{
    constructor(name, first, second, third){
        super(name, first, second); // Person의 초기값까지 세팅해줌
        this.third = third;
    }
    sum(){
        return super.sum() + this.third;
    }
    
    avg(){
        return (super.sum() + this.third) / 3;
    }
}

var noi = new PersonPlus('noi', 10, 20, 30);
console.log('noi.sum()', noi.sum());
console.log('noi.avg()', noi.avg());

1. super()과 super의 차이
    super() : 부모class의 생성자(constructor)를 참조하여 초기값 세팅한다.
    super.method() : 부모class의 method()를 참조/실행한다.

2. super가 없을 경우 비효율 / 있을 경우 편리함
    super()를 통해 초기값 세팅이 수월해짐 
    자식class에서 매개변수(parameter)를 추가해야 하는경우, super()를 통해 세팅 후 추가 변수 선언 하면 됨
    자식class에서 부모class의 method를 수정해야 하는 경우, super.method()를 통해 접근/수정이 가능
