/* 메소드에 속해있지 않은 this (global) */
function func(){
    if(global === this){
        console.log("global === this"); //전역객체와 this가 같은지 확인
    }
}
func();

/* 메소드 호출 시 this (property) */
var o = {
    func : function(){
        if(o === this){
            console.log("o === this");
        }
    }
}
o.func();


/* 생성자와 this */
var funcThis = null;

function Func(){
    funcThis = this;
}
var o1 = Func();
if(funcThis === global){
    console.log('window \n');    //생성자가 없으면(객체생성 안하면) 함수 밖의 가장 가까운 객체인 전역객체 (global)를 가리킴
}
var o2 = new Func();
if(funcThis === o2){
    console.log('o2 \n');    //생성자로 객체생성을 해줬으므로 함수 밖의 가장 가까운 객체인 o2를 가리킴
}


/* apply와 call로 this 값 제어 */
var o = {};   //o객체 선언
var p = {};   //p객체 선언
function func(){
    switch(this){
        case o:
            console.log('o \n');
            break;
        case p:
            console.log('p \n');
            break;
        case global:
            console.log('global \n');
            break;
    }
}
func();   //this = global
func.call(o);   //this 값 o로 변경      o라는 객체의 메소드가 됨
func.call(p);   //this 값 p로 변경      p라는 객체의 메소드가 됨