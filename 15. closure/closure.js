//외부함수에서 내부함수 변수 사용가능
function outter(){
    var title = 'coding  everybody';
    function inner(){
        // var title = 'coding  everybody';
        console.log(title); 
    }
    inner();
}
outter();

//외부함수를 사용하지 않을 때도 내부함수에서 외부함수 사용 가능
function outter(){
    var title = 'coding everybody';
    return function(){
        console.log(title);
    }
}
var inner = outter();
inner();

//private variable
function factory_movie(title){
    return {
        get_title : function (){
            return title;
        },
        set_title : function (_title){
            title = _title;
        }
    }
}
ghost = factory_movie('Ghost in the shell');
matrix = factory_movie('Matrix');
console.log(ghost.get_title());
console.log(matrix.get_title());
ghost.set_title('공각기동대');

console.log(ghost.get_title());
console.log(matrix.get_title());

/*
ghost, matrix에 각각의 factory_movie라는 get_title, set_title을 key값으로 가진 메소드를 저장
ghost.set_title('공각기동대') : ghost안의 메소드의 _title, 즉 title 값 변경
ghost.get_title만 변경되고 matrix.get_title은 변화없음

※private variable : closure로 ghost에 저장된 메소드의 title 값만 변경할 뿐이지
다른 변수(matrix)에 저장된 메소드의 title 값에는 영향을 미치지 않음
*/

//closure 실패 예제
var arr = []
for(var i = 0; i < 5; i++){
    arr[i] = function(){
        return i;
    }
}
for(var index in arr){
    console.log(arr[index]());
}
// i가 외부함수의 변수가 아니기 때문에 2번쨰 반복문에서는 i값을 모름


var arr = []
for(var i = 0; i < 5; i++){
    arr[i] = function(id){
        return function(){
            return id;
        }
    }(i);
}
for(var index in arr){
    console.log(arr[index]());
}
