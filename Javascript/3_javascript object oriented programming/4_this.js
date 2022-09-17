var noi = {
    name:'noi',
    first:10,
    second:20,
    sum:function(){
        return this.first + this.second;
    }
}
// console.log("noi.sum(noi.first, noi.second)", noi.sum(noi.first, noi.second));
console.log("noi.sum(noi.first, noi.second)", noi.sum());