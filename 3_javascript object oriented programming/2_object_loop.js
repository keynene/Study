/* 배열 출력 */
var memberArray = ['noi', 'keynene', 'nonung2'];
console.group('array loop');
var i=0;
while(i < memberArray.length){
    console.log(memberArray[i]);
    i=i+1;
}
console.groupEnd('array loop');

/* 객체 출력 ,  객체[변수] : 변수(key값)에 해당하는 밸류값 출력 */
var memberObject = {
    manager : 'noi',
    developer : 'keynene',
    designer : 'nonung2'
}
console.group('object loop');
for(var name in memberObject){
    console.log(name, memberObject[name]);
}
console.groupEnd('object loop');