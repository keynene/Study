function Person(name, age, w , h ){
    this.name = name;
    this.age = age;
    this.w = w;
    this.h = h;

    this.state = function (){
        console.log(this.name+', '+this.age+', '+this.w+', '+this.h);
    }

    this.eat = function(w){
        this.w = this.w + w;
        console.log('배부르다, '+this.w);
    }

    this.jump = function(){
        this.h = this.h + 10;
    }
    
    this.say = function(){
        console.log('나는 '+this.name+'입니다. \n');
    }

    this.strong = function(){
        this.h = this.h + 10;
        this.w = this.w - 10;
    }


}


var j = new Person('jang',27,60,168);
j.state(); // 상태보기

j.eat(5)
j.state()

j.jump()
j.state()

j.say()
j.state()

j.strong()//
j.state()


function Programmer(name){
    this.name = name;
}
Programmer.prototype = new Person();
Programmer.prototype.coding = function(){
    return "hello world";
}


var eun = new Programmer('keynene');
console.log(eun)
///사람객체 
//1 . 밥먹을먹는다() -> 몸무게가 10kg
//2.  줄넘기() 키 10cm증가
//3.  말하기 -> 안녕이라고 출력
//4.  상태보기() -> 이름 몸무게 나이 키 출력 
//5.  강하게 줄넘기() -> 몸무게가 -10 키카 +10