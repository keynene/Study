const id = document.getElementById('id');
const pw = document.getElementById('password');
const login = document.getElementById('login');



login.addEventListener('click', function(){
    if(id.value.length === 0){
        alert('아이디를 입력해주세요.');
    } else if(id.value === 'noi'){
        if(pw.value === '1111'){
            alert(id.value+'님 환영합니다!');
        }
        else {
            alert('비밀번호를 다시 확인해주세요.');
        }
    } else {
        alert('존재하지 않는 계정입니다.');
    }
});