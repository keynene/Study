Object.prototype.contain = function(needle){
    for(var name in this){
        if(this[name] === needle){
            return true;
        }
    }
    return false;
}
var o = {'name':'keynene', 'city':'changwon'};
console.log(o.contain('keynene')); 
var a = ['keynene','noi','nonung'];
console.log(a.contain('noi'));

// contain : 인자에 해당하는 값(value)이 객체에 있는지 확인

/* Object확장의 위험(모든 객체에 영향을 주기 때문) */
Object.prototype.contain = function(needle){
    for(var name in this){
        if(this[name] === needle){
            return true;
        }
    }
    return false;
}
var o = {'name':'keynene', 'city':'changwon'};
var a = ['keynene','noi','nonung'];
for(var name in a){
    // 해결방법 : 어떠한 객체가 자신의 고유한 프로퍼티를 가지고 있는지 확인(hasOwnProperty)
    if(a.hasOwnProperty(name)){;   // 자신의 고유한 프로퍼티 일경우 (true일경우) 출력
        console.log(name);
    }
}
// object에서 추가한 contain 속성이 추가되어 출력됨