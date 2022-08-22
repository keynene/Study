/* 랜덤하여 나라,도시 받아오기 */
var arr = new Array('seoul', 'new york', 'ladarkh', 'pusan', 'Tsukuba');
function getRandomValueFromArray(arr){
    var index = Math.floor(arr.length*Math.random());
    return arr[index];
}
console.log(getRandomValueFromArray(arr));

// Math.random : 0~1사이 소수 랜덤으로 제공  → *10하면 됨 
// Math.floor : 소수점 제거하여 정수만 저장함


/* 같은코드 스탠다드 오브젝트 사용 */
Array.prototype.random = function(){  //Array 사용하므로써 random이 array에 속해있다는 것을 알기쉬움(가독성)
    var index = Math.floor(this.length*Math.random());
    return this[index];
}
var arr = new Array('seoul', 'new york', 'Lanark', 'pusan', 'Tsukuba');
console.log(arr.random());
var arr2 = new ArrayBuffer(1);
console.log(arr2);


class Student
{
	number = 0;
	name = "noi";
    age = 27;	// 지역 Object 변수

    constructor(number , name , age){
        this.number = number;
        this.name = name;
        this.age = age;
    }

    setAge(age){
        age =age
    }
}

var noi2 = new Student(1 , "noi2" , 28)
noi2.setAge(30)
console.log(noi2)








