
var grades = {
    'list' : {'egoing': 10, 'k8805': 6, 'sorialgi': 80},
    'show' : function(){
        for(var name in this.list){
            console.log(name+' : '+this.list[name]+"\n");
        }
    },
     'test' : function(){
         this.list.egoing = this.list.egoing+'a123';
     }

};
var grades2 = grades;
grades2.test();
grades.show();

