//정규식 개념
var str = "a";
var str1 = /a/;
var str2 = new RegExp('a');
console.log(str);  //a
console.log(str1);  //  /a/
console.log(str2);  //  /a/

/* 검색 */
//pattern안의 문자열에서 원하는 문자 검색
var pattern = /a/;    
console.log(pattern.exec('abcde'));  //a반환
var pattern = /a./;    
console.log(pattern.exec('abcde'));  //ab반환  
var pattern = /a/;    
console.log(pattern.exec('bcdef'));  //null (찾고자하는 결과가 없음)

//pattern안의 문자열에서 원하는 문자 존재유무 검색
var pattern = /a/;    
console.log(pattern.test('abcde'));  //true  
console.log(pattern.test('bcde'));  //false

//pattern안의 문자열이 존재유무 확인 후 문자열 반환
var pattern = /a/;
var str = 'abcdef';
console.log(str.match(pattern));  //a반환
var str = 'bcdef';
console.log(str.match(pattern));  //null

/* 치환 */
//원하는 문자열 검색 후 치환
var pattern = /a/;
var str = 'abcdef';
console.log(str.replace(pattern, 'A'));  //Abcdef 반환



/* 옵션 */
// "i"옵션 - 대소문자 구분하지 않게해줌
var xi = /a/;
var oi = /a/i;
console.log("Abcde".match(xi));  //null
console.log("Abcde".match(oi));  //A 반환


// "g"옵션 - 중복 문자도 검색 가능하게 해줌
var xg = /a/;
var og = /a/g;
console.log("abcdea".match(xg));  //a 반환
console.log("abcdea".match(og));  //a, a 반환

/* 예제 */
//예제1 - $사용
var pattern = /(\w+)\s(\w+)/;  //모든문자  공백  모든문자
var str = "coding everybody";
var result = str.replace(pattern, "$2, $1");
console.log(result);

//예제2 - url 링크로 표현하기
var urlPattern = /\b(?:https?):\/\/[a-z0-9-+&@#\/%?=~_|!:,.;]*/gim;
var content = 'keynene벨로그 : https://velog.io/@keynene 입니다. 네이버 : http://naver.com 입니다. ';
var result = content.replace(urlPattern, function(url){
    return '<a href="'+url+'">'+url+'</a>';
});
console.log(result);