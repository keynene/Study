var person = {};
person.name = 'keynene';
person.introduce = function(){
    return 'My name is '+this.name;
}
console.log(person.introduce());