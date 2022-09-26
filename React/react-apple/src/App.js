/* eslint-disable */ //warning 제거


import { useState } from 'react';
import './App.css';

function App() {

  let post = '강남 우동 맛집'
  let [글제목, 글제목변경] = useState(['남자코트 추천', '강남 우동맛집', '파이썬독학']);
  let [따봉, 따봉변경] = useState([0,0,0]);
  let [modal, setModal] = useState(false); // 모달여부 true:열림, false:닫힘
  let [title, setTitle] = useState(0);
  let [입력값, 입력값변경] = useState('');

  return (
    <div className="App">
      <div className="black-nav">
        <h4>ReactBlog</h4>
      </div>
      {/* <button onClick={()=>{
          let copy = [...글제목];
          copy[0] = '여자코트 추천';
          글제목변경(copy);
        }}>Change</button>
        <button onClick={()=>{
          let copy = [...글제목];
          copy.sort();
          글제목변경(copy);
        }}>가나다순정렬</button> */}

        
      {/* <div className="list">
        <h4>{글제목[0]} <span onClick={()=>{
          따봉변경(따봉+1)
        }}>👍</span> {따봉} </h4>
        <p>2월 17일 발행</p>
      </div>
      <div className="list">
        <h4>{글제목[1]}</h4>
        <p>2월 17일 발행</p>
      </div>
      <div className="list">
        <h4 onClick={()=>{
          if(modal == false){
            setModal(true);
          } else {
            setModal(false);
          }
        }}>{글제목[2]}</h4>
        <p>2월 17일 발행</p>
      </div> */}
      
      
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
              <p>2월 17일 발행</p>
              <button onClick={()=>{
                let copy = [...글제목];
                copy.splice(i,1);
                글제목변경(copy);
              }}>삭제</button>
            </div>
          )
        })
      }

      <input onChange={(e)=>{
        입력값변경(e.target.value);
      }}></input>
      <button onClick={()=>{
        let copy = [...글제목];
        copy.unshift(입력값);
        글제목변경(copy)
      }}>글발행</button>



      { //컴포넌트 중간에 "중괄호{}" 입력 시 안에 자바스크립트 코드 기입 가능
        //조건식 작성 시 삼항연산자 이용
        // 조건식 ? 참일 때 실행할 코드 : 거짓일 때 실행할 코드
        modal == true ? <Modal title={title} 글제목={글제목} 글제목변경={글제목변경}/> : null
        //부모함수 → 자식함수 state 넘길 때 <Modal 작명={state}/> 하면됨
      }
      
    </div>
  );
}



function Modal(props){
  return (
    <div className="modal">
      <h4>제목 : {props.글제목[props.title]}</h4>
      <p>날짜</p>
      <p>상세내용</p>
      <button onClick={()=>{
        let copy = [...props.글제목]
        copy[0] = '여자코트 추천'
        props.글제목변경(copy)
      }}>글수정</button>
    </div>
  )
}



export default App;
