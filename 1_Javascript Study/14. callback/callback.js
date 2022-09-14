/* method(메소드) */
//객체의 속성 값으로 담겨진 함수
a = {
    b:function(){
        
    }
}
//a : key, b : value

function cal(key, num){
    return key(num) 
}
function increase(num){
    return num+1
}
function decrease(num){
    return num-1
}
console.log(cal(increase,1));
console.log(cal(decrease,1));

//객체에서의 함수사용
function cal(mode){
    var funcs = {
        'plus' : function(left, right){return left + right},
        'minus' : function(left, right){return left - right}
    }
    return funcs[mode];
}
console.log(cal('plus')(2,1));
console.log(cal('minus')(2,1));

//배열에서의 함수사용
var process = [
    function(input){ return input + 10;},
    function(input){ return input * input;},
    function(input){ return input / 2;}
];
var input = 1;
for(var i = 0; i < process.length; i++){  //i는 배열의 인덱스를 의미
    input = process[i](input);  //input은 배열 안의 함수의 파라미터를 의미
}
console.log(input);






//값으로 변환전
var numbers = [20, 10, 9,8,7,6,5,4,3,2,1];
function sortfunc(a,b){
    console.log(a,b);
    if(a > b){
        return 1;
    } else if(a < b){
        return -1;
    } else {
        return 0;
    }
}
console.log(numbers.sort(sortfunc));

//값으로 변환후 (간결해짐)
var numbers = [20, 10, 9,8,7,6,5,4,3,2,1];
var sortfunc = function(a,b){
    return a-b;
}
console.log(numbers.sort(sortfunc));


