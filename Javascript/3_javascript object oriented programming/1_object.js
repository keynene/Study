var memberArray = ['noi', 'keynene', 'nonung2'];
console.log("memberArray[2]",memberArray[2]);

var memberObject = {
    manager : 'noi',
    developer : 'keynene',
    designer : 'nonung2'
}
memberObject.designer = 'nonung';
console.log("memberObject.designer",memberObject.designer);
console.log("memberObject['designer']",memberObject['designer']);
delete memberObject.manager
console.log('after delete memberObject.manager', memberObject.manager);

