function sum(){
    var i, _sum = 0;
    for(i = 0; i < arguments.length; i++){
        console.log(i + ' : '+arguments[i]+ '\n');
        _sum += arguments[i];
    }
    return _sum;
}
console.log('result : ' + sum(1,2,3,4));
/*
자바스크립트는 함수를 선언할 때 파라미터 값을 넣지 않아도
함수를 사용할 때 아규먼트 값에서 호출을 하면,
유동적으로 값을 조절하는 기능이 있음

즉, 아규먼트는 늘어나고 줄어드는 등 유동적이어도 효용가능함
*/


/* arguments 예제1 */
function one(arg1){
    if(one.length != arguments.length){
        console.log('변수를 1개만 입력해주세요');
    }else {
        console.log(
            'one.length', one.length + '\n',  // one이라는 함수의 파라미터 갯수
            'arguments.length', arguments.length  //실제 호출될 때의 아규먼트 갯수
        );
    }
}
one('val1','val2');
