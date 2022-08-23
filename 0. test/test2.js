function Auto(){
    this.engine = 0;
    this.speed = 0;
    
    
    this.engineOn = function(){
        this.engine = 1;
    }

    this.engineOff = function(){
        this.engine = 0;
    }

    this.pedalOn = function(){
        if(this.engine === 0){
            console.log('시동켜세요');
        }else {
            this.speed = this.speed + 8;
        }
    }
    
    this.break = function(){
        if(this.engine === 0){
            console.log('시동켜세요');
        }else if(this.speed === 0) {
            console.log('속력이 0km 입니다.');
        }else {
            if(this.speed <= 10){
                this.speed = 0;
                console.log('멈춤');
            }else{
                this.speed = this.speed - 10;
            }
        }
    }
}

function Police_car(){
    this.siren = 0;
    this.criminal = 0;

    this.sirenOn = function(){
        this.siren = 1;
        this.speed = this.speed + 10;
    }

    this.sirenOff = function(){
        this.siren = 0;
    }

    this.criminal_arrest = function(){
        if(this.siren === 1){
            this.criminal = this.criminal + 1;
        } else {
            console.log('사이렌을 켜세요.');
        }

    }

}

Police_car.prototype = new Auto();

var car = new Auto();
var police = new Police_car();

police.sirenOn();
police.criminal_arrest();
police.criminal_arrest();
console.log(police);

