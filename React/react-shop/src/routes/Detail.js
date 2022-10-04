/* eslint-disable */
import React, { useEffect, useState } from "react";
import { useParams } from "react-router-dom";
// import styled from 'styled-components'

function DetailCard(props){

  let {id} = useParams(); //app.js에서 detail/:id 로 정의했는데 여기 들어가는 id를 저장함
  let found = props.shoes.find(function(x){
    return x.id == id;
  })
  let [time, setTime] = useState(true);
  let [num, setNum] = useState('');
  

  useEffect(()=>{
    let timer = setTimeout(()=>{ setTime(false) },2000); //보통 타이머는 변수에 저장해서 사용 (삭제 or 재사용 가능하게)
    if (isNaN(num) == true){
      alert("숫자만 입력하라니까!");
    }

    return ()=>{
      clearTimeout(timer);
    }
  }, [num]) 

  return (
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
          <input placeholder="숫자만 입력해주세요!" onChange={(e)=>{ 
            setNum(e.target.value)
          }} />
          <h4 className="pt-5">{found.title}</h4>
          <p>{found.content}</p>
          <p>{found.price}</p>
          <button className="btn btn-danger">주문하기</button> 
        </div>
      </div>
    </div> 
  )
}


export default DetailCard;