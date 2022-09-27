/* eslint-disable */ //warning 제거


import React, { useState } from 'react';
import './App.css';


function App() {

  const _date = new Date();
  const year = _date.getFullYear();
  const month = _date.getMonth() + 1;
  const day = _date.getDate();
  const time = _date.toLocaleTimeString('ko-kr');
  const now_date = year+'년 '+month+'월 '+day+'일, '+time+'에 발행';

  let [글제목, 글제목변경] = useState(['남자코트 추천', '강남 우동맛집', '파이썬독학']);
  let [따봉, 따봉변경] = useState([0,0,0]);
  let [modal, setModal] = useState(false); // 모달여부 true:열림, false:닫힘
  let [title, setTitle] = useState(0);
  let [입력값, 입력값변경] = useState('');
  let [date, setDate] = useState([now_date, now_date, now_date]);

  

  return (
    <div className="App">
      <div className="black-nav">
        <h4>ReactBlog</h4>
      </div>

      { //중괄호{}안에 for 등 반복문 사용불가 → map()
        // array.map(a,b) : a에 array[0], array[1], array[2] 저장됨, b는 반복문 돌 떄마다 0부터 1씩 증가함
        // 글제목.map(a) : a = 남자코트추천 등등, b=0~2
        글제목.map(function(data, i){ //글제목 array길이만큼 반복
          return (
            <div className="list" key={i}> 
            {/* 반복된 html안에는 key값이 있어야 함, key값을 지정하면 warning 사라짐 */}
              <h4 onClick={()=>{setModal(true); setTitle(i);}}>{ 글제목[i] } 
              <span onClick={(e)=>{ e.stopPropagation(); //이벤트버블링제거
                let copy = [...따봉];
                copy[i] = copy[i]+1;
                따봉변경(copy); 
              }}>👍</span> {따봉[i]} </h4>
              <p>{date[i]}</p>
              <button onClick={()=>{
                let copy_글제목 = [...글제목];
                let copy_따봉 = [...따봉];
                let copy_date = [...date];

                copy_글제목.splice(i,1);
                copy_따봉.splice(i,1);
                copy_date.splice(i,1);

                글제목변경(copy_글제목);
                따봉변경(copy_따봉);
                setDate(copy_date);
              }}>삭제</button>
            </div>
          )
        })
      }

      <input onChange={(e)=>{
        입력값변경(e.target.value);
      }}></input>

      { 
        입력값 == '' ? 
          <button onClick={()=>{alert('값을 입력해주세요!');}}>글발행</button> 
        :
          <button onClick={()=>{
            let copy_글제목 = [...글제목];
            let copy_따봉 = [...따봉];
            let copy_date = [...date];

            copy_글제목.unshift(입력값);
            copy_따봉.unshift(0);
            copy_date.unshift(now_date);

            글제목변경(copy_글제목);
            따봉변경(copy_따봉);
            setDate(copy_date);
          }}>글발행</button>
      }


      { 
        // 조건식 ? 참일 때 실행할 코드 : 거짓일 때 실행할 코드
        modal == true ? <Modal 따봉 = {따봉} date = {date} title={title} 글제목={글제목} 글제목변경={글제목변경}/> : null
        //부모함수 → 자식함수 state 넘길 때 <Modal 작명={state}/> 하면됨
      }
      <Modal2></Modal2>
    </div>
  );
}



function Modal(props){
  return (
    <div className="modal">
      <h4>제목 : {props.글제목[props.title]} <span>👍{props.따봉[props.title]}</span></h4>
      <p>날짜 : {props.date[props.title]}</p>
      <p>상세내용</p>
      <button onClick={()=>{
        let copy = [...props.글제목]
        copy[0] = '여자코트 추천'
        props.글제목변경(copy)
      }}>글수정</button>
    </div>
  )
}

/* 클래스로 컴포넌트 구현해보기 */
class Modal2 extends React.Component {
  constructor(props){
    super(props);
    this.state = {
      name : 'kim',
      age : 20
    }
  }
  render(){
    return (
      <div>안녕{this.state.age}
        <button onClick={()=>{
          this.setState({age: 21})
        }}>버튼</button>
      </div>
    )
  }
}




export default App;
