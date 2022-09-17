var kim = {name:'kim', first:10, second:20}
var jang = {name:'jang', first:10, second:10}
function sum(key){
    return key + (this.first + this.second);
}
/* method.call(this에 대입될 값, method인자값) */
// sum.call = sum();과 같은 역할이지만 원하는 변수를 불러올 수 있음 (실행)
console.log(sum.call(kim, 'kimCall ')); // this=kim, key=kimCall
console.log(sum.call(jang, 'jangCall ')); // this=jang, key=jangCall

/* method.bind(새로 생성할 this에 대입될 값, method인자값) */
// method에는 영향을 주지않고 새로운 변수에 기존 method를 복제해서 넣는 개념 (새로운함수생성)
var kimBind = sum.bind(kim, 'kimBind ');
console.log(kimBind());
