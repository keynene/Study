/* eslint-disable */
import React, { useContext, useEffect, useState } from "react";
import { useParams } from "react-router-dom";
import Nav from 'react-bootstrap/Nav';



// import styled from 'styled-components'

function DetailCard(props){

  
  let {id} = useParams(); //app.js에서 detail/:id 로 정의했는데 여기 들어가는 id를 저장함
  let found = props.shoes.find(function(x){
    return x.id == id;
  })
  let [time, setTime] = useState(true);
  let [num, setNum] = useState('');
  let [tab, setTab] = useState(0);
  let [fade_m, setFade_m] = useState('');
  
  

  useEffect(()=>{
    let timer = setTimeout(()=>{ setTime(false) },2000); //보통 타이머는 변수에 저장해서 사용 (삭제 or 재사용 가능하게)
    if (isNaN(num) == true){
      alert("숫자만 입력하라니까!");
    }


    let fadeTime = setTimeout(()=>{ setFade_m('end') }, 100);

    return ()=>{
      clearTimeout(timer);
      clearTimeout(fadeTime);
      setFade_m('');
    }
  }, [num]) 

  return (
    <div className={'container start ' + fade_m}>
      <div className="container">
        {
          time == true ?
          <div className="alert alert-warning">
            2초이내 구매시 할인
          </div>
          : null
        }
        
        <div className="row">
          <div className="col-md-6">
            <img src={"https://codingapple1.github.io/shop/shoes"+(parseInt(found.id)+1)+".jpg"} width="100%" />
          </div>
          <div className="col-md-6">
            {/* 
            /////숫자말고 다른거 입력 시 경고창이 뜨는 예제/////
            <input placeholder="숫자만 입력해주세요!" onChange={(e)=>{ 
              setNum(e.target.value)
            }} /> 
            */}
            <h4 className="pt-5">{found.title}</h4>
            <p>{found.content}</p>
            <p>{found.price}</p>
            <button className="btn btn-danger">주문하기</button> 
          </div>
        </div>

        <div className="tabs">
          <Nav variant="tabs" defaultActiveKey="link0" >
            <Nav.Item>
              <Nav.Link eventKey="link0" onClick={()=>{ setTab(0) }}>버튼0</Nav.Link>
            </Nav.Item>
            <Nav.Item>
              <Nav.Link eventKey="link1" onClick={()=>{ setTab(1) }}>버튼1</Nav.Link>
            </Nav.Item>
            <Nav.Item>
              <Nav.Link eventKey="link2" onClick={()=>{ setTab(2) }}>버튼2</Nav.Link>
            </Nav.Item>
          </Nav>
        </div>

        <TabContent tab={tab} shoes={props.shoes} />

      </div> 
    </div>
  )
}


function TabContent(props){
  // if (tab == 0){
  //   return <div>내용0</div>  
  // }
  // if(tab == 1){
  //   return <div>내용1</div> 
  // }
  // if(tab == 2){
  //   return <div>내용2</div> 
  // } 

  let [fade, setFade] = useState('');

  useEffect(()=>{ //tab이 변경될 때마다 클래스명에 "end" 붙임
    //state를 이용하여 변수를 조작하여 className 변경 가능

    //그러나 이벤트 제대로 동작하지 않음
    // > 이벤트는 클래스이름이 'start' > 'start end' 이렇게 바뀌어야지 동작함
    // 바로 end를 붙이기 전에 공백으로 세팅해줄 필요가 있음
    // useEffect 실행 전에 실행해주는 return의 clean up function 이용!
    // 그래도 동작하지 않음 >> 시간을 끌어줄 필요가 있음 (시간은 임의로 0.1초로 지정)
    // react의 automatic batching 때문임 (근접한 기능을 한데모아 재랜더링 없이 한꺼번에 실행해주기 때문에 시간이 끌어지지않앗음)
    // timer는 useEffect마다 계속 쌓이기 때문에 clean up 시켜주고 싶으면 변수에 담아서 clearTimeout해줌


    let t = setTimeout(()=>{ setFade('end'); }, 100)

    return ()=>{
      clearTimeout(t);
      setFade('');
    }
  }, [props.tab])

  /* if문과 같이 코딩하려면 */ 
  return (
    <div className={'start ' + fade}>
      { [<div>{props.shoes[0].title}</div>, <div>내용1</div>, <div>내용2</div>][props.tab] }
    </div>
    )
}


export default DetailCard;